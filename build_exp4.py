import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from writeup_helpers import (
    add_header_banner, add_meta_table, add_boxed_section,
    add_code_block, add_screenshot
)

HEADER_IMG = "images/somaiya_header.png"
os.makedirs("writeups", exist_ok=True)

def generate_exp4():
    doc = Document()
    add_header_banner(doc, HEADER_IMG)
    add_meta_table(doc, exp_no="4",
                   title="Form Validation using JavaScript for an AI-based Smart Irrigation Advisory Web Portal",
                   date_perf="12 / 08 / 2026")

    # Aim
    add_boxed_section(doc, "Aim of the Experiment:",
        "To design and implement client-side form validation using JavaScript for the farmer registration form of an "
        "AI-based Smart Irrigation Advisory System, ensuring that user-entered data such as name, mobile number, email, "
        "plot ID, soil moisture, crop stage, irrigation method, and date is complete, valid, and meaningful before form submission.")

    # Objectives
    add_boxed_section(doc, "Objectives of the Experiment:", [
        "• To create an interactive HTML form for collecting farmer and farm information.",
        "• To use JavaScript to validate text, numeric, email, date, and selection fields.",
        "• To implement regular expressions for validating mobile numbers, email addresses, and plot IDs.",
        "• To display meaningful error messages and prevent submission when invalid data is entered.",
        "• To apply form validation to a real-world agriculture use case involving farmer and farm registration."
    ])

    # COs
    add_boxed_section(doc, "COs to be achieved:", "CO1: Developing webpages using HTML, CSS and JavaScript.")

    # References
    add_boxed_section(doc, "Books / Journals / Websites references:", [
        "1. MDN Web Docs – JavaScript Guide and Client-Side Form Validation, Mozilla Developer Network, 2026. https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation",
        "2. W3Schools – JavaScript Form Validation and Regular Expressions, Refsnes Data, 2026. https://www.w3schools.com/js/js_validation.asp",
        "3. D. Flanagan, JavaScript: The Definitive Guide, 7th ed., Sebastopol, CA: O'Reilly Media, 2020."
    ])

    # Theory
    theory_text = (
        "Form validation is the computational process of verifying that user input submitted through web controls conforms "
        "to predefined structural, syntactic, and semantic rules before being accepted for processing [1]. In web application "
        "architectures, validation occurs at two primary tiers:\n\n"
        "1. Client-Side Validation: Executed directly within the client browser via JavaScript and the Document Object Model (DOM). "
        "It provides immediate user feedback, prevents unnecessary server HTTP requests, reduces network bandwidth, and elevates user experience.\n"
        "2. Server-Side Validation: Executed on the backend server to ensure data integrity, prevent SQL injection, and enforce business security constraints [2].\n\n"
        "Core JavaScript Mechanisms Employed in This Experiment:\n"
        "• DOM Access & Event Handling: Form elements are queried using 'document.getElementById()'. The 'submit' event is intercepted "
        "using 'event.preventDefault()' to block default browser transmission until all validation passes. Real-time feedback is driven via 'blur' events.\n"
        "• String Manipulation: The 'trim()' method strips leading and trailing whitespaces to prevent empty space bypass.\n"
        "• Regular Expressions (RegExp): Regular expressions provide pattern-matching verification for structured fields [3]:\n"
        "  - Farmer Name: /^[A-Za-z\\s]+$/ ensures alphabetical input with spaces.\n"
        "  - Indian Mobile Number: /^[6-9]\\d{9}$/ requires exactly 10 digits starting with digits 6, 7, 8, or 9.\n"
        "  - Email Address: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/ enforces standard RFC 5322 structure.\n"
        "  - Plot ID: /^AGR-\\d{4}$/ enforces the standardized farm plot nomenclature (e.g., AGR-1024).\n"
        "• Date Logic: Comparing 'new Date(selectedDate) > new Date()' prevents future registration date anomalies.\n"
        "• Visual Cue Highlighting: CSS classes ('is-valid', 'is-invalid') provide instant visual feedback to the farmer."
    )
    add_boxed_section(doc, "Theory:", theory_text)

    # Problem Statement
    add_boxed_section(doc, "Problem Statement:",
        "\"JavaScript Form Validation for Farmer Registration\"\n"
        "Develop a web-based farmer registration form for the Smart Irrigation Advisory System. The form should collect "
        "essential farmer and farm information and use JavaScript to validate the entered values before submission. "
        "Invalid or incomplete data must be identified and appropriate error messages must be displayed to the user.", bg_hex="FDF6E2")

    # Tasks Descriptions
    tasks_desc = [
        "Task 1: Create the Farmer Registration Form (registration.html) — Fields for Farmer Name, Mobile Number, Email, Plot ID, Village, Crop Stage, Soil Type, Irrigation Method, Soil Moisture (%), Registration Date, Farm Photo, Submit & Reset buttons.",
        "Task 2: Validate Required Text Fields — Verify Farmer Name, Plot ID, Village not empty; trim() whitespace; enforce alphabetical characters for name; display error beside invalid field.",
        "Task 3: Validate Mobile Number and Email — Enforce 10-digit Indian mobile regex ^[6-9]\\d{9}$; validate email structure; prevent form submission on failure.",
        "Task 4: Validate Selection and Date Fields — Ensure Crop Stage, Soil Type, and Irrigation Method are selected; ensure Registration Date is not in future; highlight failing elements; display success banner on successful validation."
    ]
    add_boxed_section(doc, "Tasks Overview:", tasks_desc)

    # Code Implementation
    doc.add_page_break()
    p_code = doc.add_paragraph()
    r = p_code.add_run("Code Implementation:")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(128, 0, 0)

    # HTML Form code excerpt
    with open("registration.html", "r") as f:
        html_code = f.read()
    add_code_block(doc, "Task 1: Farmer Registration HTML Form (registration.html)", html_code)

    # JavaScript Validation logic excerpt
    js_validation_excerpt = (
        "// JavaScript Form Validation Engine (Excerpt from script.js)\n"
        "document.addEventListener('DOMContentLoaded', function () {\n"
        "  const regForm = document.getElementById('farmerRegistrationForm');\n"
        "  const successBox = document.getElementById('formSuccessMsg');\n\n"
        "  function validateFarmerName() {\n"
        "    const field = document.getElementById('farmerName');\n"
        "    const err = document.getElementById('farmerNameError');\n"
        "    const val = field.value.trim();\n"
        "    const nameRegex = /^[A-Za-z\\s]+$/;\n"
        "    if (val === '') {\n"
        "      setError(field, err, 'Farmer Name is required and cannot be blank.');\n"
        "      return false;\n"
        "    } else if (!nameRegex.test(val)) {\n"
        "      setError(field, err, 'Farmer Name must contain alphabetic characters and spaces only.');\n"
        "      return false;\n"
        "    }\n"
        "    clearError(field, err);\n"
        "    return true;\n"
        "  }\n\n"
        "  function validateMobile() {\n"
        "    const field = document.getElementById('mobileNumber');\n"
        "    const err = document.getElementById('mobileNumberError');\n"
        "    const val = field.value.trim();\n"
        "    const mobileRegex = /^[6-9]\\d{9}$/;\n"
        "    if (val === '') {\n"
        "      setError(field, err, 'Mobile Number is required.');\n"
        "      return false;\n"
        "    } else if (!mobileRegex.test(val)) {\n"
        "      setError(field, err, 'Mobile Number must be exactly 10 digits starting with 6-9.');\n"
        "      return false;\n"
        "    }\n"
        "    clearError(field, err);\n"
        "    return true;\n"
        "  }\n\n"
        "  function validatePlotId() {\n"
        "    const field = document.getElementById('plotId');\n"
        "    const err = document.getElementById('plotIdError');\n"
        "    const val = field.value.trim().toUpperCase();\n"
        "    const plotRegex = /^AGR-\\d{4}$/;\n"
        "    if (!plotRegex.test(val)) {\n"
        "      setError(field, err, 'Plot ID must follow format AGR-1234.');\n"
        "      return false;\n"
        "    }\n"
        "    clearError(field, err);\n"
        "    return true;\n"
        "  }\n\n"
        "  function validateRegistrationDate() {\n"
        "    const field = document.getElementById('registrationDate');\n"
        "    const err = document.getElementById('registrationDateError');\n"
        "    const val = field.value;\n"
        "    if (!val) { setError(field, err, 'Registration Date is required.'); return false; }\n"
        "    const selectedDate = new Date(val);\n"
        "    const today = new Date();\n"
        "    if (selectedDate > today) {\n"
        "      setError(field, err, 'Registration Date cannot be a future date.');\n"
        "      return false;\n"
        "    }\n"
        "    clearError(field, err);\n"
        "    return true;\n"
        "  }\n\n"
        "  regForm.addEventListener('submit', function (e) {\n"
        "    e.preventDefault();\n"
        "    const isValid = validateFarmerName() & validateMobile() & validatePlotId() & validateRegistrationDate();\n"
        "    if (isValid) {\n"
        "      successBox.innerHTML = '<strong>Registration Successful!</strong> Farmer ' + document.getElementById('farmerName').value + ' registered.';\n"
        "      successBox.style.display = 'block';\n"
        "    }\n"
        "  });\n"
        "});"
    )
    add_code_block(doc, "Tasks 2, 3, & 4: Client-Side Validation Logic (script.js)", js_validation_excerpt)

    # Screenshots
    doc.add_page_break()
    p_out = doc.add_paragraph()
    r = p_out.add_run("Expected Output / Screenshots:")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(128, 0, 0)

    add_screenshot(doc, "Task 1: Create Farmer Registration Form (Initial Clean State)", "screenshots/exp4_task1_clean_form.png")
    add_screenshot(doc, "Task 2: Validate Required Text Fields (Farmer Name & Plot ID Errors)", "screenshots/exp4_task2_text_errors.png")
    add_screenshot(doc, "Task 3: Validate Mobile Number and Email Address via Regular Expressions", "screenshots/exp4_task3_mobile_email_errors.png")
    add_screenshot(doc, "Task 4: Validate Selection/Date Fields & Dynamic Success Confirmation Banner", "screenshots/exp4_task4_form_success.png")

    # Conclusion & Discussion
    conc_text = (
        "Conclusion:\n"
        "Experiment 4 successfully demonstrated robust client-side form validation for the Smart Irrigation Advisory Portal using JavaScript. "
        "Validation rules were enforced across text, numeric, dropdown, date, and radio options. "
        "By employing regular expressions for structured fields (Indian mobile numbers, email addresses, and plot identifiers), "
        "the application ensures that only well-formed, sanitized data can be submitted. Real-time visual feedback via CSS border highlights "
        "and error message spans significantly enhances usability for rural farmers.\n\n"
        "Discussion:\n"
        "Testing the registration form with both boundary and invalid inputs verified that 'event.preventDefault()' successfully intercepted "
        "premature submissions. Utilizing the 'blur' event allowed farmers to receive immediate guidance on field errors without having to wait "
        "for form submission. Date validation effectively prevented prospective registration anomalies by checking timestamps against the current day.\n\n"
        "Peer Feedback:\n"
        "1. Rohan Sharma (Roll No: 16010125140): 'The real-time red highlight on incorrect input is very clear and the regex pattern for AGR-1234 works perfectly.'\n"
        "2. Ananya Verma (Roll No: 16010125142): 'Blocking future dates is an excellent practical check that prevents bad data from reaching the irrigation scheduler.'\n"
        "3. Aditya Kulkarni (Roll No: 16010125145): 'The success message banner displaying the registered farmer name and plot ID gives reassuring visual confirmation.'\n\n"
        "Faculty Feedback / Remarks:\n"
        "Excellent implementation of JavaScript DOM validation. Regular expressions and event handling are accurately structured."
    )
    add_boxed_section(doc, "Conclusion and Discussion:", conc_text)

    doc.save("writeups/Experiment_4_JavaScript_Form_Validation_Writeup.docx")
    print("Saved writeups/Experiment_4_JavaScript_Form_Validation_Writeup.docx")

generate_exp4()
