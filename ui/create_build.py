from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel, QListWidgetItem
from PyQt5.QtGui import QIcon
from controllers.build_controller import get_races, get_classes_with_images, get_subclasses_with_images, get_weapons, get_armors, get_footwears, save_build_to_db

class CreateBuildWidget(QWidget):
    def __init__(self, parent):
        """Initialise le widget pour créer un nouveau build."""
        super().__init__(parent)

        layout = QVBoxLayout()

        # Sélection de la race
        self.race_combo = QComboBox()
        races = [race[0] for race in get_races()]
        self.race_combo.addItems(races)
        layout.addWidget(QLabel("Choisir une race:"))
        layout.addWidget(self.race_combo)

        # Sélection de la classe
        self.class_combo = QComboBox()
        self.load_classes_with_images()
        self.class_combo.currentIndexChanged.connect(self.update_subclasses)
        layout.addWidget(QLabel("Choisir une classe:"))
        layout.addWidget(self.class_combo)

        # Sélection de la sous-classe
        self.subclass_combo = QComboBox()
        self.update_subclasses()  # Initialiser les sous-classes pour la classe par défaut
        layout.addWidget(QLabel("Choisir une sous-classe:"))
        layout.addWidget(self.subclass_combo)

        # Sélection de l'arme
        self.weapon_combo = QComboBox()
        weapons = [weapon[1] for weapon in get_weapons()]
        self.weapon_combo.addItems(weapons)
        layout.addWidget(QLabel("Choisir une arme:"))
        layout.addWidget(self.weapon_combo)

        # Sélection de l'armure
        self.armor_combo = QComboBox()
        armors = [armor[1] for armor in get_armors()]
        self.armor_combo.addItems(armors)
        layout.addWidget(QLabel("Choisir une armure:"))
        layout.addWidget(self.armor_combo)

        # Sélection des bottes
        self.footwear_combo = QComboBox()
        footwears = [footwear[1] for footwear in get_footwears()]
        self.footwear_combo.addItems(footwears)
        layout.addWidget(QLabel("Choisir des bottes:"))
        layout.addWidget(self.footwear_combo)

        # Bouton pour enregistrer le build
        save_button = QPushButton("Enregistrer le build")
        save_button.clicked.connect(self.save_build)
        layout.addWidget(save_button)

        # Bouton de retour au menu principal
        back_button = QPushButton("Retour au menu principal")
        back_button.clicked.connect(self.return_to_main)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def load_classes_with_images(self):
        """Charge les classes avec leurs images associées dans le QComboBox."""
        self.class_combo.clear()
        classes = get_classes_with_images()
        for class_name, image_path in classes:
            icon = QIcon(f"ressources/icons/class_images/{image_path}")
            self.class_combo.addItem(icon, class_name)

    def update_subclasses(self):
        """Met à jour le menu déroulant des sous-classes en fonction de la classe sélectionnée."""
        selected_class = self.class_combo.currentText()
        subclasses = get_subclasses_with_images(selected_class)
        self.subclass_combo.clear()
        for subclass_name, image_path in subclasses:
            icon = QIcon(f"ressources/icons/class_images/{image_path}")
            self.subclass_combo.addItem(icon, subclass_name)

    def save_build(self):
        """Enregistre le build sélectionné dans la base de données."""
        race_name = self.race_combo.currentText()
        class_name = self.class_combo.currentText()
        subclass_name = self.subclass_combo.currentText()
        weapon_name = self.weapon_combo.currentText()
        armor_name = self.armor_combo.currentText()
        footwear_name = self.footwear_combo.currentText()

        # Appelle une fonction dans le contrôleur pour sauvegarder ces informations dans la base de données
        save_build_to_db(race_name, class_name, subclass_name, weapon_name, armor_name, footwear_name)
        self.return_to_main()

    def return_to_main(self):
        """Retourne au menu principal."""
        self.parent().show_main_menu()
