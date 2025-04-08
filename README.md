# Custom LaTeX Report Generator

This project is a Python-based application that allows users to dynamically generate a custom LaTeX report. Using a graphical user interface (GUI) built with PyQt, users can select which components of the report they wish to include (such as Title, Abstract, Introduction, Methodology, Results, Conclusion, and References). The selected sections are then automatically compiled into a LaTeX (.tex) file using PyLaTeX, which can be uploaded to Overleaf for PDF generation—ideal for users who do not have a local LaTeX distribution installed.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Overleaf Integration](#overleaf-integration)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **User-Friendly GUI:**  
  Built with PyQt5, the GUI allows users to select from a list of report components through checkable items.

- **Dynamic TeX Generation:**  
  Uses PyLaTeX to create a custom `.tex` file that includes only the sections chosen by the user.

- **Overleaf Integration:**  
  The generated LaTeX file can be uploaded to a pre-provided Overleaf template for PDF compilation.

- **Version Control:**  
  Code and project files are managed via GitHub with collaboration support.

## Usage

1. **Run the Application:**  
   python main.py

2. **Select Report Components:**  
   The GUI will display a list of available sections. Check the boxes next to the components you want to include in your report.

3. **Generate the TeX File:**  
    Click the "Generate PDF Report" button. This will create a custom_report.tex file in your project directory containing only the selected     sections.

## Overleaf Integration
  Since the project does not require a local LaTeX installation:

1. **Copy the Overleaf Template:**
Access the provided template and make a copy for your own project.

2. **Upload the Generated TeX File:**
Drag and drop or use the "Upload" feature in Overleaf to add the custom_report.tex file into your Overleaf project.

3. **Compile the PDF:**
Click "Recompile" on Overleaf to generate your final PDF report.




   
