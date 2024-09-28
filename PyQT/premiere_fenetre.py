import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QScrollArea

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Chat')

        # Layout principal
        self.layout = QVBoxLayout(self)

        # Ajout d'un champ de texte
        self.text = QLineEdit(self)
        self.layout.addWidget(self.text)

        # Ajout du bouton Valider
        self.bouton = QPushButton("Valider", self)
        self.bouton.clicked.connect(self.afficher_texte)
        self.layout.addWidget(self.bouton)

        # Ajout d'une zone de défilement pour les messages
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget(self.scroll_area)
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_content)
        self.layout.addWidget(self.scroll_area)

        self.setLayout(self.layout)

    def afficher_texte(self):
        label = QLabel(self.text.text(), self)
        self.scroll_layout.addWidget(label)
        self.text.clear()

app = QApplication(sys.argv)

fen = MaFenetre()
fen.show()

app.exec_()