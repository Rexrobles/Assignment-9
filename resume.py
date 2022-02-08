# PDF Resume Creator
# Create a python program that will create your personal resume in PDF format
# All personal details are stored in a JSON file
# Your program should read the JSON file and write the details in the PDF

import json
from fpdf import FPDF


# PDF layout and Format
# PDF Creating
pdf = FPDF('P', 'cm', 'A4') 
pdf.add_page()

# Reading the json file
with open('resume.json') as datafile:
    resumeInfos = json.load(datafile)
  
# getting information from json file  
# Basic Information
Last_name = resumeInfos ["basic info"]["Last Name"]
First_name = resumeInfos ["basic info"]["First Name"]
Middle_name = resumeInfos ["basic info"]["Middle Name"]
age = resumeInfos ["basic info"]["Age"]
address = resumeInfos ["basic info"]["Address"]
gender = resumeInfos ["basic info"]["gender"]
birthday = resumeInfos ["basic info"]["Birthday"]
religion = resumeInfos ["basic info"]["religion"]
citizenship = resumeInfos ["basic info"]["citizenship"] 

# Contact info
contact = resumeInfos["Contact info"]["Contact Num."]
email = resumeInfos["Contact info"]["Email"]

# Objectives
objective = resumeInfos["Objectives"]["Career Objective"]

# educational background
educ_tertiary1 = resumeInfos["Educational Background"]["Tertiary"]["School"]
educ_tertiary2 = resumeInfos["Educational Background"]["Tertiary"]["School Year"]
educ_secondary1 = resumeInfos["Educational Background"]["Secondary"]["School"]
educ_secondary2 = resumeInfos["Educational Background"]["Secondary"]["School Year"]
educ_primary1 = resumeInfos["Educational Background"]["primary"]["School"]
educ_primary2 = resumeInfos["Educational Background"]["primary"]["School Year"]

# skills
skill_1 = resumeInfos["Skill"]["Skill 1"]
skill_2 = resumeInfos["Skill"]["Skill 2"]

# customizing the header
pdf.set_font("Arial", "B", 30)
pdf.set_text_color(40,51,49)
pdf.set_fill_color(215,215,215)
pdf.cell(20, 5, f"{resumeInfos['basic info']['Last Name']}{resumeInfos['basic info']['First Name']} {resumeInfos['basic info']['Middle Name']}", ln=1, align="C", fill=1)

# adding the basic information on pdf
pdf.set_text_color(255,230,255)
pdf.set_fill_color(30,51,49)
pdf.set_font("Arial", "B", 18)
pdf.cell(0,2, "     Personal Information", align="L", ln=2, fill=1)

# adding the basic infos
pdf.set_font("Arial", "")
pdf.set_font_size(12)
pdf.set_text_color(40,40,40)
pdf.cell(0,0.9," Age: " + (resumeInfos["basic info"]["Age"]),align="L", ln=1, fill=0)
pdf.cell(0,0.9," Address: " + (resumeInfos["basic info"]["Address"]),align="L", ln=1, fill=0)
pdf.cell(0,0.9," Gender: " + (resumeInfos["basic info"]["gender"]),align="L", ln=1, fill=0)
pdf.cell(0,0.9," Birthday: " + (resumeInfos ["basic info"]["Birthday"]),align="L", ln=1, fill=0)
pdf.cell(0,0.9," Relegion: " + (resumeInfos ["basic info"]["religion"]),align="L", ln=1, fill=0)
pdf.cell(0,0.9," Citizenship: " + (resumeInfos ["basic info"]["citizenship"]),align="L", ln=1, fill=0)


pdf.output("ROBLES_REX-IMMAN.pdf")