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
with open('Assignment 9\resume.json') as datafile:
    resumeInfos = json.load(datafile)
  
# getting information from json file  
# Basic Information
Last_name = resumeInfos["Last name"]
First_name = resumeInfos["First name"]
Middle_name = resumeInfos["Middle name"]
age = resumeInfos["Age"]
address = resumeInfos["Address"]

# Contact info
contact = resumeInfos["Contact Num."]
email = resumeInfos["Email"]

# Objectives
objective = resumeInfos["Career Objective"]

pdf.output("ROBLES_REX-IMMAN.pdf")