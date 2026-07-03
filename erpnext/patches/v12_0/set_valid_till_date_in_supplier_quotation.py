import frappe


def execute():
	frappe.reload_doc("buying", "doctype", "supplier_quotation")
	# DATE_ADD(... INTERVAL ...) is MySQL-only. This is a bulk UPDATE with per-row
	# date arithmetic that cannot be precomputed in Python, so branch on the
	# dialect: PostgreSQL uses `date + INTERVAL '1 month'`.
	if frappe.db.db_type == "postgres":
		frappe.db.sql(
			"""
			UPDATE `tabSupplier Quotation`
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
