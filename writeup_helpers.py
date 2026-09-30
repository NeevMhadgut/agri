import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_border(cell, **kwargs):
    """
    Set cell borders
    kwargs: top, bottom, left, right
    values: dict(sz=12, val='single', color='000000', space='0')
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(r'''
        <w:tcBorders {} >
            <w:top w:val="{top_val}" w:sz="{top_sz}" w:space="0" w:color="{top_color}"/>
            <w:left w:val="{left_val}" w:sz="{left_sz}" w:space="0" w:color="{left_color}"/>
            <w:bottom w:val="{bottom_val}" w:sz="{bottom_sz}" w:space="0" w:color="{bottom_color}"/>
            <w:right w:val="{right_val}" w:sz="{right_sz}" w:space="0" w:color="{right_color}"/>
        </w:tcBorders>
    '''.format(
        nsdecls('w'),
        top_val=kwargs.get('top', {}).get('val', 'single'),
        top_sz=kwargs.get('top', {}).get('sz', '4'),
        top_color=kwargs.get('top', {}).get('color', '333333'),
        left_val=kwargs.get('left', {}).get('val', 'single'),
        left_sz=kwargs.get('left', {}).get('sz', '4'),
        left_color=kwargs.get('left', {}).get('color', '333333'),
        bottom_val=kwargs.get('bottom', {}).get('val', 'single'),
        bottom_sz=kwargs.get('bottom', {}).get('sz', '4'),
        bottom_color=kwargs.get('bottom', {}).get('color', '333333'),
        right_val=kwargs.get('right', {}).get('val', 'single'),
        right_sz=kwargs.get('right', {}).get('sz', '4'),
        right_color=kwargs.get('right', {}).get('color', '333333'),
    ))
    tcPr.append(tcBorders)

def set_cell_shading(cell, color_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)

def add_header_banner(doc, header_img_path):
    if os.path.exists(header_img_path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run()
        run.add_picture(header_img_path, width=Inches(6.6))
    else:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r1 = p.add_run("K. J. Somaiya School of Engineering, Mumbai-77\n")
        r1.bold = True
        r1.font.size = Pt(14)
        r1.font.color.rgb = RGBColor(178, 34, 34)
        r2 = p.add_run("(Somaiya Vidyavihar University)\nDepartment of Computer Engineering\n")
        r2.bold = True
        r2.font.size = Pt(11)

def add_meta_table(doc, exp_no, title, date_perf="29 / 07 / 2026"):
    tbl = doc.add_table(rows=3, cols=4)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    # Row 1
    # Course Name (spans 2 cols) | Semester | Academic Year
    tbl.cell(0, 0).text = "Course Name:"
    tbl.cell(0, 1).text = "Web Development Laboratory (316U01L306)"
    tbl.cell(0, 2).text = "Semester:"
    tbl.cell(0, 3).text = "III"

    # Row 2
    tbl.cell(1, 0).text = "Date of Performance:"
    tbl.cell(1, 1).text = date_perf
    tbl.cell(1, 2).text = "DIV / Batch No:"
    tbl.cell(1, 3).text = "B - 3"

    # Row 3
    tbl.cell(2, 0).text = "Student Name:"
    tbl.cell(2, 1).text = "Pranav Mendon"
    tbl.cell(2, 2).text = "Roll No:"
    tbl.cell(2, 3).text = "16010125138"

    for row in tbl.rows:
        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_border(cell, top=dict(sz=6, color='888888'),
                                  bottom=dict(sz=6, color='888888'),
                                  left=dict(sz=6, color='888888'),
                                  right=dict(sz=6, color='888888'))
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.size = Pt(9.5)
                    r.font.name = 'Calibri'

    # Make labels bold
    for r_idx in range(3):
        for c_idx in [0, 2]:
            for r in tbl.cell(r_idx, c_idx).paragraphs[0].runs:
                r.bold = True
                r.font.color.rgb = RGBColor(128, 0, 0)

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(4)
    p_sp.paragraph_format.space_after = Pt(4)

    # Exp No Banner
    p_exp = doc.add_paragraph()
    p_exp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_exp = p_exp.add_run(f"Experiment No: {exp_no}")
    r_exp.bold = True
    r_exp.font.size = Pt(13)
    r_exp.font.color.rgb = RGBColor(180, 0, 0)
    p_exp.paragraph_format.space_before = Pt(2)
    p_exp.paragraph_format.space_after = Pt(4)

    # Title Box
    t_box = doc.add_table(rows=1, cols=1)
    t_box.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t_box.cell(0, 0)
    p_t = c.paragraphs[0]
    r_tlabel = p_t.add_run("Title: ")
    r_tlabel.bold = True
    r_tlabel.font.color.rgb = RGBColor(150, 0, 0)
    r_ttext = p_t.add_run(title)
    r_ttext.bold = True
    set_cell_border(c, top=dict(sz=8, color='444444'), bottom=dict(sz=8, color='444444'),
                       left=dict(sz=8, color='444444'), right=dict(sz=8, color='444444'))
    set_cell_shading(c, "F8F9FA")
    p_t.paragraph_format.space_before = Pt(4)
    p_t.paragraph_format.space_after = Pt(4)

def add_boxed_section(doc, label, content, bg_hex="FFFFFF"):
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    p = cell.paragraphs[0]
    r_lbl = p.add_run(label + ("\n" if not label.endswith(":") else " "))
    r_lbl.bold = True
    r_lbl.font.color.rgb = RGBColor(160, 0, 0)
    r_lbl.font.size = Pt(10.5)

    if isinstance(content, str):
        r_cnt = p.add_run(content)
        r_cnt.font.size = Pt(9.5)
    elif isinstance(content, list):
        for item in content:
            p_item = cell.add_paragraph()
            p_item.paragraph_format.left_indent = Inches(0.2)
            p_item.paragraph_format.space_before = Pt(1)
            p_item.paragraph_format.space_after = Pt(1)
            r_it = p_item.add_run(f"• {item}")
            r_it.font.size = Pt(9.5)

    set_cell_border(cell, top=dict(sz=6, color='666666'), bottom=dict(sz=6, color='666666'),
                          left=dict(sz=6, color='666666'), right=dict(sz=6, color='666666'))
    if bg_hex != "FFFFFF":
        set_cell_shading(cell, bg_hex)
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)

def add_code_block(doc, title, code_str):
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(2)
    r = p_title.add_run(title)
    r.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0, 51, 102)

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_border(cell, top=dict(sz=4, color='CCCCCC'), bottom=dict(sz=4, color='CCCCCC'),
                          left=dict(sz=4, color='CCCCCC'), right=dict(sz=4, color='CCCCCC'))
    set_cell_shading(cell, "F7F9FB")
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    r_code = p.add_run(code_str)
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(8.5)
    r_code.font.color.rgb = RGBColor(34, 34, 34)

def add_screenshot(doc, title, img_path):
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(2)
    r = p_title.add_run(title)
    r.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(128, 0, 0)

    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(6)
        run = p_img.add_run()
        run.add_picture(img_path, width=Inches(6.0))

print("Helper definitions loaded successfully.")
