# Copyright (c) 2025, D codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate


class ManufacturingProcess(Document):
    # def on_submit(self):
    #     self.create_stock_entry()
    @frappe.whitelist()
    def calculate_base_quantity(self):
        if self.base_item and self.packaging_quantity:
            uoms = frappe.get_all(
                "UOM Conversion Detail",
                filters={"parent": self.base_item, "uom": "Litre"},
                fields=["conversion_factor"],
                limit_page_length=1
            )
            if uoms:
                conversion_factor = uoms[0].conversion_factor
                self.base_quantity = self.packaging_quantity * conversion_factor

@frappe.whitelist()
def get_boms_for_packaging_item(packaging_item):
    """
    Fetch all BOM names linked to the selected packaging item.
    Returns a list of BOM names.
    """
    if not packaging_item:
        return []
        # Fetch BOMs where item matches the selected packaging_item
    boms = frappe.get_all("BOM",filters={"item": packaging_item, "is_active": 1, "is_default": 1},pluck="item")
    return boms


@frappe.whitelist()
def get_boms_for_base_item(base_item):
    """
    Fetch all BOM names linked to the selected packaging item.
    Returns a list of BOM names.
    """
    if not base_item:
        return []
    
    # Fetch BOMs where item matches the selected packaging_item
    boms = frappe.get_all("BOM",filters={"item": base_item, "is_active": 1, "is_default": 1},pluck="item")
    return boms





