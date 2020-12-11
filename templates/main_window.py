# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 761)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.verticalLayout_2.addWidget(self.header)
        self.XML_type_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.XML_type_label.setFont(font)
        self.XML_type_label.setTextFormat(QtCore.Qt.AutoText)
        self.XML_type_label.setScaledContents(False)
        self.XML_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.XML_type_label.setObjectName("XML_type_label")
        self.verticalLayout_2.addWidget(self.XML_type_label)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_21 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.label_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setToolTip("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.acronym = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.acronym.setFont(font)
        self.acronym.setStyleSheet("border-color: rgb(255, 85, 0);")
        self.acronym.setObjectName("acronym")
        self.verticalLayout_3.addWidget(self.acronym)
        self.label_6 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.name = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.verticalLayout_3.addWidget(self.name)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.data_begin = QtWidgets.QDateEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.data_begin.setFont(font)
        self.data_begin.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.data_begin.setObjectName("data_begin")
        self.gridLayout.addWidget(self.data_begin, 1, 0, 1, 1)
        self.data_end = QtWidgets.QDateEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.data_end.setFont(font)
        self.data_end.setObjectName("data_end")
        self.gridLayout.addWidget(self.data_end, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.label_8 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.description = QtWidgets.QTextEdit(self.tab)
        self.description.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setOverwriteMode(True)
        self.description.setTabStopWidth(80)
        self.description.setObjectName("description")
        self.verticalLayout_3.addWidget(self.description)
        self.label_9 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.comments = QtWidgets.QTextEdit(self.tab)
        self.comments.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.comments.setFont(font)
        self.comments.setOverwriteMode(True)
        self.comments.setTabStopWidth(80)
        self.comments.setObjectName("comments")
        self.verticalLayout_3.addWidget(self.comments)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_4.addWidget(self.label_22)
        self.label_ORCIDE = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ORCIDE.setFont(font)
        self.label_ORCIDE.setObjectName("label_ORCIDE")
        self.verticalLayout_4.addWidget(self.label_ORCIDE)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.organization_1_acronym = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.organization_1_acronym.setFont(font)
        self.organization_1_acronym.setObjectName("organization_1_acronym")
        self.gridLayout_8.addWidget(self.organization_1_acronym, 0, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_8.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setMinimumSize(QtCore.QSize(0, 0))
        self.label_28.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_8.addWidget(self.label_28, 1, 0, 1, 1)
        self.organization_1_name = QtWidgets.QTextEdit(self.tab_2)
        self.organization_1_name.setMinimumSize(QtCore.QSize(0, 0))
        self.organization_1_name.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.organization_1_name.setFont(font)
        self.organization_1_name.setTabStopWidth(80)
        self.organization_1_name.setObjectName("organization_1_name")
        self.gridLayout_8.addWidget(self.organization_1_name, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_8)
        self.label_ResearcherID = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ResearcherID.setFont(font)
        self.label_ResearcherID.setObjectName("label_ResearcherID")
        self.verticalLayout_4.addWidget(self.label_ResearcherID)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.organization_2_acronym = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.organization_2_acronym.setFont(font)
        self.organization_2_acronym.setObjectName("organization_2_acronym")
        self.gridLayout_9.addWidget(self.organization_2_acronym, 0, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_9.addWidget(self.label_29, 0, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setMinimumSize(QtCore.QSize(0, 0))
        self.label_30.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_9.addWidget(self.label_30, 1, 0, 1, 1)
        self.organization_2_name = QtWidgets.QTextEdit(self.tab_2)
        self.organization_2_name.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.organization_2_name.setFont(font)
        self.organization_2_name.setObjectName("organization_2_name")
        self.gridLayout_9.addWidget(self.organization_2_name, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_9)
        self.label_ScopusAuthorID = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ScopusAuthorID.setFont(font)
        self.label_ScopusAuthorID.setObjectName("label_ScopusAuthorID")
        self.verticalLayout_4.addWidget(self.label_ScopusAuthorID)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.organization_3_acronym = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.organization_3_acronym.setFont(font)
        self.organization_3_acronym.setObjectName("organization_3_acronym")
        self.gridLayout_10.addWidget(self.organization_3_acronym, 0, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_10.addWidget(self.label_31, 0, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        self.label_32.setMinimumSize(QtCore.QSize(0, 0))
        self.label_32.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout_10.addWidget(self.label_32, 1, 0, 1, 1)
        self.organization_3_name = QtWidgets.QTextEdit(self.tab_2)
        self.organization_3_name.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.organization_3_name.setFont(font)
        self.organization_3_name.setObjectName("organization_3_name")
        self.gridLayout_10.addWidget(self.organization_3_name, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_10)
        self.label_ScopusAuthorID_2 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ScopusAuthorID_2.setFont(font)
        self.label_ScopusAuthorID_2.setObjectName("label_ScopusAuthorID_2")
        self.verticalLayout_4.addWidget(self.label_ScopusAuthorID_2)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.organization_4_acronym = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.organization_4_acronym.setFont(font)
        self.organization_4_acronym.setObjectName("organization_4_acronym")
        self.gridLayout_11.addWidget(self.organization_4_acronym, 0, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_11.addWidget(self.label_33, 0, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.tab_2)
        self.label_34.setMinimumSize(QtCore.QSize(0, 0))
        self.label_34.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_11.addWidget(self.label_34, 1, 0, 1, 1)
        self.organization_4_name = QtWidgets.QTextEdit(self.tab_2)
        self.organization_4_name.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.organization_4_name.setFont(font)
        self.organization_4_name.setObjectName("organization_4_name")
        self.gridLayout_11.addWidget(self.organization_4_name, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_11)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setObjectName("label_23")
        self.verticalLayout.addWidget(self.label_23)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.link_1_name = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.link_1_name.setFont(font)
        self.link_1_name.setObjectName("link_1_name")
        self.gridLayout_5.addWidget(self.link_1_name, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)
        self.link_1_url = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.link_1_url.setFont(font)
        self.link_1_url.setObjectName("link_1_url")
        self.gridLayout_5.addWidget(self.link_1_url, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.link_2_name = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.link_2_name.setFont(font)
        self.link_2_name.setObjectName("link_2_name")
        self.gridLayout_3.addWidget(self.link_2_name, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.link_2_url = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.link_2_url.setFont(font)
        self.link_2_url.setObjectName("link_2_url")
        self.gridLayout_3.addWidget(self.link_2_url, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)
        self.link_3_name = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.link_3_name.setFont(font)
        self.link_3_name.setObjectName("link_3_name")
        self.gridLayout_6.addWidget(self.link_3_name, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 1, 0, 1, 1)
        self.link_3_url = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.link_3_url.setFont(font)
        self.link_3_url.setObjectName("link_3_url")
        self.gridLayout_6.addWidget(self.link_3_url, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 0, 0, 1, 1)
        self.link_4_name = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.link_4_name.setFont(font)
        self.link_4_name.setObjectName("link_4_name")
        self.gridLayout_7.addWidget(self.link_4_name, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setMinimumSize(QtCore.QSize(0, 0))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 1, 0, 1, 1)
        self.link_4_url = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.link_4_url.setFont(font)
        self.link_4_url.setObjectName("link_4_url")
        self.gridLayout_7.addWidget(self.link_4_url, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.label_35 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.verticalLayout.addWidget(self.label_35)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_36 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout_12.addWidget(self.label_36, 0, 0, 1, 1)
        self.link_5_name = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.link_5_name.setFont(font)
        self.link_5_name.setObjectName("link_5_name")
        self.gridLayout_12.addWidget(self.link_5_name, 0, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.tab_3)
        self.label_37.setMinimumSize(QtCore.QSize(0, 0))
        self.label_37.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout_12.addWidget(self.label_37, 1, 0, 1, 1)
        self.link_5_url = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.link_5_url.setFont(font)
        self.link_5_url.setObjectName("link_5_url")
        self.gridLayout_12.addWidget(self.link_5_url, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_12)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 1, 0, 1, 1)
        self.btn_address_1 = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_address_1.setFont(font)
        self.btn_address_1.setObjectName("btn_address_1")
        self.gridLayout_4.addWidget(self.btn_address_1, 2, 0, 1, 1)
        self.btn_address_3 = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_address_3.setFont(font)
        self.btn_address_3.setObjectName("btn_address_3")
        self.gridLayout_4.addWidget(self.btn_address_3, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 5, 0, 1, 1)
        self.btn_address_2 = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_address_2.setFont(font)
        self.btn_address_2.setObjectName("btn_address_2")
        self.gridLayout_4.addWidget(self.btn_address_2, 3, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.btn_fill = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fill.setObjectName("btn_fill")
        self.verticalLayout_2.addWidget(self.btn_fill)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.acronym)
        MainWindow.setTabOrder(self.acronym, self.name)
        MainWindow.setTabOrder(self.name, self.data_begin)
        MainWindow.setTabOrder(self.data_begin, self.data_end)
        MainWindow.setTabOrder(self.data_end, self.description)
        MainWindow.setTabOrder(self.description, self.comments)
        MainWindow.setTabOrder(self.comments, self.organization_1_acronym)
        MainWindow.setTabOrder(self.organization_1_acronym, self.organization_1_name)
        MainWindow.setTabOrder(self.organization_1_name, self.organization_2_acronym)
        MainWindow.setTabOrder(self.organization_2_acronym, self.organization_2_name)
        MainWindow.setTabOrder(self.organization_2_name, self.organization_3_acronym)
        MainWindow.setTabOrder(self.organization_3_acronym, self.organization_3_name)
        MainWindow.setTabOrder(self.organization_3_name, self.organization_4_acronym)
        MainWindow.setTabOrder(self.organization_4_acronym, self.organization_4_name)
        MainWindow.setTabOrder(self.organization_4_name, self.link_1_name)
        MainWindow.setTabOrder(self.link_1_name, self.link_1_url)
        MainWindow.setTabOrder(self.link_1_url, self.link_2_name)
        MainWindow.setTabOrder(self.link_2_name, self.link_2_url)
        MainWindow.setTabOrder(self.link_2_url, self.link_3_name)
        MainWindow.setTabOrder(self.link_3_name, self.link_3_url)
        MainWindow.setTabOrder(self.link_3_url, self.link_4_name)
        MainWindow.setTabOrder(self.link_4_name, self.link_4_url)
        MainWindow.setTabOrder(self.link_4_url, self.link_5_name)
        MainWindow.setTabOrder(self.link_5_name, self.link_5_url)
        MainWindow.setTabOrder(self.link_5_url, self.btn_address_1)
        MainWindow.setTabOrder(self.btn_address_1, self.btn_address_2)
        MainWindow.setTabOrder(self.btn_address_2, self.btn_address_3)
        MainWindow.setTabOrder(self.btn_address_3, self.btn_fill)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SSHADE Laboratory XML template"))
        self.header.setText(_translate("MainWindow", "SSHADE XML generator"))
        self.XML_type_label.setText(_translate("MainWindow", "<html><head/><body><p>Laboratory template</p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "Laboratory information"))
        self.label_5.setText(_translate("MainWindow", "Acronym **"))
        self.acronym.setToolTip(_translate("MainWindow", "<html><head/><body><p>Acronym of the laboratory</p></body></html>"))
        self.acronym.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Full name of the laboratory **"))
        self.name.setToolTip(_translate("MainWindow", "<html><head/><body><p>Full name of the laboratory</p></body></html>"))
        self.data_begin.setToolTip(_translate("MainWindow", "<html><head/><body><p>Beginning date of the laboratory</p></body></html>"))
        self.data_begin.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.data_end.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ending date of the laboratory (COMPULSORY when lab stop activity)</p></body></html>"))
        self.data_end.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.label_7.setText(_translate("MainWindow", "Date begin"))
        self.label_26.setText(_translate("MainWindow", "Date end (if it exists)"))
        self.checkBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>add ending date of the laboratory</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Description"))
        self.description.setToolTip(_translate("MainWindow", "<html><head/><body><p>General description of the scientific/technical activity of the laboratory</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Any additional information"))
        self.comments.setToolTip(_translate("MainWindow", "<html><head/><body><p>Additional information on the laboratory (Tel, contacts, ...)</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1 Info"))
        self.label_22.setText(_translate("MainWindow", "Laboratory related organizations"))
        self.label_ORCIDE.setText(_translate("MainWindow", "Organization 1 *"))
        self.organization_1_acronym.setToolTip(_translate("MainWindow", "<html><head/><body><p>Acronym of the parent organization to which belong the laboratory</p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "acronym"))
        self.label_28.setText(_translate("MainWindow", "name"))
        self.organization_1_name.setToolTip(_translate("MainWindow", "<html><head/><body><p>Name of the parent organization to which belong the laboratory</p></body></html>"))
        self.label_ResearcherID.setText(_translate("MainWindow", "Organization 2"))
        self.organization_2_acronym.setToolTip(_translate("MainWindow", "<html><head/><body><p>Acronym of the parent organization to which belong the laboratory</p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "acronym"))
        self.label_30.setText(_translate("MainWindow", "name"))
        self.organization_2_name.setToolTip(_translate("MainWindow", "<html><head/><body><p>Name of the parent organization to which belong the laboratory</p></body></html>"))
        self.label_ScopusAuthorID.setText(_translate("MainWindow", "Organization 3"))
        self.organization_3_acronym.setToolTip(_translate("MainWindow", "<html><head/><body><p>Acronym of the parent organization to which belong the laboratory</p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "acronym"))
        self.label_32.setText(_translate("MainWindow", "name"))
        self.organization_3_name.setToolTip(_translate("MainWindow", "<html><head/><body><p>Name of the parent organization to which belong the laboratory</p></body></html>"))
        self.label_ScopusAuthorID_2.setText(_translate("MainWindow", "Organization 4"))
        self.organization_4_acronym.setToolTip(_translate("MainWindow", "<html><head/><body><p>Acronym of the parent organization to which belong the laboratory</p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "acronym"))
        self.label_34.setText(_translate("MainWindow", "name"))
        self.organization_4_name.setToolTip(_translate("MainWindow", "<html><head/><body><p>Name of the parent organization to which belong the laboratory</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "2 Organizations"))
        self.label.setText(_translate("MainWindow", "Laboratories and organizations Web Pages"))
        self.label_23.setText(_translate("MainWindow", "Web page 1 *"))
        self.link_1_name.setToolTip(_translate("MainWindow", "<html><head/><body><p>Name of the web page</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "name"))
        self.label_11.setText(_translate("MainWindow", "URL "))
        self.link_1_url.setToolTip(_translate("MainWindow", "<html><head/><body><p>URL address (avoid non-perennial commercial URL)</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Web page 2"))
        self.label_12.setText(_translate("MainWindow", "name"))
        self.link_2_name.setToolTip(_translate("MainWindow", "<html><head/><body><p>Name of the web page</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "URL "))
        self.link_2_url.setToolTip(_translate("MainWindow", "<html><head/><body><p>URL address (avoid non-perennial commercial URL)</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Web page 3"))
        self.label_14.setText(_translate("MainWindow", "name"))
        self.link_3_name.setToolTip(_translate("MainWindow", "<html><head/><body><p>Name of the web page</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "URL "))
        self.link_3_url.setToolTip(_translate("MainWindow", "<html><head/><body><p>URL address (avoid non-perennial commercial URL)</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Web page 4"))
        self.label_16.setText(_translate("MainWindow", "name"))
        self.link_4_name.setToolTip(_translate("MainWindow", "<html><head/><body><p>Name of the web page</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "URL "))
        self.link_4_url.setToolTip(_translate("MainWindow", "<html><head/><body><p>URL address (avoid non-perennial commercial URL)</p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "Web page 5"))
        self.label_36.setText(_translate("MainWindow", "name"))
        self.link_5_name.setToolTip(_translate("MainWindow", "<html><head/><body><p>Name of the web page</p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "URL "))
        self.link_5_url.setToolTip(_translate("MainWindow", "<html><head/><body><p>URL address (avoid non-perennial commercial URL)</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "3 Links"))
        self.label_18.setText(_translate("MainWindow", "At least one address must be given"))
        self.btn_address_1.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add an address</p></body></html>"))
        self.btn_address_1.setText(_translate("MainWindow", "Address 1"))
        self.btn_address_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add one more address</p></body></html>"))
        self.btn_address_3.setText(_translate("MainWindow", "Address 3"))
        self.btn_address_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add another address</p></body></html>"))
        self.btn_address_2.setText(_translate("MainWindow", "Address 2"))
        self.label_24.setText(_translate("MainWindow", "Laboratory addresses"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "4 Addresses"))
        self.label_20.setText(_translate("MainWindow", "**: This information is mandatory\n"
"*: This information is recommended"))
        self.btn_fill.setText(_translate("MainWindow", "Fill the XML template with this information"))
        self.actionAbout.setText(_translate("MainWindow", "About"))