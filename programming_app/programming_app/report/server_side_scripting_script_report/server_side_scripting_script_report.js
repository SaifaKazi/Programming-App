// Copyright (c) 2025, D codE and contributors
// For license information, please see license.txt

frappe.query_reports["Server Side Scripting Script Report"] = {
	"filters": [
		{
			"fieldname":"first_name",
			"label":("First Name"),
			"fieldtype":"Link",
			"options":"Server Side Scripting1",
			"reqd": 0,
		},
		{
			"fieldname":"middle_name",
			"label":("Middle Name"),
			"fieldtype":"Link",
			"options":"Server Side Scripting1"
		},
		{
			"fieldname":"last_name",
			"label":("Last Name"),
			"fieldtype":"Link",
			"options":"Server Side Scripting1"
		},
		{
			"fieldname":"full_name",
			"label":("Full Name"),
			"fieldtype":"Link",
			"options":"Server Side Scripting1"
		},
		{
			"fieldname":"email",
			"label":("Email"),
			"fieldtype":"Data",
			"options":"Server Side Scripting1"
		},
		{
			"fieldname":"dob",
			"label": ("DOB"),
			"fieldtype":"Date",
		},
		{
			"fieldname":"age",
			"label":("Age"),
			"fieldtype":"Data",
		}
	]
};

