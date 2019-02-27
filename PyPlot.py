#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from PyPlot_functions import*
from PyMid import*
import os

# compatible with Prisma + (quodera), HiQUAD, Hidden, QMA125


class PyRGA(QDialog):

    def loadfile_overlap_plot(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        filename, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileName()","G:\Departments\TE\Groups\VSC\LBV\VAC113", "All Files (*);;Excel file (*.xlsx)", options=options)
        plot(filename)

    def loadfile_overlap_plot_norm_water(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        filename, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileName()","G:\Departments\TE\Groups\VSC\LBV\VAC113", "All Files (*);;Python Files (*.py)", options=options)
        plot_norm_water(filename)

    def loadfile_overlap_plot_norm_hydrogen(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        filename, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileName()","G:\Departments\TE\Groups\VSC\LBV\VAC113", "All Files (*);;Python Files (*.py)", options=options)
        plot_norm_hydrogen(filename)

    def loadfile_plot_acceptance_before_bo(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        filename, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileName()","G:\Departments\TE\Groups\VSC\LBV\VAC113", "All Files (*);;Python Files (*.py)", options=options)
        plot_norm_before_bo(filename)

    def loadfile_plot_acceptance_after_bo(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        filename, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileName()","G:\Departments\TE\Groups\VSC\LBV\VAC113", "All Files (*);;Python Files (*.py)", options=options)
        plot_norm_after_bo(filename)

    def mass_follow_quadera(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        filename, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileName()", "G:\Departments\TE\Groups\VSC\LBV\VAC113","All Files (*);;Python Files (*.py)", options=options)
        plot_mid_quadera(filename)

    def mass_follow_massoft(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        filename, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileName()","G:\Departments\TE\Groups\VSC\LBV\VAC113", "All Files (*);;Python Files (*.py)", options=options)
        plot_mid_massoft(filename)
    def mass_follow_antoine(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        filename, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileName()","G:\Departments\TE\Groups\VSC\LBV\VAC113", "All Files (*);;Python Files (*.py)", options=options)
        plot_mid_antoine(filename)
    def open_window(self):

      super(PyRGA, self).__init__()
      loadUi('Main_window_GUI.ui', self)
      self.setWindowTitle('PyPlot')
      self.setWindowIcon(QtGui.QIcon('Icon.ico'))

      self.pushButton.clicked.connect(self.loadfile_overlap_plot)
      self.pushButton_2.clicked.connect(self.loadfile_overlap_plot_norm_water)
      self.pushButton_3.clicked.connect(self.loadfile_overlap_plot_norm_hydrogen)
      self.pushButton_4.clicked.connect(self.loadfile_plot_acceptance_before_bo)
      self.pushButton_5.clicked.connect(self.loadfile_plot_acceptance_after_bo)
      self.pushButton_7.clicked.connect(self.mass_follow_quadera)
      self.pushButton_6.clicked.connect(self.mass_follow_massoft)
      self.pushButton_8.clicked.connect(self.mass_follow_antoine)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = PyRGA()
    soft=widget.open_window()

    widget.show()

    sys.exit(app.exec_())







