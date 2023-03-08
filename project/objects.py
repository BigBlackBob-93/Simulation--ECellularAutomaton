from PyQt6.QtWidgets import (QMainWindow, QLabel, QSpinBox, QPushButton, QTableWidget, QLineEdit)

# window
window = QMainWindow()
window.setWindowTitle("Simulation: Cellular Automaton")
window.setGeometry(350, 300, 270, 200)

# variables
rule = 90
NUM = 14
# ------! depends on the NUM !------
initial_state = '00000011000100'
mask = "BBBBBBBBBBBBBB;"


# parameters
def SetSpinBox(spin_box: QSpinBox, above: int, left: int = 60) -> None:
    spin_box.setRange(0, 256)
    spin_box.setSingleStep(10)
    spin_box.move(left, above)


def SetLable(label: QLabel, text: str, above: int, left: int = 60) -> None:
    label.setText(text)
    label.move(left, above)


rule_l = QLabel(window)
rule_sb = QSpinBox(window)
rule_sb.setValue(rule)
SetLable(rule_l, "Rule:", above=20)
SetSpinBox(rule_sb, above=20, left=100)

set_init_l = QLabel(window)
SetLable(set_init_l, "Set Init:", above=60, left=55)

set_init_le = QLineEdit(window)
set_init_le.move(105, 60)
set_init_le.setText(initial_state)
set_init_le.setInputMask(mask)

# buttons
launch_btn = QPushButton(window)
launch_btn.move(70, 120)
launch_btn.setText("Start/Stop")

# table
table = QTableWidget()
table.setWindowTitle("Simulation: Cellular Automaton - RESULTS")
table.setGeometry(1300, 300, 570, 400)

table.setColumnCount(NUM)
for num in range(table.columnCount()):
    table.setColumnWidth(num, 1)

window.show()
table.show()
