# Copyright (c) 2025
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import fitz  # PyMuPDF
import re
import os


class PDFReader(Document):
    @frappe.whitelist()
    def exreact_pdf(self):
        frappe.msgprint("Starting PDF extraction...")

        if not self.attach_pdf:
            frappe.throw("Please attach a PDF first.")

        # Get file path from File doctype
        file_doc = frappe.get_doc("File", {"file_url": self.attach_pdf})
        file_path = frappe.get_site_path("public", file_doc.file_url.replace("/files/", "files/"))

        # Read text from PDF
        text = ""
        with fitz.open(file_path) as pdf:
            for page in pdf:
                text += page.get_text("text")  # normal text
                # If you also want table-like extraction, you can use 'blocks' or 'words' methods.

        # Extract using regex or keywords
        self.name1 = self.extract_value(text, r"Name\s*[:\-]?\s*(.*)")
        self.age = self.extract_value(text, r"Age\s*[:\-]?\s*(\d+)")
        self.company = self.extract_value(text, r"Company\s*[:\-]?\s*(.*)")
        self.pincode = self.extract_value(text, r"Pincode\s*[:\-]?\s*(\d+)")

        # You can extract second set of data similarly
        self.name11 = self.extract_value(text, r"Name1\s*[:\-]?\s*(.*)")
        self.age1 = self.extract_value(text, r"Age1\s*[:\-]?\s*(\d+)")
        self.address1 = self.extract_value(text, r"Address1\s*[:\-]?\s*(.*)")
        self.pincode1 = self.extract_value(text, r"Pincode1\s*[:\-]?\s*(\d+)")

        self.save(ignore_permissions=True)
        frappe.msgprint("PDF data extracted successfully!")

    def extract_value(self, text, pattern):
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return ""