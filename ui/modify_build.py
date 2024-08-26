from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel

from controllers.build_controller import get_races, get_classes, get_weapons, get_armors, get_footwears, update_build, \
    get_subclasses, get_classes_with_images, get_subclasses_with_images


class ModifyBuildWidget(QWidget):
    def __init__(self, parent, build_id, current_build_data):
        """Initialise le widget pour modifier un build existant."""
        super().__init__(parent)
        self.build_id = build_id

        layout = QVBoxLayout()

        # Sélection de la race
        self.race_combo = QComboBox()
        races = [race[0] for race in get_races()]
        self.race_combo.addItems(races)
        self.race_combo.setCurrentText(current_build_data['race_name'])
        layout.addWidget(QLabel("Modifier la race:"))
        layout.addWidget(self.race_combo)

        # Sélection de la classe
        self.class_combo = QComboBox()
        self.load_classes_with_images(current_build_data['class_name'])
        self.class_combo.currentIndexChanged.connect(self.update_subclasses)
        layout.addWidget(QLabel("Modifier la classe:"))
        layout.addWidget(self.class_combo)

        # Sélection de la sous-classe
        self.subclass_combo = QComboBox()
        self.update_subclasses()  # Initialiser les sous-classes pour la classe par défaut
        layout.addWidget(QLabel("Modifier la sous-classe:"))
        layout.addWidget(self.subclass_combo)

        # Sélection de l'arme
        self.weapon_combo = QComboBox()
        weapons = [weapon[1] for weapon in get_weapons()]
        self.weapon_combo.addItems(weapons)
        self.weapon_combo.setCurrentText(current_build_data['weapon_name'])
        layout.addWidget(QLabel("Modifier l'arme:"))
        layout.addWidget(self.weapon_combo)

        # Sélection de l'armure
        self.armor_combo = QComboBox()
        armors = [armor[1] for armor in get_armors()]
        self.armor_combo.addItems(armors)
        self.armor_combo.setCurrentText(current_build_data['armor_name'])
        layout.addWidget(QLabel("Modifier l'armure:"))
        layout.addWidget(self.armor_combo)

        # Sélection des bottes
        self.footwear_combo = QComboBox()
        footwears = [footwear[1] for footwear in get_footwears()]
        self.footwear_combo.addItems(footwears)
        self.footwear_combo.setCurrentText(current_build_data['footwear_name'])
        layout.addWidget(QLabel("Modifier les bottes:"))
        layout.addWidget(self.footwear_combo)

        # Bouton pour enregistrer les modifications
        save_button = QPushButton("Sauvegarder les modifications")
        save_button.clicked.connect(self.save_changes)
        layout.addWidget(save_button)

        # Bouton de retour au menu principal
        back_button = QPushButton("Retour au menu principal")
        back_button.clicked.connect(self.return_to_main)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def load_classes_with_images(self, current_class_name):
        """Charge les classes avec leurs images associées dans le QComboBox."""
        self.class_combo.clear()
        classes = get_classes_with_images()
        for class_name, image_path in classes:
            icon = QIcon(f"ressources/icons/class_images/{image_path}")
            self.class_combo.addItem(icon, class_name)
        self.class_combo.setCurrentText(current_class_name)

    def update_subclasses(self):
        """Met à jour le menu déroulant des sous-classes en fonction de la classe sélectionnée."""
        selected_class = self.class_combo.currentText()
        subclasses = get_subclasses_with_images(selected_class)
        self.subclass_combo.clear()
        for subclass_name, image_path in subclasses:
            icon = QIcon(f"ressources/icons/class_images/{image_path}")
            self.subclass_combo.addItem(icon, subclass_name)

        # Sélectionner la sous-classe actuelle, si elle existe
        if 'subclass_name' in vars(self):
            self.subclass_combo.setCurrentText(self.subclass_combo.currentText())


    def save_changes(self):
        """Enregistre les modifications apportées au build."""
        race_name = self.race_combo.currentText()
        class_name = self.class_combo.currentText()
        subclass_name = self.subclass_combo.currentText()
        weapon_name = self.weapon_combo.currentText()
        armor_name = self.armor_combo.currentText()
        footwear_name = self.footwear_combo.currentText()

        # Appelle une fonction dans le contrôleur pour mettre à jour le build dans la base de données
        update_build(self.build_id, race_name, class_name, subclass_name, weapon_name, armor_name, footwear_name)

        # Retourner au menu principal après la sauvegarde
        self.return_to_main()

    def return_to_main(self):
        """Retourne au menu principal."""
        self.parent().show_main_menu()
