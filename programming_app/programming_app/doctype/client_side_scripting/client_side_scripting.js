// Copyright (c) 2025, D codE and contributors
// For license information, please see license.txt

//*******Set a value in Doc Fields:-
// frappe.ui.form.on("Client Side Scripting", {
// 	refresh(frm) {
//         // frappe.msgprint("hello")
//         // frappe.throw("Error msg")
        
// 	},
// });

//******Add static values to child table:-
// frappe.ui.form.on("Client Side Scripting",{
//     validate:function(frm){
//         // frm.set_value("full_name",frm.doc.first_name +" "+ frm.doc.middle_name +" "+ frm.doc.last_name)
//         let row = frm.add_child("family_members",{
//         name1:'Samir Kazi',//set static values 
//         relation:'Father',
//         age:56,
//         })
//         // frm.refresh_field("family_members");
//     }
// });

//*******setup doc field property using client side scripting:-
// frappe.ui.form.on("Client Side Scripting",{
//     enable:function(frm){ //"enable" is the fieldname of a checkbox field in your DocType..uspar trigger hoga
//         frm.set_df_property('first_name','reqd',1)
//         frm.set_df_property('middle_name','read_only',1)
//         frm.toggle_reqd('age',true) //also work like read only method
//     }
// });

 //********Add Cutom Button:-
// frappe.ui.form.on("Client Side Scripting",{
//     refresh:function(frm){
//         frm.add_custom_button('Button 1',() => {
//             frappe.msgprint("You Clicked !")
//         })
//         // dropdown button
//         frm.add_custom_button('Click Here 1',() => {
//             frappe.msgprint(__("You Clicked 1"));
//         },'Button 2')
//         frm.add_custom_button('Click Here 2',() => {
//             frappe.msgprint(__("You Clicked 2"));
//         },'Button 2')
//     }
// });

//*******Fatch Value:-(from field)
// frappe.ui.form.on("Client Side Scripting",{
//     after_save:function(frm){
//         frappe.msgprint(__("the full name is '{0}'",
//             [frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name]
//         ))
        //*******Fatch Value:-(from child table)
//         for(let row of frm.doc.family_members){
//             frappe.msgprint(__("{0}. the famil member name is '{1}' and reln is '{2}'",
//                 [row.idx,row.name1,row.relation]
//             ))
//         }
//     }
//  });

//********set_intro in document :-
// frappe.ui.form.on("Client Side Scripting",{
//     refresh:function(frm){
//     // frm.set_intro("now you can crate new Client Side Scripting doctype")
//         if(frm.is_new()){
//             frm.set_intro("now you can crate new Client Side Scripting doctype")
//         } 
//     }
// });

//******events
// frappe.ui.form.on("Client Side Scripting",{
//     refresh:function(frm){
//         frappe.msgprint("refresh event")
//     },
//     onload:function(frm){
//         frappe.msgprint("onload event")
//     },
//     validate:function(frm){
//         frappe.throw("'validate' event")
//     },
//     before_save:function(frm){
//         frappe.throw("before_save event")
//     },
//     after_save:function(frm){
//         frappe.throw("after_save event")
//     },
//     enable:function(frm){ //this is fieid based event trriger
//         frappe.msgprint("enable event")
//     },
//     age:function(frm){ //this is fieid based event trriger
//         frappe.msgprint("age event")
//     },
//     family_members_on_form_rendered:function(frm){ //trriger fuction when add a child table row.(child table ke row ke edit pr click karne ke bad ye trriger click hoga)
//         frappe.msgprint("family_member_on_form_rendered event")
//     },
//     before_submit:function(frm){ 
//         frappe.throw("before_submit event")
//     },
//     on_submit:function(frm){ 
//         frappe.msgprint("on_submit event")
//     },
//     before_cancel:function(frm){ 
//         frappe.throw("before_cancel event")
//     },
//     after_cancel:function(frm){ 
//         frappe.msgprint("after_cancel event")
//     },        
// });

// ***************************************************************
//*******event trrigring using child table fields:-
// frappe.ui.form.on('Family Members',{
//     // name1:function(frm){ //it will trriger name1 event and print msg
//     //     frappe.msgprint("hello")
//     // }

//     age(frm,cdt,cdn){ //This is an event handler for the age field of the child table.
//         frappe.msgprint("hello")
//     }
// })