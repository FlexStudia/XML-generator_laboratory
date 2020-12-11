# coding: utf-8

# IMPORTS
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QLabel, QAction, QApplication
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
import sys
from templates.main_window import Ui_MainWindow as Ui_MainWindow
from templates.add_address_dialog import Ui_add_address_dialog as Ui_AddAddress
from XMLgenerator_laboratory import address_data_verification as address_data_verification
from XMLgenerator_laboratory import global_data_verification as global_data_verification
from XMLgenerator_laboratory import xml_parse_and_fill as xml_parse_and_fill
from XMLgenerator_laboratory import accent_letters_replace as accent_letters_replace

# GLOBALS
# variables
__version__ = 0.82
__copyright__ = "CC-BY 4.0 (Authors attribution alone required)"
__author_mail__ = "flex.studia.dev@gmail.com"
__bug_support_mail__ = "XML.generator.laboratory@gmail.com"
# XML template: laboratory
template = "<?xml version='1.0' encoding='UTF-8'?><!--  Data type : Laboratory Specific notes : 	-  	 General notes :  	- Most of the tags are optional, you can remove the really unnecessary ones. 	- Tags marked as 'multiple' can be copied (with its block of sub-tag, up to the ending tag) if needed. 	- all blocs marked 'OPTION' can be fully removed if not needed (now or in the future) 	- **ABS MANDATORY / ABS COMPULSORY**: a value need to be absolutely provided, no way to escape! (SSHADE will not function properly if absent). 	- **MANDATORY / COMPULSORY**: very important values for the search of the data. If the value (txt or numeric) of one tag is not known (or irrelevant in your case), then put 'NULL' and write a comment to keep track of the missing value. Remove comment when value is added. 	- **MANDATORY / COMPULSORY only for ...**: when a value is optionally MANDATORY the condition is written.  	- 'LINK to existing UID' (unique identifier): references to another table in SSHADE. You have to reconstruct (easy for some: rule is in comment) or found this existing UID in the database beforehand (use 'Provider/Full Search' menu in SSHADE). 	- 'UID to CREATE': you need to create this UID using their specific rules of creation that are explained in their attached comment. Use only alphanumeric characters and '_'. 	- For UID you can use only alpha-numeric characters and the following: '_', '-' 	- Enumeration type ('Enum' or 'OpenEnum') must contain one single item from the list given in brackets {}. 	- use a CDATA tag when a value contains at least one special character (ie: &, >, <,...). Example: <![CDATA[AT&T]]> for AT&T 	- The data format is noted beetween [] and is 'ascii' when not specified. Ex: [Float], [Integer]. For [float] 2 formats are possible: decimal (123.456) or scientific (1.234e-56)   	- when no numerical format or Enum is specified, it is free text but limited to 256 characters. Only those noted [blob] have no size limitation. 	- to import data for the first time you have to set <import_mode>='first import'. To correct data you have to change it to 'correction'. 	- when a <filename> is given, then the file should be ziped with this xml file for import.    --><import type='laboratory' ssdm_version='0.9.0' xmlns='http://sshade.eu/schema/import' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://sshade.eu/schema/import http://sshade.eu/schema/import-0.9.xsd'><laboratory><!-- multiple --><import_mode>first import</import_mode> <!-- **ABS MANDATORY** Mode of import of the 'laboratory' data. Enum: {first import, ignore, draft, no change, correction} --><uid>LAB_</uid> <!-- **ABS MANDATORY to CREATE** Unique identifier code given to the laboratory. Should be of the style ‘LAB_LabAcronym’ where ‘LabAcronym’ is the acronym of the laboratory. Format: in UPPERCASES --><manager_databases> <!-- **ABS MANDATORY at least one** --><database_uid>DB_</database_uid><!-- multiple --> <!-- **ABS MANDATORY** LINK to the existing UID of the database which manages this laboratory information [‘DB_DatabaseAcronym’] --></manager_databases><!-- LABORATORY DESCRIPTION --><acronym></acronym> <!-- **ABS MANDATORY** Acronym of the laboratory -->	<name><![CDATA[]]></name> <!-- **ABS MANDATORY** Full name of the laboratory --><description><![CDATA[]]></description><!-- General description of the scientific/technical activity of the laboratory [blob] --><organizations> <!-- **MANDATORY at least one** --><organization><!-- multiple --> <acronym></acronym> <!-- **MANDATORY** Acronym of the parent organization to which belong the laboratory -->	<name><![CDATA[]]></name> <!-- **MANDATORY** Name of the parent organization to which belong the laboratory --></organization></organizations><addresses> <!-- **ABS MANDATORY at least one** --><address><!-- multiple --> <label></label> <!-- Label of the address (postal/geographic) or name of the geographic site of the laboratory (with multiple sites) --><street><![CDATA[]]></street> <!-- **MANDATORY** Street address, building number/name of the laboratory, and/or PO Box --><postal_code></postal_code> <!-- **MANDATORY** Postal code of the laboratory --><city></city> <!-- **MANDATORY** City/locality of the laboratory --><region><![CDATA[]]></region>  <!-- Region, state, province, or county of the laboratory --><country_code></country_code> <!-- **ABS MANDATORY** 2-digit country code of the laboratory. Enum: {CH, DE, ES, FR, GB, HU, IT, PL, …} [norm ISO 3166-1 alpha-2] see  https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 --></address></addresses><!-- LABORATORY HISTORY --><date_begin></date_begin> <!-- Beginning date of the laboratory. [Format: ‘YYYY-MM-DD’] Ex: '1999-10-05' --><date_end></date_end> <!-- **COMPULSORY when lab stop activity** Ending date of the laboratory. [Format: ‘YYYY-MM-DD’] --><!-- LABORATORY WEB SITES --><links> <!-- **MANDATORY at least one** Link(s) to current web page(s) of the laboratory and organization(s) --><link><!-- multiple --> <name><![CDATA[]]></name> <!-- **MANDATORY** Name of the web page(s) --><url><![CDATA[]]></url> <!-- **MANDATORY** URL address (avoid non-perennial commercial URL) --></link></links><comments><![CDATA[]]></comments> <!-- Additional information on the laboratory (Tel, …) [blob] --></laboratory></import>"
# styles
button_style = 'QPushButton{padding: 5px}'
# dicts
address_array = dict()
address_array.update({'address_1_label': ''})
address_array.update({'address_1_street': ''})
address_array.update({'address_1_postal_code': ''})
address_array.update({'address_1_city': ''})
address_array.update({'address_1_region': ''})
address_array.update({'address_1_country_code': ''})
address_array.update({'address_1_country_code_index': 0})
address_array.update({'address_2_label': ''})
address_array.update({'address_2_street': ''})
address_array.update({'address_2_postal_code': ''})
address_array.update({'address_2_city': ''})
address_array.update({'address_2_region': ''})
address_array.update({'address_2_country_code': ''})
address_array.update({'address_2_country_code_index': 0})
address_array.update({'address_3_label': ''})
address_array.update({'address_3_street': ''})
address_array.update({'address_3_postal_code': ''})
address_array.update({'address_3_city': ''})
address_array.update({'address_3_region': ''})
address_array.update({'address_3_country_code': ''})
address_array.update({'address_3_country_code_index': 0})


# FUNCTIONS
# style function to add colors, borders & padding to fields
def style_color_add(field_type, color):
    if color == 'red':
        border_color = '251,157,111'
        background_color = '255,250,245'
    elif color == 'green':
        border_color = '86,231,200'
        background_color = '249,255,254'
    elif color == 'gray':
        border_color = '190,190,190'
        background_color = '240,240,240'
    else:
        border_color = '240,200,41'
        background_color = '253,253,241'
    return f"{field_type}[border-width: 2px; border-style: solid; border-color: rgb({border_color}); " \
           f"background-color: rgb({background_color}); padding: 2px; font-size: 16px]" \
        .replace("[", "{").replace("]", "}")


# class to make a clickable area for QLabel
class QLabelClickable(QLabel):
    clicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)

    def mousePressEvent(self, event):
        self.ultimo = "Clic"

    def mouseReleaseEvent(self, event):
        QTimer.singleShot(QApplication.instance().doubleClickInterval()/6,
                          self.performSingleClickAction)

    def performSingleClickAction(self):
        if self.ultimo == "Clic":
            self.clicked.emit(self.ultimo)


# MAIN WINDOW class
class XMLGeneratorMainW(QtWidgets.QMainWindow):
    def __init__(self):
        super(XMLGeneratorMainW, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # GUI beauties
        self.setWindowTitle(f'SSHADE Laboratory XML template v{__version__}')
        # acronym
        self.ui.acronym.setStyleSheet(f'{style_color_add("QLineEdit", "red")}')
        # name
        self.ui.name.setStyleSheet(f'{style_color_add("QLineEdit", "red")}')
        # date begin
        self.ui.data_begin.setStyleSheet(f'{style_color_add("QDateEdit", "green")}')
        # checkBox
        self.ui.checkBox.setChecked(False)
        self.ui.checkBox.setStyleSheet('QCheckBox{padding-left: 10px; padding-right: 0; margin-right: -7px}')
        # date end
        self.ui.data_end.setStyleSheet(f'{style_color_add("QDateEdit", "gray")}')
        self.ui.data_end.setDisabled(True)
        # description
        self.ui.description.setStyleSheet(f'{style_color_add("QTextEdit", "green")}')
        # comments
        self.ui.comments.setStyleSheet(f'{style_color_add("QTextEdit", "green")}')
        # organization 1
        self.ui.organization_1_acronym.setStyleSheet(f'{style_color_add("QLineEdit", "yellow")}')
        self.ui.organization_1_name.setStyleSheet(f'{style_color_add("QTextEdit", "yellow")}')
        # organization 2
        self.ui.organization_2_acronym.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        self.ui.organization_2_name.setStyleSheet(f'{style_color_add("QTextEdit", "green")}')
        # organization 3
        self.ui.organization_3_acronym.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        self.ui.organization_3_name.setStyleSheet(f'{style_color_add("QTextEdit", "green")}')
        # organization 4
        self.ui.organization_4_acronym.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        self.ui.organization_4_name.setStyleSheet(f'{style_color_add("QTextEdit", "green")}')
        # link 1
        self.ui.link_1_name.setStyleSheet(f'{style_color_add("QLineEdit", "yellow")}')
        self.ui.link_1_url.setStyleSheet(f'{style_color_add("QLineEdit", "yellow")}')
        # link 2
        self.ui.link_2_name.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        self.ui.link_2_url.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        # link 3
        self.ui.link_3_name.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        self.ui.link_3_url.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        # link 4
        self.ui.link_4_name.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        self.ui.link_4_url.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        # link 5
        self.ui.link_5_name.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        self.ui.link_5_url.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        # address 1
        self.ui.btn_address_1.setStyleSheet(f'{button_style}')
        # address 2
        self.ui.btn_address_2.setStyleSheet(f'{button_style}')
        # address 3
        self.ui.btn_address_3.setStyleSheet(f'{button_style}')
        # fill & submit button
        self.ui.btn_fill.setStyleSheet(f'{button_style}')
        # Menu
        extractAction = QAction("&About", self)
        extractAction.setStatusTip('About The App')
        extractAction.triggered.connect(self.show_about)
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&Help')
        fileMenu.addAction(extractAction)
        # Signal & Slots
        # data_end checkbox toggle
        self.ui.checkBox.stateChanged.connect(self.checkbox_toggle)
        self.ui.labelImagen = QLabelClickable(self)
        self.ui.labelImagen.setGeometry(260, 313, 200, 22)
        #self.ui.labelImagen.setStyleSheet("QLabel {background-color: white; border: 1px solid #01DFD7; border-radius: 5px;}")
        self.ui.labelImagen.clicked.connect(self.label_checkbox_toggle)
        # fill XML button
        self.ui.btn_fill.clicked.connect(self.fill_xml_function)
        # address buttons
        self.ui.btn_address_1.clicked.connect(self.add_address_1)
        self.ui.btn_address_2.clicked.connect(self.add_address_2)
        self.ui.btn_address_3.clicked.connect(self.add_address_3)

    def resizeEvent(self, event):
        self.ui.labelImagen.setGeometry(self.ui.label_26.x(), 313, self.ui.label_26.width(), 22)
        QtWidgets.QMainWindow.resizeEvent(self, event)

    def label_checkbox_toggle(self):
        if self.ui.checkBox.isChecked():
            self.ui.checkBox.setChecked(False)
        else:
            self.ui.checkBox.setChecked(True)

    def checkbox_toggle(self):
        if self.ui.checkBox.isChecked():
            self.ui.data_end.setStyleSheet(f'{style_color_add("QDateEdit", "green")}')
            self.ui.data_end.setDisabled(False)
        else:
            self.ui.data_end.setStyleSheet(f'{style_color_add("QDateEdit", "gray")}')
            self.ui.data_end.setDisabled(True)

    def show_about(self):
        self.dialog_ok(f"<b>XML generator: laboratory</b> v{__version__}"
                       f"<p>Copyright: {__copyright__}</p>"
                       f"<p>Created by Gorbacheva Maria ({__author_mail__})</p>"
                       "<p>Scientific base by Bernard Schmitt, IPAG (bernard.schmitt@univ-grenoble-alpes.fr)</p>"
                       f"<p>For any questions and bug reports, please, mail at {__bug_support_mail__}</p>"
                       "<p>In case of a bug, please report it and specify your operating system, "
                       "provide a detailed description of the problem with screenshots "
                       "and the files used and produced, if possible. Your contribution matters to make it better!</p>")

    def dialog_ok(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Ok!')
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Information)
        dlg.show()

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Error!')
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def add_address_1(self):
        AddAddressW(1)

    def add_address_2(self):
        AddAddressW(2)

    def add_address_3(self):
        AddAddressW(3)

    def fill_xml_function(self):
        # data verification
        verification_result = global_data_verification(self.ui.acronym.text().strip(),
                                                       self.ui.name.text().strip(),
                                                       self.ui.description.toPlainText(),
                                                       self.ui.comments.toPlainText(),
                                                       self.ui.organization_1_acronym.text().strip(),
                                                       self.ui.organization_1_name.toPlainText(),
                                                       self.ui.organization_2_acronym.text().strip(),
                                                       self.ui.organization_2_name.toPlainText(),
                                                       self.ui.organization_3_acronym.text().strip(),
                                                       self.ui.organization_3_name.toPlainText(),
                                                       self.ui.organization_4_acronym.text().strip(),
                                                       self.ui.organization_4_name.toPlainText(),
                                                       address_array['address_1_label'],
                                                       address_array['address_1_street'],
                                                       address_array['address_1_postal_code'],
                                                       address_array['address_1_city'],
                                                       address_array['address_1_region'],
                                                       address_array['address_1_country_code'],
                                                       address_array['address_2_label'],
                                                       address_array['address_2_street'],
                                                       address_array['address_2_postal_code'],
                                                       address_array['address_2_city'],
                                                       address_array['address_2_region'],
                                                       address_array['address_2_country_code'],
                                                       address_array['address_3_label'],
                                                       address_array['address_3_street'],
                                                       address_array['address_3_postal_code'],
                                                       address_array['address_3_city'],
                                                       address_array['address_3_region'],
                                                       address_array['address_3_country_code'],
                                                       self.ui.data_begin.date().toString("yyyy-MM-dd"),
                                                       self.ui.data_end.date().toString("yyyy-MM-dd"),
                                                       self.ui.link_1_name.text().strip(),
                                                       self.ui.link_1_url.text().strip(),
                                                       self.ui.link_2_name.text().strip(),
                                                       self.ui.link_2_url.text().strip(),
                                                       self.ui.link_3_name.text().strip(),
                                                       self.ui.link_3_url.text().strip(),
                                                       self.ui.link_4_name.text().strip(),
                                                       self.ui.link_4_url.text().strip(),
                                                       self.ui.link_5_name.text().strip(),
                                                       self.ui.link_5_url.text().strip())
        verification_Ok = verification_result[0]
        if not verification_Ok:
            if verification_result[1][0] == 'acronym':
                self.ui.tabWidget.setCurrentIndex(0)
                self.ui.acronym.setFocus()
            elif verification_result[1][0] == 'name':
                self.ui.tabWidget.setCurrentIndex(0)
                self.ui.name.setFocus()
            elif verification_result[1][0] == 'btn_address':
                self.ui.tabWidget.setCurrentIndex(3)
                self.ui.btn_address_1.setFocus()
            elif verification_result[1][0] == 'acronym of organization 1':
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.organization_1_acronym.setFocus()
            elif verification_result[1][0] == 'acronym of organization 2':
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.organization_2_acronym.setFocus()
            elif verification_result[1][0] == 'acronym of organization 3':
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.organization_3_acronym.setFocus()
            elif verification_result[1][0] == 'acronym of organization 4':
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.organization_4_acronym.setFocus()
            elif verification_result[1][0] == 'name of organization 1':
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.organization_1_name.setFocus()
            elif verification_result[1][0] == 'name of organization 2':
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.organization_2_name.setFocus()
            elif verification_result[1][0] == 'name of organization 3':
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.organization_3_name.setFocus()
            elif verification_result[1][0] == 'name of organization 4':
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.organization_4_name.setFocus()
            elif verification_result[1][0] == 'name of link 1':
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.link_1_name.setFocus()
            elif verification_result[1][0] == 'name of link 2':
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.link_2_name.setFocus()
            elif verification_result[1][0] == 'name of link 3':
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.link_3_name.setFocus()
            elif verification_result[1][0] == 'name of link 4':
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.link_4_name.setFocus()
            elif verification_result[1][0] == 'name of link 5':
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.link_5_name.setFocus()
            elif verification_result[1][0] == 'URL of link 1':
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.link_1_url.setFocus()
            elif verification_result[1][0] == 'URL of link 2':
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.link_2_url.setFocus()
            elif verification_result[1][0] == 'URL of link 3':
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.link_3_url.setFocus()
            elif verification_result[1][0] == 'URL of link 4':
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.link_4_url.setFocus()
            elif verification_result[1][0] == 'URL of link 5':
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.link_5_url.setFocus()
            self.dialog_critical(verification_result[1][1])
        else:
            # fill XML
            if self.ui.data_end.isEnabled():
                data_end = self.ui.data_end.date().toString("yyyy-MM-dd")
            else:
                data_end = ''
            str_to_upload = xml_parse_and_fill(template, self.ui.acronym.text().strip(),
                                               self.ui.name.text().strip(),
                                               self.ui.description.toPlainText(),
                                               self.ui.comments.toPlainText(),
                                               self.ui.organization_1_acronym.text().strip(),
                                               self.ui.organization_1_name.toPlainText(),
                                               self.ui.organization_2_acronym.text().strip(),
                                               self.ui.organization_2_name.toPlainText(),
                                               self.ui.organization_3_acronym.text().strip(),
                                               self.ui.organization_3_name.toPlainText(),
                                               self.ui.organization_4_acronym.text().strip(),
                                               self.ui.organization_4_name.toPlainText(),
                                               address_array['address_1_label'],
                                               address_array['address_1_street'],
                                               address_array['address_1_postal_code'],
                                               address_array['address_1_city'],
                                               address_array['address_1_region'],
                                               address_array['address_1_country_code'],
                                               address_array['address_2_label'],
                                               address_array['address_2_street'],
                                               address_array['address_2_postal_code'],
                                               address_array['address_2_city'],
                                               address_array['address_2_region'],
                                               address_array['address_2_country_code'],
                                               address_array['address_3_label'],
                                               address_array['address_3_street'],
                                               address_array['address_3_postal_code'],
                                               address_array['address_3_city'],
                                               address_array['address_3_region'],
                                               address_array['address_3_country_code'],
                                               self.ui.data_begin.date().toString("yyyy-MM-dd"),
                                               data_end,
                                               self.ui.link_1_name.text().strip(),
                                               self.ui.link_1_url.text().strip(),
                                               self.ui.link_2_name.text().strip(),
                                               self.ui.link_2_url.text().strip(),
                                               self.ui.link_3_name.text().strip(),
                                               self.ui.link_3_url.text().strip(),
                                               self.ui.link_4_name.text().strip(),
                                               self.ui.link_4_url.text().strip(),
                                               self.ui.link_5_name.text().strip(),
                                               self.ui.link_5_url.text().strip())
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self, "Save File",
                                                       f"laboratory_{accent_letters_replace(self.ui.acronym.text().strip()).upper().replace('-', '_').replace(' ', '_')}.xml",
                                                       "Text Files (*.xml)", options=options)
            if file_name:
                with open(file_name, 'wb') as file_output:
                    file_output.write(str_to_upload)
                self.dialog_ok('The XML was saved!')


# add address class
class AddAddressW(QtWidgets.QDialog):
    def __init__(self, current_address_number):
        super(AddAddressW, self).__init__()
        self.ui = Ui_AddAddress()
        self.ui.setupUi(self)
        # GLOBALS
        self.current_address_number = current_address_number
        # GUI beauties
        # window title
        self.setWindowTitle(f'Add/Edit address {current_address_number}')
        # label
        self.ui.address_label.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        self.ui.address_label.setText(address_array[f'address_{self.current_address_number}_label'])
        # street
        self.ui.address_street.setStyleSheet(f'{style_color_add("QLineEdit", "yellow")}')
        self.ui.address_street.setText(address_array[f'address_{self.current_address_number}_street'])
        # postal_code
        self.ui.address_postal_code.setStyleSheet(f'{style_color_add("QLineEdit", "yellow")}')
        self.ui.address_postal_code.setText(address_array[f'address_{self.current_address_number}_postal_code'])
        # city
        self.ui.address_city.setStyleSheet(f'{style_color_add("QLineEdit", "yellow")}')
        self.ui.address_city.setText(address_array[f'address_{self.current_address_number}_city'])
        # region
        self.ui.address_region.setStyleSheet(f'{style_color_add("QLineEdit", "green")}')
        self.ui.address_region.setText(address_array[f'address_{self.current_address_number}_region'])
        # country_code
        self.ui.address_country_code.setStyleSheet(f'{style_color_add("QComboBox", "red")}')
        country_array = ["none", "other", "AD - Andorra", "AE - United Arab Emirates", "AF - Afghanistan",
                         "AG - Antigua and Barbuda", "AI - Anguilla", "AL - Albania", "AM - Armenia", "AO - Angola",
                         "AQ - Antarctica", "AR - Argentina", "AS - American Samoa", "AT - Austria", "AU - Australia",
                         "AW - Aruba", "AX - Åland Islands", "AZ - Azerbaijan", "BA - Bosnia and Herzegovina",
                         "BB - Barbados", "BD - Bangladesh", "BE - Belgium", "BF - Burkina Faso", "BG - Bulgaria",
                         "BH - Bahrain", "BI - Burundi", "BJ - Benin", "BL - Saint Barthélemy", "BM - Bermuda",
                         "BN - Brunei Darussalam", "BO - Bolivia (Plurinational State of)",
                         "BQ - Bonaire, Sint Eustatius and Saba", "BR - Brazil", "BS - Bahamas", "BT - Bhutan",
                         "BV - Bouvet Island", "BW - Botswana", "BY - Belarus", "BZ - Belize", "CA - Canada",
                         "CC - Cocos (Keeling) Islands", "CD - Congo, Democratic Republic of the",
                         "CF - Central African Republic", "CG - Congo", "CH - Switzerland", "CI - Côte d'Ivoire",
                         "CK - Cook Islands", "CL - Chile", "CM - Cameroon", "CN - China", "CO - Colombia",
                         "CR - Costa Rica", "CU - Cuba", "CV - Cabo Verde", "CW - Curaçao", "CX - Christmas Island",
                         "CY - Cyprus", "CZ - Czechia", "CZ - Czech Republic", "DE - Germany", "DJ - Djibouti",
                         "DK - Denmark", "DM - Dominica", "DO - Dominican Republic", "DZ - Algeria", "EC - Ecuador",
                         "EE - Estonia", "EG - Egypt", "EH - Western Sahara", "ER - Eritrea", "ES - Spain",
                         "ET - Ethiopia", "FI - Finland", "FJ - Fiji", "FK - Falkland Islands (Malvinas)",
                         "FM - Micronesia (Federated States of)", "FO - Faroe Islands", "FR - France", "GA - Gabon",
                         "GB - United Kingdom of Great Britain and Northern Ireland", "GD - Grenada", "GE - Georgia",
                         "GF - French Guiana", "GG - Guernsey", "GH - Ghana", "GI - Gibraltar", "GL - Greenland",
                         "GM - Gambia", "GN - Guinea", "GP - Guadeloupe", "GQ - Equatorial Guinea", "GR - Greece",
                         "GS - South Georgia and the South Sandwich Islands", "GT - Guatemala", "GU - Guam",
                         "GW - Guinea-Bissau", "GY - Guyana", "HK - Hong Kong",
                         "HM - Heard Island and McDonald Islands", "HN - Honduras", "HR - Croatia", "HT - Haiti",
                         "HU - Hungary", "ID - Indonesia", "IE - Ireland", "IL - Israel", "IM - Isle of Man",
                         "IN - India", "IO - British Indian Ocean Territory", "IQ - Iraq", "IR - Iran",
                         "IR - Islamic Republic of Iran", "IS - Iceland", "IT - Italy", "JE - Jersey", "JM - Jamaica",
                         "JO - Jordan", "JP - Japan", "KE - Kenya", "KG - Kyrgyzstan", "KH - Cambodia", "KI - Kiribati",
                         "KM - Comoros", "KN - Saint Kitts and Nevis", "KP - Korea (Democratic People's Republic of)",
                         "KR - Korea, Republic of", "KW - Kuwait", "KY - Cayman Islands", "KZ - Kazakhstan",
                         "LA - Lao People's Democratic Republic", "LB - Lebanon", "LC - Saint Lucia",
                         "LI - Liechtenstein", "LK - Sri Lanka", "LR - Liberia", "LS - Lesotho", "LT - Lithuania",
                         "LU - Luxembourg", "LV - Latvia", "LY - Libya", "MA - Morocco", "MC - Monaco",
                         "MD - Moldova, Republic of", "ME - Montenegro", "MF - Saint Martin (French part)",
                         "MG - Madagascar", "MH - Marshall Islands", "MK - North Macedonia", "ML - Mali",
                         "MM - Myanmar", "MN - Mongolia", "MO - Macao", "MP - Northern Mariana Islands",
                         "MQ - Martinique", "MR - Mauritania", "MS - Montserrat", "MT - Malta", "MU - Mauritius",
                         "MV - Maldives", "MW - Malawi", "MX - Mexico", "MY - Malaysia", "MZ - Mozambique",
                         "NA - Namibia", "NC - New Caledonia", "NE - Niger", "NF - Norfolk Island", "NG - Nigeria",
                         "NI - Nicaragua", "NL - Netherlands", "NO - Norway", "NP - Nepal", "NR - Nauru", "NU - Niue",
                         "NZ - New Zealand", "OM - Oman", "PA - Panama", "PE - Peru", "PF - French Polynesia",
                         "PG - Papua New Guinea", "PH - Philippines", "PK - Pakistan", "PL - Poland",
                         "PM - Saint Pierre and Miquelon", "PN - Pitcairn", "PR - Puerto Rico",
                         "PS - Palestine, State of", "PT - Portugal", "PW - Palau", "PY - Paraguay", "QA - Qatar",
                         "RE - Réunion", "RO - Romania", "RS - Serbia", "RU - Russian Federation", "RU - Russia",
                         "RW - Rwanda", "SA - Saudi Arabia", "SB - Solomon Islands", "SC - Seychelles", "SD - Sudan",
                         "SE - Sweden", "SG - Singapore", "SH - Saint Helena, Ascension and Tristan da Cunha",
                         "SI - Slovenia", "SJ - Svalbard and Jan Mayen", "SK - Slovakia", "SL - Sierra Leone",
                         "SM - San Marino", "SN - Senegal", "SO - Somalia", "SR - Suriname", "SS - South Sudan",
                         "ST - Sao Tome and Principe", "SV - El Salvador", "SX - Sint Maarten (Dutch part)",
                         "SY - Syrian Arab Republic", "SZ - Eswatini", "TC - Turks and Caicos Islands", "TD - Chad",
                         "TF - French Southern Territories", "TG - Togo", "TH - Thailand", "TJ - Tajikistan",
                         "TK - Tokelau", "TL - Timor-Leste", "TM - Turkmenistan", "TN - Tunisia", "TO - Tonga",
                         "TR - Turkey", "TT - Trinidad and Tobago", "TV - Tuvalu", "TW - Taiwan, Province of China",
                         "TZ - Tanzania, United Republic of", "UA - Ukraine", "UG - Uganda",
                         "UM - United States Minor Outlying Islands", "US - United States",
                         "US - United States of America", "UY - Uruguay", "UZ - Uzbekistan", "VA - Holy See",
                         "VC - Saint Vincent and the Grenadines", "VE - Venezuela (Bolivarian Republic of)",
                         "VG - Virgin Islands (British)", "VI - Virgin Islands (U.S.)", "VN - Viet Nam", "VU - Vanuatu",
                         "WF - Wallis and Futuna", "WS - Samoa", "YE - Yemen", "YT - Mayotte", "ZA - South Africa",
                         "ZM - Zambia", "ZW - Zimbabwe"]
        for index in range(0, len(country_array)):
            self.ui.address_country_code.insertItem(index, country_array[index])
        self.ui.address_country_code.setCurrentIndex(
            address_array[f'address_{self.current_address_number}_country_code_index'])
        # buttons
        self.ui.clear_btn.setStyleSheet(f'{button_style}')
        self.ui.buttonBox.setStyleSheet(f'{button_style}')
        self.ui.cancel_btn.setStyleSheet(f'{button_style}')
        # SIGNALS & SLOTS
        self.ui.buttonBox.clicked.connect(self.add_address_action)
        self.ui.cancel_btn.clicked.connect(self.close_add)
        self.ui.clear_btn.clicked.connect(self.clear_add)
        # WINDOW show
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.show()
        self.exec_()

    def add_address_action(self):
        # verificaton
        if self.ui.address_country_code.currentIndex() == 0:
            country_code = ''
        elif self.ui.address_country_code.currentIndex() == 1:
            country_code = self.ui.address_country_code.currentText()
        else:
            country_code = self.ui.address_country_code.currentText()[:2]
        verification_result = address_data_verification(self.ui.address_label.text(), self.ui.address_street.text(),
                                                        self.ui.address_postal_code.text(), self.ui.address_city.text(),
                                                        self.ui.address_region.text(), country_code)
        verification_OK = verification_result[0]
        # add data to dict
        if verification_OK:
            address_array[f'address_{self.current_address_number}_label'] = self.ui.address_label.text().strip()
            address_array[f'address_{self.current_address_number}_street'] = self.ui.address_street.text().strip()
            address_array[f'address_{self.current_address_number}_postal_code'] = \
                self.ui.address_postal_code.text().strip()
            address_array[f'address_{self.current_address_number}_city'] = self.ui.address_city.text().strip()
            address_array[f'address_{self.current_address_number}_region'] = self.ui.address_region.text().strip()
            address_array[f'address_{self.current_address_number}_country_code'] = country_code
            address_array[f'address_{self.current_address_number}_country_code_index'] = \
                self.ui.address_country_code.currentIndex()
            self.close()
        else:
            if verification_result[1][0] == 'street':
                self.ui.address_street.setFocus()
            elif verification_result[1][0] == 'postal code':
                self.ui.address_postal_code.setFocus()
            elif verification_result[1][0] == 'city':
                self.ui.address_city.setFocus()
            elif verification_result[1][0] == 'country code':
                self.ui.address_country_code.setFocus()
            self.dialog_critical(verification_result[1][1])

    def close_add(self):
        self.close()

    def clear_add(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to clear the form?\nAll its data will be lost", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.ui.address_label.setText('')
            self.ui.address_street.setText('')
            self.ui.address_postal_code.setText('')
            self.ui.address_city.setText('')
            self.ui.address_region.setText('')
            self.ui.address_country_code.setCurrentIndex(0)

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Error!')
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = XMLGeneratorMainW()
    win.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
    win.show()
    sys.exit(app.exec())
