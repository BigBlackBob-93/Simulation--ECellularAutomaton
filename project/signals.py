from PyQt6.QtCore import QTimer
from PyQt6 import QtGui
from PyQt6.QtWidgets import QTableWidgetItem
from objects import (
    rule_sb, set_init_le,  # parameters
    launch_btn,  # buttons
    table  # table
)


time: QTimer
sensor = False
count = 0
patterns = ['111', '110', '101', '100', '011', '010', '001', '000']
rule: dict
generation: list


def check_state():
    if sensor:
        stop()
    else:
        start()


def start():
    global sensor, rule, generation

    sensor = True
    clear()

    generation = list(set_init_le.displayText())
    add_row(colour='#84889F')

    states = bin(rule_sb.value())[2:]
    while len(states) < 8:
        states = '0' + states
    rule = {pattern: state for state, pattern in zip(list(states), patterns)}

    timer()


def timer():
    global time

    time = QTimer()
    time.start()
    time.setInterval(500)
    time.timeout.connect(shot)


def shot():
    global generation

    generation = create_generation()
    add_row()


def create_generation() -> list:
    up = generation
    down = []
    for i in range(len(up)):
        if i == 0:
            part = up[0:2]
            part.insert(0, up[-1])
        elif i == len(up) - 1:
            part = up[-2:]
            part.append(up[0])
        else:
            part = up[i - 1:i + 2]
        down.append(rule[''.join(part)])
    return down


def stop():
    global sensor, count, time
    time.stop()
    time.deleteLater()
    sensor = False
    count = 0


def clear():
    table.setRowCount(0)


def add_row(colour: str = '#A6AAC7'):
    global count
    table.insertRow(count)
    index = 0
    for char in generation:
        if char == '1':
            table.setItem(count, index, QTableWidgetItem(' '))
            table.item(count, index).setBackground(QtGui.QColor(colour))
        index += 1
    count += 1


launch_btn.clicked.connect(check_state)
