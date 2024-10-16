import frappe

def boot_session(bootinfo):
    try:
        # Check if the 'Gleap Settings' DocType exists
        if frappe.db.table_exists('Gleap Settings'):
            # Fetch the Gleap Settings record
            gleap_settings = frappe.get_single("Gleap Settings")
            # Assign values to bootinfo
            bootinfo['gleap_api_key'] = gleap_settings.gleap_api_key
            bootinfo['enable_gleap'] = gleap_settings.enable_gleap
        else:
            # Fallback if the table doesn't exist
            bootinfo['gleap_api_key'] = None
            bootinfo['enable_gleap'] = False
    except Exception as e:
        # Log any exception encountered
        frappe.log_error(message=frappe.get_traceback(), title="Gleap Boot Session Error")
        bootinfo['gleap_api_key'] = None
        bootinfo['enable_gleap'] = False