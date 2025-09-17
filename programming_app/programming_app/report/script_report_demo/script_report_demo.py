# Copyright (c) 2025, D codE and contributors
# For license information, please see license.txt

import frappe
from frappe import msgprint
from frappe import _

def execute(filters=None):
	if not filters:filters={}
	columns, data = [], []
	columns=get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		msgprint(_('No record found..'))
		return columns,cs_data
	
	data=[]
	for d in cs_data:
		row=frappe._dict({
		    'item_code':d.item_code,
			'item_name':d.item_name,
			'uom':d.uom,
			'is_active':d.is_active
		})
		data.append(row)
	return columns,data

def get_columns():
	return[
		{
			"fieldname":"item_code",
			"label":("Item Code"),
			"fieldtype":"data",
			"width":"90"
		},
		{
			"fieldname":"item_name",
			"label":("Item Name"),
			"fieldtype":"data",
			"width":"90"
		},
		{
			"fieldname":"uom",
			"label":("UOM"),
			"fieldtype":"link",
			"width":"90"
		},
		{
			"fieldname":"is_active",
			"label":("Is Active"),
			"fieldtype":"check",
			"width":"90"
			
		}
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype=('Server Side Scripting'),
		fields=('item_code','item_name','uom','is_active'),
		filters=conditions,
		order_by='item_code desc'
	)
	return data

def get_conditions(filters):
	conditions={}
	for key,value in filters.items():
		if filters.get(key):
			conditions[key]=value
	return conditions