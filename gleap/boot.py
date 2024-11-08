# Copyright (c) 2024, @adamgranted and contributors
# For license information, please see license.txt

import frappe


def boot_session(bootinfo):
	try:
		if frappe.db.exists("Gleap Settings", "Gleap Settings"):
			gleap_settings = frappe.get_doc("Gleap Settings", "Gleap Settings")
			bootinfo["gleap_api_key"] = gleap_settings.get_password("gleap_api_key")
			bootinfo["enable_gleap"] = gleap_settings.enable_gleap
		else:
			bootinfo["gleap_api_key"] = None
			bootinfo["enable_gleap"] = False
	except Exception as e:
		frappe.log_error(message=frappe.get_traceback(), title="Gleap Boot Session Error")
		bootinfo["gleap_api_key"] = None
		bootinfo["enable_gleap"] = False
