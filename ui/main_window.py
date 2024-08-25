from PyQt5.QtWidgets import QMainWindow, QAction

from ui.create_build import CreateBuildWidget
from ui.show_armours import ShowarmoursWidget
from ui.show_weapons import ShowWeaponsWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Baldur's Gate 3 Companion Tool")
        self.setGeometry(100, 100, 800, 600)
        self.create_menu()

    def create_menu(self):
        # Création du bouton Outils en menu déroulant
        menubar = self.menuBar()
        tools_menu = menubar.addMenu("Outils")

        # Ajout des options du menu déroulant Outils
        # Créer un build
        create_build_action = QAction("Créer un Build", self)
        create_build_action.triggered.connect(self.show_create_build)
        tools_menu.addAction(create_build_action)

        # Armes
        weapons_action = QAction("Afficher les Armes", self)
        weapons_action.triggered.connect(self.show_weapons)
        tools_menu.addAction(weapons_action)

        # Armures
        armours_action = QAction("Afficher les Armures", self)
        armours_action.triggered.connect(self.show_armours)
        tools_menu.addAction(armours_action)

    def show_create_build(self):
        """Affiche l'interface de création de build."""
        create_build_widget = CreateBuildWidget()
        self.setCentralWidget(create_build_widget)

    def show_weapons(self):
        weapons_widget = ShowWeaponsWidget()
        self.setCentralWidget(weapons_widget)

    def show_armours(self):
        armours_widget = ShowarmoursWidget()
        self.setCentralWidget(armours_widget)
