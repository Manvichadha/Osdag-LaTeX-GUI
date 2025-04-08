import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QLabel, QScrollArea

def extract_component(component, full_text):
    pattern = r"(\\(?:sub)*section\*?\{" + re.escape(component) + r"\})(.*?)(?=\\(?:sub)*section|\\end\{document\})"
    match = re.search(pattern, full_text, re.DOTALL)
    if match:
        return match.group(0)
    else:
        return f"% {component} not found in template.\n\n"

class ComponentSelector(QWidget):
    def __init__(self, components, template_file):
        super().__init__()
        self.setWindowTitle("LaTeX Report Customizer")
        self.setGeometry(100, 100, 450, 350)
        self.checkboxes = []
        self.template_file = template_file

        layout = QVBoxLayout()

        label = QLabel("Select components to include in the report:")
        layout.addWidget(label)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        for comp in components:
            cb = QCheckBox(comp)
            scroll_layout.addWidget(cb)
            self.checkboxes.append(cb)

        scroll_area.setWidget(scroll_widget)
        layout.addWidget(scroll_area)

        generate_button = QPushButton("Generate Custom LaTeX File")
        generate_button.clicked.connect(self.generate_latex)
        layout.addWidget(generate_button)

        self.setLayout(layout)
    
    def generate_latex(self):
        selected = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        if not selected:
            print("No components selected!")
            return
        
        print("Selected components:", selected)

        try:
            with open(self.template_file, "r") as f:
                template_text = f.read()
        except Exception as e:
            print(f"Error reading {self.template_file}: {e}")
            return

        custom_body = ""
        for comp in selected:
            component_text = extract_component(comp, template_text)
            custom_body += component_text + "\n\n"
        
        header_match = re.search(r"^(.*?\\begin\{document\})", template_text, re.DOTALL)
        footer_match = re.search(r"(\\end\{document\}.*)$", template_text, re.DOTALL)
        
        if header_match and footer_match:
            header = header_match.group(1)
            footer = footer_match.group(1)
        else:
            header = r"\documentclass{article}\begin{document}"
            footer = r"\end{document}"
        
        final_tex = header + "\n\n" + custom_body + "\n" + footer

        output_filename = "custom_report.tex"
        with open(output_filename, "w") as f_out:
            f_out.write(final_tex)
        print(f"Custom LaTeX file '{output_filename}' created.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    components = [
        "Input Parameters",
        "List of Input Section",
        "Design Checks",
        "Selected Member Data",
        "Spacing Check",
        "Member Check",
        "Design Log"
    ]
    template_file = "template.tex"
    window = ComponentSelector(components, template_file)
    window.show()
    sys.exit(app.exec_())
