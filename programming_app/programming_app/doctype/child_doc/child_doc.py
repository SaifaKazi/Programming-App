# Copyright (c) 2025, D codE and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ChildDoc(Document):
	@frappe.whitelist()
	def list_all_parent_docs(self,doctype):
		data=frappe.get_all(doctype,fields=["*"])
		for d in data:
			self.append("parent_list",{
				"full_name":d.full_name,
				"age":d.age
			})
	# def validate(self):
	# 	frappe.msgprint(_("Hello frappe from 'validate' Event"))
    
	# def before_save(self):
	# 	frappe.msgprint(_("Hello frappe from 'before save' Event"))

	# def before_insert(self):
	# 	frappe.msgprint(_("Hello frappe from 'before_insert' Event"))

	# def before_submit(self):
	# 	frappe.msgprint(_("Hello frappe from 'before_submit' Event"))

	# def on_submit(self):
	# 	frappe.msgprint(_("Hello frappe from 'on_submit' Event"))

	# def on_cancel(self):
	# 	frappe.msgprint(_("Hello frappe from 'on_cancel' Event"))

	# def after_delete(self):
	# 	frappe.msgprint(_("Hello frappe from 'after_delete' Event"))
	
	
	
	# def validate(self):
	# 	self.get_value()
	# def get_value(self):
	# 	first_name, last_name = frappe.db.get_value('Parent Doc','Aanu',['first_name','last_name'])
	# 	frappe.msgprint(_("The parent First Name is {0} and Last Name is {1}").format(first_name,last_name))
	
	
	# def validate(self):
	# 	self.new_document()

	# def get_document(self):
	# 	doc = frappe.get_doc('Parent Doc',self.parent_doc_link)
	# 	frappe.throw(str(doc.as_dict()))#it is used to get all document in doctype
	# 	frappe.msgprint(_("The parent full name{0} and age is{1}").format(doc.full_name,doc.age))#use to get specific field in doctype
      
	# def new_document(self):
	# 	doc=frappe.new_doc('Parent Doc')
	# 	doc.first_name='Mona'
	# 	doc.last_name='KaziPatel'
	# 	doc.age=23
	# 	doc.save()


	# def validate(self):
	# 	frappe.delete_doc('Parent doc','Mona')



	# def validate(self):
	# 	self.new_document()
	# def new_document(self):
	# 	doc=frappe.new_doc('Parent Doc')
	# 	doc.first_name='Maya'
	# 	doc.last_name='Bhide'
	# 	doc.age=34
	# 	doc.insert()

	# def validate(self):
	# 	self.save_document()
	# def save_document(self):
	# 	doc=frappe.new_doc('Parent Doc')
	# 	doc.first_name='Radha'
	# 	doc.last_name='Joshi'
	# 	doc.age=23
	# 	doc.save()


	# def validate(self):
	# 	self.delete_document()
	# def delete_document(self):
	# 	doc=frappe.get_doc('Parent Doc','Radha')
	# 	doc.delete()


	# def validate(self):
	# 	self.db_set_document()
	# def db_set_document(self):
	# 	doc=frappe.get_doc('Parent Doc','Akash')
	# 	doc.db_set('age',45)


	# def validate(self):
	# 	self.get_list()
	# def get_list(self):
	# 	s_doc=frappe.db.get_list('Parent Doc', filters={'enable':1}, fields=['first_name','last_name'])
	# 	for d in s_doc:
	# 		frappe.msgprint(_("The Parent First Name is{0} and Last Name is{1}").format(d.first_name,d.last_name))


	# def validate(self):
	# 	if frappe.db.exists('Parent Doc','Neesha'):
	# 		frappe.msgprint(_('The document is exist in Database'))
	# 	else:
	# 		frappe.msgprint(_('The document in dose not exist in database'))


	# def validate(self):
	# 	doc_count=frappe.db.count('Parent Doc',{'enable':1})
	# 	frappe.msgprint(_("The Enable document count is{0}").format(doc_count))


	# def validate(self):
	# 	self.sql()
	# def sql(self):
	# 	data=frappe.db.sql("""
	# 				 SELECT 
	# 				 	first_name,
	# 				 	last_name
	# 				 from
	# 				 	`tabParent Doc`
	# 				 WHERE
	# 					enable=1
	# 				 """,as_dict=1)
	# 	for d in data:
	# 		frappe.msgprint(_("The Parent First Name is {0} and Last Name {1}").format(d.first_name,d.last_name))




























































































































































































































