// apps/my_custom_app/public/js/gleap.js

frappe.ready(function () {
  // Create a new script element
  var gleapScript = document.createElement("script");
  gleapScript.type = "text/javascript";
  gleapScript.async = true;
  gleapScript.defer = true;
  gleapScript.src = "https://app.gleap.io/assets/js/gleap.min.js"; // Replace with your Gleap script URL

  // Optionally, initialize Gleap with your API key or other configurations
  gleapScript.onload = function () {
    Gleap.init(""); // Replace with your actual Gleap API key
  };

  // Append the script to the <head> section
  document.head.appendChild(gleapScript);
});
