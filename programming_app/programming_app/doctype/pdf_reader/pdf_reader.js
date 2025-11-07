// Copyright (c) 2025, D codE and contributors
// For license information, please see license.txt

frappe.ui.form.on("PDF Reader", {
    attach_pdf: function(frm) {
        if (frm.doc.attach_pdf) {
            frappe.call({
                method: "exreact_pdf",
                doc: frm.doc,
                freeze: true,
                freeze_message: "Extracting PDF data...",
                callback: function(r) {
                    frm.reload_doc();
                }
            });
        }
    }
});