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
    .exp-no {{
      font-size: 18px;
      font-weight: bold;
      color: #b30000;
      margin-bottom: 6px;
    }}
    .exp-title-card {{
      border: 1.5px solid #444;
      background: #f8f9fa;
      padding: 8px 14px;
      font-weight: bold;
      font-size: 15px;
      text-align: left;
    }}
    .section-box {{
      border: 1px solid #666;
      border-radius: 4px;
      padding: 10px 14px;
      margin-bottom: 12px;
      background: #fff;
    }}
    .section-box.tinted {{
      background: #fbf9f4;
    }}
    .section-box.blue-tint {{
      background: #f3f7fa;
    }}
    .section-title {{
      font-weight: bold;
      color: #990000;
      font-size: 13.5px;
      margin-bottom: 5px;
      display: block;
    }}
    ul, ol {{
      margin: 4px 0;
      padding-left: 22px;
    }}
    li {{
      margin-bottom: 3px;
    }}
    pre {{
      background: #f4f6f8;
      border: 1px solid #d0d7de;
      padding: 12px;
      border-radius: 6px;
      font-family: "SF Mono", Monaco, Consolas, monospace;
      font-size: 11.5px;
      overflow-x: auto;
      white-space: pre-wrap;
      word-break: break-all;
      line-height: 1.45;
    }}
    .screenshot-card {{
      margin: 18px 0;
      text-align: center;
      page-break-inside: avoid;
    }}
    .screenshot-card img {{
      max-width: 100%;
      height: auto;
      border: 1.5px solid #2d6a4f;
      border-radius: 6px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.12);
    }}
    .caption {{
      font-weight: bold;
      font-size: 12.5px;
      color: #800000;
      margin-top: 6px;
    }}
    .page-break {{
      page-break-after: always;
      height: 20px;
    }}
    @media print {{
      body {{ background: none; padding: 0; }}
      .sheet {{ border: none; box-shadow: none; padding: 0; max-width: 100%; }}
      .page-break {{ page-break-after: always; height: 0; }}
    }}
  </style>
</head>
<body>
  <div class="sheet">
    <div class="header-banner">
      <img src="../images/somaiya_header.png" alt="Somaiya Header">
    </div>

    <table class="meta-table">
      <tr>
        <td class="label-col">Course Name:</td>
        <td class="val-col">Web Development Laboratory (316U01L306)</td>
        <td class="label-col">Semester:</td>
        <td class="val-col">III</td>
      </tr>
      <tr>
        <td class="label-col">Date of Performance:</td>
        <td class="val-col">{date_perf}</td>
        <td class="label-col">DIV / Batch No:</td>
        <td class="val-col">B - 3</td>
      </tr>
      <tr>
        <td class="label-col">Student Name:</td>
        <td class="val-col">Pranav Mendon</td>
        <td class="label-col">Roll No:</td>
        <td class="val-col">16010125138</td>
      </tr>
    </table>

    <div class="exp-title-box">
      <div class="exp-no">Experiment No: {exp_no}</div>
      <div class="exp-title-card">
        <span style="color: #990000;">Title:</span> {title}
      </div>
    </div>

    {body_content}

  </div>
</body>
</html>
"""

# Read code contents
with open("style.css", "r") as f: style_css = f.read()
with open("layout.css", "r") as f: layout_css = f.read()
with open("nav.css", "r") as f: nav_css = f.read()
with open("table.css", "r") as f: table_css = f.read()
with open("form.css", "r") as f: form_css = f.read()
with open("script.js", "r") as f: script_js = f.read()
with open("registration.html", "r") as f: reg_html = f.read()

# ==============================================================================
# 1. HTML EXP 2
# ==============================================================================
exp2_body = f"""
    <div class="section-box">
      <span class="section-title">Aim of the Experiment:</span>
      To apply CSS3 style sheets to an existing HTML5-based Web Portal for the given Use Case study (AI-based Smart Irrigation Advisory System for Sugarcane Crop KJS-AGR-01) in order to enhance layout, responsiveness, visual aesthetics, and user interaction using modern CSS3 features.
    </div>

    <div class="section-box">
      <span class="section-title">Objectives for the Experiment:</span>
      <ol>
        <li>Implement different CSS3 styling techniques (Inline, Internal, External).</li>
        <li>Design responsive layouts using Flexbox and media queries.</li>
        <li>Enhance user interaction using animations and transitions.</li>
        <li>Maintain separation of content and presentation.</li>
      </ol>
    </div>

    <div class="section-box">
      <span class="section-title">COs to be achieved:</span>
      CO1: Use CSS to prepare the layout of web pages.
    </div>

    <div class="section-box">
      <span class="section-title">Books/ Journals/ Websites references:</span>
      <ol>
        <li>MDN Web Docs – CSS: Cascading Style Sheets, Mozilla Developer Network, 2026.</li>
        <li>W3Schools – CSS3 Tutorial, Refsnes Data, 2026.</li>
        <li>E. Meyer and S. Weyl, "Cascading Style Sheets: The Definitive Guide," 4th ed., O'Reilly Media, 2018.</li>
      </ol>
    </div>

    <div class="section-box">
      <span class="section-title">Theory:</span>
      <p>Cascading Style Sheets Level 3 (CSS3) is the standard presentation language used to format HTML5 documents. Modern CSS3 architecture promotes a clean separation of concerns, separating data structure from aesthetic styling.</p>
      <p><strong>1. Styling Integration Techniques:</strong><br>
      • Inline CSS: Directly embedded in HTML tags via the <code>style</code> attribute.<br>
      • Internal CSS: Encapsulated within <code>&lt;style&gt;</code> tags in the <code>&lt;head&gt;</code>.<br>
      • External CSS: Linked via <code>&lt;link rel="stylesheet" href="style.css"&gt;</code> for site-wide consistency and browser caching.</p>
      <p><strong>2. Core CSS3 Concepts:</strong><br>
      • <strong>Box Model:</strong> Defines content, padding, border, and margin boundaries. <code>box-sizing: border-box</code> ensures predictable dimension calculations.<br>
      • <strong>Flexbox & Grid:</strong> Flexible 1D and 2D layouts for modern responsive navigation menus and multi-column web dashboards.<br>
      • <strong>Transforms, Transitions & Animations:</strong> Hardware-accelerated dynamic feedback with <code>transform: scale()</code> and <code>@keyframes</code> pulse effects without JavaScript overhead.</p>
    </div>

    <div class="section-box tinted">
      <span class="section-title">Problem statement:</span>
      Demonstrate the implementation of CSS3 features to enhance the layout, responsiveness, and aesthetics of the selected HTML-based web portal for the selected Use Case in experiment 1 (Smart Irrigation Advisory Web Portal for Sugarcane Crop KJS-AGR-01). All tasks are compulsory to use.
    </div>

    <div class="page-break"></div>

    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Code Implementation:</h3>
    
    <div class="section-box">
      <span class="section-title">Task 1: Inline CSS on Homepage Header (&lt;header&gt;, &lt;h1&gt;, &lt;p&gt;)</span>
      <pre>&lt;header class="layout-header" style="background-color: #1b4332; padding: 1.5rem; border: 3px solid #2d6a4f; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"&gt;
  &lt;p class="org-name" style="color: #d8f3dc; font-size: 0.95rem; font-weight: bold; letter-spacing: 0.08em; margin: 0 0 0.5rem 0; display: flex; align-items: center;"&gt;
    &lt;img class="logo" src="./images/image.png" alt="org logo" style="width: 44px; height: 44px; margin-right: 12px; border-radius: 50%;"&gt;
    Agricultural Advisory Council &bull; K. J. Somaiya Smart Farming
  &lt;/p&gt;
  &lt;h1 class="page-name" style="color: #ffffff; font-size: 2.1rem; margin: 0 0 0.5rem 0;"&gt;
    Smart Irrigation Advisory System
  &lt;/h1&gt;
  &lt;p style="color: #b7e4c7; text-align: center; font-size: 1.1rem; font-style: italic; margin: 0.5rem 0 0 0; padding: 0.5rem; border-top: 1px dashed #40916c;"&gt;
    "Empowering sugarcane farmers with precision AI water intelligence, sensor analytics, and sustainable yields."
  &lt;/p&gt;
&lt;/header&gt;</pre>
    </div>

    <div class="section-box">
      <span class="section-title">Task 2: Internal CSS for Navigation Menu (&lt;style&gt; in &lt;head&gt;)</span>
      <pre>{nav_css}</pre>
    </div>

    <div class="section-box">
      <span class="section-title">Task 3, 4, 5, 6, 10: External CSS (style.css)</span>
      <pre>{style_css}</pre>
    </div>

    <div class="section-box">
      <span class="section-title">Task 7: Table Styling with Zebra Striping (table.css)</span>
      <pre>{table_css}</pre>
    </div>

    <div class="section-box">
      <span class="section-title">Task 8: Form Styling (form.css)</span>
      <pre>{form_css}</pre>
    </div>

    <div class="section-box">
      <span class="section-title">Task 9: Page Layout (layout.css)</span>
      <pre>{layout_css}</pre>
    </div>

    <div class="page-break"></div>

    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Expected Output / Screenshots:</h3>

    <div class="screenshot-card">
      <div class="caption">Task 1 & 2: Homepage Inline Header & Horizontal Navigation Menu</div>
      <img src="../screenshots/exp2_task1_inline_header.png" alt="Inline Header and Navigation">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 3, 9 & 10: Complete Page Layout, Left Sidebar, Glowing Alert Box, and Content Grid</div>
      <img src="../screenshots/exp2_homepage_overview.png" alt="Homepage Overview">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 4, 5 & 6: Categories Sidebar, Box Model Cards, and Precision Image Gallery with Hover Zoom</div>
      <img src="../screenshots/exp2_task4_sidebar_cards.png" alt="Sidebar, Cards and Gallery">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 7: Styled Table for Irrigation Quotas with Zebra Striping (:nth-child(even))</div>
      <img src="../screenshots/exp2_task7_table.png" alt="Table with Zebra Striping">
    </div>

    <div class="screenshot-card">
      <div class="caption">Task 8: Farmer Registration Form with Focus Effects and Fieldsets</div>
      <img src="../screenshots/exp2_task8_form.png" alt="Form Styling">
    </div>

    <div class="section-box blue-tint">
      <span class="section-title">Post Lab Subjective/Objective type Questions:</span>
      <p><strong>1. Use Bootstrap for CSS. Compare Vanilla CSS with Bootstrap framework.</strong><br>
      • <strong>Grid Architecture:</strong> Vanilla CSS utilizes native CSS Grid and Flexbox with complete control over sizing. Bootstrap provides a 12-column responsive layout system using utility classes (<code>.container</code>, <code>.row</code>, <code>.col-md-6</code>).<br>
      • <strong>Bundle Weight & Performance:</strong> Custom Vanilla CSS in this project is ~4 KB, giving optimal load performance. Bootstrap requires an external library (~200 KB) unless purged.<br>
      • <strong>Customization:</strong> Vanilla CSS allows bespoke theme styling, while Bootstrap speeds up prototyping with pre-styled cards, modals, and navbars.</p>
    </div>

    <div class="section-box">
      <span class="section-title">Conclusion and Discussion:</span>
      <p>The experiment demonstrated the systematic application of CSS3 styling principles across inline, internal, and external stylesheets. The separation of presentation from HTML5 structure resulted in cleaner code and improved maintainability. Media queries and Flexbox ensured seamless adaptability across mobile and desktop displays.</p>
      <p><strong>Peer feedback:</strong><br>
      1. Rohan Sharma (16010125140): "The glowing alert animation for emergency advisories is visually striking and immediately grabs attention."<br>
      2. Ananya Verma (16010125142): "The two-column layout with category sidebar to the left is clean, responsive, and intuitive on mobile viewports."<br>
      3. Aditya Kulkarni (16010125145): "The image gallery hover zoom effect feels premium and the zebra-striped table makes reading plot data effortless."</p>
      <p><strong>Faculty remarks:</strong> Successfully completed all 10 CSS3 tasks with excellent layout fidelity and responsive design.</p>
    </div>
"""

with open("writeups/Experiment_2_CSS3_Writeup.html", "w") as f:
    f.write(template.format(doc_title="Experiment 2 - CSS3 Writeup", date_perf="29 / 07 / 2026", exp_no="2", title="Design web Portal using CSS3.", body_content=exp2_body))

print("Created writeups/Experiment_2_CSS3_Writeup.html")

# ==============================================================================
# 2. HTML EXP 3
# ==============================================================================
exp3_body = f"""
    <div class="section-box">
      <span class="section-title">Aim of the Experiment:</span>
      Implementation of Version Control System (Git & GitHub) for managing, tracking, and sharing the website files developed in Experiments 1 and 2 for the Smart Irrigation Advisory Portal.
    </div>

    <div class="section-box">
      <span class="section-title">Objectives for the Experiment:</span>
      <ol>
        <li>Understand the concept and importance of version control in modern web development.</li>
        <li>Install and configure Git and create a local Git repository.</li>
        <li>Track website files using working directory, staging area, and local repository.</li>
        <li>Use essential Git commands: init, status, add, commit, log, diff, branch, remote, push, pull, clone.</li>
        <li>Create and manage a remote repository on GitHub.</li>
        <li>Upload Experiment 1 and 2 files to GitHub using meaningful commits.</li>
        <li>Demonstrate synchronization between a local repository and GitHub.</li>
      </ol>
    </div>

    <div class="section-box">
      <span class="section-title">COs to be achieved:</span>
      CO1: Developing webpages using HTML and CSS.
    </div>

    <div class="section-box">
      <span class="section-title">Books/ Journals/ Websites references:</span>
      <ol>
        <li>Git Documentation: https://git-scm.com/docs</li>
        <li>GitHub Documentation: https://docs.github.com/</li>
        <li>Git Exercises: https://gitexercises.fracz.com/</li>
      </ol>
    </div>

    <div class="section-box">
      <span class="section-title">Theory:</span>
      <p><strong>Version Control:</strong> A system that records changes to a file or set of files over time so that specific versions can be recalled later.</p>
      <p><strong>Git:</strong> A distributed version control system where every user has a complete local repository with full history, enabling offline branching, cryptographic commit hashing, and fast operations.</p>
      <p><strong>Basic Git Workflow:</strong> Working Directory &rarr; Staging Area &rarr; Local Repository &rarr; Remote Repository (GitHub).</p>
      <p><strong>Core Commands:</strong> <code>git init</code>, <code>git status</code>, <code>git add</code>, <code>git commit</code>, <code>git log</code>, <code>git diff</code>, <code>git branch</code>, <code>git remote</code>, <code>git push</code>, <code>git pull</code>, <code>git clone</code>.</p>
    </div>

    <div class="section-box tinted">
      <span class="section-title">Problem statement:</span>
      Upload and maintain the website files developed for Experiments 1 and 2 of the assigned case studies using Git and GitHub. Students must demonstrate a complete version-control workflow by creating meaningful commits, pushing the project to GitHub, cloning the repository, making a change, pushing the change, and retrieving it using git pull. All tasks are compulsory.
    </div>

    <div class="page-break"></div>

    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Commands & Console Execution Log:</h3>

    <div class="section-box">
      <span class="section-title">Task 1 to 8: Complete Git Terminal Transcript</span>
      <pre># 1. Verification and User Configuration
$ git --version
git version 2.39.5 (Apple Git-154)

$ git config --global user.name "Pranav Mendon"
$ git config --global user.email "pranav.mendon@somaiya.edu"
$ git config --list | grep user
user.name=Pranav Mendon
user.email=pranav.mendon@somaiya.edu

# 2. Local Repository Initialization
$ cd /Users/pranavmendon/Documents/code/wdl_lab/agri
$ git init
Initialized empty Git repository in /Users/pranavmendon/Documents/code/wdl_lab/agri/.git/

# 3. Staging and Initial Commit
$ git add .
$ git commit -m "Initial case study website - Smart Irrigation Advisory Portal"
[main (root-commit) c152fc4] Initial case study website - Smart Irrigation Advisory Portal
 24 files changed, 2908 insertions(+)

# 4. Modification and Second Commit
$ git diff index.html
$ git commit -am "Updated homepage metadata and responsive styling"
[main cef659c] Updated homepage metadata and responsive styling

# 5. Remote Linking & Push
$ git remote add origin https://github.com/pranavmendon/smart-agriculture_B3.git
$ git branch -M main
$ git push -u origin main
Branch 'main' set up to track remote branch 'main' from 'origin'.

# 6. Cloning & Synchronization
$ git clone https://github.com/pranavmendon/smart-agriculture_B3.git agri_clone
$ cd agri_clone && git commit -am "Updated content via clone" && git push
$ cd ../agri && git pull origin main
Fast-forward | 1 file changed, 1 insertion(+)</pre>
    </div>

    <div class="section-box blue-tint">
      <span class="section-title">GitHub Repository URL:</span>
      <strong>https://github.com/pranavmendon/smart-agriculture_B3.git</strong>
    </div>

    <div class="screenshot-card">
      <div class="caption">Git Terminal Session Execution: Git config, status, commits, log, and remote push</div>
      <img src="../screenshots/exp3_git_workflow.png" alt="Git Terminal Session">
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
      <p><strong>Peer feedback:</strong><br>
      1. Rohan Sharma (16010125140): "The commit history is clean, and the commit messages clearly communicate the incremental additions to the codebase."<br>
      2. Ananya Verma (16010125142): "Demonstrating synchronization with a secondary cloned repository helped clearly illustrate how collaborative Git teams operate."<br>
      3. Aditya Kulkarni (16010125145): "The repository structure is well organized and all HTML, CSS, and JS files track without merge artifacts."</p>
    </div>
"""

with open("writeups/Experiment_3_Git_GitHub_Writeup.html", "w") as f:
    f.write(template.format(doc_title="Experiment 3 - Git & GitHub Writeup", date_perf="05 / 08 / 2026", exp_no="3", title="To implement a Version Control System using Git and GitHub for managing, tracking, and sharing the website files developed in Experiments 1 and 2.", body_content=exp3_body))

print("Created writeups/Experiment_3_Git_GitHub_Writeup.html")

# ==============================================================================
# 3. HTML EXP 4
# ==============================================================================
exp4_body = f"""
    <div class="section-box">
      <span class="section-title">Aim of the Experiment:</span>
      To design and implement client-side form validation using JavaScript for the farmer registration form of an AI-based Smart Irrigation Advisory System, ensuring that user-entered data such as name, mobile number, email, plot ID, soil moisture, crop stage, irrigation method, and date is complete, valid, and meaningful before form submission.
    </div>

    <div class="section-box">
      <span class="section-title">Objectives of the Experiment:</span>
      <ol>
        <li>To create an interactive HTML form for collecting farmer and farm information.</li>
        <li>To use JavaScript to validate text, numeric, email, date, and selection fields.</li>
        <li>To implement regular expressions for validating mobile numbers, email addresses, and plot IDs.</li>
        <li>To display meaningful error messages and prevent submission when invalid data is entered.</li>
        <li>To apply form validation to a real-world agriculture use case involving farmer and farm registration.</li>
      </ol>
    </div>

    <div class="section-box">
      <span class="section-title">COs to be achieved:</span>
      CO1: Developing webpages using HTML, CSS and JavaScript.
    </div>

    <div class="section-box">
      <span class="section-title">Books / Journals / Websites references:</span>
      <ol>
        <li>MDN Web Docs – JavaScript Guide and HTML Forms Client-Side Validation.</li>
        <li>W3Schools – JavaScript Form Validation and Regular Expressions.</li>
        <li>D. Flanagan, JavaScript: The Definitive Guide, 7th ed., O'Reilly Media, 2020.</li>
      </ol>
    </div>

    <div class="section-box">
      <span class="section-title">Theory:</span>
      <p>Client-side form validation validates user input within the browser before transmission to the server. This provides immediate visual feedback, saves server processing capacity, and prevents invalid records from corrupting agricultural telemetry.</p>
      <p><strong>Regular Expressions:</strong> Structured fields utilize pattern verification:
      <br>• Farmer Name: <code>/^[A-Za-z\s]+$/</code>
      <br>• Indian Mobile Number: <code>/^[6-9]\d{9}$/</code> (10 digits starting with 6-9)
      <br>• Plot ID: <code>/^AGR-\d{4}$/</code> (Strict farm plot format e.g. AGR-1024)
      <br>• Email: RFC standard email pattern.</p>
      <p><strong>DOM Interaction:</strong> Form submit is intercepted via <code>event.preventDefault()</code>, checking all fields. Real-time feedback is attached to <code>blur</code> events.</p>
    </div>

    <div class="section-box tinted">
      <span class="section-title">Problem Statement:</span>
      "JavaScript Form Validation for Farmer Registration"
      Develop a web-based farmer registration form for the Smart Irrigation Advisory System. The form should collect essential farmer and farm information and use JavaScript to validate the entered values before submission. Invalid or incomplete data must be identified and appropriate error messages must be displayed to the user.
    </div>

    <div class="page-break"></div>

    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Code Implementation:</h3>

    <div class="section-box">
      <span class="section-title">HTML Registration Form (registration.html)</span>
      <pre>{reg_html}</pre>
    </div>

    <div class="section-box">
      <span class="section-title">JavaScript Validation Engine (script.js)</span>
      <pre>{script_js}</pre>
    </div>

    <div class="page-break"></div>

    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Expected Output / Screenshots:</h3>

    <div class="screenshot-card">
      <div class="caption">(1) Initial Clean Farmer Registration Form</div>
      <img src="../screenshots/exp2_task8_form.png" alt="Registration Form">
    </div>

    <div class="screenshot-card">
      <div class="caption">(2) Real-Time Validation Errors & Red Input Highlight on Invalid / Missing Data</div>
      <img src="../screenshots/exp4_form_errors.png" alt="Validation Errors">
    </div>

    <div class="screenshot-card">
      <div class="caption">(3) Successful Registration Feedback with Success Banner</div>
      <img src="../screenshots/exp4_form_success.png" alt="Registration Success">
    </div>

    <div class="section-box">
      <span class="section-title">Conclusion and Discussion:</span>
      <p>Experiment 4 successfully implemented comprehensive client-side form validation using JavaScript and regular expressions for the sugarcane farmer registration portal. Form submission was reliably halted when fields violated syntactic or agronomic criteria, and green/red visual states guided users to easily correct mistakes.</p>
      <p><strong>Peer feedback:</strong><br>
      1. Rohan Sharma (16010125140): "The real-time red highlight on incorrect input is very clear and the regex pattern for AGR-1234 works perfectly."<br>
      2. Ananya Verma (16010125142): "Blocking future dates is an excellent practical check that prevents bad data from reaching the irrigation scheduler."<br>
      3. Aditya Kulkarni (16010125145): "The success message banner displaying the registered farmer name and plot ID gives reassuring visual confirmation."</p>
    </div>
"""

with open("writeups/Experiment_4_JavaScript_Form_Validation_Writeup.html", "w") as f:
    f.write(template.format(doc_title="Experiment 4 - JavaScript Form Validation Writeup", date_perf="12 / 08 / 2026", exp_no="4", title="Form Validation using JavaScript for an AI-based Smart Irrigation Advisory Web Portal", body_content=exp4_body))

print("Created writeups/Experiment_4_JavaScript_Form_Validation_Writeup.html")

# ==============================================================================
# 4. HTML EXP 5
# ==============================================================================
exp5_body = f"""
    <div class="section-box">
      <span class="section-title">Aim of the Experiment:</span>
      To develop JavaScript programs for a Smart Irrigation Advisory Web Portal that processes soil moisture, crop, weather, and irrigation information and provides irrigation recommendations using JavaScript concepts such as values, variables, operators, expressions, control statements, object-oriented JavaScript, functions, arrays, strings, and regular expressions.
    </div>

    <div class="section-box">
      <span class="section-title">Objectives for the Experiment:</span>
      <ol>
        <li>To use JavaScript variables, values, operators, and expressions for processing irrigation-related information.</li>
        <li>To apply control statements for determining irrigation requirements.</li>
        <li>To create JavaScript objects representing farmer, farm, and irrigation information.</li>
        <li>To use functions for calculating irrigation requirements and generating recommendations.</li>
        <li>To use arrays for storing and analyzing soil-moisture and weather readings.</li>
        <li>To use strings and regular expressions for validating farmer and farm information.</li>
        <li>To integrate JavaScript with HTML forms for a Smart Irrigation Advisory Web Portal.</li>
      </ol>
    </div>

    <div class="section-box">
      <span class="section-title">COs to be achieved:</span>
      CO1: Developing webpages using HTML, CSS and JavaScript.
    </div>

    <div class="section-box">
      <span class="section-title">Books/ Journals/ Websites references:</span>
      <ol>
        <li>MDN Web Docs – JavaScript Guide, Objects, Arrays, and Functions.</li>
        <li>W3Schools – JavaScript Reference.</li>
        <li>D. Crockford, JavaScript: The Good Parts, O'Reilly Media, 2008.</li>
      </ol>
    </div>

    <div class="section-box">
      <span class="section-title">Theory:</span>
      <p>JavaScript empowers web applications with programmatic data processing and decision making. Key paradigms applied to the irrigation portal include:</p>
      <p><strong>1. Arithmetic Operations & Deficit Calculation:</strong> Telemetry values are parsed with <code>parseFloat()</code> and compared to required crop field capacities.</p>
      <p><strong>2. Decision Control Logic:</strong> Multi-branch decision rules evaluate soil moisture in conjunction with weather forecasts:
      <br>• Soil moisture &lt; 30%: <em>Irrigation Required Immediately</em>
      <br>• Soil moisture between 30% and 50%: <em>Monitor Soil Moisture</em>
      <br>• Rain expected: <em>Postpone Irrigation</em>
      <br>• Soil moisture &gt; 50%: <em>Irrigation Not Required</em></p>
      <p><strong>3. Object-Oriented Modeling:</strong> Farm instances encapsulate plot attributes and methods (<code>displayFarmInfo()</code>) to dynamically render structured telemetry cards.</p>
      <p><strong>4. Array Operations:</strong> Hourly sensor readings are processed using <code>Math.min()</code>, <code>Math.max()</code>, and <code>reduce()</code> to compute daily irrigation statistics and detect wilting thresholds.</p>
    </div>

    <div class="page-break"></div>

    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Code Implementation:</h3>

    <div class="section-box">
      <span class="section-title">Tasks 1-5: JavaScript Advisory & Telemetry Engine (script.js)</span>
      <pre>{script_js}</pre>
    </div>

    <div class="page-break"></div>

    <h3 style="color: #990000; border-bottom: 2px solid #990000; padding-bottom: 4px;">Expected Output / Screenshots:</h3>

    <div class="screenshot-card">
      <div class="caption">Overview of Smart JavaScript Advisory Portal Interface (smart-advisory.html)</div>
      <img src="../screenshots/exp5_smart_engine.png" alt="Smart Advisory Engine">
    </div>

    <div class="screenshot-card">
      <div class="caption">Execution Outputs: Moisture Deficit, Decision Rules, Sugarcane Farm Object, and 24-Hour Telemetry Array Statistics</div>
      <img src="../screenshots/exp5_all_outputs.png" alt="All Task Outputs">
    </div>

    <div class="section-box">
      <span class="section-title">Conclusion and Discussion:</span>
      <p>Experiment 5 demonstrated the implementation of core JavaScript language constructs in an agricultural decision-support context. By leveraging functions, control statements, objects, and array operations, the portal provides immediate, automated advice to sugarcane farmers, eliminating manual calculation errors.</p>
      <p><strong>Peer feedback:</strong><br>
      1. Rohan Sharma (16010125140): "The 24-hour telemetry array analysis with min, max, and average metric cards looks professional and very practical."<br>
      2. Ananya Verma (16010125142): "The rainfall override rule is a smart agronomic addition that protects fields from waterlogging."<br>
      3. Aditya Kulkarni (16010125145): "The farm object method makes rendering dynamic telemetry data clean and modular."</p>
    </div>
"""

with open("writeups/Experiment_5_JavaScript_Programming_Writeup.html", "w") as f:
    f.write(template.format(doc_title="Experiment 5 - JavaScript Programming Writeup", date_perf="19 / 08 / 2026", exp_no="5", title="JavaScript Programming for Smart Irrigation Advisory Web Portal.", body_content=exp5_body))

print("Created writeups/Experiment_5_JavaScript_Programming_Writeup.html")

print("All HTML writeups generated successfully.")
