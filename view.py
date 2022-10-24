from PyQt6.QtWidgets import *
from PyQt6 import uic

import controller


class View(QMainWindow):
    op1: QSpinBox
    op2: QSpinBox
    oper: QComboBox
    close_pb: QPushButton
    execute_pb: QPushButton
    reset_pb: QPushButton
    ergebnis: QLabel
    statusbar: QStatusBar

    def __init__(self, c: controller):
        super().__init__()
        uic.loadUi("viewUI.ui", self)
        self.oper.addItem("+")
        self.oper.addItem("-")
        self.oper.addItem("*")
        self.oper.addItem("/")
        self.execute_pb.clicked.connect(c.execute)
        self.reset_pb.clicked.connect(c.reset)

    def reset(self) -> None:
        self.oper.setCurrentIndex(0)
        self.op1.setValue(0)
        self.op2.setValue(0)
        self.ergebnis.setText("Noch kein Ergebnis")
        self.set_text_statusbar(
            "Bitte zwei Werte für die Operanden eingeben."
            "Einen Operator auswählen und mit Ausführen "
            "berechnen lassen.")

    def set_ergebnis(self, t: str) -> None:
        self.ergebnis.setText(t)

    def set_text_statusbar(self, t: str) -> None:
        self.statusbar.showMessage(t)

    def get_op1(self) -> int:
        return self.op1.value()

    def get_op2(self) -> int:
        return self.op2.value()

    def get_operator(self) -> str:
        return self.oper.currentText()


if __name__ == '__main__':
    import sys

    app = QApplication([])
    v = View()
    v.show()
    sys.exit(app.exec())
