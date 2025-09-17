function update_total_and_amount(frm) {
    // Calculate total per hours salary
    let total_per_hours = frm.doc.custom_labour_details.reduce((acc, row) => {
        return acc + (row.per_hours_salary || 0);
    }, 0);

    // Update custom_total_per_hours_salary
    frappe.model.set_value(frm.doctype, frm.docname, "custom_total_per_hours_salary", total_per_hours);
    frm.refresh_field("custom_total_per_hours_salary");

    // Update amount in Landed Cost Taxes and Charges for Direct Income - S
    frm.doc.additional_costs.forEach(row => {
        if (row.expense_account === "Direct Income - S") {
            row.amount = total_per_hours;
        }
    });
    frm.refresh_field("additional_costs");
}
frappe.ui.form.on('Labour Charges Details', { //for Labour Details child table
    employee: function (frm,cdt,cdn) {  // //access specific field
        let d = locals[cdt][cdn];
        let duplicate = frm.doc.custom_labour_details.some(row => 
            row.employee === d.employee && row.name !== d.name
        );

        if (duplicate) {
            frappe.msgprint(`Employee ${d.employee_name} already exists!`);
            d.employee = ""; 
            frm.refresh_field("custom_labour_details");
            return; 
        }

        frappe.call({
            method: "programming_app.public.py.stock_entry.data", 
            args:{
                doc: frm.doc,
            },
            callback:function(r){
               if(r.message){
                    let emp_data = r.message.find(e => e.employee === d.employee);
                    if(emp_data){
                        d.salary = emp_data.base;           
                        d.day_salary = emp_data.day_salary; 
                        d.per_hours_salary = emp_data.per_hours_salary;
                        frm.refresh_field("custom_labour_details");
                        let total_per_hours = frm.doc.custom_labour_details.reduce((acc, row) => {
                            return acc + (row.per_hours_salary || 0);
                        }, 0);

                        frappe.model.set_value(frm.doctype, frm.docname, "custom_total_per_hours_salary", total_per_hours);
                        frm.refresh_field("custom_total_per_hours_salary");
                        update_total_and_amount(frm);

                    }
                }
                
            }
        });
    },

    custom_labour_details_remove: function(frm, cdt, cdn) { //function for Labour Details child table 
        update_total_and_amount(frm);
        // let total_per_hours = frm.doc.custom_labour_details.reduce((acc, row) => {
        //     return acc + (row.per_hours_salary || 0);}, 0);

        // frappe.model.set_value(frm.doctype, frm.docname, "custom_total_per_hours_salary", total_per_hours);
        // frm.refresh_field("custom_total_per_hours_salary");
        }
    });
frappe.ui.form.on('Landed Cost Taxes and Charges', { //for Additional Costs child table 
    expense_account: function(frm, cdt, cdn) {     //access specific field
        let d = locals[cdt][cdn];
        let duplicate = frm.doc.additional_costs.some(row => 
            row.expense_account === "Direct Income - S" && row.name !== d.name
        );

        if (duplicate && d.expense_account === "Direct Income - S") {
            frappe.msgprint("Direct Income - S already exists!");
            d.expense_account = ""; 
            frm.refresh_field("landed_cost_taxes_and_charges");
            return;
        }
        if(d.expense_account === "Direct Income - S") {
            d.amount = frm.doc.custom_total_per_hours_salary || 0;
            d.description =  "Direct Income - S"

            frm.refresh_field("landed_cost_taxes_and_charges");
        }
    },

});

