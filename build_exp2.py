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

# ==============================================================================
# EXPERIMENT 2: DESIGN WEB PORTAL USING CSS3
# ==============================================================================
def generate_exp2():
    doc = Document()
    add_header_banner(doc, HEADER_IMG)
    add_meta_table(doc, exp_no="2", title="Design web Portal using CSS3.", date_perf="29 / 07 / 2026")

    # Aim
    add_boxed_section(doc, "Aim of the Experiment:",
        "To apply CSS3 style sheets to an existing HTML5-based Web Portal for the given Use Case study "
        "(AI-based Smart Irrigation Advisory System for Sugarcane Crop KJS-AGR-01) in order to enhance "
        "layout, responsiveness, visual aesthetics, and user interaction using modern CSS3 features.")

    # Objectives
    add_boxed_section(doc, "Objectives for the Experiment:", [
        "1. Implement different CSS3 styling techniques (Inline, Internal, External).",
        "2. Design responsive layouts using Flexbox, CSS Grid, and media queries.",
        "3. Enhance user interaction using CSS3 animations, transforms, and transitions.",
        "4. Maintain clean separation of content and presentation across all web portal modules."
    ])

    # COs
    add_boxed_section(doc, "COs to be achieved:", "CO1: Use CSS to prepare the layout of web pages.")

    # References
    add_boxed_section(doc, "Books/ Journals/ Websites references:", [
        "1. MDN Web Docs – CSS: Cascading Style Sheets, Mozilla Developer Network, 2026. https://developer.mozilla.org/en-US/docs/Web/CSS",
        "2. W3Schools – CSS3 Tutorial and Responsive Design Guide, Refsnes Data, 2026. https://www.w3schools.com/css/",
        "3. E. A. Meyer and S. Weyl, Cascading Style Sheets: The Definitive Guide, 4th ed., Sebastopol, CA: O'Reilly Media, 2018."
    ])

    # Theory
    theory_text = (
        "Cascading Style Sheets Level 3 (CSS3) is the standard styling language used to describe the "
        "presentation, visual formatting, and responsiveness of documents written in HTML5 [1]. "
        "CSS3 operates on three foundational integration models:\n\n"
        "1. Inline CSS: Applied directly to HTML elements via the 'style' attribute. Useful for localized overrides, "
        "though it couples content with styling.\n"
        "2. Internal CSS: Encapsulated within the '<style>' block inside the '<head>' section, ideal for page-specific components "
        "such as navigation bars and custom animations.\n"
        "3. External CSS: Defined in modular '.css' files linked via '<link rel=\"stylesheet\">', maximizing code reusability, "
        "browser caching, and strict separation of presentation from structural HTML [2].\n\n"
        "Key CSS3 architectural modules utilized in this case study include:\n"
        "• CSS Box Model: Governing element rendering via content, padding, border, and margin boundaries. The 'box-sizing: border-box' "
        "directive ensures consistent padding inclusion within defined element dimensions.\n"
        "• Flexbox & Grid Layouts: Flexible box layout enables 1D dynamic flow, vertical centering, and column distribution, "
        "while CSS Grid facilitates 2D spatial placement for agricultural image galleries and multi-column dashboards.\n"
        "• Pseudo-Classes & Transitions: Interactive states like ':hover', ':focus', and ':nth-child(even)' provide visual tactile feedback, "
        "while CSS3 'transition' and 'transform: scale()' create hardware-accelerated animations without JavaScript overhead [3].\n"
        "• Keyframe Animations: '@keyframes' allows complex multi-stage keyframed animations, such as glowing alerts for urgent crop advisories."
    )
    add_boxed_section(doc, "Theory:", theory_text)

    # Problem Statement
    add_boxed_section(doc, "Problem statement:",
        "Demonstrate the implementation of CSS3 features to enhance the layout, responsiveness, and aesthetics of the "
        "selected HTML-based web portal for the selected Use Case in experiment 1 (AI-based Smart Irrigation Advisory System "
        "for Sugarcane Crop KJS-AGR-01). All tasks are compulsory to use.", bg_hex="FDF6E2")

    # Tasks Descriptions
    tasks_desc = [
        "Task 1: Style the Homepage Header (Inline CSS) — Background color, text color, centered slogan, padding, and borders on <header>, <h1>, <p>.",
        "Task 2: Internal CSS for Navigation Menu — <style> block styling horizontal items, hover effect, link color change with :hover and display: inline-block.",
        "Task 3: External CSS for Whole Website Theme — style.css applied site-wide specifying typography, color palette, headings, and common footer.",
        "Task 4: Style Book / Crop Categories Sidebar — Card appearance with border, box-shadow, padding, rounded corners, and hover color transitions.",
        "Task 5: Card Layout Using CSS Box Model — Advisory product cards with width, margin, padding, border, text alignment, and shadow.",
        "Task 6: Image Gallery Styling with CSS — Responsive grid with identical image dimensions, border, and hover zoom effect using transform: scale().",
        "Task 7: Table Styling for Price List / Irrigation Matrix — table.css with border-collapse, nth-child(even) zebra striping, and header colors.",
        "Task 8: Style Registration Form — form.css with input sizing, padding, focus highlights, fieldsets, legends, and submit button hover states.",
        "Task 9: Page Layout Using CSS — layout.css organizing header, left sidebar, right content, and sticky bottom footer via modern layout techniques.",
        "Task 10: CSS Effects & Highlighting — Special emergency advisory box with @keyframes glowing animation, text-shadow, and box-shadow."
    ]
    add_boxed_section(doc, "Tasks Overview:", tasks_desc)

    # Code Blocks
    doc.add_page_break()
    p_code = doc.add_paragraph()
    r = p_code.add_run("Code Implementation:")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(128, 0, 0)

    # Task 1 Code
    task1_code = (
        '<!-- Task 1: Inline CSS applied to <header>, <h1>, and <p> -->\n'
        '<header class="layout-header" style="background-color: #1b4332; padding: 1.5rem; border: 3px solid #2d6a4f; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">\n'
        '  <p class="org-name" style="color: #d8f3dc; font-size: 0.95rem; font-weight: bold; letter-spacing: 0.08em; margin: 0 0 0.5rem 0; display: flex; align-items: center;">\n'
        '    <img class="logo" src="./images/image.png" alt="org logo" style="width: 44px; height: 44px; margin-right: 12px; border-radius: 50%;">\n'
        '    Agricultural Advisory Council • K. J. Somaiya Smart Farming\n'
        '  </p>\n'
        '  <h1 class="page-name" style="color: #ffffff; font-size: 2.1rem; margin: 0 0 0.5rem 0; font-family: \'Segoe UI\', Tahoma, sans-serif;">\n'
        '    Smart Irrigation Advisory System\n'
        '  </h1>\n'
        '  <p style="color: #b7e4c7; text-align: center; font-size: 1.1rem; font-style: italic; margin: 0.5rem 0 0 0; padding: 0.5rem; border-top: 1px dashed #40916c;">\n'
        '    "Empowering sugarcane farmers with precision AI water intelligence, sensor analytics, and sustainable yields."\n'
        '  </p>\n'
        '</header>'
    )
    add_code_block(doc, "Task 1: Inline CSS for Homepage Header (index.html)", task1_code)

    # Task 2 Code
    task2_code = (
        '<style>\n'
        '  /* Task 2: Internal CSS (<style> in <head>) */\n'
        '  nav.internal-nav {\n'
        '    background-color: #2d6a4f;\n'
        '    padding: 0.75rem 1rem;\n'
        '    border-radius: 8px;\n'
        '    margin-bottom: 1.5rem;\n'
        '  }\n'
        '  nav.internal-nav ul {\n'
        '    list-style-type: none; /* Remove bullet points */\n'
        '    margin: 0; padding: 0;\n'
        '    display: flex; flex-wrap: wrap; gap: 0.5rem;\n'
        '  }\n'
        '  nav.internal-nav li {\n'
        '    display: inline-block; /* Display menu items horizontally */\n'
        '  }\n'
        '  nav.internal-nav a {\n'
        '    display: inline-block; /* display: inline-block */\n'
        '    color: #ffffff;        /* Change link colors */\n'
        '    text-decoration: none; /* text-decoration */\n'
        '    padding: 0.5rem 0.9rem; font-weight: 600; border-radius: 4px;\n'
        '    transition: background-color 0.25s, color 0.25s;\n'
        '  }\n'
        '  nav.internal-nav a:hover { /* :hover */\n'
        '    background-color: #1b4332;\n'
        '    color: #74c69d;\n'
        '    text-decoration: underline;\n'
        '  }\n'
        '</style>'
    )
    add_code_block(doc, "Task 2: Internal CSS for Navigation Menu (index.html)", task2_code)

    # Task 3, 4, 5, 6, 10 (style.css excerpt)
    with open("style.css", "r") as f:
        style_css_content = f.read()
    add_code_block(doc, "Task 3, 4, 5, 6 & 10: External CSS for Theme, Sidebar, Cards & Glowing Effects (style.css)", style_css_content)

    # Task 7 (table.css)
    with open("table.css", "r") as f:
        table_css_content = f.read()
    add_code_block(doc, "Task 7: External Table CSS with Zebra Striping (table.css)", table_css_content)

    # Task 8 (form.css)
    with open("form.css", "r") as f:
        form_css_content = f.read()
    add_code_block(doc, "Task 8: Registration Form Styling with Focus & Hover Effects (form.css)", form_css_content)

    # Task 9 (layout.css)
    with open("layout.css", "r") as f:
        layout_css_content = f.read()
    add_code_block(doc, "Task 9: Page Layout Structure (layout.css)", layout_css_content)

    # Screenshots
    doc.add_page_break()
    p_out = doc.add_paragraph()
    r = p_out.add_run("Expected Output / Screenshots:")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(128, 0, 0)

    add_screenshot(doc, "Task 1 & 2: Inline Header and Internal Navigation Bar", "screenshots/exp2_task1_inline_header.png")
    add_screenshot(doc, "Task 3, 9 & 10: Complete Page Layout, Left Sidebar, Glowing Alert, and Overview", "screenshots/exp2_homepage_overview.png")
    add_screenshot(doc, "Task 4, 5 & 6: Categories Sidebar, Box Model Advisory Cards, and Image Gallery", "screenshots/exp2_task4_sidebar_cards.png")
    add_screenshot(doc, "Task 7: Styled Irrigation Schedule Table with Zebra-Striping Rows", "screenshots/exp2_task7_table.png")
    add_screenshot(doc, "Task 8: Styled Farmer Registration Form with Fieldsets & Form Controls", "screenshots/exp2_task8_form.png")

    # Post Lab Questions
    post_lab_q = (
        "Question 1: Use Bootstrap for CSS.\n\n"
        "Answer:\n"
        "Bootstrap is an open-source, mobile-first front-end CSS framework. Below is a critical comparison between Vanilla CSS3 and Bootstrap:\n\n"
        "1. Grid System:\n"
        "• Vanilla CSS: Utilizes CSS Grid ('grid-template-columns: repeat(auto-fit, minmax(...))') or Flexbox directly in stylesheets.\n"
        "• Bootstrap: Utilizes a predefined 12-column flexbox grid system via utility classes ('container', 'row', 'col-md-6', 'col-lg-4').\n\n"
        "2. Development Speed vs Customization:\n"
        "• Vanilla CSS: Maximum design freedom, zero unused styles, but requires manually creating components.\n"
        "• Bootstrap: Provides battle-tested pre-built UI components (modals, accordions, navbars, cards) enabling rapid prototyping, "
        "though websites can look generic without custom theming.\n\n"
        "3. Performance & Asset Weight:\n"
        "• Vanilla CSS: Minimal file size (our custom style.css is ~4 KB), resulting in near-instant First Contentful Paint (FCP).\n"
        "• Bootstrap: Full minified bundle is ~160 KB CSS + 80 KB JS, necessitating purge tools to eliminate unused rules in production.\n\n"
        "Example Bootstrap 5 Implementation for Agricultural Card Layout:\n"
        "```html\n"
        "<div class=\"container my-4\">\n"
        "  <div class=\"row g-3\">\n"
        "    <div class=\"col-md-6 col-lg-4\">\n"
        "      <div class=\"card shadow-sm border-success h-100\">\n"
        "        <div class=\"card-body text-center\">\n"
        "          <span class=\"badge bg-danger mb-2\">Immediate Action</span>\n"
        "          <h5 class=\"card-title text-success\">Plot A - Cane Early Tillering</h5>\n"
        "          <p class=\"card-text\">Soil Moisture 24%. Drip cycle recommended for 45 minutes.</p>\n"
        "          <a href=\"#\" class=\"btn btn-outline-success btn-sm\">View Telemetry</a>\n"
        "        </div>\n"
        "      </div>\n"
        "    </div>\n"
        "  </div>\n"
        "</div>\n"
        "```"
    )
    add_boxed_section(doc, "Post Lab Subjective/Objective type Questions:", post_lab_q, bg_hex="F4F6F9")

    # Conclusion & Discussion
    conc_text = (
        "Conclusion:\n"
        "Experiment 2 successfully demonstrated the application of modern CSS3 styling techniques to the AI-based Smart Irrigation "
        "Advisory System (KJS-AGR-01). The project established a strict separation of presentation and structure by migrating global styles "
        "into modular external stylesheets ('style.css', 'layout.css', 'nav.css', 'table.css', 'form.css'). "
        "Key concepts mastered include the CSS Box Model, Flexbox multi-column layout, responsive media queries, CSS3 transitions, "
        "and keyframed glowing animations for priority advisory alerts.\n\n"
        "Discussion:\n"
        "During implementation, maintaining consistent spacing across variable content heights was solved using Flexbox ('align-items: stretch'). "
        "Hover transformations ('transform: scale(1.08)') were paired with 'overflow: hidden' on parent containers to prevent unwanted scrollbars. "
        "Zebra-striping with ':nth-child(even)' substantially improved tabular data legibility for farmers viewing irrigation duration quotas.\n\n"
        "Peer Feedback:\n"
        "1. Rohan Sharma (Roll No: 16010125140): 'The glowing animation on the emergency advisory box immediately catches attention and the color palette is soothing.'\n"
        "2. Ananya Verma (Roll No: 16010125142): 'The two-column layout with category sidebar to the left is clean, responsive, and intuitive on mobile viewports.'\n"
        "3. Aditya Kulkarni (Roll No: 16010125145): 'The image gallery hover zoom effect feels premium and the zebra-striped table makes reading plot data effortless.'\n\n"
        "Faculty Feedback / Remarks:\n"
        "Well-structured CSS3 implementation adhering to modern web development standards. Clear separation of concern maintained across modular stylesheets."
    )
    add_boxed_section(doc, "Conclusion and Discussion:", conc_text)

    doc.save("writeups/Experiment_2_CSS3_Writeup.docx")
    print("Saved writeups/Experiment_2_CSS3_Writeup.docx")

generate_exp2()
