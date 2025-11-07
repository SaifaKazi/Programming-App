// Copyright (c) 2025, D codE and contributors
// For license information, please see license.txt

frappe.ui.form.on("Server Side Scripting1", {
    enable: function(frm) {
        frappe.call({
            method: "programming_app.programming_app.doctype.client_side_scripting.client_side_scripting.frappe_call",
            args: { msg: "Hello Saifa" },
            freeze: true,
            freeze_message: __('Calling frappe_call Method'),
            callback: function(r) {
                // frappe.msgprint(r.message)
            }
        });
    }
});