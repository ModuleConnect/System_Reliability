import sys

sys.path.append('../')
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog,
                             QTextEdit, QHBoxLayout)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


from src.file_sys import *
from src.gen_exp import *


class ReliabilityApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Header
        app_title = QLabel("Reliability Calculation App")
        app_description = QLabel("This application calculates the reliability of the system based on the provided block diagram data.")


        # Instruction Image and Input Field
        instruction_label = QLabel("Enter the reliability block diagram data below:")

        # Add image to QLabel
        pixmap = QPixmap('../Module_Diagram.jpg')  # Replace with the path to your image file
        image_label = QLabel()
        image_label.setPixmap(pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))  # Set size according to your need
        layout.addWidget(image_label)

        # Add new instruction label
        new_instruction_label = QLabel(
            """Instructions on how to enter the input data: (Text description goes here)
                This input should be a text file of the following format:

                        \START1 \END5
                        -L_N1 -MModuleA -R0.99 -R_N2
                        -L_N2 -MModuleB -R0.97 -R_N3
                        -L_N2 -MModuleC -R0.98 -R_N3
                        -L_N3 -MModuleD -R0.90 -R_N4
  

            Each line represents a module with options:
            -L_N for the left node, 
            -M for the module value/name, 
            -R for the relaibility value, and -R_N for the right node. 
            ALso The Iinput needs to have a starting node and an ending node""")
        layout.addWidget(new_instruction_label)

        self.input_text = QTextEdit()


        # Buttons
        btn_calculate = QPushButton("Calculate")
        btn_reset = QPushButton("Reset")

        btn_calculate.clicked.connect(self.calculate_reliability)
        btn_reset.clicked.connect(self.reset_app)

        # Footer Layout
        footer_layout = QHBoxLayout()
        footer_layout.addWidget(btn_calculate)
        footer_layout.addWidget(btn_reset)

        # Add widgets to main layout
        layout.addWidget(app_title)
        layout.addWidget(app_description)
        layout.addWidget(instruction_label)
        layout.addWidget(self.input_text)
        layout.addLayout(footer_layout)

        self.setLayout(layout)
        self.setWindowTitle('Reliability Calculation App')
        self.resize(1000, 800)

        self.setMinimumWidth(700)
        self.setMinimumHeight(700)
        self.show()

    def write_to_file(self, data):
        with open('Input.txt', 'w') as file:
            file.write(data)

    def calculate_reliability(self):
        # Write input to Input.txt

        data = self.input_text.toPlainText().rstrip()
        # self.write_to_file(data)
      
        print(self.input_text.toPlainText())


        # Dummy calculation for demonstration purposes.
        # Use the function/module you have in your app directory to get the actual reliability value.
        reliability_value = 0.99        
        # Testing the backend
        list_of_modules, nodes = read_modules_from_string(data)
        dictionary = dictionarize(list_of_modules)
        print("The following are the information retrieved form the file\n")
        print(f"Start Node:{nodes[0]} and End Node:{nodes[1]}")

        exp = buildExpression(list_of_modules, int(nodes[0]), int(nodes[1]), )
        print(exp)

        # final_exp = postfix_to_infix(['ModA', 'ModB', '|', 'ModC', '*', 'ModD', '*'])
        final_exp = postfix_to_infix(exp)

        print("The Expresion Of The New System:",final_exp)


        res = eval(final_exp, dictionary)
        print(res)
        reliability_value = res.rel
        ######################################################################################

        # Display the result (you can use a QDialog or a QLabel)
        
# Create a QDialog
        dialog = QDialog()
        dialog.setWindowTitle("Result Dialog")

        # Create a QLabel for the result
        result_label = QLabel(f"""The Expresion Of The System is :{final_exp},
                              Total Reliability: {reliability_value}
                              """, parent=dialog)

        # Set the layout for the dialog and add the result label
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(result_label)
        dialog.setLayout(dialog_layout)

        # Show the dialog
        dialog.exec()

    def reset_app(self):
        self.input_text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ReliabilityApp()
    with open("./styles.qss", "r") as f:
        styles = f.read()
        app.setStyleSheet(styles)
    sys.exit(app.exec())
