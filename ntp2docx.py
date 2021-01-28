#from md2py import md2py
import fnmatch
import os
import re
import mistune
from bs4 import BeautifulSoup
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.oxml.xmlchemy import OxmlElement

# following function from https://stackoverflow.com/a/48666968/1018206
def insert_paragraph_after(paragraph, text=None, style=None):
    """Insert a new paragraph after the given paragraph."""
    new_p = OxmlElement("w:p")
    paragraph._p.addnext(new_p)
    new_para = Paragraph(new_p, paragraph._parent)
    if text:
        new_para.add_run(text)
    if style is not None:
        new_para.style = style
    return new_para

# following function modified from https://github.com/python-openxml/python-docx/issues/846#issuecomment-660494075
def add_bookmark(paragraph, _id):
    """Insert bookmark to a paragraph."""
    name = '_Ref_id_num_' + _id
    start = OxmlElement('w:bookmarkStart')
    start.set(qn('w:name'), name)
    start.set(qn('w:id'), str(_id))
    paragraph._p.append(start)
    end = OxmlElement('w:bookmarkEnd')
    end.set(qn('w:id'), str(_id))
    paragraph._p.append(end)
    return name

# following function modified from https://github.com/python-openxml/python-docx/issues/846#issuecomment-660494075
def append_ref_to_paragraph(paragraph, refName, text = ''):
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('w:anchor'), refName)
    hyperlinktext = OxmlElement('w:r')
    hyperlinktextproperty = OxmlElement('w:rPr')
    hyperlinktextpropertystyle = OxmlElement('w:rStyle')
    hyperlinktextpropertystyle.set(qn('w:val'), "InternetLink")
    hyperlinktextcontent = OxmlElement('w:t')
    hyperlinktextcontent.text = text
    hyperlinktextproperty.append(hyperlinktextpropertystyle)
    hyperlinktext.append(hyperlinktextproperty)
    hyperlinktext.append(hyperlinktextcontent)
    hyperlink.append(hyperlinktext)
    paragraph._p.append(hyperlink)

def find(pattern, path):
    """Find files in a path based on a filename pattern with numbers and sorted by the number ASC."""
    result = {}
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                tpfile = os.path.join(root, name)
                tpnumber = re.findall("[0-9]+", tpfile)
                result[tpfile] = tpnumber
    result = sorted(result.items(), key=lambda kv: kv[1])
    return result

# open template.docx
document = Document("template.docx")

# find the heading of the property declarations
pdparagraphs = document.paragraphs
for pdparagraph in pdparagraphs:
    if pdparagraph.text == "CRMntp Property Declarations":
         break

# find all files with property definitions as included in the repo
files = find('tp*.md', 'source')
properties = {}
curpara = pdparagraph

for file in files:
    mdfile = open(file[0], "r").read()
    html = mistune.markdown(mdfile)
    parsed_html = BeautifulSoup(html)
    heading1 = parsed_html.find_all('h1')[0].contents[0] #should be only one
    propid = str.lower(heading1[:heading1.find(" ")])
    curpara = insert_paragraph_after(curpara, heading1, "CRM Property Label")
    curbookmark = add_bookmark(curpara, propid)
    properties[propid] = [curpara, curbookmark, parsed_html]

for propertyname, property in properties.items():
    headings2 = property[2].find_all('h2')
    curpara = property[0]
    for heading2 in headings2:
        curpara = insert_paragraph_after(curpara, heading2.contents[0], "CRM Description Label")
        curtextruns = heading2.find_next("p")
        if heading2.contents[0] == "Domain:" or heading2.contents[0] == "Range:":
            curstyle = "CRM Domain Range"
        elif heading2.contents[0] == "Subproperty of:":
            curstyle = "CRM Super Sub Property"
        elif heading2.contents[0] == "Quantification:":
            curstyle = "CRM Quantification"
        elif heading2.contents[0] == "Scope note:":
            curstyle = "CRM Scope Note Text"

        curpara = insert_paragraph_after(curpara, None, curstyle)
        for curtextrun in curtextruns:
            if curtextrun.name == "a": # if this part of the run is a link
                for attr, curlink in curtextrun.attrs.items():
                    if attr == 'href':
                        curlink = "_Ref_id_num_" + curlink[1:] #trim the '#' from markdown
                        append_ref_to_paragraph(curpara, curlink, curtextrun.contents[0])
            else: # treat everything else as text for now
                curpara.add_run(curtextrun)

#curpara = insert_paragraph_after(curpara, "domain ")
#append_ref_to_paragraph(curpara, properties[propid][1], "link")

# for file in files:
#     mdfile = open(file[0], "r").read()
#     html = mistune.markdown(mdfile)
#     parsed_html = BeautifulSoup(html)
#     heading1 = parsed_html.find_all('h1')[0].contents[0] #should be only one
#     curpara = insert_paragraph_after(pdparagraph, heading1, "CRM Property Label")
#     headings2 = parsed_html.find_all('h2')
#     for heading2 in headings2:
#         curpara = insert_paragraph_after(curpara, heading2.contents[0], "CRM Description Label")
#         curtext = heading2.find_next("p").contents[0]
#         if heading2.contents[0] == "Domain:" or heading2.contents[0] == "Range:":
#             curpara = insert_paragraph_after(curpara, curtext, "CRM Domain Range")
#         elif heading2.contents[0] == "Subproperty of:":
#             curpara = insert_paragraph_after(curpara, curtext, "CRM Super Sub Property")
#         elif heading2.contents[0] == "Quantification:":
#             curpara = insert_paragraph_after(curpara, curtext, "CRM Quantification")
#         elif heading2.contents[0] == "Scope note:":
#             curpara = insert_paragraph_after(curpara, curtext, "CRM Scope Note Text")

# styles = document.styles

# paragraph_styles = [
#    s for s in styles if s.type == WD_STYLE_TYPE.PARAGRAPH
# ]

document.save('demo.docx')

# for style in paragraph_styles:
#      if style == "Heading 1":
#          pass

# document.add_heading('Document Title', 0)
#
# p = document.add_paragraph('A plain paragraph having some ')
# p.add_run('bold').bold = True
# p.add_run(' and some ')
# p.add_run('italic.').italic = True
#
# document.add_heading('Heading, level 1', level=1)
# document.add_paragraph('Intense quote', style='Intense Quote')
#
# document.add_paragraph(
#     'first item in unordered list', style='List Bullet'
# )
# document.add_paragraph(
#     'first item in ordered list', style='List Number'
# )
#
# document.add_picture('monty-truth.png', width=Inches(1.25))
#
# records = (
#     (3, '101', 'Spam'),
#     (7, '422', 'Eggs'),
#     (4, '631', 'Spam, spam, eggs, and spam')
# )
#
# table = document.add_table(rows=1, cols=3)
# hdr_cells = table.rows[0].cells
# hdr_cells[0].text = 'Qty'
# hdr_cells[1].text = 'Id'
# hdr_cells[2].text = 'Desc'
# for qty, id, desc in records:
#     row_cells = table.add_row().cells
#     row_cells[0].text = str(qty)
#     row_cells[1].text = id
#     row_cells[2].text = desc
#
# document.add_page_break()
#
# document.save('demo.docx')