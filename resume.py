# PDF Resume Creator
# Create a python program that will create your personal resume in PDF format
# All personal details are stored in a JSON file
# Your program should read the JSON file and write the details in the PDF

import json
from fpdf import FPDF


# PDF layout and Format
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
educ_tertiary1 = resumeInfos["Educational Backgroud"]["Tertiary"]["School"]
educ_tertiary2 = resumeInfos["Educational Background"]["Tertiary"]["School Year"]
educ_secondary1 = resumeInfos["Educational Background"]["Secondary"]["School"]
educ_secondary2 = resumeInfos["Educational Background"]["Secondary"]["School Year"]
educ_primary1 = resumeInfos["Educational Background"]["primary"]["School"]
educ_primary2 = resumeInfos["Educational Background"]["primary"]["School Year"]

# skills
skill_1 = resumeInfos["Skill"]["Skill 1"]
skill_2 = resumeInfos["Skill"]["Skill 2"]

# customizing the header

    
    

pdf.output("ROBLES_REX-IMMAN.pdf")