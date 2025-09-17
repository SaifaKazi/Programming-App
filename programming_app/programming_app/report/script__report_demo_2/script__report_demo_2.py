# Copyright (c) 2025, D codE and contributors
# For license information, please see license.txt

import frappe

def execute(filters):
	# frappe.errprint(filter)
    columns, data = [], []
    columns = get_columns(filters)
    data = get_data(filters)
    return columns,data

def get_columns(filters):
    columns = [
       {
			"fieldname":"quotation",
			"label":("Quotation"),
			"fieldtype":"Link",
            "options":"Quotation",
			"width":"200"
		},
        {
			"fieldname":"so",
			"label":("Sales Order"),
			"fieldtype":"Link",
            "options":"Sales Order",
			"width":"200"
		},
		 {
			"fieldname":"dn",
			"label":("Delivery Note"),
			"fieldtype":"Link",
            "options":"Delivery Note",
			"width":"200"
		},
		{
			"fieldname":"si",
			"label":("Sales Invoice"),
			"fieldtype":"Link",
			"options":"Sales Invoice",
			"width":"200"
		},
		{
			"fieldname":"pe",
			"label":("Payment Entry"),
			"fieldtype":"Link",
			"options":"Payment Entry",
			"width":"200"
		}

	]
    return columns


def get_data(filters):
	filter={}
	data = []
	if filters.get("quotation"):
		so_filters = {"prevdoc_docname":filters.get("quotation")}
		if filters.get("so"):
			so_filters["parent"] = filters.get("so")
		so_list = frappe.get_all("Sales Order Item",so_filters,"distinct(parent) as parent")
		for so in so_list:
			dn_filters={"against_sales_order":so.get("parent")}
			if filters.get("dn"):
				dn_filters["parent"]=filters.get("dn")			
			dn_list = frappe.get_all("Delivery Note Item",dn_filters,"distinct(parent) as parent") 
			if dn_list:
				for dn in dn_list:
					si_filters ={"delivery_note":dn.get("parent")}
					if filters.get("si"):
						si_filters["parent"] =filters.get("si")
					si_list = frappe.get_all("Sales Invoice Item",si_filters,"distinct(parent) as parent")
					if si_list:
						for si in si_list:
							pe_filters={"reference_name":si.get("parent")}
							if filters.get("pe"):
								pe_filters["parent"]=filters.get("pe")
							pe_list=frappe.get_all("Payment Entry Reference",pe_filters,"distinct(parent) as parent")
							if pe_list:
								for pe in pe_list:
									data.append({
										"quotation": filters.get("quotation"),
										"so": so.get("parent"),
										"dn": dn.get("parent"),
										"si": si.get("parent"),
										"pe": pe.get("parent")
							})
							else:
								data.append({
								"quotation": filters.get("quotation"),
								"so": so.get("parent"),
								"dn": dn.get("parent"),
								"si": si.get("parent"),
								})
					else:
						data.append({
								"quotation": filters.get("quotation"),
								"so": so.get("parent"),
								"dn": dn.get("parent"),
							})
					
			else:
				data.append({
						"quotation":filters.get("quotation"),
						"so":so.get("parent"),
					})
				
				
				
	return data
        


# def get_data(filters):
# 	if not filters.get("quotation"):
# 		return []

# 	quotation = filters.get("quotation")

# 	query = """
# 		SELECT
# 			q.name AS quotation,
# 			so_item.parent AS so,
# 			dn_item.parent AS dn,
# 			si_item.parent AS si,
#             pe_item.parent AS pe
# 		FROM
# 			`tabQuotation` q
# 		LEFT JOIN
# 			`tabSales Order Item` so_item ON so_item.prevdoc_docname = q.name
# 		LEFT JOIN
# 			`tabDelivery Note Item` dn_item ON dn_item.against_sales_order = so_item.parent
# 		LEFT JOIN
# 			`tabSales Invoice Item` si_item ON si_item.delivery_note = dn_item.parent
#         LEFT JOIN
# 			`tabPayment Entry Reference` pe_item ON pe_item.reference_name = si_item.parent
# 		WHERE
# 			q.name = %s
# 		GROUP BY
# 			so_item.parent, dn_item.parent, si_item.parent, pe_item.parent
# 	"""

# 	return frappe.db.sql(query, (quotation,), as_dict=True)



