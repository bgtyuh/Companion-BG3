from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton

from controllers.build_controller import get_races, get_classes, get_weapons, get_armors, get_footwears, \
    save_build_to_db


class CreateBuildWidget(QWidget):
    def __init__(self, parent):
        """Initialise le widget pour créer un nouveau build."""
        super().__init__(parent)

        layout = QVBoxLayout()

        # Sélection de la race
        self.race_combo = QComboBox()
        self.race_combo.addItems([race[0] for race in get_races()])
        layout.addWidget(QLabel("Choisir une race:"))
        layout.addWidget(self.race_combo)

        # Sélection de la classe
        self.class_combo = QComboBox()
        self.class_combo.addItems([cls[0] for cls in get_classes()])
        layout.addWidget(QLabel("Choisir une classe:"))
        layout.addWidget(self.class_combo)

        # Sélection de l'arme
        self.weapon_combo = QComboBox()
        self.weapon_combo.addItems([weapon[1] for weapon in get_weapons()])
        layout.addWidget(QLabel("Choisir une arme:"))
        layout.addWidget(self.weapon_combo)

        # Sélection de l'armure
        self.armor_combo = QComboBox()
        self.armor_combo.addItems([armor[1] for armor in get_armors()])
        layout.addWidget(QLabel("Choisir une armure:"))
        layout.addWidget(self.armor_combo)

        # Sélection des bottes
        self.footwear_combo = QComboBox()
        self.footwear_combo.addItems([footwear[1] for footwear in get_footwears()])
        layout.addWidget(QLabel("Choisir des bottes:"))
        layout.addWidget(self.footwear_combo)

        # Bouton pour enregistrer le build
        self.save_button = QPushButton("Enregistrer le build")
        self.save_button.clicked.connect(self.save_build)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        # Bouton de retour au menu principal
        back_button = QPushButton("Retour au menu principal")
        back_button.clicked.connect(self.return_to_main)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def return_to_main(self):
        """Retourne au menu principal."""
        self.parent().show_main_menu()

    def save_build(self):
        """Enregistre le build sélectionné dans la base de données en utilisant les noms des items."""
        race_name = self.race_combo.currentText()  # Nom de la race sélectionnée
        class_name = self.class_combo.currentText()  # Nom de la classe sélectionnée
        weapon_name = self.weapon_combo.currentText()  # Nom de l'arme sélectionnée
        armor_name = self.armor_combo.currentText()  # Nom de l'armure sélectionnée
        footwear_name = self.footwear_combo.currentText()  # Nom des bottes sélectionnées

        # Appelle une fonction dans le contrôleur pour sauvegarder ces informations dans la base de données
        save_build_to_db(race_name, class_name, weapon_name, armor_name, footwear_name)
