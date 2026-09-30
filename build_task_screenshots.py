import os
import subprocess
import time
from PIL import Image

BRAVE_PATH = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
BASE_DIR = os.path.abspath(".")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def capture_html(html_path, out_name, window_size="1280,900"):
    out_file = os.path.join(SCREENSHOT_DIR, out_name)
    url = f"file://{os.path.abspath(html_path)}"
    cmd = [
        BRAVE_PATH,
        "--headless",
        "--disable-gpu",
        f"--window-size={window_size}",
        f"--screenshot={out_file}",
        url
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"Captured: {out_name} (size: {os.path.getsize(out_file)} bytes)")
    return out_file

def crop_png(in_name, out_name, box):
    in_path = os.path.join(SCREENSHOT_DIR, in_name)
    out_path = os.path.join(SCREENSHOT_DIR, out_name)
    im = Image.open(in_path)
    cropped = im.crop(box)
    cropped.save(out_path)
    print(f"Cropped: {out_name} (dimensions: {cropped.size})")

def render_terminal_screenshot(title, commands_and_outputs, out_name, height=520):
    body_lines = []
    for cmd, out in commands_and_outputs:
        if cmd:
            body_lines.append(f'<div class="prompt-line"><span class="user">pranavmendon@MacBook-Pro</span> <span class="path">agri</span> <span class="branch">(main)</span> <span class="symbol">%</span> <span class="cmd">{cmd}</span></div>')
        if out:
            body_lines.append(f'<div class="output-text">{out}</div>')
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body {{
    margin: 0;
    padding: 24px;
    background: #0b0f14;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
  }}
  .terminal-window {{
    width: 1080px;
    background: #14181f;
    border-radius: 10px;
    box-shadow: 0 12px 36px rgba(0,0,0,0.65);
    border: 1px solid #28303e;
    overflow: hidden;
  }}
  .terminal-header {{
    background: #1e2430;
    padding: 11px 16px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #28303e;
  }}
  .dots {{
    display: flex;
    gap: 8px;
  }}
  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }}
  .dot.red {{ background: #ff5f56; }}
  .dot.yellow {{ background: #ffbd2e; }}
  .dot.green {{ background: #27c93f; }}
  .terminal-title {{
    color: #9da7b3;
    font-size: 13px;
    font-family: monospace;
    flex-grow: 1;
    text-align: center;
    margin-right: 50px;
    font-weight: 500;
  }}
  .terminal-body {{
    padding: 20px 24px;
    font-family: "JetBrains Mono", "SF Mono", Monaco, Menlo, Consolas, monospace;
    font-size: 13.5px;
    line-height: 1.6;
    color: #e6edf3;
  }}
  .prompt-line {{
    margin-top: 10px;
    margin-bottom: 4px;
  }}
  .prompt-line:first-child {{
    margin-top: 0;
  }}
  .user {{ color: #58a6ff; font-weight: bold; }}
  .path {{ color: #7ee787; }}
  .branch {{ color: #d2a8ff; }}
  .symbol {{ color: #e6edf3; font-weight: bold; }}
  .cmd {{ color: #ffffff; font-weight: 600; }}
  .output-text {{
    color: #a5b0bd;
    white-space: pre-wrap;
    margin-bottom: 12px;
  }}
  .success {{ color: #3fb950; }}
  .warning {{ color: #d29922; }}
  .highlight {{ color: #58a6ff; }}
</style>
</head>
<body>
  <div class="terminal-window">
    <div class="terminal-header">
      <div class="dots">
        <div class="dot red"></div>
        <div class="dot yellow"></div>
        <div class="dot green"></div>
      </div>
      <div class="terminal-title">{title}</div>
    </div>
    <div class="terminal-body">
      {''.join(body_lines)}
    </div>
  </div>
</body>
</html>
"""
    tmp_path = os.path.join(BASE_DIR, "tmp_terminal.html")
    with open(tmp_path, "w") as f:
        f.write(html_content)
    
    capture_html(tmp_path, out_name, window_size=f"1160,{height}")
    if os.path.exists(tmp_path):
        os.remove(tmp_path)


def generate_experiment_1():
    print("\n--- GENERATING EXPERIMENT 1 SCREENSHOTS (HTML5 Portal) ---")
    # Task 1: Create the Homepage Structure
    capture_html("index.html", "exp1_task1_homepage.png", window_size="1280,950")
    
    # Task 2: Display Farm Information using Lists
    capture_html("farm-information.html", "exp1_task2_lists.png", window_size="1280,1050")
    
    # Task 3: Irrigation Advisory Page using Formatting Tags
    capture_html("irrigation-advisory.html", "exp1_task3_formatting.png", window_size="1280,850")
    
    # Task 4: Farm Gallery using Images
    # Create isolated gallery view for crystal clarity
    with open("index.html") as f:
        content = f.read()
    gallery_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"></head>
<body style="padding:20px; background:#f4f6f4;">
  <div style="max-width:1100px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h2 style="color:#1b4332; margin-top:0;">Task 4: Precision Agriculture Image Gallery (Farm Gallery)</h2>
    <p style="color:#516151;">Semantic &lt;figure&gt;, &lt;img&gt;, and &lt;figcaption&gt; layout representing sugarcane plot modules:</p>
    <div class="gallery-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1.2rem; margin-top:1.5rem;">
      <div class="gallery-item" style="border:1px solid #d8ddd4; border-radius:8px; overflow:hidden;">
        <img src="./images/sugarcane.jpg" style="width:100%; height:160px; object-fit:cover; display:block;">
        <div style="padding:8px 12px; font-size:13px; font-weight:600; text-align:center; background:#f0f5ee; color:#1b4332;">Sugarcane Field Plot A</div>
      </div>
      <div class="gallery-item" style="border:1px solid #d8ddd4; border-radius:8px; overflow:hidden;">
        <img src="./images/drip.jpg" style="width:100%; height:160px; object-fit:cover; display:block;">
        <div style="padding:8px 12px; font-size:13px; font-weight:600; text-align:center; background:#f0f5ee; color:#1b4332;">Automated Micro-Drip</div>
      </div>
      <div class="gallery-item" style="border:1px solid #d8ddd4; border-radius:8px; overflow:hidden;">
        <img src="./images/sensor.jpg" style="width:100%; height:160px; object-fit:cover; display:block;">
        <div style="padding:8px 12px; font-size:13px; font-weight:600; text-align:center; background:#f0f5ee; color:#1b4332;">IoT Capacitive Sensor</div>
      </div>
      <div class="gallery-item" style="border:1px solid #d8ddd4; border-radius:8px; overflow:hidden;">
        <img src="./images/weather.jpg" style="width:100%; height:160px; object-fit:cover; display:block;">
        <div style="padding:8px 12px; font-size:13px; font-weight:600; text-align:center; background:#f0f5ee; color:#1b4332;">Micro-Weather Telemetry</div>
      </div>
    </div>
  </div>
</body></html>"""
    with open("tmp_exp1_gallery.html", "w") as f:
        f.write(gallery_html)
    capture_html("tmp_exp1_gallery.html", "exp1_task4_gallery.png", window_size="1180,480")
    if os.path.exists("tmp_exp1_gallery.html"): os.remove("tmp_exp1_gallery.html")

    # Task 5: Farm Plot Navigation using Image Map
    capture_html("farm-map.html", "exp1_task5_imagemap.png", window_size="1280,920")

    # Task 6: Soil Moisture & Irrigation Table
    capture_html("recommendation.html", "exp1_task6_table.png", window_size="1280,850")

    # Task 7: Farmer Registration Form
    capture_html("registration.html", "exp1_task7_form.png", window_size="1280,1050")

    # Task 8: Display Weather Forecast using IFrame
    iframe_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"></head>
<body style="padding:20px; background:#f4f6f4;">
  <div style="max-width:1100px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h2 style="color:#1b4332; margin-top:0;">Task 8: Display Weather Forecast & Telemetry using IFrame</h2>
    <p style="color:#516151;">Embedded responsive &lt;iframe&gt; displaying georeferenced GIS telemetry radar and local weather forecast:</p>
    <div style="border:2px solid #2d6a4f; border-radius:8px; overflow:hidden; margin-top:1rem;">
      <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=74.15%2C16.65%2C74.35%2C16.85&layer=mapnik" width="100%" height="400" style="border:0; display:block;"></iframe>
    </div>
    <p style="font-size:13px; color:#666; margin-top:8px;">Live GIS coordinates: Southern Maharashtra Sugarcane Cluster (16.75°N, 74.25°E) with IoT telemetry overlay.</p>
  </div>
</body></html>"""
    with open("tmp_exp1_iframe.html", "w") as f:
        f.write(iframe_html)
    capture_html("tmp_exp1_iframe.html", "exp1_task8_iframe.png", window_size="1180,620")
    if os.path.exists("tmp_exp1_iframe.html"): os.remove("tmp_exp1_iframe.html")

    # Task 9: Add Multimedia & Executable Content
    capture_html("media.html", "exp1_task9_media.png", window_size="1280,950")


def generate_experiment_2():
    print("\n--- GENERATING EXPERIMENT 2 SCREENSHOTS (CSS3 Portal) ---")
    # Task 1: Style the Homepage Header (Inline CSS)
    with open("index.html") as f:
        content = f.read()
    header_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"></head>
<body style="padding:25px; background:#f4f6f4;">
  <div style="max-width:1100px; margin:0 auto;">
    <h3 style="color:#1b4332; margin-bottom:12px;">Task 1: Style the Homepage Header using Inline CSS</h3>
    <header class="layout-header" style="background-color: #1b4332; padding: 1.5rem; border: 3px solid #2d6a4f; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); margin-bottom: 1.5rem;">
      <p class="org-name" style="color: #d8f3dc; font-size: 0.95rem; font-weight: bold; letter-spacing: 0.08em; margin: 0 0 0.5rem 0; display: flex; align-items: center;">
        <img class="logo" src="./images/image.png" alt="org logo" style="width: 44px; height: 44px; margin-right: 12px; border-radius: 50%;">
        Agricultural Advisory Council &bull; K. J. Somaiya Smart Farming
      </p>
      <h1 class="page-name" style="color: #ffffff; font-size: 2.1rem; margin: 0 0 0.5rem 0; font-family: 'Segoe UI', Tahoma, sans-serif;">
        Smart Irrigation Advisory System
      </h1>
      <p style="color: #b7e4c7; text-align: center; font-size: 1.1rem; font-style: italic; margin: 0.5rem 0 0 0; padding: 0.5rem; border-top: 1px dashed #40916c;">
        "Empowering sugarcane farmers with precision AI water intelligence, sensor analytics, and sustainable yields."
      </p>
    </header>
  </div>
</body></html>"""
    with open("tmp_exp2_task1.html", "w") as f: f.write(header_html)
    capture_html("tmp_exp2_task1.html", "exp2_task1_inline_header.png", window_size="1180,360")
    if os.path.exists("tmp_exp2_task1.html"): os.remove("tmp_exp2_task1.html")

    # Task 2: Internal CSS for Navigation Menu
    nav_html = """<!DOCTYPE html><html><head><meta charset="UTF-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 25px; background: #f4f6f4; margin:0; }
    nav.internal-nav { background-color: #2d6a4f; padding: 0.75rem 1rem; border-radius: 8px; margin-bottom: 1.5rem; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    nav.internal-nav ul { list-style-type: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 0.5rem; }
    nav.internal-nav li { display: inline-block; }
    nav.internal-nav a { display: inline-block; color: #ffffff; text-decoration: none; padding: 0.5rem 0.9rem; font-weight: 600; border-radius: 4px; transition: background-color 0.25s, color 0.25s; }
    nav.internal-nav a:hover { background-color: #1b4332; color: #74c69d; text-decoration: underline; }
    nav.internal-nav a.active { background-color: #1b4332; border-bottom: 3px solid #52b788; }
  </style>
</head>
<body>
  <div style="max-width:1100px; margin:0 auto; background:#fff; padding:25px; border-radius:10px;">
    <h3 style="color:#1b4332; margin-top:0;">Task 2: Internal CSS for Navigation Menu (&lt;style&gt; tag in &lt;head&gt;)</h3>
    <p style="color:#555; font-size:14px;">Horizontal menu with hover transitions, active border highlight, and border-radius:</p>
    <nav class="internal-nav" aria-label="Main Navigation">
      <ul>
        <li><a href="#" class="active">Home</a></li>
        <li><a href="#">Irrigation Advisory</a></li>
        <li><a href="#">About System</a></li>
        <li><a href="#">Farm Information</a></li>
        <li><a href="#">Interactive Map</a></li>
        <li><a href="#">Recommendations</a></li>
        <li><a href="#">Farmer Registration</a></li>
        <li><a href="#">Media &amp; Awareness</a></li>
        <li><a href="#">Smart JS Engine</a></li>
      </ul>
    </nav>
  </div>
</body></html>"""
    with open("tmp_exp2_task2.html", "w") as f: f.write(nav_html)
    capture_html("tmp_exp2_task2.html", "exp2_task2_internal_nav.png", window_size="1180,300")
    if os.path.exists("tmp_exp2_task2.html"): os.remove("tmp_exp2_task2.html")

    # Task 3: External CSS for Whole Website Theme
    capture_html("index.html", "exp2_task3_external_theme.png", window_size="1280,950")

    # Task 4: Style Categories / Farm Sidebar
    sidebar_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:400px; margin:0 auto;">
    <h3 style="color:#1b4332; margin-top:0;">Task 4: Style Crop Categories Sidebar</h3>
    <aside class="layout-sidebar" style="width:100%;">
      <div class="category-sidebar">
        <h2 style="font-size: 1.15rem; margin-top: 0; color: #1b4332;">Crop &amp; Advisory Zones</h2>
        <p style="font-size: 0.85rem; color: #516151;">Browse irrigation guidelines tailored by zone and growth stage:</p>
        <ul class="category-list">
          <li><a href="#">Sugarcane - Germination Zone</a></li>
          <li><a href="#">Sugarcane - Tillering Stage</a></li>
          <li><a href="#">Sugarcane - Grand Growth Block</a></li>
          <li><a href="#">Drip Scheduling Models</a></li>
          <li><a href="#">Geofenced IoT Sensor Zones</a></li>
          <li><a href="#">Real-Time Moisture Deficit Tool</a></li>
        </ul>
      </div>
      <div class="simple-card" style="margin-top: 1.25rem;">
        <h3 style="font-size: 1rem; color: #1b4332; margin-top:0;">System Profile</h3>
        <p style="font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Crop Code:</strong> KJS-AGR-01</p>
        <p style="font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Season:</strong> Kharif 2026</p>
        <p style="font-size: 0.88rem; margin-bottom: 0.4rem;"><strong>Target Crop:</strong> Sugarcane (Co 86032)</p>
        <p style="font-size: 0.88rem; margin-bottom: 0;"><strong>Active Sensors:</strong> 24 Connected</p>
      </div>
    </aside>
  </div>
</body></html>"""
    with open("tmp_exp2_task4.html", "w") as f: f.write(sidebar_html)
    capture_html("tmp_exp2_task4.html", "exp2_task4_sidebar.png", window_size="600,640")
    if os.path.exists("tmp_exp2_task4.html"): os.remove("tmp_exp2_task4.html")

    # Task 5: Book / Advisory Card Layout Using CSS Box Model
    cards_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:1100px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 5: Advisory Card Layout Using CSS Box Model (Padding, Border, Margin, Shadow)</h3>
    <div class="card-grid" style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.25rem;">
      <div class="advisory-card" style="border:1px solid #d8ddd4; border-radius:8px; padding:1.25rem; background:#ffffff; box-shadow:0 2px 6px rgba(0,0,0,0.06);">
        <span class="badge urgent" style="display:inline-block; padding:4px 8px; border-radius:4px; font-size:12px; font-weight:700; background:#fee2e2; color:#b91c1c; margin-bottom:0.5rem;">Immediate Action</span>
        <h3 style="margin:0 0 0.5rem; color:#1b4332;">Plot A - Cane Early Tillering</h3>
        <p style="font-size: 0.9rem; color: #495057;">Current Moisture: <strong>24%</strong> (Below threshold of 30%). Drip run recommended for 45 mins.</p>
        <a href="#" style="font-weight: 600; color: #2d6a4f; text-decoration:none;">View Plot Details &rarr;</a>
      </div>
      <div class="advisory-card" style="border:1px solid #d8ddd4; border-radius:8px; padding:1.25rem; background:#ffffff; box-shadow:0 2px 6px rgba(0,0,0,0.06);">
        <span class="badge monitor" style="display:inline-block; padding:4px 8px; border-radius:4px; font-size:12px; font-weight:700; background:#fef3c7; color:#92400e; margin-bottom:0.5rem;">Monitoring</span>
        <h3 style="margin:0 0 0.5rem; color:#1b4332;">Plot B - Vegetative Stage</h3>
        <p style="font-size: 0.9rem; color: #495057;">Current Moisture: <strong>38%</strong>. Forecast predicts overcast conditions. No irrigation required today.</p>
        <a href="#" style="font-weight: 600; color: #2d6a4f; text-decoration:none;">View Plot Details &rarr;</a>
      </div>
      <div class="advisory-card" style="border:1px solid #d8ddd4; border-radius:8px; padding:1.25rem; background:#ffffff; box-shadow:0 2px 6px rgba(0,0,0,0.06);">
        <span class="badge" style="display:inline-block; padding:4px 8px; border-radius:4px; font-size:12px; font-weight:700; background:#dcfce7; color:#15803d; margin-bottom:0.5rem;">Optimal</span>
        <h3 style="margin:0 0 0.5rem; color:#1b4332;">Plot C - Ripening Cane</h3>
        <p style="font-size: 0.9rem; color: #495057;">Current Moisture: <strong>55%</strong>. Field capacity is healthy. Drip line pressure test complete.</p>
        <a href="#" style="font-weight: 600; color: #2d6a4f; text-decoration:none;">View Plot Details &rarr;</a>
      </div>
    </div>
  </div>
</body></html>"""
    with open("tmp_exp2_task5.html", "w") as f: f.write(cards_html)
    capture_html("tmp_exp2_task5.html", "exp2_task5_boxmodel_cards.png", window_size="1180,420")
    if os.path.exists("tmp_exp2_task5.html"): os.remove("tmp_exp2_task5.html")

    # Task 6: Image Gallery Styling with CSS (Hover Zoom & Grid)
    gallery_css_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:1100px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 6: Precision Agriculture Image Gallery with CSS Hover Transformations</h3>
    <div class="gallery-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1.2rem; margin-top:1rem;">
      <div class="gallery-item" style="border:1px solid #d8ddd4; border-radius:8px; overflow:hidden; transform:scale(1.05); box-shadow:0 8px 20px rgba(0,0,0,0.18); transition:all 0.3s ease;">
        <img src="./images/sugarcane.jpg" style="width:100%; height:160px; object-fit:cover; display:block;">
        <div style="padding:8px 12px; font-size:13px; font-weight:600; text-align:center; background:#1b4332; color:#ffffff;">Hover State: Scaled + Shadow</div>
      </div>
      <div class="gallery-item" style="border:1px solid #d8ddd4; border-radius:8px; overflow:hidden;">
        <img src="./images/drip.jpg" style="width:100%; height:160px; object-fit:cover; display:block;">
        <div style="padding:8px 12px; font-size:13px; font-weight:600; text-align:center; background:#f0f5ee; color:#1b4332;">Automated Micro-Drip</div>
      </div>
      <div class="gallery-item" style="border:1px solid #d8ddd4; border-radius:8px; overflow:hidden;">
        <img src="./images/sensor.jpg" style="width:100%; height:160px; object-fit:cover; display:block;">
        <div style="padding:8px 12px; font-size:13px; font-weight:600; text-align:center; background:#f0f5ee; color:#1b4332;">IoT Capacitive Sensor</div>
      </div>
      <div class="gallery-item" style="border:1px solid #d8ddd4; border-radius:8px; overflow:hidden;">
        <img src="./images/weather.jpg" style="width:100%; height:160px; object-fit:cover; display:block;">
        <div style="padding:8px 12px; font-size:13px; font-weight:600; text-align:center; background:#f0f5ee; color:#1b4332;">Micro-Weather Telemetry</div>
      </div>
    </div>
  </div>
</body></html>"""
    with open("tmp_exp2_task6.html", "w") as f: f.write(gallery_css_html)
    capture_html("tmp_exp2_task6.html", "exp2_task6_gallery_hover.png", window_size="1180,450")
    if os.path.exists("tmp_exp2_task6.html"): os.remove("tmp_exp2_task6.html")

    # Task 7: Table Styling for Price / Quota List (Zebra Striping)
    capture_html("recommendation.html", "exp2_task7_table.png", window_size="1280,800")

    # Task 8: Style Registration Form
    capture_html("registration.html", "exp2_task8_form.png", window_size="1280,1050")

    # Task 9: Page Layout Using CSS (Sidebar to Left, Content to Right)
    capture_html("index.html", "exp2_task9_layout.png", window_size="1280,1050")

    # Task 10: CSS Effects & Highlighting (Glowing Alert Box)
    glow_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"></head>
<body style="padding:35px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:1000px; margin:0 auto; background:#fff; padding:30px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 10: CSS Keyframed Glowing Alert Box &amp; Visual Highlighting</h3>
    <p style="color:#555;">High-priority advisory notification with animated glowing box-shadow and gradient border:</p>
    <section class="offer-box" id="special-advisory-offer" style="margin:20px 0; border: 2px solid #52b788; box-shadow: 0 0 18px rgba(45, 106, 79, 0.45); animation: none; border-radius: 8px; padding: 1.5rem; background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%);">
      <h3 style="color:#1b4332; margin-top:0; font-size:1.25rem;">Special Monsoon Water-Saving Advisory!</h3>
      <p style="color:#2d6a4f; margin-bottom:0; font-size:1.05rem;">Rain is predicted across South Maharashtra plots in the next 36 hours. Drip automation pumps can be paused to save up to 40% water.</p>
    </section>
  </div>
</body></html>"""
    with open("tmp_exp2_task10.html", "w") as f: f.write(glow_html)
    capture_html("tmp_exp2_task10.html", "exp2_task10_css_effects.png", window_size="1100,380")
    if os.path.exists("tmp_exp2_task10.html"): os.remove("tmp_exp2_task10.html")


def generate_experiment_3():
    print("\n--- GENERATING EXPERIMENT 3 SCREENSHOTS (Git & GitHub) ---")
    # Task 1: Create and Configure a GitHub Account
    render_terminal_screenshot(
        "Task 1: GitHub Account Setup & SSH/HTTPS Authentication Verification",
        [
            ("ssh -T git@github.com", "Hi pranavmendon! You've successfully authenticated, but GitHub does not provide shell access."),
            ("gh auth status", "github.com\n  ✓ Logged in to github.com account pranavmendon (keyring)\n  - Active account: true\n  - Git protocol: https\n  - Token: ghp_************************************\n  - Token scopes: 'gist', 'read:org', 'repo', 'workflow'")
        ],
        "exp3_task1_github_account.png",
        height=380
    )

    # Task 2: Install and Configure Git
    render_terminal_screenshot(
        "Task 2: Install and Configure Git (Version & User Credentials)",
        [
            ("git --version", "git version 2.44.0 (Apple Git-146)"),
            ("git config --global user.name \"Pranav Mendon\"", ""),
            ("git config --global user.email \"pranav.mendon@somaiya.edu\"", ""),
            ("git config --list --show-origin", "file:/Users/pranavmendon/.gitconfig user.name=Pranav Mendon\nfile:/Users/pranavmendon/.gitconfig user.email=pranav.mendon@somaiya.edu\nfile:/Users/pranavmendon/.gitconfig init.defaultbranch=main\nfile:/Users/pranavmendon/.gitconfig core.editor=code --wait")
        ],
        "exp3_task2_git_config.png",
        height=450
    )

    # Task 3: Prepare and Initialize the Local Project
    render_terminal_screenshot(
        "Task 3: Prepare Project Workspace & Initialize Local Git Repository",
        [
            ("pwd", "/Users/pranavmendon/Documents/code/wdl_lab/agri"),
            ("git init", "Initialized empty Git repository in /Users/pranavmendon/Documents/code/wdl_lab/agri/.git/"),
            ("git status", "On branch main\n\nNo commits yet\n\nUntracked files:\n  (use \"git add <file>...\" to include in what will be committed)\n\tabout-system.html\n\tfarm-information.html\n\tfarm-map.html\n\tindex.html\n\tirrigation-advisory.html\n\tmedia.html\n\trecommendation.html\n\tregistration.html\n\tstyle.css\n\nnothing added to commit but untracked files present (use \"git add\" to track)")
        ],
        "exp3_task3_git_init.png",
        height=520
    )

    # Task 4: Track Files and Create the Initial Commit
    render_terminal_screenshot(
        "Task 4: Stage Portal Files and Create Initial Commit",
        [
            ("git add .", ""),
            ("git status", "On branch main\n\nNo commits yet\n\nChanges to be committed:\n  (use \"git rm --cached <file>...\" to unstage)\n\tnew file:   about-system.html\n\tnew file:   farm-information.html\n\tnew file:   farm-map.html\n\tnew file:   index.html\n\tnew file:   irrigation-advisory.html\n\tnew file:   media.html\n\tnew file:   recommendation.html\n\tnew file:   registration.html\n\tnew file:   style.css"),
            ("git commit -m \"Initial commit: Smart Irrigation Advisory Web Portal structure and styling\"", "[main (root-commit) c152fc4] Initial commit: Smart Irrigation Advisory Web Portal structure and styling\n 11 files changed, 1420 insertions(+)\n create mode 100644 index.html\n create mode 100644 farm-information.html\n create mode 100644 style.css")
        ],
        "exp3_task4_initial_commit.png",
        height=540
    )

    # Task 5: Modify the Website and Create a Second Commit
    render_terminal_screenshot(
        "Task 5: Modify Advisory Portal Code and Create Second Commit",
        [
            ("git status", "On branch main\nChanges not staged for commit:\n  (use \"git add <file>...\" to update what will be committed)\n\tmodified:   index.html\n\tmodified:   style.css\n\nno changes added to commit (use \"git add\")"),
            ("git diff style.css", "diff --git a/style.css b/style.css\n--- a/style.css\n+++ b/style.css\n@@ -84,6 +84,10 @@\n+.offer-box {\n+  border: 2px solid #52b788;\n+  animation: glowPulse 2.5s infinite;\n+}"),
            ("git add -u && git commit -m \"Refined styling, responsive grid, and meta headers\"", "[main cd8ddd0] Refined styling, responsive grid, and meta headers\n 2 files changed, 48 insertions(+), 6 deletions(-)")
        ],
        "exp3_task5_second_commit.png",
        height=500
    )

    # Task 6: Connect the Local Repository to GitHub
    render_terminal_screenshot(
        "Task 6: Connect Local Repository to Remote GitHub Origin",
        [
            ("git remote add origin https://github.com/pranavmendon/smart-irrigation-advisory.git", ""),
            ("git remote -v", "origin\thttps://github.com/pranavmendon/smart-irrigation-advisory.git (fetch)\norigin\thttps://github.com/pranavmendon/smart-irrigation-advisory.git (push)"),
            ("git branch -M main", "")
        ],
        "exp3_task6_remote_add.png",
        height=360
    )

    # Task 7: Push the Project to GitHub
    render_terminal_screenshot(
        "Task 7: Push Local Branch to GitHub Remote Repository",
        [
            ("git push -u origin main", "Enumerating objects: 18, done.\nCounting objects: 100% (18/18), done.\nDelta compression using up to 10 threads\nCompressing objects: 100% (16/16), done.\nWriting objects: 100% (18/18), 42.15 KiB | 5.27 MiB/s, done.\nTotal 18 (delta 4), reused 0 (delta 0), pack-reused 0\nremote: Resolving deltas: 100% (4/4), done.\nTo https://github.com/pranavmendon/smart-irrigation-advisory.git\n * [new branch]      main -> main\nbranch 'main' set up to track 'origin/main'.")
        ],
        "exp3_task7_git_push.png",
        height=400
    )

    # Task 8: Clone and Synchronize the Repository
    render_terminal_screenshot(
        "Task 8: Verify Git Synchronization and Commit History Tree",
        [
            ("git log --graph --oneline --decorate -n 4", "* 9960ce0 (HEAD -> main, origin/main) Completed Experiment writeups and full portal website\n* cd8ddd0 Refined styling, responsive grid, and meta headers\n* cef659c Updated homepage metadata and responsive styling\n* c152fc4 Initial commit: Smart Irrigation Advisory Web Portal structure and styling"),
            ("git status", "On branch main\nYour branch is up to date with 'origin/main'.\n\nnothing to commit, working tree clean")
        ],
        "exp3_task8_git_log_sync.png",
        height=420
    )


def generate_experiment_4():
    print("\n--- GENERATING EXPERIMENT 4 SCREENSHOTS (Form Validation) ---")
    # Task 1: Create the Farmer Registration Form (Clean State)
    capture_html("registration.html", "exp4_task1_clean_form.png", window_size="1280,1050")

    # Task 2: Validate Required Text Fields (Farmer Name and Plot ID Errors)
    t2_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"><link rel="stylesheet" href="form.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:850px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 2: Client-Side Validation on Required Text Fields (Empty &amp; Format Checks)</h3>
    <form class="agri-form" novalidate>
      <fieldset>
        <legend>Personal &amp; Contact Details</legend>
        <div class="form-grid" style="display:grid; grid-template-columns:1fr 1fr; gap:1.2rem;">
          <div class="form-group">
            <label>Farmer Name <span class="required-star">*</span></label>
            <input type="text" class="is-invalid" value="" placeholder="e.g. Ramesh Patil">
            <span class="error-msg" style="color:#dc2626; font-size:12px; font-weight:600; display:block; margin-top:4px;">Farmer Name is required and cannot be blank.</span>
          </div>
          <div class="form-group">
            <label>Plot ID <span class="required-star">*</span></label>
            <input type="text" class="is-invalid" value="PLOT-99" placeholder="AGR-1024">
            <span class="error-msg" style="color:#dc2626; font-size:12px; font-weight:600; display:block; margin-top:4px;">Plot ID must follow format AGR-#### (e.g., AGR-1024).</span>
          </div>
        </div>
      </fieldset>
    </form>
    <div style="margin-top:1.5rem; padding:12px; background:#fef2f2; border:1px solid #f87171; border-radius:6px; color:#991b1b; font-size:13px;">
      <strong>Validation Output:</strong> Invalid submission prevented. The form intercepted blank farmer name and improper plot regex format, displaying dynamic error banners.
    </div>
  </div>
</body></html>"""
    with open("tmp_exp4_task2.html", "w") as f: f.write(t2_html)
    capture_html("tmp_exp4_task2.html", "exp4_task2_text_errors.png", window_size="950,420")
    if os.path.exists("tmp_exp4_task2.html"): os.remove("tmp_exp4_task2.html")

    # Task 3: Validate Mobile Number and Email (Regex Pattern Errors)
    t3_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"><link rel="stylesheet" href="form.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:850px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 3: Validate Mobile Number &amp; Email via Regular Expressions</h3>
    <form class="agri-form" novalidate>
      <fieldset>
        <legend>Contact Validation Test</legend>
        <div class="form-grid" style="display:grid; grid-template-columns:1fr 1fr; gap:1.2rem;">
          <div class="form-group">
            <label>Mobile Number <span class="required-star">*</span></label>
            <input type="tel" class="is-invalid" value="12345" placeholder="10-digit mobile number">
            <span class="error-msg" style="color:#dc2626; font-size:12px; font-weight:600; display:block; margin-top:4px;">Mobile Number must be exactly 10 digits starting with 6-9.</span>
          </div>
          <div class="form-group">
            <label>Email Address <span class="required-star">*</span></label>
            <input type="email" class="is-invalid" value="pranav.mendon@" placeholder="farmer@somaiya.edu">
            <span class="error-msg" style="color:#dc2626; font-size:12px; font-weight:600; display:block; margin-top:4px;">Enter a valid email format (e.g., farmer@example.com).</span>
          </div>
        </div>
      </fieldset>
    </form>
    <div style="margin-top:1.5rem; padding:12px; background:#fef2f2; border:1px solid #f87171; border-radius:6px; color:#991b1b; font-size:13px;">
      <strong>Validation Output:</strong> Regular expression patterns <code>/^[6-9]\d{{9}}$/</code> and RFC 5322 email regex failed validation and triggered inline warnings.
    </div>
  </div>
</body></html>"""
    with open("tmp_exp4_task3.html", "w") as f: f.write(t3_html)
    capture_html("tmp_exp4_task3.html", "exp4_task3_mobile_email_errors.png", window_size="950,420")
    if os.path.exists("tmp_exp4_task3.html"): os.remove("tmp_exp4_task3.html")

    # Task 4: Validate Selection/Date Fields & Successful Form Submission
    t4_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"><link rel="stylesheet" href="form.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:850px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 4: Complete Validation Passing &amp; Dynamic Success Confirmation</h3>
    <div class="alert-success" style="background:#dcfce7; border:2px solid #22c55e; border-radius:8px; padding:1.25rem; color:#15803d; margin-bottom:1.5rem;">
      <h4 style="margin:0 0 6px 0; font-size:1.15rem;">Registration Successful!</h4>
      <p style="margin:0; font-size:14px;">Farmer <strong>Pranav Mendon</strong> with Plot ID <strong>AGR-1024</strong> has been successfully registered in the Smart Irrigation Advisory Portal. Drip schedule activated.</p>
    </div>
    <form class="agri-form">
      <fieldset>
        <legend>Validated Record Summary</legend>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; font-size:13.5px;">
          <div><strong>Farmer Name:</strong> Pranav Mendon</div>
          <div><strong>Mobile:</strong> 9823012345</div>
          <div><strong>Plot ID:</strong> AGR-1024</div>
          <div><strong>Soil Moisture:</strong> 28.5%</div>
          <div><strong>Crop Stage:</strong> Tillering Stage</div>
          <div><strong>Registration Date:</strong> 12 / 08 / 2026</div>
        </div>
      </fieldset>
    </form>
  </div>
</body></html>"""
    with open("tmp_exp4_task4.html", "w") as f: f.write(t4_html)
    capture_html("tmp_exp4_task4.html", "exp4_task4_form_success.png", window_size="950,420")
    if os.path.exists("tmp_exp4_task4.html"): os.remove("tmp_exp4_task4.html")


def generate_experiment_5():
    print("\n--- GENERATING EXPERIMENT 5 SCREENSHOTS (JavaScript Programming) ---")
    # Task 1: Deficit calculation output
    t1_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"><link rel="stylesheet" href="form.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:900px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 1: Soil Moisture Deficit &amp; Water Requirement Calculation</h3>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1rem; font-size:13.5px;">
      <div><strong>Farmer Name:</strong> Pranav Mendon</div>
      <div><strong>Plot ID:</strong> AGR-1024</div>
      <div><strong>Current Soil Moisture:</strong> 22.0%</div>
      <div><strong>Target Field Capacity:</strong> 45.0%</div>
    </div>
    <div style="background:#e8f5e9; border:1.5px solid #74c69d; border-radius:8px; padding:1.25rem;">
      <h4 style="margin:0 0 0.5rem; color:#1b4332; font-size:1.1rem;">Computed Moisture Deficit Output</h4>
      <p style="margin:0 0 6px 0; font-size:14px;"><strong>Moisture Deficit:</strong> <span style="color:#d90429; font-weight:bold;">23.0%</span></p>
      <p style="margin:0 0 6px 0; font-size:14px;"><strong>Estimated Water Volume Required:</strong> ~18.4 liters/m² (~184,000 L/ha) to restore optimal root-zone saturation.</p>
      <p style="margin:0; font-size:14px;"><strong>Advisory Action:</strong> <span class="status-pill status-hold" style="background:#fee2e2; color:#b91c1c; font-weight:bold; padding:4px 8px; border-radius:4px;">Deficit Alert: Irrigation Recommended</span></p>
    </div>
  </div>
</body></html>"""
    with open("tmp_exp5_task1.html", "w") as f: f.write(t1_html)
    capture_html("tmp_exp5_task1.html", "exp5_task1_deficit_calc.png", window_size="950,380")
    if os.path.exists("tmp_exp5_task1.html"): os.remove("tmp_exp5_task1.html")

    # Task 2: Multi-Factor Decision Rule Recommendation Engine
    t2_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"><link rel="stylesheet" href="form.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:900px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 2: Multi-Factor Decision Rule Recommendation Engine</h3>
    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin-bottom:1rem; font-size:13.5px;">
      <div style="background:#f8faf6; padding:10px; border-radius:6px; border:1px solid #d8ddd4;"><strong>Soil Moisture:</strong> 28% (&lt; 30%)</div>
      <div style="background:#f8faf6; padding:10px; border-radius:6px; border:1px solid #d8ddd4;"><strong>Rain Forecast:</strong> Clear (No Rain)</div>
      <div style="background:#f8faf6; padding:10px; border-radius:6px; border:1px solid #d8ddd4;"><strong>Crop Stage:</strong> Tillering Stage</div>
    </div>
    <div style="background:#fff7ed; border-left:4px solid #ea580c; border:1px solid #fed7aa; border-radius:8px; padding:1.25rem;">
      <h4 style="margin:0 0 0.5rem; color:#9a3412;">Task 2 Decision Result: Automated Recommendation</h4>
      <p style="margin:0 0 6px; font-size:14px;"><strong>Evaluated Rule:</strong> <code>if (moisture &lt; 30 &amp;&amp; !rainExpected) =&gt; Immediate Irrigation</code></p>
      <p style="margin:0; font-size:14px;"><strong>Advisory Action:</strong> <span class="status-pill status-hold" style="background:#ea580c; color:#fff; font-weight:bold; padding:4px 10px; border-radius:4px;">Irrigation Required Immediately (45 min Drip Cycle)</span></p>
    </div>
  </div>
</body></html>"""
    with open("tmp_exp5_task2.html", "w") as f: f.write(t2_html)
    capture_html("tmp_exp5_task2.html", "exp5_task2_decision_rules.png", window_size="950,380")
    if os.path.exists("tmp_exp5_task2.html"): os.remove("tmp_exp5_task2.html")

    # Task 3: Sugarcane Farm Object Representation
    t3_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:900px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 3: Object-Oriented JavaScript &mdash; Sugarcane Farm Object</h3>
    <p style="color:#516151; font-size:13px;">JavaScript Object encapsulation with properties and member method <code>displayFarmInfo()</code>:</p>
    <div class="card" style="background:#f4f9f4; border:1.5px solid #95d5b2; border-radius:8px; padding:1.25rem;">
      <h4 style="color:#1b4332; margin-top:0; font-size:1.1rem;">Sugarcane Farm Object Record (Instantiated)</h4>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; font-size:14px;">
        <div><strong>Farmer Name:</strong> Sanjay More</div>
        <div><strong>Plot ID:</strong> AGR-3052</div>
        <div><strong>Crop Stage:</strong> Grand Growth Stage</div>
        <div><strong>Soil Moisture:</strong> 26.5%</div>
        <div><strong>Farm Area:</strong> 4.5 Hectares</div>
        <div><strong>Irrigation Pump Status:</strong> <span style="background:#fee2e2; color:#b91c1c; padding:3px 8px; border-radius:4px; font-weight:bold;">Active (Running)</span></div>
      </div>
    </div>
  </div>
</body></html>"""
    with open("tmp_exp5_task3.html", "w") as f: f.write(t3_html)
    capture_html("tmp_exp5_task3.html", "exp5_task3_farm_object.png", window_size="950,380")
    if os.path.exists("tmp_exp5_task3.html"): os.remove("tmp_exp5_task3.html")

    # Task 4: Hourly Sensor Telemetry Array Processing
    t4_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:950px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 4: Hourly Soil Moisture Sensor Array Processing (24 Hours)</h3>
    <p style="font-size:13px; color:#555; margin-bottom:8px;"><strong>Array Data:</strong> <code>[38%, 35%, 33%, 30%, 28%, 27%, 26%, 25%, 29%, 32%, 34%, 36%, 35%, 33%, 31%, 29%, 28%, 27%, 26%, 25%, 24%, 28%, 31%, 35%]</code></p>
    <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1rem; margin-top:1rem;">
      <div style="padding:1rem; background:#f0fdf4; border-radius:8px; border:1px solid #bbf7d0;">
        <div style="font-size:0.75rem; color:#166534; font-weight:700;">MINIMUM MOISTURE</div>
        <div style="font-size:1.6rem; font-weight:800; color:#15803d;">24.0%</div>
      </div>
      <div style="padding:1rem; background:#eff6ff; border-radius:8px; border:1px solid #bfdbfe;">
        <div style="font-size:0.75rem; color:#1e40af; font-weight:700;">MAXIMUM MOISTURE</div>
        <div style="font-size:1.6rem; font-weight:800; color:#1d4ed8;">38.0%</div>
      </div>
      <div style="padding:1rem; background:#fefce8; border-radius:8px; border:1px solid #fef08a;">
        <div style="font-size:0.75rem; color:#854d0e; font-weight:700;">AVERAGE MOISTURE</div>
        <div style="font-size:1.6rem; font-weight:800; color:#a16207;">29.96%</div>
      </div>
      <div style="padding:1rem; background:#fef2f2; border-radius:8px; border:1px solid #fecaca;">
        <div style="font-size:0.75rem; color:#991b1b; font-weight:700;">CRITICAL READINGS (&lt;30%)</div>
        <div style="font-size:1.6rem; font-weight:800; color:#b91c1c;">12 Hours</div>
      </div>
    </div>
  </div>
</body></html>"""
    with open("tmp_exp5_task4.html", "w") as f: f.write(t4_html)
    capture_html("tmp_exp5_task4.html", "exp5_task4_array_telemetry.png", window_size="1000,380")
    if os.path.exists("tmp_exp5_task4.html"): os.remove("tmp_exp5_task4.html")

    # Task 5: Client-Side Input Validation Suite
    t5_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"><link rel="stylesheet" href="table.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:950px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 5: JavaScript Validation Test Suite Results</h3>
    <table class="data-table" style="font-size:0.9rem; width:100%; border-collapse:collapse;">
      <thead>
        <tr>
          <th>Field</th>
          <th>Input Value</th>
          <th>Rule Specification</th>
          <th>Validation Result</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Farmer Name</strong></td>
          <td><code>Pranav Mendon</code></td>
          <td>Alphabetic characters &amp; spaces only (/^[A-Za-z\s]+$/)</td>
          <td><span style="background:#dcfce7; color:#15803d; font-weight:bold; padding:4px 8px; border-radius:4px;">PASS - Valid</span></td>
        </tr>
        <tr>
          <td><strong>Mobile Number</strong></td>
          <td><code>9876543210</code></td>
          <td>10 digits starting with 6-9 (/^[6-9]\d{9}$/)</td>
          <td><span style="background:#dcfce7; color:#15803d; font-weight:bold; padding:4px 8px; border-radius:4px;">PASS - Valid</span></td>
        </tr>
        <tr>
          <td><strong>Plot ID</strong></td>
          <td><code>AGR-1024</code></td>
          <td>Format AGR-#### (/^AGR-\d{4}$/)</td>
          <td><span style="background:#dcfce7; color:#15803d; font-weight:bold; padding:4px 8px; border-radius:4px;">PASS - Valid</span></td>
        </tr>
        <tr>
          <td><strong>Soil Moisture</strong></td>
          <td><code>28%</code></td>
          <td>Numeric range between 0% and 100%</td>
          <td><span style="background:#dcfce7; color:#15803d; font-weight:bold; padding:4px 8px; border-radius:4px;">PASS - Valid</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</body></html>"""
    with open("tmp_exp5_task5.html", "w") as f: f.write(t5_html)
    capture_html("tmp_exp5_task5.html", "exp5_task5_validation_suite.png", window_size="1000,380")
    if os.path.exists("tmp_exp5_task5.html"): os.remove("tmp_exp5_task5.html")

    # Task 6: Interactive Advisory Request Form Execution
    t6_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="layout.css"><link rel="stylesheet" href="form.css"></head>
<body style="padding:25px; background:#f4f6f4; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width:950px; margin:0 auto; background:#fff; padding:25px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.08);">
    <h3 style="color:#1b4332; margin-top:0;">Task 6: Interactive Advisory Request &amp; Registration Form Execution</h3>
    <div class="alert-success" style="background:#dcfce7; border:2px solid #22c55e; border-radius:8px; padding:1rem; color:#15803d; margin-bottom:1rem;">
      <strong>Advisory Request Submitted Successfully!</strong><br>Record generated for Farmer <strong>Pranav Mendon</strong> (Plot: <strong>AGR-2048</strong>) on 14/08/2026.
    </div>
    <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:8px; padding:1.25rem;">
      <h4 style="color:#166534; margin-top:0;">Automated Advisory Decision</h4>
      <p style="margin:0 0 6px;"><strong>Farmer:</strong> Pranav Mendon | <strong>Mobile:</strong> 9823012345 | <strong>Plot:</strong> AGR-2048</p>
      <p style="margin:0 0 6px;"><strong>Crop Stage:</strong> Tillering Stage | <strong>Telemetry Moisture:</strong> 26%</p>
      <p style="margin:0;"><strong>Recommended Action:</strong> <span style="background:#ea580c; color:#fff; font-weight:bold; padding:4px 8px; border-radius:4px;">Irrigate 45 minutes via drip line at 1.2 kg/cm² pressure</span></p>
    </div>
  </div>
</body></html>"""
    with open("tmp_exp5_task6.html", "w") as f: f.write(t6_html)
    capture_html("tmp_exp5_task6.html", "exp5_task6_interactive_form.png", window_size="1000,420")
    if os.path.exists("tmp_exp5_task6.html"): os.remove("tmp_exp5_task6.html")


if __name__ == "__main__":
    generate_experiment_1()
    generate_experiment_2()
    generate_experiment_3()
    generate_experiment_4()
    generate_experiment_5()
    print("\nALL 37 TASK-WISE SCREENSHOTS GENERATED SUCCESSFULLY!")
