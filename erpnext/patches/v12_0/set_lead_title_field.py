import frappe


# def execute():
# 	frappe.reload_doc("crm", "doctype", "lead")
# 	frappe.db.sql(
# 		"""
# 		UPDATE
# 			`tabLead`
# 		SET
# 			title = IF(organization_lead = 1, company_name, lead_name)
# 	"""
# 	)

import frappe


def execute():
    frappe.reload_doc("crm", "doctype", "lead")

    frappe.db.sql(
        """
        UPDATE `tabLead`
        SET
            title =
                CASE
                    WHEN organization_lead = 1
                    THEN company_name
                    ELSE lead_name
                END
        """
    )