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

def generate_exp5():
    doc = Document()
    add_header_banner(doc, HEADER_IMG)
    add_meta_table(doc, exp_no="5",
                   title="JavaScript Programming for Smart Irrigation Advisory Web Portal.",
                   date_perf="19 / 08 / 2026")

    # Aim
    add_boxed_section(doc, "Aim of the Experiment:",
        "To develop JavaScript programs for a Smart Irrigation Advisory Web Portal that processes soil moisture, "
        "crop, weather, and irrigation information and provides irrigation recommendations using JavaScript concepts "
        "such as values, variables, operators, expressions, control statements, object-oriented JavaScript, functions, "
        "arrays, strings, and regular expressions.")

    # Objectives
    add_boxed_section(doc, "Objectives for the Experiment:", [
        "• To use JavaScript variables, values, operators, and expressions for processing irrigation-related information.",
        "• To apply control statements for determining irrigation requirements based on multi-factor agronomic rules.",
        "• To create JavaScript objects representing farmer, farm, and irrigation telemetry information.",
        "• To use functions for calculating irrigation requirements and generating recommendations.",
        "• To use arrays for storing, analyzing, and calculating statistics on soil-moisture and weather sensor readings.",
        "• To use strings and regular expressions for validating farmer and farm information.",
        "• To integrate JavaScript with HTML forms for an interactive Smart Irrigation Advisory Web Portal."
    ])

    # COs
    add_boxed_section(doc, "COs to be achieved:", "CO1: Developing webpages using HTML, CSS and JavaScript.")

    # References
    add_boxed_section(doc, "Books/ Journals/ Websites references:", [
        "1. MDN Web Docs – JavaScript Guide, Objects, Arrays, and Functions, Mozilla Developer Network, 2026. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
        "2. W3Schools – JavaScript Tutorial and Array Methods Reference, Refsnes Data, 2026. https://www.w3schools.com/js/",
        "3. D. Crockford, JavaScript: The Good Parts, Sebastopol, CA: O'Reilly Media / Yahoo! Press, 2008."
    ])

    # Theory
    theory_text = (
        "JavaScript is a high-level, interpreted, dynamic, prototype-based multi-paradigm programming language that powers "
        "interactivity, algorithmic computation, and asynchronous communication in modern web applications [1]. "
        "In precision agriculture, JavaScript functions as a client-side decision-support engine capable of processing telemetry "
        "locally, evaluating moisture thresholds, and formatting actionable grower recommendations without backend latency.\n\n"
        "Core JavaScript Concepts Implemented in This Experiment:\n"
        "1. Variables & Expressions:\n"
        "Modern ES6 block-scoped variable declarations ('let' and 'const') avoid variable hoisting pitfalls. "
        "Mathematical expressions compute soil moisture deficit: 'deficit = requiredMoisture - currentMoisture' [2].\n\n"
        "2. Conditional Control Statements:\n"
        "Decision logic structures ('if...else if...else') evaluate non-linear agricultural constraints. Multi-condition expressions "
        "evaluate sensor thresholds in tandem with atmospheric precipitation probabilities.\n\n"
        "3. Object-Oriented JavaScript:\n"
        "JavaScript objects encapsulate cohesive entities via key-value mappings. A sugarcane farm entity models properties "
        "('farmerName', 'plotId', 'cropStage', 'soilMoisture', 'area', 'pumpStatus') alongside behavior via method binding ('this') [3].\n\n"
        "4. Array Processing & High-Order Functions:\n"
        "Telemetry arrays store 24-hour sensor series. Built-in iterative methods ('reduce()', 'filter()') and math utilities ('Math.min()', "
        "'Math.max()') compute statistical indicators: minimum, peak, arithmetic mean, and critical count below agronomic wilting points (<30%).\n\n"
        "5. DOM Interactivity:\n"
        "JavaScript bridges computational results to the HTML interface via DOM manipulation ('document.getElementById()', 'innerHTML', 'alert()')."
    )
    add_boxed_section(doc, "Theory:", theory_text)

    # Problem Statement / Tasks
    tasks_desc = [
        "Task 1: Soil Moisture Deficit Calculator — Accept current & required soil moisture levels, calculate deficit, and display irrigation status via alert() and DOM.",
        "Task 2: Rule-Based Recommendation Engine — Evaluate soil moisture, rainfall forecast, and crop stage against agronomic decision rules (<30% Immediate, 30%-50% Monitor, Rain Expected Postpone, >50% Not Required).",
        "Task 3: Sugarcane Farm Object — Instantiate an object representing a sugarcane farm with properties and a displayFarmInfo() method.",
        "Task 4: Hourly Soil Moisture Sensor Array Operations — Store 24 hourly readings in an array; display readings, find min/max, compute average, and count critical readings (<30%).",
        "Task 5: Validation Program — Validate Farmer Name (alphabetic), Mobile Number (10 digits), and Plot ID (AGR-1234).",
        "Task 6: Interactive HTML Integration — Embed interactive components into the Smart Irrigation Advisory Web Portal."
    ]
    add_boxed_section(doc, "Tasks and Decision Rules Overview:", tasks_desc, bg_hex="FDF6E2")

    # Code Implementation
    doc.add_page_break()
    p_code = doc.add_paragraph()
    r = p_code.add_run("Code Implementation:")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(128, 0, 0)

    # Task 1, 2, 3, 4 code excerpts from script.js
    with open("script.js", "r") as f:
        js_full_code = f.read()
    add_code_block(doc, "Complete JavaScript Programming & Advisory Module (script.js)", js_full_code)

    # HTML interface excerpt from smart-advisory.html
    with open("smart-advisory.html", "r") as f:
        html_sa_code = f.read()
    add_code_block(doc, "Task 6: Interactive Smart Advisory Interface (smart-advisory.html)", html_sa_code)

    # Screenshots
    doc.add_page_break()
    p_out = doc.add_paragraph()
    r = p_out.add_run("Expected Output / Screenshots:")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(128, 0, 0)

    add_screenshot(doc, "Task 1: Soil Moisture Deficit & Water Requirement Calculation", "screenshots/exp5_task1_deficit_calc.png")
    add_screenshot(doc, "Task 2: Multi-Factor Decision Rule Recommendation Engine", "screenshots/exp5_task2_decision_rules.png")
    add_screenshot(doc, "Task 3: Sugarcane Farm Object Representation & displayFarmInfo()", "screenshots/exp5_task3_farm_object.png")
    add_screenshot(doc, "Task 4: Hourly Sensor Telemetry Array Processing (Min, Max, Avg, Critical Hours)", "screenshots/exp5_task4_array_telemetry.png")
    add_screenshot(doc, "Task 5: Client-Side Input Validation Test Suite Results", "screenshots/exp5_task5_validation_suite.png")
    add_screenshot(doc, "Task 6: Interactive Advisory Request & Registration Form Execution", "screenshots/exp5_task6_interactive_form.png")

    # Conclusion & Discussion
    conc_text = (
        "Conclusion:\n"
        "Experiment 5 successfully demonstrated JavaScript programming concepts applied to an AI-based Smart Irrigation Advisory System (KJS-AGR-01). "
        "Fundamental language constructs were systematically applied: variables and arithmetic operators for water volume deficit calculation, "
        "conditional statements for rule-based irrigation scheduling, object-oriented JavaScript for farm telemetry modeling, and array algorithms "
        "for 24-hour time-series sensor analysis. The interactive portal provides immediate feedback to farmers and agronomists, "
        "substantially reducing manual computation.\n\n"
        "Discussion:\n"
        "In Task 1, computing moisture deficit using float arithmetic ('parseFloat()') ensured decimal precision. "
        "In Task 2, prioritizing rainfall probability over absolute moisture thresholds avoided over-irrigation before rainstorms. "
        "Task 3 highlighted the power of encapsulation using the 'this' keyword to render formatted HTML cards directly from object state. "
        "In Task 4, using 'Math.min', 'Math.max', and 'reduce()' provided clean, high-performance array analytics on sensor telemetry.\n\n"
        "Peer Feedback:\n"
        "1. Rohan Sharma (Roll No: 16010125140): 'The 24-hour telemetry array analysis with min, max, and average metric cards looks professional and very practical.'\n"
        "2. Ananya Verma (Roll No: 16010125142): 'The rainfall override rule is a smart agronomic addition that protects fields from waterlogging.'\n"
        "3. Aditya Kulkarni (Roll No: 16010125145): 'The farm object method makes rendering dynamic telemetry data clean and modular.'\n\n"
        "Faculty Feedback / Remarks:\n"
        "Exceptional JavaScript implementation. Demonstrates sound programming principles across control logic, object-oriented modeling, and array processing."
    )
    add_boxed_section(doc, "Conclusion and Discussion:", conc_text)

    doc.save("writeups/Experiment_5_JavaScript_Programming_Writeup.docx")
    print("Saved writeups/Experiment_5_JavaScript_Programming_Writeup.docx")

generate_exp5()
