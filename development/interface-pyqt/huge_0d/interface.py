# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(934, 706)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(50, 40, 361, 201))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(60, 10, 221, 140))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.mAB = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.mAB.setObjectName("mAB")
        self.gridLayout_3.addWidget(self.mAB, 0, 1, 1, 1)
        self.peierls = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.peierls.setObjectName("peierls")
        self.gridLayout_3.addWidget(self.peierls, 2, 1, 1, 1)
        self.fermi = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.fermi.setObjectName("fermi")
        self.gridLayout_3.addWidget(self.fermi, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_36.setObjectName("label_36")
        self.gridLayout_3.addWidget(self.label_36, 3, 0, 1, 1)
        self.haldane = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.haldane.setObjectName("haldane")
        self.gridLayout_3.addWidget(self.haldane, 3, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayoutWidget_14 = QtWidgets.QWidget(self.tab_11)
        self.gridLayoutWidget_14.setGeometry(QtCore.QRect(60, 30, 251, 41))
        self.gridLayoutWidget_14.setObjectName("gridLayoutWidget_14")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.edge_potential = QtWidgets.QLineEdit(self.gridLayoutWidget_14)
        self.edge_potential.setObjectName("edge_potential")
        self.gridLayout_14.addWidget(self.edge_potential, 0, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget_14)
        self.label_35.setObjectName("label_35")
        self.gridLayout_14.addWidget(self.label_35, 0, 0, 1, 1)
        self.show_potential = QtWidgets.QPushButton(self.tab_11)
        self.show_potential.setGeometry(QtCore.QRect(90, 100, 171, 28))
        self.show_potential.setObjectName("show_potential")
        self.tabWidget_2.addTab(self.tab_11, "")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 290, 421, 341))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(40, 10, 308, 31))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.geometry_mode = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.geometry_mode.setObjectName("geometry_mode")
        self.geometry_mode.addItem("")
        self.gridLayout_4.addWidget(self.geometry_mode, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 391, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 311, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lattice = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.lattice.setObjectName("lattice")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.gridLayout.addWidget(self.lattice, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setEnabled(False)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.rotation = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.rotation.setObjectName("rotation")
        self.gridLayout.addWidget(self.rotation, 1, 1, 1, 1)
        self.target_diameter = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.target_diameter.setEnabled(False)
        self.target_diameter.setText("")
        self.target_diameter.setObjectName("target_diameter")
        self.gridLayout.addWidget(self.target_diameter, 4, 1, 1, 1)
        self.clean_island = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.clean_island.setText("")
        self.clean_island.setObjectName("clean_island")
        self.gridLayout.addWidget(self.clean_island, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setEnabled(False)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.desired_dameter = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.desired_dameter.setEnabled(False)
        self.desired_dameter.setObjectName("desired_dameter")
        self.gridLayout.addWidget(self.desired_dameter, 5, 1, 1, 1)
        self.size = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.size.setObjectName("size")
        self.gridLayout.addWidget(self.size, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(22, 99, 231, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.nedges = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.nedges.setObjectName("nedges")
        self.gridLayout_2.addWidget(self.nedges, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(470, 220, 421, 411))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget_3.setGeometry(QtCore.QRect(10, 60, 391, 341))
        self.tabWidget_3.setToolTip("")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(40, 90, 291, 176))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)
        self.select_atoms_dos = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.select_atoms_dos.setObjectName("select_atoms_dos")
        self.gridLayout_5.addWidget(self.select_atoms_dos, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1)
        self.LDOS_num_atom = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.LDOS_num_atom.setObjectName("LDOS_num_atom")
        self.gridLayout_5.addWidget(self.LDOS_num_atom, 0, 1, 1, 1)
        self.LDOS_polynomials = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.LDOS_polynomials.setObjectName("LDOS_polynomials")
        self.gridLayout_5.addWidget(self.LDOS_polynomials, 1, 1, 1, 1)
        self.smearing_local_dos = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.smearing_local_dos.setObjectName("smearing_local_dos")
        self.gridLayout_5.addWidget(self.smearing_local_dos, 2, 1, 1, 1)
        self.num_ene_ldos = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.num_ene_ldos.setObjectName("num_ene_ldos")
        self.gridLayout_5.addWidget(self.num_ene_ldos, 3, 1, 1, 1)
        self.energy_cutoff_local_dos = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.energy_cutoff_local_dos.setObjectName("energy_cutoff_local_dos")
        self.gridLayout_5.addWidget(self.energy_cutoff_local_dos, 4, 1, 1, 1)
        self.show_ldos = QtWidgets.QPushButton(self.tab_4)
        self.show_ldos.setGeometry(QtCore.QRect(70, 40, 251, 28))
        self.show_ldos.setObjectName("show_ldos")
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.tab_5)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(50, 60, 291, 176))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 0, 0, 1, 1)
        self.DOS_polynomials = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.DOS_polynomials.setObjectName("DOS_polynomials")
        self.gridLayout_7.addWidget(self.DOS_polynomials, 0, 1, 1, 1)
        self.DOS_iterations = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.DOS_iterations.setObjectName("DOS_iterations")
        self.gridLayout_7.addWidget(self.DOS_iterations, 1, 1, 1, 1)
        self.smearing_dos = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.smearing_dos.setObjectName("smearing_dos")
        self.gridLayout_7.addWidget(self.smearing_dos, 2, 1, 1, 1)
        self.num_ene_dos = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.num_ene_dos.setObjectName("num_ene_dos")
        self.gridLayout_7.addWidget(self.num_ene_dos, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 1, 0, 1, 1)
        self.show_dos = QtWidgets.QPushButton(self.tab_5)
        self.show_dos.setGeometry(QtCore.QRect(90, 20, 211, 28))
        self.show_dos.setObjectName("show_dos")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_6)
        self.tabWidget_4.setGeometry(QtCore.QRect(30, 100, 331, 201))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.tab_7)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(40, 10, 241, 141))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_20.setObjectName("label_20")
        self.gridLayout_8.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_21.setObjectName("label_21")
        self.gridLayout_8.addWidget(self.label_21, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_22.setObjectName("label_22")
        self.gridLayout_8.addWidget(self.label_22, 2, 0, 1, 1)
        self.mode_stm = QtWidgets.QComboBox(self.gridLayoutWidget_8)
        self.mode_stm.setObjectName("mode_stm")
        self.mode_stm.addItem("")
        self.mode_stm.addItem("")
        self.gridLayout_8.addWidget(self.mode_stm, 0, 1, 1, 1)
        self.smearing_spatial_DOS = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.smearing_spatial_DOS.setObjectName("smearing_spatial_DOS")
        self.gridLayout_8.addWidget(self.smearing_spatial_DOS, 1, 1, 1, 1)
        self.nwaves_dos = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.nwaves_dos.setObjectName("nwaves_dos")
        self.gridLayout_8.addWidget(self.nwaves_dos, 2, 1, 1, 1)
        self.tabWidget_4.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.tab_8)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(80, 40, 160, 80))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.energy_spatial_DOS = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.energy_spatial_DOS.setObjectName("energy_spatial_DOS")
        self.gridLayout_9.addWidget(self.energy_spatial_DOS, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_9)
        self.label_23.setObjectName("label_23")
        self.gridLayout_9.addWidget(self.label_23, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.tab_9)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(70, 40, 201, 104))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_10)
        self.label_24.setObjectName("label_24")
        self.gridLayout_10.addWidget(self.label_24, 0, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_10)
        self.label_25.setObjectName("label_25")
        self.gridLayout_10.addWidget(self.label_25, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_10)
        self.label_26.setObjectName("label_26")
        self.gridLayout_10.addWidget(self.label_26, 2, 0, 1, 1)
        self.mine_movie = QtWidgets.QLineEdit(self.gridLayoutWidget_10)
        self.mine_movie.setObjectName("mine_movie")
        self.gridLayout_10.addWidget(self.mine_movie, 0, 1, 1, 1)
        self.maxe_movie = QtWidgets.QLineEdit(self.gridLayoutWidget_10)
        self.maxe_movie.setObjectName("maxe_movie")
        self.gridLayout_10.addWidget(self.maxe_movie, 1, 1, 1, 1)
        self.stepse_movie = QtWidgets.QLineEdit(self.gridLayoutWidget_10)
        self.stepse_movie.setObjectName("stepse_movie")
        self.gridLayout_10.addWidget(self.stepse_movie, 2, 1, 1, 1)
        self.tabWidget_4.addTab(self.tab_9, "")
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.tab_6)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(50, 50, 301, 31))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.mode_dosmap = QtWidgets.QComboBox(self.gridLayoutWidget_11)
        self.mode_dosmap.setObjectName("mode_dosmap")
        self.mode_dosmap.addItem("")
        self.mode_dosmap.addItem("")
        self.gridLayout_11.addWidget(self.mode_dosmap, 0, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.label_27.setObjectName("label_27")
        self.gridLayout_11.addWidget(self.label_27, 0, 0, 1, 1)
        self.show_spatial_dos = QtWidgets.QPushButton(self.tab_6)
        self.show_spatial_dos.setGeometry(QtCore.QRect(30, 10, 331, 28))
        self.show_spatial_dos.setObjectName("show_spatial_dos")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayoutWidget_12 = QtWidgets.QWidget(self.tab_10)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(90, 203, 211, 104))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget_12")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.label_29.setObjectName("label_29")
        self.gridLayout_12.addWidget(self.label_29, 1, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.label_30.setObjectName("label_30")
        self.gridLayout_12.addWidget(self.label_30, 2, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.label_28.setObjectName("label_28")
        self.gridLayout_12.addWidget(self.label_28, 0, 0, 1, 1)
        self.initial_atom = QtWidgets.QLineEdit(self.gridLayoutWidget_12)
        self.initial_atom.setObjectName("initial_atom")
        self.gridLayout_12.addWidget(self.initial_atom, 0, 1, 1, 1)
        self.final_atom = QtWidgets.QLineEdit(self.gridLayoutWidget_12)
        self.final_atom.setObjectName("final_atom")
        self.gridLayout_12.addWidget(self.final_atom, 1, 1, 1, 1)
        self.width_path = QtWidgets.QLineEdit(self.gridLayoutWidget_12)
        self.width_path.setObjectName("width_path")
        self.gridLayout_12.addWidget(self.width_path, 2, 1, 1, 1)
        self.gridLayoutWidget_13 = QtWidgets.QWidget(self.tab_10)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(50, 50, 271, 111))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_13)
        self.label_33.setObjectName("label_33")
        self.gridLayout_13.addWidget(self.label_33, 2, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget_13)
        self.label_32.setObjectName("label_32")
        self.gridLayout_13.addWidget(self.label_32, 1, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_13)
        self.label_31.setObjectName("label_31")
        self.gridLayout_13.addWidget(self.label_31, 0, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget_13)
        self.label_34.setObjectName("label_34")
        self.gridLayout_13.addWidget(self.label_34, 3, 0, 1, 1)
        self.pols_path = QtWidgets.QLineEdit(self.gridLayoutWidget_13)
        self.pols_path.setObjectName("pols_path")
        self.gridLayout_13.addWidget(self.pols_path, 0, 1, 1, 1)
        self.ecut_path = QtWidgets.QLineEdit(self.gridLayoutWidget_13)
        self.ecut_path.setObjectName("ecut_path")
        self.gridLayout_13.addWidget(self.ecut_path, 1, 1, 1, 1)
        self.num_ene_path = QtWidgets.QLineEdit(self.gridLayoutWidget_13)
        self.num_ene_path.setObjectName("num_ene_path")
        self.gridLayout_13.addWidget(self.num_ene_path, 2, 1, 1, 1)
        self.smearing_path_dos = QtWidgets.QLineEdit(self.gridLayoutWidget_13)
        self.smearing_path_dos.setObjectName("smearing_path_dos")
        self.gridLayout_13.addWidget(self.smearing_path_dos, 3, 1, 1, 1)
        self.show_path = QtWidgets.QPushButton(self.tab_10)
        self.show_path.setGeometry(QtCore.QRect(150, 170, 105, 28))
        self.show_path.setObjectName("show_path")
        self.show_path_dos = QtWidgets.QPushButton(self.tab_10)
        self.show_path_dos.setGeometry(QtCore.QRect(30, 10, 311, 28))
        self.show_path_dos.setObjectName("show_path_dos")
        self.tabWidget_3.addTab(self.tab_10, "")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(720, 40, 179, 98))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.show_lattice = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.show_lattice.setObjectName("show_lattice")
        self.gridLayout_6.addWidget(self.show_lattice, 0, 0, 1, 1)
        self.initialize = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.initialize.setObjectName("initialize")
        self.gridLayout_6.addWidget(self.initialize, 1, 0, 1, 1)
        self.save_results = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.save_results.setObjectName("save_results")
        self.gridLayout_6.addWidget(self.save_results, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Huge islands"))
        self.label_9.setText(_translate("MainWindow", "Fermi shift"))
        self.label_8.setText(_translate("MainWindow", "AB imbalance"))
        self.mAB.setToolTip(_translate("MainWindow", "Sublattice imbalance in a bipartite lattice"))
        self.mAB.setText(_translate("MainWindow", "0.0"))
        self.peierls.setToolTip(_translate("MainWindow", "Orbital magnetic field, creates Landau levels"))
        self.peierls.setText(_translate("MainWindow", "0.0"))
        self.fermi.setToolTip(_translate("MainWindow", "Global shift of the onsite energies"))
        self.fermi.setText(_translate("MainWindow", "0.0"))
        self.label_10.setText(_translate("MainWindow", "Magnetic field"))
        self.label_36.setText(_translate("MainWindow", "Haldane"))
        self.haldane.setToolTip(_translate("MainWindow", "Haldane coupling, creates a quantum anomalous Hall state"))
        self.haldane.setText(_translate("MainWindow", "0.0"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Global parameters"))
        self.edge_potential.setToolTip(_translate("MainWindow", "This term will introduce an onsite term in the edge atoms"))
        self.edge_potential.setText(_translate("MainWindow", "0.0"))
        self.label_35.setText(_translate("MainWindow", "Potential"))
        self.show_potential.setToolTip(_translate("MainWindow", "This shows in which atoms the edge potential is added"))
        self.show_potential.setText(_translate("MainWindow", "Show edge atoms"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("MainWindow", "Edge perturbation"))
        self.geometry_mode.setItemText(0, _translate("MainWindow", "Recipe"))
        self.label_11.setText(_translate("MainWindow", "Geometry generation mode"))
        self.lattice.setItemText(0, _translate("MainWindow", "Honeycomb"))
        self.lattice.setItemText(1, _translate("MainWindow", "Square"))
        self.lattice.setItemText(2, _translate("MainWindow", "Triangular"))
        self.lattice.setItemText(3, _translate("MainWindow", "Lieb"))
        self.lattice.setItemText(4, _translate("MainWindow", "Kagome"))
        self.label_2.setText(_translate("MainWindow", "Rotation"))
        self.label_5.setText(_translate("MainWindow", "Target diameter"))
        self.label_3.setText(_translate("MainWindow", "Size"))
        self.rotation.setToolTip(_translate("MainWindow", "Global rotation of the unit cell used to build the island"))
        self.rotation.setText(_translate("MainWindow", "30"))
        self.label.setText(_translate("MainWindow", "Lattice"))
        self.label_4.setText(_translate("MainWindow", "Remove single bonded"))
        self.label_6.setText(_translate("MainWindow", "Desired diameter"))
        self.desired_dameter.setText(_translate("MainWindow", "40"))
        self.size.setToolTip(_translate("MainWindow", "Size of the supercell used to build the island, controls the overal size of hte island"))
        self.size.setText(_translate("MainWindow", "11"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Common options"))
        self.nedges.setText(_translate("MainWindow", "3"))
        self.label_7.setText(_translate("MainWindow", "Number of edges"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Recipe"))
        self.label_15.setText(_translate("MainWindow", "Energy cutoff"))
        self.label_14.setText(_translate("MainWindow", "Number of energies"))
        self.label_13.setText(_translate("MainWindow", "Smearing"))
        self.select_atoms_dos.setText(_translate("MainWindow", "Select atoms"))
        self.label_12.setText(_translate("MainWindow", "# of polynomials"))
        self.LDOS_num_atom.setText(_translate("MainWindow", "1"))
        self.LDOS_polynomials.setText(_translate("MainWindow", "600"))
        self.smearing_local_dos.setText(_translate("MainWindow", "0.01"))
        self.num_ene_ldos.setText(_translate("MainWindow", "300"))
        self.energy_cutoff_local_dos.setText(_translate("MainWindow", "0.8"))
        self.show_ldos.setToolTip(_translate("MainWindow", "Shows the local density of states in specific atoms"))
        self.show_ldos.setText(_translate("MainWindow", "Compute DOS in certain atoms"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("MainWindow", "Local DOS"))
        self.label_16.setText(_translate("MainWindow", "# of energies"))
        self.label_17.setText(_translate("MainWindow", "Smearing"))
        self.label_19.setText(_translate("MainWindow", "# of polynomials"))
        self.DOS_polynomials.setText(_translate("MainWindow", "600"))
        self.DOS_iterations.setText(_translate("MainWindow", "20"))
        self.smearing_dos.setText(_translate("MainWindow", "0.01"))
        self.num_ene_dos.setText(_translate("MainWindow", "300"))
        self.label_18.setText(_translate("MainWindow", "Iterations"))
        self.show_dos.setToolTip(_translate("MainWindow", "Show the density of states avergaed over the whole sample"))
        self.show_dos.setText(_translate("MainWindow", "Compute total DOS "))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "Total DOS"))
        self.label_20.setText(_translate("MainWindow", "Mode"))
        self.label_21.setText(_translate("MainWindow", "Smearing"))
        self.label_22.setText(_translate("MainWindow", "# of waves"))
        self.mode_stm.setItemText(0, _translate("MainWindow", "Eigen"))
        self.mode_stm.setItemText(1, _translate("MainWindow", "Full"))
        self.smearing_spatial_DOS.setText(_translate("MainWindow", "0.01"))
        self.nwaves_dos.setText(_translate("MainWindow", "100"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_7), _translate("MainWindow", "Common options"))
        self.energy_spatial_DOS.setText(_translate("MainWindow", "0.0"))
        self.label_23.setText(_translate("MainWindow", "Energy"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_8), _translate("MainWindow", "Single shot"))
        self.label_24.setText(_translate("MainWindow", "Initial energy"))
        self.label_25.setText(_translate("MainWindow", "Final energy"))
        self.label_26.setText(_translate("MainWindow", "# of energies"))
        self.mine_movie.setText(_translate("MainWindow", "-0.5"))
        self.maxe_movie.setText(_translate("MainWindow", "0.5"))
        self.stepse_movie.setText(_translate("MainWindow", "100"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_9), _translate("MainWindow", "Movie"))
        self.mode_dosmap.setItemText(0, _translate("MainWindow", "Single shot"))
        self.mode_dosmap.setItemText(1, _translate("MainWindow", "Movie"))
        self.label_27.setText(_translate("MainWindow", "Mode ofr spatial DOS"))
        self.show_spatial_dos.setToolTip(_translate("MainWindow", "Show a spatial profile of the density of states at a specific energy"))
        self.show_spatial_dos.setText(_translate("MainWindow", "Compute spatially resolved DOS"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "DOS map"))
        self.label_29.setText(_translate("MainWindow", "Final atom"))
        self.label_30.setText(_translate("MainWindow", "Width accepted"))
        self.label_28.setText(_translate("MainWindow", "Initial atom"))
        self.initial_atom.setText(_translate("MainWindow", "0"))
        self.final_atom.setText(_translate("MainWindow", "1"))
        self.width_path.setText(_translate("MainWindow", "1.5"))
        self.label_33.setText(_translate("MainWindow", "# of energies"))
        self.label_32.setText(_translate("MainWindow", "Energy cutoff"))
        self.label_31.setText(_translate("MainWindow", "# of polynomials"))
        self.label_34.setText(_translate("MainWindow", "Smearing"))
        self.pols_path.setText(_translate("MainWindow", "200"))
        self.ecut_path.setText(_translate("MainWindow", "0.8"))
        self.num_ene_path.setText(_translate("MainWindow", "200"))
        self.smearing_path_dos.setText(_translate("MainWindow", "0.01"))
        self.show_path.setText(_translate("MainWindow", "Show path"))
        self.show_path_dos.setToolTip(_translate("MainWindow", "Shows the density of states in a sequence of atoms that intersect a certain line"))
        self.show_path_dos.setText(_translate("MainWindow", "Compute DOS in a line of atoms"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("MainWindow", "DOS in a line"))
        self.show_lattice.setToolTip(_translate("MainWindow", "Show the geometry created"))
        self.show_lattice.setText(_translate("MainWindow", "Show island"))
        self.initialize.setToolTip(_translate("MainWindow", "Write the Hamiltonian to a file, to allow quick access for the rest of the computations"))
        self.initialize.setText(_translate("MainWindow", "Initialize Hamiltonian"))
        self.save_results.setToolTip(_translate("MainWindow", "Copy the results to a local folder"))
        self.save_results.setText(_translate("MainWindow", "Save results"))

