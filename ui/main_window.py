from PyQt5.QtWidgets import QMainWindow, QAction
from ui.show_weapons import ShowWeaponsWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Baldur's Gate 3 Companion Tool")
        self.setGeometry(100, 100, 800, 600)
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        tools_menu = menubar.addMenu("Outils")

        weapons_action = QAction("Afficher les Armes", self)
        weapons_action.triggered.connect(self.show_weapons)
        tools_menu.addAction(weapons_action)

    def show_weapons(self):
        weapons_widget = ShowWeaponsWidget()
        self.setCentralWidget(weapons_widget)
