import sys

from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow

if __name__ == "__main__":
    # Exemple pour appliquer un stylesheet global à toute l'application
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QPushButton {
        background-color: #d1c5a5;  /* Couleur papyrus gris */
        color: #2C2C2C;  /* Couleur foncée pour le texte */
        border: 1px solid #8F8F91;  /* Bordure légère pour délimiter le bouton */
        border-radius: 8px;  /* Arrondir légèrement les coins */
        padding: 10px 20px;  /* Espacement interne */
        font-size: 16px;  /* Taille du texte */
        font-weight: bold;  /* Texte en gras */
    }
    
    QPushButton:hover {
        background-color: #a69b80;  /* Gris légèrement plus foncé au survol */
    }

    QPushButton:pressed {
        background-color: #807762;  /* Gris plus foncé lorsque le bouton est enfoncé */
    }
""")


    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
