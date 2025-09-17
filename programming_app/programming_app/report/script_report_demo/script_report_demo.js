// Copyright (c) 2025, D codE and contributors
// For license information, please see license.txt

frappe.query_reports["Script Report Demo"] = {
	"filters": [
		{
			"fieldname":"item_code",
			"label":("Item Code"),
			"fieldtype":"Link",
			"options":"Server Side Scripting"
		},
		{
			"fieldname":"is_active",
			"label":("Is Active"),
			"fieldtype":"Check",
		}
	]
};