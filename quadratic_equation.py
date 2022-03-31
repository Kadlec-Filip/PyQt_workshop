import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Quadratic equation')
        self.setMinimumSize(QSize(800, 600))
        self.content = QWidget()
        layout = QGridLayout()

        # -------------------------------------------------------
        # |    a    |  input   |  matplotlib Canvas             |
        # ----------------------                                |
        # |    b    |  input   |                                |
        # ----------------------                                |
        # |    c    |  input   |                                |
        # ----------------------                                |
        # |   *redraw button*  |                                |
        # |   ... stretch...   |                                |
        # -------------------------------------------------------

        # jednoradkove textove pole, vstup
        self.a_input = QLineEdit('1')
        self.b_input = QLineEdit('2')
        self.c_input = QLineEdit('3')

        # labels for inputs above
        layout.addWidget(QLabel('a'), 0, 0)
        layout.addWidget(QLabel('b'), 1, 0)
        layout.addWidget(QLabel('c'), 2, 0)


        layout.addWidget(self.a_input, 0, 1)
        layout.addWidget(self.b_input, 1, 1)
        layout.addWidget(self.c_input, 2, 1)

        # vytvori mackaci tlacitko
        self.redraw_button = QPushButton("Redraw!")

        # once clicked, zavola se co je connected (metody, fce)
        self.redraw_button.clicked.connect(self.redraw_plot)

        # radek tri, sloupec nula a bude to pres jeden radek a dva sloupce
        layout.addWidget(self.redraw_button, 3, 0, 1, 2)

        #  vypln, přišprcni buttony nahoru a roztahuj se vertikalne, horizontalne ne
        spacer1 = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # spaceritem je item, ne widgeta, nekresi, nereaguje na vstup...
        # od 4. radku, 0. sloupec pres radek a dva sloupce
        layout.addItem(spacer1, 4, 0, 1, 2)

        # figure objekt, feed into canvas. once repainting canvas, it will know it should repaint canvas
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axes = self.figure.add_subplot(111)
        layout.addWidget(self.canvas, 0, 2, 5, 1)



        self.content.setLayout(layout)
        self.setCentralWidget(self.content)



    def redraw_plot(self):
        try:
            # text - metoda qlineedit
            a = float(self.a_input.text())
            b = float(self.a_input.text())
            c = float(self.a_input.text())
        except ValueError as e:
            QMessageBox.critical(self, 'Error', 'Wrong coefficients:\nValueError: ' + str(e))
            return

        x = np.linspace(-5, 5, 100)
        y = a*x**2 +b*x + c
        self.axes.clear()
        self.axes.plot(x, y, 'rx-')
        self.axes.grid()
        self.canvas.draw()  # platno se ma prekreslit


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
