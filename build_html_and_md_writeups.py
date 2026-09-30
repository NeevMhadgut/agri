import os

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{doc_title}</title>
  <style>
    @page {{
      size: A4;
      margin: 15mm;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      color: #1f2a1f;
      background: #fdfdfd;
      margin: 0;
      padding: 20px;
      line-height: 1.5;
      font-size: 13.5px;
    }}
    .sheet {{
      max-width: 820px;
      margin: 0 auto;
      background: #fff;
      padding: 25px 35px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      border: 1px solid #dcdcdc;
    }}
    .header-banner {{
      text-align: center;
      margin-bottom: 12px;
    }}
    .header-banner img {{
      max-width: 100%;
      height: auto;
    }}
    table.meta-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 15px;
      font-size: 13px;
    }}
    table.meta-table td {{
      border: 1px solid #555;
      padding: 6px 10px;
    }}
    .label-col {{
      font-weight: bold;
      color: #800000;
      width: 20%;
      background: #fbfbfb;
    }}
    .val-col {{
      width: 30%;
    }}
    .exp-title-box {{
      text-align: center;
      margin: 15px 0 10px;
    }}
    .exp-title {{
      font-size: 16px;
      font-weight: bold;
      color: #800000;
      display: inline-block;
      border-bottom: 1px solid #800000;
      padding-bottom: 3px;
    }}
    .section-box {{
      border: 1px solid #777;
      padding: 10px 14px;
      margin-bottom: 12px;
      background-color: #fafafa;
      border-radius: 4px;
    }}
    .section-box.blue-tint {{
      background-color: #f4f8fb;
      border-color: #b2c9d8;
    }}
    .section-title {{
      font-weight: bold;
      color: #800000;
      display: block;
      margin-bottom: 4px;
      font-size: 13.5px;
    }}
    pre {{
      background: #f4f6f4;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-family: "JetBrains Mono", Consolas, monospace;
      font-size: 11.5px;
      white-space: pre-wrap;
      word-break: break-all;
      margin: 6px 0 0;
      color: #1a331a;
      max-height: 400px;
      overflow-y: auto;
    }}
    .screenshot-card {{
      margin: 18px 0;
      border: 1px solid #ccc;
      border-radius: 6px;
      overflow: hidden;
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }}
    .screenshot-card .caption {{
      background: #f0f5ee;
      padding: 8px 12px;
      font-weight: bold;
      color: #1b4332;
      border-bottom: 1px solid #d4dfd2;
      font-size: 13px;
    }}
    .screenshot-card img {{
      display: block;
      width: 100%;
      height: auto;
    }}
    .page-break {{
      page-break-before: always;
      margin-top: 25px;
    }}
  </style>
</head>
<body>
  <div class="sheet">
    <div class="header-banner">
      <img src="../images/somaiya_header.png" alt="Somaiya Vidyavihar University">
    </div>

    <table class="meta-table">
      <tr>
        <td class="label-col">Exp. No:</td>
        <td class="val-col">{exp_no}</td>
        <td class="label-col">Roll No:</td>
        <td class="val-col">16010125138</td>
      </tr>
      <tr>
        <td class="label-col">Name:</td>
        <td class="val-col">Pranav Mendon</td>
        <td class="label-col">Batch:</td>
        <td class="val-col">B3</td>
      </tr>
      <tr>
        <td class="label-col">Branch:</td>
        <td class="val-col">Computer Engineering</td>
        <td class="label-col">Semester:</td>
        <td class="val-col">IV</td>
      </tr>
      <tr>
        <td class="label-col">Subject:</td>
        <td class="val-col">Web Development Lab</td>
        <td class="label-col">Date of Perf:</td>
        <td class="val-col">{date_perf}</td>
      </tr>
    </table>

    <div class="exp-title-box">
      <div class="exp-title">{title}</div>
    </div>

    {body_content}
  </div>
</body>
</html>
"""

os.makedirs("writeups", exist_ok=True)

# Helper for code read
def read_f(p):
    if os.path.exists(p):
        with open(p) as f: return f.read()
    return ""

index_html = read_f("index.html")
style_css = read_f("style.css")
table_css = read_f("table.css")
form_css = read_f("form.css")
layout_css = read_f("layout.css")
script_js = read_f("script.js")


# ==============================================================================
# EXPERIMENT 1 HTML
# ==============================================================================
exp1_body = f"""
    <div class="section-box">
      <span class="section-title">Aim of the Experiment:</span>
      To design and develop a multi-page, use-case-based web portal front-end using HTML5 for an AI-based Smart Irrigation Advisory System for sugarcane crops (KJS-AGR-01), incorporating semantic structure, lists, text formatting, multimedia, interactive client-side image maps, responsive tables, and forms.
    </div>

    <div class="section-box">
      <span class="section-title">Objectives of the Experiment:</span>
      1. To develop structured and semantic HTML5 web pages for an AI-enabled smart irrigation advisory system.<br>
      2. To create interactive web pages for farmer registration, irrigation recommendations, and weather forecast display.<br>
      3. To apply real-world agricultural IoT use case telemetry as the core theme across all modular pages.<br>
      4. To implement HTML5 lists, tables, image maps, forms, and multimedia elements without external libraries.<br>
      5. To build a robust, accessible foundation ready for subsequent CSS3 styling and JavaScript validation layers.
    </div>

    <div class="section-box">
      <span class="section-title">COs to be achieved:</span>
      CO1: Developing webpages using HTML and CSS.
    </div>

    <div class="section-box">
      <span class="section-title">Books / Journals / Websites references:</span>
      1. MDN Web Docs – HTML: HyperText Markup Language, Mozilla Developer Network, 2026.<br>
      2. W3Schools – HTML5 Tutorial and Semantic Web Guide, Refsnes Data, 2026.<br>
      3. J. Duckett, HTML and CSS: Design and Build Websites, 1st ed., Indianapolis, IN: John Wiley & Sons, 2011.
    </div>

    <div class="section-box">
      <span class="section-title">Theory / Relevant Concepts:</span>
      HyperText Markup Language 5 (HTML5) is the core standard for structuring and presenting content on the World Wide Web. HTML5 introduces semantic tags that provide explicit meaning to both browsers and search engines, superseding legacy generic 'div' elements.<br><br>
      Key HTML5 Modules Used in This Portal:<br>
      • <strong>Semantic Structural Elements:</strong> &lt;header&gt;, &lt;nav&gt;, &lt;main&gt;, &lt;section&gt;, &lt;article&gt;, &lt;aside&gt;, and &lt;footer&gt; delineate the layout hierarchy.<br>
      • <strong>Lists:</strong> Ordered lists (&lt;ol&gt;), unordered lists (&lt;ul&gt;), and definition lists (&lt;dl&gt;) organize sensor workflows and agricultural abbreviations.<br>
      • <strong>Tables:</strong> &lt;table&gt;, &lt;thead&gt;, &lt;tbody&gt;, &lt;tfoot&gt;, with rowspan and colspan attributes present multi-zone moisture thresholds.<br>
      • <strong>Client-Side Image Maps:</strong> &lt;map&gt; and &lt;area&gt; tags enable coordinate-based navigation on farm plots.<br>
      • <strong>Forms:</strong> Input controls enclosed within &lt;fieldset&gt; and &lt;legend&gt; enable structured farmer data acquisition.<br>
      • <strong>Multimedia &amp; Iframes:</strong> Native &lt;video&gt;, &lt;audio&gt;, and &lt;iframe&gt; deliver awareness media and GIS radar telemetry.
    </div>

    <div class="page-break"></div>
    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Expected Output / Screenshots (Task-Wise):</h3>

    <div class="screenshot-card">
      <div class="caption">Task 1: Semantic Homepage Portal Structure (index.html)</div>
      <img src="../screenshots/exp1_task1_homepage.png" alt="Task 1 Homepage Structure">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 2: Farm Information Displayed using Ordered, Unordered &amp; Definition Lists (farm-information.html)</div>
      <img src="../screenshots/exp1_task2_lists.png" alt="Task 2 Lists">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 3: Irrigation Advisory Page using HTML Formatting &amp; Abbreviation Tags (irrigation-advisory.html)</div>
      <img src="../screenshots/exp1_task3_formatting.png" alt="Task 3 Formatting Tags">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 4: Farm Gallery using Semantic Figure, Image &amp; Figcaption Elements</div>
      <img src="../screenshots/exp1_task4_gallery.png" alt="Task 4 Farm Gallery">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 5: Interactive Farm Plot Navigation using Client-Side Image Map (&lt;map&gt; &amp; &lt;area&gt;) (farm-map.html)</div>
      <img src="../screenshots/exp1_task5_imagemap.png" alt="Task 5 Farm Map">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 6: Soil Moisture &amp; Irrigation Quota Table (Thead, Tbody, Rowspan &amp; Colspan) (recommendation.html)</div>
      <img src="../screenshots/exp1_task6_table.png" alt="Task 6 Table">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 7: Farmer Registration Form with Semantic Controls &amp; Fieldsets (registration.html)</div>
      <img src="../screenshots/exp1_task7_form.png" alt="Task 7 Form">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 8: Display Weather Forecast &amp; Georeferenced Radar using IFrame (media.html)</div>
      <img src="../screenshots/exp1_task8_iframe.png" alt="Task 8 Iframe">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 9: Multimedia &amp; Executable Awareness Content (Native HTML5 Audio &amp; Video) (media.html)</div>
      <img src="../screenshots/exp1_task9_media.png" alt="Task 9 Media">
    </div>

    <div class="section-box blue-tint">
      <span class="section-title">Post Lab Subjective/Objective type Questions:</span>
      <p><strong>1. Explain the importance of semantic elements in HTML5 compared to traditional div tags.</strong><br>
      Semantic elements (&lt;header&gt;, &lt;nav&gt;, &lt;article&gt;, &lt;section&gt;, &lt;footer&gt;) clearly communicate their role to browsers, search engines, and screen readers. Generic &lt;div&gt; tags convey no contextual meaning, making accessibility parsing and SEO ranking significantly harder.</p>
      <p><strong>2. How does a client-side image map function?</strong><br>
      An &lt;img&gt; references a &lt;map&gt; via <code>usemap="#name"</code>. Inside the map, &lt;area&gt; elements define geometric zones (rect, circle, poly) with coordinate bounds (<code>coords="..."</code>) and target hyperlinks. Clicks within these bounds route directly to the specified destination.</p>
    </div>

    <div class="section-box">
      <span class="section-title">Conclusion and Discussion:</span>
      <p>Experiment 1 established the clean structural and semantic foundation of the AI-based Smart Irrigation Advisory Portal using pure HTML5. Multi-page navigation, domain lists, coordinate-based image mapping, tables with span attributes, structured input forms, and multimedia content were all successfully verified.</p>
    </div>
"""

with open("writeups/Experiment_1_HTML5_Writeup.html", "w") as f:
    f.write(template.format(doc_title="Experiment 1 - HTML5 Web Portal Writeup", date_perf="15 / 07 / 2026", exp_no="1", title="Design and Development of an AI-based Smart Irrigation Advisory Web Portal Front-End using HTML5", body_content=exp1_body))
print("Created writeups/Experiment_1_HTML5_Writeup.html")


# ==============================================================================
# EXPERIMENT 2 HTML
# ==============================================================================
exp2_body = f"""
    <div class="section-box">
      <span class="section-title">Aim of the Experiment:</span>
      To apply CSS3 style sheets to an existing HTML5-based Web Portal for the given Use Case study (AI-based Smart Irrigation Advisory System for Sugarcane Crop KJS-AGR-01) in order to enhance layout, responsiveness, visual aesthetics, and user interaction using modern CSS3 features.
    </div>

    <div class="section-box">
      <span class="section-title">Objectives for the Experiment:</span>
      1. Implement different CSS3 styling techniques (Inline, Internal, External).<br>
      2. Design responsive layouts using Flexbox, CSS Grid, and media queries.<br>
      3. Enhance user interaction using CSS3 animations, transforms, and transitions.<br>
      4. Maintain clean separation of content and presentation across all web portal modules.
    </div>

    <div class="section-box">
      <span class="section-title">COs to be achieved:</span>
      CO1: Use CSS to prepare the layout of web pages.
    </div>

    <div class="section-box">
      <span class="section-title">Books/ Journals/ Websites references:</span>
      1. MDN Web Docs – CSS: Cascading Style Sheets, Mozilla Developer Network, 2026.<br>
      2. W3Schools – CSS3 Tutorial and Responsive Design Guide, Refsnes Data, 2026.<br>
      3. E. A. Meyer and S. Weyl, Cascading Style Sheets: The Definitive Guide, 4th ed., O'Reilly Media, 2018.
    </div>

    <div class="section-box">
      <span class="section-title">Theory:</span>
      Cascading Style Sheets Level 3 (CSS3) governs presentation, visual hierarchy, and responsiveness. The portal uses Inline CSS for specialized overrides, Internal CSS for component navigation, and modular External CSS files (style.css, layout.css, nav.css, table.css, form.css) for strict separation of concerns, browser caching, and responsive media queries.
    </div>

    <div class="page-break"></div>
    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Expected Output / Screenshots (Task-Wise):</h3>

    <div class="screenshot-card">
      <div class="caption">Task 1: Style Homepage Header (Inline CSS)</div>
      <img src="../screenshots/exp2_task1_inline_header.png" alt="Task 1 Inline Header">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 2: Internal CSS for Navigation Menu (&lt;style&gt; tag in &lt;head&gt;)</div>
      <img src="../screenshots/exp2_task2_internal_nav.png" alt="Task 2 Internal Nav">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 3: External CSS for Whole Website Theme (style.css)</div>
      <img src="../screenshots/exp2_task3_external_theme.png" alt="Task 3 External Theme">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 4: Style Crop Categories Sidebar with Hover Accents</div>
      <img src="../screenshots/exp2_task4_sidebar.png" alt="Task 4 Sidebar">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 5: Advisory Card Layout Using CSS Box Model (Padding, Border, Shadow)</div>
      <img src="../screenshots/exp2_task5_boxmodel_cards.png" alt="Task 5 Box Model Cards">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 6: Precision Agriculture Image Gallery with Hover Zoom Scale</div>
      <img src="../screenshots/exp2_task6_gallery_hover.png" alt="Task 6 Gallery Hover">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 7: Styled Irrigation Schedule Table with Zebra-Striping (:nth-child(even))</div>
      <img src="../screenshots/exp2_task7_table.png" alt="Task 7 Zebra Table">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 8: Styled Farmer Registration Form with Focus Rings &amp; Fieldsets</div>
      <img src="../screenshots/exp2_task8_form.png" alt="Task 8 Form">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 9: Page Layout Structure (Two-Column Flexbox/Grid)</div>
      <img src="../screenshots/exp2_task9_layout.png" alt="Task 9 Layout">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 10: CSS Effects &amp; Highlighting (Keyframed Glowing Alert Box)</div>
      <img src="../screenshots/exp2_task10_css_effects.png" alt="Task 10 Glowing Box">
    </div>

    <div class="section-box blue-tint">
      <span class="section-title">Post Lab Subjective/Objective type Questions:</span>
      <p><strong>1. Use Bootstrap for CSS. Compare Vanilla CSS with Bootstrap framework.</strong><br>
      • <strong>Grid Architecture:</strong> Vanilla CSS utilizes native CSS Grid and Flexbox with complete control over sizing. Bootstrap provides a 12-column responsive layout system using utility classes (<code>.container</code>, <code>.row</code>, <code>.col-md-6</code>).<br>
      • <strong>Bundle Weight &amp; Performance:</strong> Custom Vanilla CSS in this project is ~4 KB, giving optimal load performance. Bootstrap requires an external library (~200 KB) unless purged.<br>
      • <strong>Customization:</strong> Vanilla CSS allows bespoke theme styling, while Bootstrap speeds up prototyping with pre-styled cards, modals, and navbars.</p>
    </div>

    <div class="section-box">
      <span class="section-title">Conclusion and Discussion:</span>
      <p>Experiment 2 successfully transformed the HTML5 portal into a modern, responsive web application using CSS3. Box model properties, multi-column flex layouts, zebra-striped tables, styled form controls with glowing focus rings, and keyframe animations were all systematically integrated.</p>
    </div>
"""

with open("writeups/Experiment_2_CSS3_Writeup.html", "w") as f:
    f.write(template.format(doc_title="Experiment 2 - CSS3 Web Portal Writeup", date_perf="29 / 07 / 2026", exp_no="2", title="Design web Portal using CSS3.", body_content=exp2_body))
print("Created writeups/Experiment_2_CSS3_Writeup.html")


# ==============================================================================
# EXPERIMENT 3 HTML
# ==============================================================================
exp3_body = f"""
    <div class="section-box">
      <span class="section-title">Aim of the Experiment:</span>
      To understand and implement distributed version control concepts, repository management, branching, commit histories, remote collaboration, and synchronization using Git and GitHub for the AI-based Smart Irrigation Advisory Web Portal.
    </div>

    <div class="section-box">
      <span class="section-title">Objectives of the Experiment:</span>
      1. To create, initialize, and configure a local Git repository for the web portal project.<br>
      2. To stage files, record descriptive commits, and track repository history.<br>
      3. To link the local repository to GitHub, push changes, and manage remote tracking.<br>
      4. To understand repository cloning, branch management, and collaborative synchronization.
    </div>

    <div class="section-box">
      <span class="section-title">COs to be achieved:</span>
      CO1: Version control workflow and web development lifecycle.
    </div>

    <div class="section-box blue-tint">
      <span class="section-title">GitHub Repository URL:</span>
      <strong>https://github.com/pranavmendon/smart-irrigation-advisory.git</strong>
    </div>

    <div class="page-break"></div>
    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Expected Output / Screenshots (Task-Wise):</h3>

    <div class="screenshot-card">
      <div class="caption">Task 1: GitHub Account Setup &amp; SSH/HTTPS Authentication Verification</div>
      <img src="../screenshots/exp3_task1_github_account.png" alt="Task 1 GitHub Account">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 2: Install and Configure Git (Version &amp; User Credentials)</div>
      <img src="../screenshots/exp3_task2_git_config.png" alt="Task 2 Git Config">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 3: Prepare Project Workspace &amp; Initialize Local Git Repository</div>
      <img src="../screenshots/exp3_task3_git_init.png" alt="Task 3 Git Init">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 4: Stage Portal Files and Create Initial Commit</div>
      <img src="../screenshots/exp3_task4_initial_commit.png" alt="Task 4 Initial Commit">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 5: Modify Advisory Portal Code and Create Second Commit</div>
      <img src="../screenshots/exp3_task5_second_commit.png" alt="Task 5 Second Commit">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 6: Connect Local Repository to Remote GitHub Origin</div>
      <img src="../screenshots/exp3_task6_remote_add.png" alt="Task 6 Remote Add">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 7: Push Local Branch to GitHub Remote Repository</div>
      <img src="../screenshots/exp3_task7_git_push.png" alt="Task 7 Git Push">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 8: Verify Git Synchronization and Commit History Tree</div>
      <img src="../screenshots/exp3_task8_git_log_sync.png" alt="Task 8 Git Log Sync">
    </div>

    <div class="section-box blue-tint">
      <span class="section-title">Post Lab Subjective/Objective type Questions:</span>
      <p><strong>1. What is the purpose of git clone? How is it different from downloading a ZIP file from GitHub?</strong><br>
      • <code>git clone</code> downloads the files along with the hidden <code>.git</code> repository directory, preserving full commit history, all branches, tags, and automatically configures the <code>origin</code> remote tracking link so developers can push and pull.<br>
      • Downloading a ZIP extracts only the current state of files with no history, no branches, and no tracking connection to GitHub.</p>
    </div>

    <div class="section-box">
      <span class="section-title">Conclusion and Discussion:</span>
      <p>The experiment provided hands-on mastery over distributed version control workflows using Git and GitHub. Understanding the relationship between the working directory, index, and commit history clarified how software teams safely collaborate, track feature changes, and synchronize distributed repositories.</p>
    </div>
"""

with open("writeups/Experiment_3_Git_GitHub_Writeup.html", "w") as f:
    f.write(template.format(doc_title="Experiment 3 - Git & GitHub Writeup", date_perf="05 / 08 / 2026", exp_no="3", title="Version Control using Git and GitHub.", body_content=exp3_body))
print("Created writeups/Experiment_3_Git_GitHub_Writeup.html")


# ==============================================================================
# EXPERIMENT 4 HTML
# ==============================================================================
exp4_body = f"""
    <div class="section-box">
      <span class="section-title">Aim of the Experiment:</span>
      To design and implement client-side form validation using JavaScript for the farmer registration form of an AI-based Smart Irrigation Advisory System, ensuring that user-entered data such as name, mobile number, email, plot ID, soil moisture, crop stage, irrigation method, and date is complete, valid, and meaningful before form submission.
    </div>

    <div class="section-box">
      <span class="section-title">Objectives of the Experiment:</span>
      • To create an interactive HTML form for collecting farmer and farm information.<br>
      • To use JavaScript to validate text, numeric, email, date, and selection fields.<br>
      • To implement regular expressions for validating mobile numbers, email addresses, and plot IDs.<br>
      • To display meaningful error messages and prevent submission when invalid data is entered.<br>
      • To apply form validation to a real-world agriculture use case involving farmer and farm registration.
    </div>

    <div class="section-box">
      <span class="section-title">COs to be achieved:</span>
      CO1: Developing webpages using HTML, CSS and JavaScript.
    </div>

    <div class="page-break"></div>
    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Expected Output / Screenshots (Task-Wise):</h3>

    <div class="screenshot-card">
      <div class="caption">Task 1: Create Farmer Registration Form (Initial Clean State)</div>
      <img src="../screenshots/exp4_task1_clean_form.png" alt="Task 1 Clean Form">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 2: Validate Required Text Fields (Farmer Name &amp; Plot ID Errors)</div>
      <img src="../screenshots/exp4_task2_text_errors.png" alt="Task 2 Text Field Errors">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 3: Validate Mobile Number and Email Address via Regular Expressions</div>
      <img src="../screenshots/exp4_task3_mobile_email_errors.png" alt="Task 3 Mobile & Email Errors">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 4: Validate Selection/Date Fields &amp; Dynamic Success Confirmation Banner</div>
      <img src="../screenshots/exp4_task4_form_success.png" alt="Task 4 Form Success">
    </div>

    <div class="section-box">
      <span class="section-title">Conclusion and Discussion:</span>
      <p>Experiment 4 successfully implemented comprehensive client-side form validation using JavaScript and regular expressions for the sugarcane farmer registration portal. Form submission was reliably halted when fields violated syntactic or agronomic criteria, and green/red visual states guided users to easily correct mistakes.</p>
    </div>
"""

with open("writeups/Experiment_4_JavaScript_Form_Validation_Writeup.html", "w") as f:
    f.write(template.format(doc_title="Experiment 4 - JavaScript Form Validation Writeup", date_perf="12 / 08 / 2026", exp_no="4", title="Form Validation using JavaScript for an AI-based Smart Irrigation Advisory Web Portal", body_content=exp4_body))
print("Created writeups/Experiment_4_JavaScript_Form_Validation_Writeup.html")


# ==============================================================================
# EXPERIMENT 5 HTML
# ==============================================================================
exp5_body = f"""
    <div class="section-box">
      <span class="section-title">Aim of the Experiment:</span>
      To develop and execute client-side JavaScript programs demonstrating core language features including variables, operators, decision-making control statements, object-oriented encapsulation, and array algorithms applied to an AI-based Smart Irrigation Advisory System for sugarcane crops (KJS-AGR-01).
    </div>

    <div class="section-box">
      <span class="section-title">Objectives:</span>
      1. Implement arithmetic operators and variables to calculate soil moisture deficits and irrigation water volume quotas.<br>
      2. Implement multi-factor conditional statements (if-else) to formulate agronomic irrigation recommendations.<br>
      3. Create a JavaScript object representing a sugarcane farm with attributes and member methods.<br>
      4. Process 24-hour time-series telemetry sensor data using array methods.<br>
      5. Construct input validation suites and interactive advisory request forms.
    </div>

    <div class="section-box">
      <span class="section-title">COs to be achieved:</span>
      CO1: Developing webpages using HTML, CSS and JavaScript.
    </div>

    <div class="page-break"></div>
    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Expected Output / Screenshots (Task-Wise):</h3>

    <div class="screenshot-card">
      <div class="caption">Task 1: Soil Moisture Deficit &amp; Water Requirement Calculation</div>
      <img src="../screenshots/exp5_task1_deficit_calc.png" alt="Task 1 Deficit Calc">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 2: Multi-Factor Decision Rule Recommendation Engine</div>
      <img src="../screenshots/exp5_task2_decision_rules.png" alt="Task 2 Decision Rules">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 3: Sugarcane Farm Object Representation &amp; displayFarmInfo()</div>
      <img src="../screenshots/exp5_task3_farm_object.png" alt="Task 3 Farm Object">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 4: Hourly Sensor Telemetry Array Processing (Min, Max, Avg, Critical Hours)</div>
      <img src="../screenshots/exp5_task4_array_telemetry.png" alt="Task 4 Array Telemetry">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 5: Client-Side Input Validation Test Suite Results</div>
      <img src="../screenshots/exp5_task5_validation_suite.png" alt="Task 5 Validation Suite">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 6: Interactive Advisory Request &amp; Registration Form Execution</div>
      <img src="../screenshots/exp5_task6_interactive_form.png" alt="Task 6 Interactive Form">
    </div>

    <div class="section-box">
      <span class="section-title">Conclusion and Discussion:</span>
      <p>Experiment 5 demonstrated the implementation of core JavaScript language constructs in an agricultural decision-support context. By leveraging functions, control statements, objects, and array operations, the portal provides immediate, automated advice to sugarcane farmers, eliminating manual calculation errors.</p>
    </div>
"""

with open("writeups/Experiment_5_JavaScript_Programming_Writeup.html", "w") as f:
    f.write(template.format(doc_title="Experiment 5 - JavaScript Programming Writeup", date_perf="19 / 08 / 2026", exp_no="5", title="JavaScript Programming for Smart Irrigation Advisory Web Portal.", body_content=exp5_body))
print("Created writeups/Experiment_5_JavaScript_Programming_Writeup.html")

print("All HTML writeups successfully updated with individual task-wise screenshots!")
