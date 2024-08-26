from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QComboBox, QPushButton

from controllers.weapon_controller import get_all_weapons, get_weapon_details


class ShowWeaponsWidget(QWidget):
    def __init__(self, parent):
        """Initialise le widget pour afficher les armes et leurs détails.

        Crée l'interface utilisateur avec une liste d'armes, une zone pour afficher les détails,
        et un menu déroulant pour choisir les informations à afficher.
        """
        super().__init__(parent)

        layout = QVBoxLayout()

        self.weapon_list = QListWidget()
        self.weapon_list.itemClicked.connect(self.display_weapon_options)
        layout.addWidget(self.weapon_list)

        self.detail_label = QLabel("Sélectionnez une arme pour voir les détails.")
        layout.addWidget(self.detail_label)

        self.options_combo = QComboBox()
        self.options_combo.addItems(["Damage", "Notes", "Special Abilities", "Weapon Actions", "Weapon Locations"])
        self.options_combo.currentIndexChanged.connect(self.display_selected_info)
        layout.addWidget(self.options_combo)
        self.options_combo.hide()  # Cacher le menu déroulant au départ

        self.setLayout(layout)

        # Charger la liste des armes
        self.load_weapons()

        # Bouton de retour au menu principal
        back_button = QPushButton("Retour au menu principal")
        back_button.clicked.connect(self.return_to_main)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def return_to_main(self):
        """Retourne au menu principal."""
        self.parent().show_main_menu()

    def load_weapons(self):
        """Charge la liste des armes depuis la base de données et les affiche dans la liste."""
        weapons = get_all_weapons()
        for weapon in weapons:
            item = QListWidgetItem(f"{weapon[1]} - {weapon[2]}")
            item.setData(1, weapon[0])  # Stocke l'ID de l'arme dans l'item
            self.weapon_list.addItem(item)

    def display_weapon_options(self, item):
        """Affiche le menu déroulant pour choisir les détails à afficher pour l'arme sélectionnée.

        Arguments:
            item (QListWidgetItem): L'élément sélectionné dans la liste des armes.
        """
        self.current_weapon_id = item.data(1)
        self.detail_label.setText(f"Sélectionnez les informations à afficher pour l'arme: {item.text()}")
        self.options_combo.show()

    def display_selected_info(self):
        """Affiche les informations choisies par l'utilisateur pour l'arme sélectionnée.

        Cette méthode récupère les détails de la base de données en fonction de l'option
        sélectionnée dans le menu déroulant et les affiche dans `detail_label`.
        """
        selected_option = self.options_combo.currentText()
        details = get_weapon_details(self.current_weapon_id, selected_option)
        self.detail_label.setText(details)
