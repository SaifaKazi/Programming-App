# Copyright (c) 2025, D codE and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ServerSideScripting1(Document):
    pass
	# def validate(self):
	# 	frappe.msgprint("validate event")
	# def before_save(self):
	# 	frappe.msgprint("before_save event")
	# def before_insert(self):
	# 	frappe.msgprint("before_insert event")
	# def after_insert(self):
	# 	frappe.throw("after_insert event")
	# def on_update(self):
	# 	frappe.msgprint("on_update event")
	# def before_submit(self):
	# 	frappe.msgprint("before_submit event")
	# def on_submit(self):
	# 	frappe.msgprint("on_submit event")
	# def on_cancel(self):
	# 	frappe.msgprint("on_cancel event")
	# def on_trash(self):
	# 	frappe.msgprint("on_trash event")#when cancel the form and delete it will triger
	# def after_delete(self):
	# 	frappe.msgprint("after_delete event")
    
# **************set_value
	# frappe.db.get_value(doctype,name,fieldname) or frappe.db.get_value(doctype,filters,fieldname)
    
	# def validate(self):
	# 	self.get_value()
	# def get_value(self):
	# 	first_name,age=frappe.db.get_value('Client Side Scripting','PR-0001',['first_name','age'])
	# 	frappe.msgprint(_("the parent first name is {0} and age is {1}").format(first_name,age))

# **************get_value
    # frappe.db.set_value(doctype,name,fieldname,value)

	# def validate(self):
	# 	self.set_value()
	# def set_value(self):
	# 	frappe.db.set_value('Client Side Scripting','PR-0001','age',25)
	# 	first_name,age=frappe.db.get_value('Client Side Scripting','PR-0001',['first_name','age'])
	# 	frappe.msgprint(_("the parent first name is {0} and new age is {1}").format(first_name,age))
    
	# *******exists method
    # frappe.db.exists(doctype,name)
	# def validate(self):
	# 	if frappe.db.exists('Client Side Scripting','PR-0001'):
	# 		frappe.msgprint(_("the document is exists in database"))
	# 	else:
	# 		frappe.msgprint(_("the document does not exists in database"))
    
	#*******count method for count doctype
    #frappe.db.count(doctype,filters)
    # def validate(self):
    #     doc_count=frappe.db.count('Client Side Scripting',{'enable:1'})
    #     frappe.msgprint(_("the Enable document count is {0}").format(doc_count))
    
	#******sql
    #frappe.db.sql(query,filters,as_dict)
    # def validate(self):
    #     self.sql()

    # def sql(self):
    #     data = frappe.db.sql("""
    #         SELECT
    #             first_name,
    #             age
    #         FROM
    #             `tabClient Side Scripting`
    #         WHERE
    #             enable = 1
    #     """, as_dict=1)

    #     for d in data:
    #         frappe.msgprint(_("The parent first name is {0} and age is {1}").format(d.first_name, d.age))
    
	#*********fatch value
    # def validate(self):
    #     frappe.msgprint(_("my full name is '{0}'").format(
    #         self.first_name+ " " +self.middle_name+ " " +self.last_name))
    
	#**********fatch values from child table
    # def validate(self):
    #     for row in self.get("family_members"):
    #         frappe.msgprint(_("{0}. the family member name is '{1}' and relation is '{2}'").format(row.idx,row.name1,row.relation))
    
	#**********get_doc
    #***********frappe.get_doc(doctype,name)
	# def validate(self):
	# 	self.get_document()
	# def get_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
	# 	frappe.msgprint(_("The first name is {0} and age is {1}").format(doc.first_name, doc.age))

	# 	for row in doc.get("family_members"):
	# 		frappe.msgprint(_("{0}. The family member name is '{1}' and relation is '{2}'").format(row.idx, row.name1, row.relation))

	#************new doc (frappe.new_doc(doctype)
	# def validate(self):
	# 	self.new_document()
		
	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'Saifa'
	# 	doc.last_name = 'Patel'
	# 	doc.age = 23
	# 	doc.append("family_members",{
	# 		"name1":"Jishan",
	# 		"relation":"Husband",
	# 		"age":29
	# 	})
	# 	doc.insert()	
    
	#************delete doc (frappe.delete_doc(doctype,name)
    # def validate(self):
    #     frappe.delete_doc('Client Side Scripting','PR-0001')
    
	# *******some escape hatches that can be used to skip certain checks
	# doc .insert(
	# 	ignore_permissions=True, #ignore write permissions during insert
	# 	ignore_links=True, #ignore link validation in the document
	# 	ignore_if_duplicate=True, #dont insert if DuplicateEntryError is thrown
	# 	ignore_mandatory=True #insert even if mandatory fields are not set
	# )
    
	# #*******doc.save()
	# def validate(self):
	# 	self.save_document()
	# def save_document(self):
	# 	doc=frappe.new_doc('Client Side Scripting')
	# 	doc.first_name='Daya',
	# 	doc.age=44
	# 	doc.save()
		
	# 	doc.save(
	# 		ignore_permissions=True,
	# 		ignore_version=True
	# 	)
    
	#*********doc.delete()
    # def validate(self):
    #     self.delete_document()
    # def delete_document(self):
    #     doc=frappe.get_doc('Client Side Scripting','PR-0003')
    #     doc.delete()
        
	# #********doc.db_set()
    # def validate(self):
    #     self.db_set_document()
    # def db_set_document(self):
    #     doc=frappe.get_doc('Client Side Scripting','PR-0011')
    #     doc.db_set('last_name','Gada')
    
	#*********get_list
    # # frappe.db.get_list(doctype,filters, or_filters,fields,order_by,group_by,start,page_length)
    # def validate(self):
    #     self.get_list()
    # def get_list(self):
    #     doc=frappe.db.get_list('Client Side Scripting',filters={'enable':1},fields=['first_name','age'])
    #     for d in doc:
    #         frappe.msgprint(_("the parent first name {0} and age is {1}").format(d.first_name,d.age))
    
	#frm.call
    # @frappe.whitelist()
    # def frm_call(self,msg):
    #     # import time
    #     # time.sleep(5)
    #     # frappe.msgprint(msg)
    #     # self.mobile_number = 9879797979
    #     return "msg from frm_call"
    
	# @frappe.whitelist()
	# def frm_call(self, msg):
	# 	return f"Message from Python: {msg}"