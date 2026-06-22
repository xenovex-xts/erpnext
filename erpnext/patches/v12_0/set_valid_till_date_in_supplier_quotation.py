# import frappe


# def execute():
# 	frappe.reload_doc("buying", "doctype", "supplier_quotation")
# 	frappe.db.sql(
# 		"""UPDATE `tabSupplier Quotation`
# 		SET valid_till = DATE_ADD(transaction_date , INTERVAL 1 MONTH)
# 		WHERE docstatus < 2"""
# 	)


import frappe


def execute():
	frappe.reload_doc("buying", "doctype", "supplier_quotation")

	if frappe.db.db_type == "postgres":
		frappe.db.sql(
			"""
			UPDATE "tabSupplier Quotation"
			SET valid_till = transaction_date + INTERVAL '1 month'
			WHERE docstatus < 2
			"""
		)
	else:
		frappe.db.sql(
			"""
			UPDATE `tabSupplier Quotation`
			SET valid_till = DATE_ADD(transaction_date, INTERVAL 1 MONTH)
			WHERE docstatus < 2
			"""
		)