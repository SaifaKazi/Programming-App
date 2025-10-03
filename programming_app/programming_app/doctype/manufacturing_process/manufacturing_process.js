// Copyright (c) 2025, D codE and contributors
// For license information, please see license.txt

frappe.ui.form.on("Manufacturing Process", {
    base_item: function(frm) {
        calculate_base_quantity(frm);
        filter_boms_for_base_item(frm); // Filter BOM2 when base_item changes
    },
    packaging_quantity: function(frm) {
        if(frm.doc.packaging_quantity && frm.doc.base_item) {
            frappe.call({
                method: "calculate_base_quantity",
                doc:frm.doc,
                callback: function(res) {
                    frm.refresh_fields()
                }
            });
        }
    },
    packaging_item: function(frm) {
        if (frm.doc.packaging_item) {
            frappe.db.get_value("Item", frm.doc.packaging_item, "custom_base_item")
                .then(r => {
                    if (r.message && r.message.custom_base_item) {
                        frm.set_value("base_item", r.message.custom_base_item);

                        calculate_base_quantity(frm);

                        filter_boms_for_base_item(frm);
                    } else {
                        frm.set_value("base_item", "");
                        frm.set_value("bom2", "");
                    }
                });

            filter_boms_for_packaging_item(frm);
        } else {
            frm.set_value("base_item", "");
            frm.set_value("bom1", "");
            frm.set_value("bom2", "");
        }
    },
    bom1: function(frm) {
        if (frm.doc.bom1) {
            frappe.db.get_doc('BOM', frm.doc.bom1)
            .then(bom_doc => {
                frm.clear_table('packing_items');
                
                (bom_doc.items || []).forEach(row => {
                    let child = frm.add_child('packing_items');
                    child.item_code = row.item_code;
                    child.qty = row.qty;
                    child.uom = row.uom;
                    child.item_name=row.item_name;
                    child.source_warehouse=row.source_warehouse;
                    if (frm.doc.packaging_quantity) {
                        child.required_qty = frm.doc.packaging_quantity * row.qty;
                    } 
                    else {
                        child.required_qty = 0;
                    }
                    if (child.item_code && child.source_warehouse) {
                    frappe.db.get_value('Bin', 
                        { item_code: child.item_code, warehouse: child.source_warehouse }, 
                        'actual_qty'
                    ).then(r => {
                        child.available_qty_at_warehouse = r.message ? r.message.actual_qty : 0;
                        frm.refresh_field('packing_items');
                    });
                }
                });

                frm.refresh_field('packing_items');
            });
        }
    },
    bom2: function(frm) {
    if (frm.doc.bom2) {
        frappe.db.get_doc('BOM', frm.doc.bom2)
        .then(bom_doc => {
            frm.clear_table('table_loet');
            
            let bom_qty = bom_doc.quantity || 1;
            (bom_doc.items || []).forEach(row => {
                let child = frm.add_child('table_loet');
                child.item_code = row.item_code;
                child.qty = row.qty;
                child.uom = row.uom;
                child.item_name = row.item_name;
                child.source_warehouse = row.source_warehouse;

                // required_qty = base_quantity * row.qty
                if (frm.doc.base_quantity) {
                    child.required_qty = (frm.doc.base_quantity * row.qty) / bom_qty;
                } else {
                    child.required_qty = 0;
                }

                // Fetch actual_qty from Bin for this item + warehouse
                if (child.item_code && child.source_warehouse) {
                    frappe.db.get_value('Bin', 
                        { item_code: child.item_code, warehouse: child.source_warehouse }, 
                        'actual_qty'
                    ).then(r => {
                        child.available_qty_at_warehouse = r.message ? r.message.actual_qty : 0;
                        frm.refresh_field('table_loet');
                    });
                }
            });
                frm.refresh_field('table_loet');
            });
        }
    },
    refresh: function(frm) {
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__('Finished Base Item'), function() {
                frappe.model.with_doctype('Manufacturing Process', function() {
                    let stock_entry = frappe.model.get_new_doc('Stock Entry');
                    stock_entry.stock_entry_type="Manufacture";
                    stock_entry.from_bom = 1;
                    stock_entry.bom_no = frm.doc.bom2;
                    stock_entry.fg_completed_qty=frm.doc.base_quantity;
                    // stock_entry.items=frm.doc.table_loet;
                    
                    frappe.set_route('Form', 'Stock Entry', stock_entry.name);
                });
            })
        }
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__('Finished Packaging Item'), function() {
                frappe.model.with_doctype('Manufacturing Process', function() {
                    let stock_entry = frappe.model.get_new_doc('Stock Entry');
                    stock_entry.stock_entry_type="Manufacture";
                    stock_entry.from_bom = 1;
                    stock_entry.bom_no = frm.doc.bom1;
                    stock_entry.fg_completed_qty=frm.doc.packaging_quantity;
                    // stock_entry.items=frm.doc.packing_items;
                    
                    frappe.set_route('Form', 'Stock Entry', stock_entry.name);
                });
            })
        }
    },
    
});

function calculate_base_quantity(frm) {
    if (frm.doc.base_item && frm.doc.packaging_quantity) {
        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "UOM Conversion Detail",
                filters: { parent: frm.doc.base_item, uom: "Litre" },
                fields: ["conversion_factor"],
                limit_page_length: 1
            },
            callback: function(res) {
                if (res.message && res.message.length > 0) {
                    let conversion_factor = res.message[0].conversion_factor;
                    frm.set_value("base_quantity", frm.doc.packaging_quantity * conversion_factor);
                }
            }
        });
    }
}

function filter_boms_for_packaging_item(frm) {
    if (!frm.doc.packaging_item) return;

    frappe.call({
        method: "programming_app.programming_app.doctype.manufacturing_process.manufacturing_process.get_boms_for_packaging_item",
        args: { packaging_item: frm.doc.packaging_item },
        callback: function(res) {
            let bom_list = res.message || [];

            frm.set_query("bom1", () => ({ filters: { item: ["in", bom_list] } }));

            if (frm.doc.bom1 && !bom_list.includes(frm.doc.bom1)) {
                frm.set_value("bom1", "");
                frappe.msgprint("Selected BOM does not belong to the selected Packaging Item. Please choose a valid BOM.");
            }

            if (bom_list.length === 0) {
                frm.set_value("bom1", "");
            }
        }
    });
}
function filter_boms_for_base_item(frm) {
    if (!frm.doc.base_item) return;

    frappe.call({
        method: "programming_app.programming_app.doctype.manufacturing_process.manufacturing_process.get_boms_for_base_item",
        args: { base_item: frm.doc.base_item },
        callback: function(res) {
            let bom_list = res.message || [];

            frm.set_query("bom2", () => ({ filters: { item: ["in", bom_list] } }));

            if (frm.doc.bom2 && !bom_list.includes(frm.doc.bom2)) {
                frm.set_value("bom2", "");
                frappe.msgprint("Selected BOM does not belong to the selected Packaging Item. Please choose a valid BOM.");
            }

            if (bom_list.length === 0) {
                frm.set_value("bom2", "");
            }
        }
    });
}
frappe.ui.form.on("Base Items",{
    source_warehouse: function(frm,cdt, cdn) {
        let row = locals[cdt][cdn];
        if(row.item_code && row.source_warehouse) {
            frappe.db.get_value('Bin', {
                item_code: row.item_code,
                warehouse: row.source_warehouse
            }, 'actual_qty').then(r => {
                if(r.message) {
                    row.available_qty_at_warehouse = r.message.actual_qty
                 
                } else {
                    row.available_qty_at_warehouse = 0
                }
                frm.refresh_fields()
            });
        } else {
            row.available_qty_at_warehouse = 0

        }
    },

})
frappe.ui.form.on("Packaging Items",{
    source_warehouse: function(frm,cdt, cdn) {
        let row = locals[cdt][cdn];
        if(row.item_code && row.source_warehouse) {
            frappe.db.get_value('Bin', {
                item_code: row.item_code,
                warehouse: row.source_warehouse
            }, 'actual_qty').then(r => {
                if(r.message) {
                    row.available_qty_at_warehouse = r.message.actual_qty
                 
                } else {
                    row.available_qty_at_warehouse = 0
                }
                frm.refresh_fields()
            });
        } else {
            row.available_qty_at_warehouse = 0

        }
    },
})




