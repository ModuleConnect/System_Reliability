import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, 
                             QTextEdit, QGraphicsView, QGraphicsScene, QHBoxLayout)
from PyQt6.QtGui import QPixmap

class ReliabilityApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Header
        app_title = QLabel("Reliability Calculation App")
        app_description = QLabel("This application calculates the reliability of the system based on the provided block diagram data.")

        # Instruction and Input Field
        instruction_label = QLabel("Enter the reliability block diagram data below:")
        self.input_text = QTextEdit()
        instruction_text = "Instructions on how to enter the input data :\n- First indicate how modules are connected by using - for series and | for parallel. \n- Secondly, represent each module in this notation ModA, ModB and so on. \n- Thirdly, after the first line that indicated how the modules are connected, the second lines should show the various reliabilities of each module like this: ModA = 0.99, MOdB = 0.89, and so on."
        self.input_text.setPlaceholderText(instruction_text)

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
        self.setMinimumWidth(1000)
        self.setMinimumHeight(800)
        self.show()

    def write_to_file(self, data):
        with open('Input.txt', 'w') as file:
            file.write(data)

    def calculate_reliability(self):
        # Write input to Input.txt
        data = self.input_text.toPlainText()
        self.write_to_file(data)

        # Dummy calculation for demonstration purposes.
        # Use the function/module you have in your app directory to get the actual reliability value.
        reliability_value = 0.99

        # Display the result (you can use a QDialog or a QLabel)
        result_label = QLabel(f'Total Reliability: {reliability_value}')
        result_label.show()

    def reset_app(self):
        self.input_text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ReliabilityApp()
    with open("gui/styles.qss", "r") as f:
        styles = f.read()
        app.setStyleSheet(styles)
    sys.exit(app.exec())
