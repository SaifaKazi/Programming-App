frappe.query_reports["Script  Report Demo 2"] = {
    filters: [
        {
            fieldname: "quotation",
            label: "Quotation",
            fieldtype: "Link",
            options: "Quotation",
			// "reqd":1
        },
		 {
            fieldname: "so",
            label:("Sales Order"),
            fieldtype: "Link",
            options: "Sales Order",
            "reqd":0
        },
		{
            fieldname: "dn",
            label: "Delivery Note",
            fieldtype: "Link",
            options: "Delivery Note",
        },
        {
            fieldname: "si",
            label: "Sales Invoice",
            fieldtype: "Link",
            options: "Sales Invoice",
        },
        {

            fieldname:"pe",
            label: "Payment Entry",
            fieldtype: "Link",
            options: "Payment Entry",
        }
    ]
};
