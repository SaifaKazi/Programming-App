# Copyright (c) 2025, D codE and contributors
# For license information, please see license.txt

# import frappe
import frappe 
from frappe.model.document import Document


class ParentDoc(Document):
	def on_(self):
		frappe.msgprint("Hello frappe")
    