// Copyright (c) 2025, D codE and contributors
// For license information, please see license.txt
// frappe.ui.form.on("Child Doc", {
// 	refresh(frm) {

// 	},
// });

// frappe.ui.form.on('Child Doc',{
// 	parent_doc_link:function(frm){
// 			frappe.call({
// 				method:"frappe.client.get",
// 				args:{
// 					doctype:"Parent Doc",
// 					name:frm.doc.parent_doc_link,
// 				},
// 				callback:(r)=>{
// 					if(r.message){
// 						frm.set_value('parent_full_name',r.message.full_name)
// 						frm.set_value('parent_age',r.message.age)
// 						frm.set_value('parent_present_address',r.message.present_address)
// 					}
// 				}
// 		});
// 	}
// 				   });


frappe.ui.form.on('Child Doc',{
	button:function(frm){
			frappe.call({
				method:"list_all_parent_docs",
                doc:frm.doc,
				args:{
					doctype:"Parent Doc",
				},
				callback:(r)=>{
					frappe.msgprint("Successfully Updated")
                    frm.refresh_field('parent_list');
				}
		});
	}
				   });
