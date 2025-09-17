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
			'first_name':d.first_name,
			'middle_name':d.middle_name,
			'last_name':d.last_name,
			'full_name':d.full_name,
			'email':d.email,
			'dob':d.dob,
			'age':d.age
		})
		data.append(row)


	return columns,data

def get_columns():
	return[
		{
			'fieldname':'first_name',
			'label':('First Name'),
			'fieldtype':'Data',
			'width':'90'
		},
		{
			'fieldname':'middle_name',
			'label':('Middle Name'),
			'fieldtype':'Data',
			'width':'90'
		},
		{
			'fieldname':'last_name',
			'label':('last Name'),
			'fieldtype':'Data',
			'width':'90'
		},
		{
			'fieldname':'full_name',
			'label':('Full Name'),
			'fieldtype':'Data',
			'width':'90'
		},
		{
			'fieldname':'email',
			'label':('Email'),
			'fieldtype':'Data',
			'width':'90'
		},
		{
			'fieldname':'dob',
			'label':('DOB'),
			'fieldtype':'Date',
			'width':'90'
		},
		{
			'fieldname':'age',
			'label':('Age'),
			'fieldtype':'Data',
			'width':'90'
		}
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype=('Server Side Scripting1'),
		fields=('first_name','middle_name','full_name','last_name','email','dob','age'),
		filters=conditions,
		
	)
	return data

def get_conditions(filters):
	conditions={}
	for key,value in filters.items():
		if filters.get(key):
			conditions[key]=value
	return conditions