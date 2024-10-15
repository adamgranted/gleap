// apps/gleap/gleap/public/js/gleap.js

frappe.ready(function () {
  // Retrieve the Gleap API Key and enable flag from frappe.boot
  var gleap_api_key = frappe.boot.gleap_api_key;
  var enable_gleap = frappe.boot.enable_gleap;

  if (enable_gleap && gleap_api_key) {
    // Create a new script element for Gleap
    var gleapScript = document.createElement("script");
    gleapScript.type = "text/javascript";
    gleapScript.async = true;
    gleapScript.defer = true;
    gleapScript.src = "https://app.gleap.io/assets/js/gleap.min.js"; // Replace with your Gleap script URL if different

    // Initialize Gleap once the script is loaded
    gleapScript.onload = function () {
      Gleap.init(gleap_api_key);
    };

    // Append the Gleap script to the <head> section
    document.head.appendChild(gleapScript);
  } else {
    console.warn("Gleap Integration is disabled or API Key not set.");
  }
});
