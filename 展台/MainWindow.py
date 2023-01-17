from ui_MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

class MainWindow(Ui_MainWindow):
    def __init__(self,ui) -> None:
        super().setupUi(ui)