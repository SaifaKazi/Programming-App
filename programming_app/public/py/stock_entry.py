import frappe
import json
import calendar
from datetime import datetime

@frappe.whitelist()
def data(doc):
    doc = json.loads(doc)
    result = []  
    for row in doc.get('custom_labour_details', []):
        salary = frappe.get_value(
            'Salary Structure Assignment',
            {"employee": row["employee"]},
            ["base","from_date"],
            as_dict=True
        )
        if salary:
            base = salary["base"]
            from_date = salary["from_date"]
            if isinstance(from_date, str):
                from_date = datetime.strptime(from_date, "%Y-%m-%d")

            month_name = from_date.strftime("%B")
            total_days = calendar.monthrange(from_date.year, from_date.month)[1]
            day_salary = base / total_days
            per_hours_salary = day_salary / 8
            # frappe.msgprint(f"Employee {row['employee']} per_hours_salary: {per_hours_salary}")
            result.append({
                "employee": row["employee"],
                "base": base,
                "month_name": month_name,
                "total_days": total_days,
                "day_salary": day_salary,
                "per_hours_salary": per_hours_salary
            })
    return result

# @frappe.whitelist()
# def data(doc, method=None):
#     so = frappe.get_value("Work Order", {"name": doc.work_order}, "sales_order")
#     item_code = frappe.get_value("Work Order", {"name": doc.work_order}, "production_item")

#     qty = frappe.get_value(
#         "Sales Order Item",
#         {"parent": so, "item_code": item_code},
#         "qty"
#     )

#     if doc.stock_entry_type == "Manufacture":
#         for row in doc.items:
#             if row.is_finished_item:
#                 stock_reserve = frappe.new_doc("Stock Reservation Entry")
#                 stock_reserve.item_code = row.item_code
#                 stock_reserve.reserved_qty = row.qty
#                 stock_reserve.voucher_type = "Sales Order"
#                 stock_reserve.voucher_no = so
#                 stock_reserve.warehouse = row.t_warehouse
#                 stock_reserve.voucher_detail_no = row.name
#                 stock_reserve.voucher_qty = qty
#                 stock_reserve.reserved_qty=qty
#                 # stock_reserve.available_qty_to_reserve = qty
#                 stock_reserve.insert(ignore_permissions=True)


# @frappe.whitelist()
# def on_submit_stock_entry(doc, method=None):
#     if doc.stock_entry_type != "Manufacture":
#         return

#     so = frappe.get_value("Work Order", doc.work_order, "sales_order")
#     item_code = frappe.get_value("Work Order", doc.work_order, "production_item")

#     so_item = frappe.get_value(
#         "Sales Order Item",
#         {"parent": so, "item_code": item_code},
#         ["name", "qty"],
#         as_dict=True
#     )

#     row_name = so_item.name
#     qty = so_item.qty

#     for row in doc.items:
#         if row.is_finished_item:
#             # Calculate available quantity in the target warehouse
#             available_qty = frappe.get_value(
#                 "Bin",
#                 {"item_code": row.item_code, "warehouse": row.t_warehouse},
#                 "actual_qty"
#             ) or 0

#             # Skip if nothing is available
#             if available_qty <= 0:
#                 frappe.msgprint(f"No stock available in warehouse {row.t_warehouse} for item {row.item_code}")
#                 continue
            
#             stock_reserve = frappe.get_doc({
#                 "doctype": "Stock Reservation Entry",
#                 "item_code": row.item_code,
#                 "warehouse": row.t_warehouse,
#                 "voucher_type": "Sales Order",
#                 "voucher_no": so,
#                 "voucher_detail_no": row_name,
#                 "voucher_qty": qty,
#                 "reserved_qty": min(qty, available_qty),
#                 "available_qty": available_qty,  # mandatory field
#                 "company": doc.company
#             })

#             stock_reserve.insert(ignore_permissions=True)
#             stock_reserve.submit()




@frappe.whitelist()
def on_submit_stock_entry(doc, method=None):
    # frappe.msgprint("hi")
    # Run only for Manufacture type Stock Entries
    if doc.stock_entry_type != "Manufacture":
        return

    # Fetch Sales Order and Production Item from Work Order
    so = frappe.get_value("Work Order", doc.work_order, "sales_order")
    item_code = frappe.get_value("Work Order", doc.work_order, "production_item")

    if not so or not item_code:
        frappe.msgprint("Missing Sales Order or Production Item in Work Order.")
        return

    # Fetch SO Item details
    so_item = frappe.get_value(
        "Sales Order Item",
        {"parent": so, "item_code": item_code},
        ["name", "qty"],
        as_dict=True
    )

    if not so_item:
        frappe.msgprint(f"No Sales Order Item found for {item_code} in {so}")
        return

    row_name = so_item.name
    qty = so_item.qty

    # Loop through Stock Entry Items
    for row in doc.items:
        if not row.is_finished_item:
            continue

        projected_qty = frappe.db.get_value(
            "Bin",
            {"item_code": row.item_code, "warehouse": row.t_warehouse},
            "projected_qty"
        ) or 0

        # Skip if no stock projection
        if projected_qty <= 0:
            frappe.msgprint(f"No projected stock in warehouse {row.t_warehouse} for item {row.item_code}")
            continue

        # Create Stock Reservation Entry
        stock_reserve = frappe.get_doc({
            "doctype": "Stock Reservation Entry",
            "item_code": row.item_code,
            "warehouse": row.t_warehouse,
            "voucher_type": "Sales Order",
            "voucher_no": so,
            "voucher_detail_no": row_name,
            "voucher_qty": qty,
            "reserved_qty": frappe.get_value("Work Order", doc.work_order, "produced_qty") or 0,
            "available_qty": projected_qty,
            "company": doc.company
        })

        stock_reserve.insert(ignore_permissions=True)
        stock_reserve.submit()

    frappe.msgprint("Stock Reservation Entry created successfully")

    