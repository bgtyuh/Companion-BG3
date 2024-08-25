from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QComboBox
from controllers.armour_controller import get_all_armours, get_armour_details


class ShowarmoursWidget(QWidget):
    def __init__(self):
        """Initialise le widget pour afficher les armes et leurs détails.

        Crée l'interface utilisateur avec une liste d'armes, une zone pour afficher les détails,
        et un menu déroulant pour choisir les informations à afficher.
        """
        super().__init__()

        layout = QVBoxLayout()

        self.armour_list = QListWidget()
        self.armour_list.itemClicked.connect(self.display_armour_options)
        layout.addWidget(self.armour_list)

        self.detail_label = QLabel("Sélectionnez une arme pour voir les détails.")
        layout.addWidget(self.detail_label)

        self.options_combo = QComboBox()
        self.options_combo.addItems(["Armour", "Locations", "Specials"])
        self.options_combo.currentIndexChanged.connect(self.display_selected_info)
        layout.addWidget(self.options_combo)
        self.options_combo.hide()  # Cacher le menu déroulant au départ

        self.setLayout(layout)

        # Charger la liste des armes
        self.load_armours()

    def load_armours(self):
        """Charge la liste des armes depuis la base de données et les affiche dans la liste."""
        armours = get_all_armours()
        for armour in armours:
            item = QListWidgetItem(f"{armour[1]} - {armour[2]}")
            item.setData(1, armour[0])  # Stocke l'ID de l'arme dans l'item
            self.armour_list.addItem(item)

    def display_armour_options(self, item):
        """Affiche le menu déroulant pour choisir les détails à afficher pour l'arme sélectionnée.

        Arguments:
            item (QListWidgetItem): L'élément sélectionné dans la liste des armes.
        """
        self.current_armour_id = item.data(1)
        self.detail_label.setText(f"Sélectionnez les informations à afficher pour l'arme: {item.text()}")
        self.options_combo.show()

    def display_selected_info(self):
        """Affiche les informations choisies par l'utilisateur pour l'arme sélectionnée.

        Cette méthode récupère les détails de la base de données en fonction de l'option
        sélectionnée dans le menu déroulant et les affiche dans `detail_label`.
        """
        selected_option = self.options_combo.currentText()
        details = get_armour_details(self.current_armour_id, selected_option)
        self.detail_label.setText(details)
