# imports and global variables
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys
from PyQt6.QtCore import QSize, Qt

app = QApplication(sys.argv)


# logics
def calculate_bmi_and_result():
    result = None
    weight = float(weight_entry.text())
    height = float(height_entry.text())
    bmi = weight // (height**2)

    if bmi < 18.5:
        result = "Under Weight"
    elif 18.5 <= bmi < 25:
        result = "Normal"
    elif 25 <= bmi < 30:
        result = "Over Weight"
    elif 30 <= bmi < 35:
        result = "Obese"
    else:
        result = "Extremely Obese"
    result_label.setText(f"Result: {result}")


# ui design
window = QMainWindow()
window.setWindowTitle("GUI BMI Calculator")
window.setFixedSize(QSize(400, 300))
widget = QWidget()
layout = QVBoxLayout()

height_label = QLabel("Height (m):")
height_entry = QLineEdit()

weight_label = QLabel("Weight (kg):")
weight_entry = QLineEdit()

calculate_button = QPushButton(text="Calculate BMI")
calculate_button.clicked.connect(calculate_bmi_and_result)
result_label = QLabel("Result:")


layout.addWidget(height_label)
layout.addWidget(height_entry)
layout.addWidget(weight_label)
layout.addWidget(weight_entry)
layout.addWidget(calculate_button)
layout.addWidget(result_label)
widget.setLayout(layout)
window.setCentralWidget(widget)
window.show()

# Start the event loop.

# running the application
app.exec()