# Copyright (c) 2025, D codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ClientSideScripting(Document):
	pass

@frappe.whitelist()
def frappe_call(msg):
	import time
	time.sleep(3)
	frappe.msgprint(msg)
	# self.mobile_number = 9879797979
	# return f"msg from frappe_call: {msg}"

