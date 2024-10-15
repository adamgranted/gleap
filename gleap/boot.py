# apps/gleap/gleap/boot.py

import frappe

def boot_session(bootinfo):
    gleap_settings = frappe.get_single("Gleap Settings")
    if gleap_settings and gleap_settings.enable_gleap:
        bootinfo.gleap_api_key = gleap_settings.gleap_api_key
        bootinfo.enable_gleap = gleap_settings.enable_gleap
    else:
        bootinfo.gleap_api_key = None
        bootinfo.enable_gleap = False