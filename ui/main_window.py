from PyQt5.QtWidgets import QMainWindow, QAction
from controllers.build_controller import get_all_builds
from ui.show_builds import ShowBuildsWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Baldur's Gate 3 Companion Tool")
        self.setGeometry(100, 100, 800, 600)
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        tools_menu = menubar.addMenu("Outils")

        builds_action = QAction("Gestion des Builds", self)
        builds_action.triggered.connect(self.show_builds)
        tools_menu.addAction(builds_action)

    def show_builds(self):
        builds = get_all_builds()  # Appelle la fonction du contrôleur pour obtenir les builds
        builds_widget = ShowBuildsWidget(builds)  # Crée le widget pour afficher les builds
        self.setCentralWidget(builds_widget)  # Affiche le widget dans la fenêtre principale
