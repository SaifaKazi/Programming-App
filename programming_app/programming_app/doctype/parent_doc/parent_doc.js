// Copyright (c) 2025, D codE and contributors
// For license information, please see license.txt

frappe.ui.form.on("Parent Doc", { 
// this control file is use for control the client side script of Parent Doc
//  refresh: function(frm) {
//     frappe.msgprint(__("Hello World from 'refresh' event"))
// }

//      
// validate: function(frm) {
//     frappe.throw(__("Hello World from 'validate' event")) //used to raise an exception and stop further execution of the code. validate event will triger before the save action.
// }  
// before_save: function(frm) {
//     frappe.throw(__("Hello World from 'before_save' event")) //used to raise an exception and stop further execution of the code. validate event will triger before the save action.
// }
// after_save: function(frm) {
//     frappe.throw(__("Hello World from 'after_save' event")) //used to raise an exception and stop further execution of the code. validate event will triger before the save action.
// }   
// enable: function(frm) {
//     frappe.throw(__("Hello World from 'enable' event")) //used to raise an exception and stop further execution of the code. validate event will triger before the save action.
//  }   ,
// age: function(frm) {
//     frappe.throw(__("Hello World from 'age' event")) //used to raise an exception and stop further execution of the code. validate event will triger before the save action.
// } 
// before_submit: function(frm) {
//     frappe.throw(__("Hello World from 'before_save' event")) //used to raise an exception and stop further execution of the code. validate event will triger before the save action.
// }
// on_submit: function(frm) {
//     frappe.throw(__("Hello World from 'on_save' event")) //used to raise an exception and stop further execution of the code. validate event will triger before the save action.
// }
// after_cancel: function(frm) {
//     frappe.throw(__("Hello World from 'after_cancel' event")) //used to raise an exception and stop further execution of the code. validate event will triger before the save action.
// }

// after_save:function(frm){
//     frappe.msgprint(__("The age is {0}",[frm.doc.age]))//fatch age
// }
// after_save:function(frm){
//     frappe.msgprint({
//         title:__("Notification"),
//         indicator: 'red',
//         message: __('Hello World')
//     });
// }

// refresh: function(frm) {
// //     frappe.msgprint(__("Hello World from 'refresh' event"))
// // }
// if(frm.is_new()){
// frm.set_intro('Now you can create a new parent doc type')
// }
// }


// validate:function(frm){
//     frm.set_value('full_name',frm.doc.first_name + "" + frm.doc.last_name)
// }


// refresh:function(frm){
//     if(frm.is_new()){
// let d=new frappe.ui.Dialog({
//     title: 'Enter the Parent Details',
//     fields:[{
//         label:'First Name',
//         fieldname:'first_name',
//         fieldtype:'Data'
//     },
//     {
//         label:'Last Name',
//         fieldname:'last_name',
//         fieldtype:'Data'
//     },
//     {
//         label:'Age',
//         fieldname:'age',
//         fieldtype:'Data'
//     }],
//     primary_action_label:'submit',
//     primary_action(values){
//         console.log(values)
//             frm.set_value('first_name',values.first_name)
//             frm.set_value('last_name',values.last_name )
//             frm.set_value('age',values.age )
//     d.hide()
//     }
// });
// d.show();
//     }


//     enable:function(frm){
//         if(frm.is_dirty()){
//         frappe.msgprint(__('plase save the document'))
    
// }

//     }
//    refresh:function(frm){
// frm.add_custom_button('Click Me',()=>{
//     frappe.msgprint(__('You Clicked !!'))
// },'Click Me !')
// frm.add_custom_button('Click Me 2',()=>{
//     frappe.msgprint(__('You Clicked 2 !!'))
// })

//    }



// refresh:function(frm){
//     if(!frm.is_new()){
//         frm.trigger('test_fun');
//     }
// },
// // enable:function(frm){
// //     frappe.msgprint(__('the event is triggered'))
// // }
// test_fun(frm){
//     frappe.msgprint(__('this massage is from test_fun'))
// }



enable:function(frm){
    let row = frm.add_child('date_and_values',{
        date:frappe.datetime.get_today(),
        value1:10,
        value2:20,
    })
    frm.refresh_field('date_and_values')
}
}); 