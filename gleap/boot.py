# apps/gleap/gleap/boot.py

import frappe

def boot_session(bootinfo):
    try:
        gleap_settings = frappe.get_single("Gleap Settings")
        if gleap_settings and gleap_settings.enable_gleap:
            bootinfo.gleap_api_key = gleap_settings.gleap_api_key
            bootinfo.enable_gleap = gleap_settings.enable_gleap
        else:
            bootinfo.gleap_api_key = None
            bootinfo.enable_gleap = False
    except frappe.DoesNotExistError:
        # Gleap Settings DocType or record doesn't exist yet
        bootinfo.gleap_api_key = None
        bootinfo.enable_gleap = False
    except Exception as e:
        # Log unexpected exceptions without halting the boot process
        frappe.log_error(title="Gleap Boot Session Error", message=frappe.get_traceback())
        bootinfo.gleap_api_key = None
        bootinfo.enable_gleap = False