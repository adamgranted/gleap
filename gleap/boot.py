# apps/gleap/gleap/boot.py

import frappe

def boot_session(bootinfo):
    try:
        # Check if the 'Gleap Settings' DocType exists
        if frappe.db.table_exists('Gleap Settings'):
            # Try to get the single instance of Gleap Settings
            gleap_settings = frappe.get_single("Gleap Settings")
            if gleap_settings and gleap_settings.enable_gleap:
                bootinfo['gleap_api_key'] = gleap_settings.gleap_api_key
                bootinfo['enable_gleap'] = gleap_settings.enable_gleap
            else:
                bootinfo['gleap_api_key'] = None
                bootinfo['enable_gleap'] = False
        else:
            # 'Gleap Settings' DocType does not exist yet
            bootinfo['gleap_api_key'] = None
            bootinfo['enable_gleap'] = False
    except Exception as e:
        # Log the exception without interrupting the boot process
        frappe.log_error(message=frappe.get_traceback(), title="Gleap Boot Session Error")
        bootinfo['gleap_api_key'] = None
        bootinfo['enable_gleap'] = False