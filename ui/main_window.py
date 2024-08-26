from PyQt5.QtWidgets import QMainWindow, QAction, QWidget, QVBoxLayout, QPushButton, QLabel

from ui.create_build import CreateBuildWidget
from ui.manage_builds import ManageBuildsWidget
from ui.modify_build import ModifyBuildWidget
from ui.show_armours import ShowArmoursWidget
from ui.show_weapons import ShowWeaponsWidget


class MainWindow(QMainWindow):
    def __init__(self):
        """Initialise la fenêtre principale et le menu."""
        super().__init__()
        self.setWindowTitle("Baldur's Gate 3 Companion Tool")
        self.setGeometry(100, 100, 800, 600)
        self.create_menu()
        self.show_main_menu()

    def create_menu(self):
        """Crée le menu principal avec des sections File, Edit, Help."""
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        # Option pour quitter l'application
        exit_action = QAction("Quitter", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu("Edit")
        help_menu = menubar.addMenu("Help")

        about_action = QAction("À propos", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def show_main_menu(self):
        """Affiche l'interface principale avec les boutons de navigation."""
        main_widget = QWidget()
        layout = QVBoxLayout()

        create_build_button = QPushButton("Créer un Build")
        create_build_button.clicked.connect(self.show_create_build)
        layout.addWidget(create_build_button)

        manage_builds_button = QPushButton("Gérer les Builds")
        manage_builds_button.clicked.connect(self.show_manage_builds)
        layout.addWidget(manage_builds_button)

        weapons_button = QPushButton("Afficher les Armes")
        weapons_button.clicked.connect(self.show_weapons)
        layout.addWidget(weapons_button)

        armours_button = QPushButton("Afficher les Armures")
        armours_button.clicked.connect(self.show_armours)
        layout.addWidget(armours_button)

        info_label = QLabel("Sélectionnez une option pour commencer.")
        layout.addWidget(info_label)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def show_create_build(self):
        """Affiche l'interface de création de build."""
        create_build_widget = CreateBuildWidget(self)
        self.setCentralWidget(create_build_widget)

    def show_manage_builds(self):
        """Affiche l'interface pour gérer les builds."""
        manage_builds_widget = ManageBuildsWidget(self)
        self.setCentralWidget(manage_builds_widget)

    def show_modify_build(self, build_id):
        """Affiche l'interface pour modifier un build spécifique."""
        build_data = self.get_build_data(build_id)
        modify_build_widget = ModifyBuildWidget(self, build_id, build_data)
        self.setCentralWidget(modify_build_widget)

    def show_weapons(self):
        """Affiche l'interface pour visualiser les armes."""
        weapons_widget = ShowWeaponsWidget(self)
        self.setCentralWidget(weapons_widget)

    def show_armours(self):
        """Affiche l'interface pour visualiser les armures."""
        armours_widget = ShowArmoursWidget(self)
        self.setCentralWidget(armours_widget)

    def show_about(self):
        """Affiche une fenêtre avec des informations sur l'application."""
        # Implémenter une fenêtre modale ou un message d'information
        pass
