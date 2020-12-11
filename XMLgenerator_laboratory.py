# coding: utf-8

# IMPORTS
from lxml import etree

# GLOBALS
template = "<?xml version='1.0' encoding='UTF-8'?><!--  Data type : Laboratory Specific notes : 	-  	 General notes :  	- Most of the tags are optional, you can remove the really unnecessary ones. 	- Tags marked as 'multiple' can be copied (with its block of sub-tag, up to the ending tag) if needed. 	- all blocs marked 'OPTION' can be fully removed if not needed (now or in the future) 	- **ABS MANDATORY / ABS COMPULSORY**: a value need to be absolutely provided, no way to escape! (SSHADE will not function properly if absent). 	- **MANDATORY / COMPULSORY**: very important values for the search of the data. If the value (txt or numeric) of one tag is not known (or irrelevant in your case), then put 'NULL' and write a comment to keep track of the missing value. Remove comment when value is added. 	- **MANDATORY / COMPULSORY only for ...**: when a value is optionally MANDATORY the condition is written.  	- 'LINK to existing UID' (unique identifier): references to another table in SSHADE. You have to reconstruct (easy for some: rule is in comment) or found this existing UID in the database beforehand (use 'Provider/Full Search' menu in SSHADE). 	- 'UID to CREATE': you need to create this UID using their specific rules of creation that are explained in their attached comment. Use only alphanumeric characters and '_'. 	- For UID you can use only alpha-numeric characters and the following: '_', '-' 	- Enumeration type ('Enum' or 'OpenEnum') must contain one single item from the list given in brackets {}. 	- use a CDATA tag when a value contains at least one special character (ie: &, >, <,...). Example: <![CDATA[AT&T]]> for AT&T 	- The data format is noted beetween [] and is 'ascii' when not specified. Ex: [Float], [Integer]. For [float] 2 formats are possible: decimal (123.456) or scientific (1.234e-56)   	- when no numerical format or Enum is specified, it is free text but limited to 256 characters. Only those noted [blob] have no size limitation. 	- to import data for the first time you have to set <import_mode>='first import'. To correct data you have to change it to 'correction'. 	- when a <filename> is given, then the file should be ziped with this xml file for import.    --><import type='laboratory' ssdm_version='0.9.0' xmlns='http://sshade.eu/schema/import' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://sshade.eu/schema/import http://sshade.eu/schema/import-0.9.xsd'><laboratory><!-- multiple --><import_mode>first import</import_mode> <!-- **ABS MANDATORY** Mode of import of the 'laboratory' data. Enum: {first import, ignore, draft, no change, correction} --><uid>LAB_</uid> <!-- **ABS MANDATORY to CREATE** Unique identifier code given to the laboratory. Should be of the style ‘LAB_LabAcronym’ where ‘LabAcronym’ is the acronym of the laboratory. Format: in UPPERCASES --><manager_databases> <!-- **ABS MANDATORY at least one** --><database_uid>DB_</database_uid><!-- multiple --> <!-- **ABS MANDATORY** LINK to the existing UID of the database which manages this laboratory information [‘DB_DatabaseAcronym’] --></manager_databases><!-- LABORATORY DESCRIPTION --><acronym></acronym> <!-- **ABS MANDATORY** Acronym of the laboratory -->	<name><![CDATA[]]></name> <!-- **ABS MANDATORY** Full name of the laboratory --><description><![CDATA[]]></description><!-- General description of the scientific/technical activity of the laboratory [blob] --><organizations> <!-- **MANDATORY at least one** --><organization><!-- multiple --> <acronym></acronym> <!-- **MANDATORY** Acronym of the parent organization to which belong the laboratory -->	<name><![CDATA[]]></name> <!-- **MANDATORY** Name of the parent organization to which belong the laboratory --></organization></organizations><addresses> <!-- **ABS MANDATORY at least one** --><address><!-- multiple --> <label></label> <!-- Label of the address (postal/geographic) or name of the geographic site of the laboratory (with multiple sites) --><street><![CDATA[]]></street> <!-- **MANDATORY** Street address, building number/name of the laboratory, and/or PO Box --><postal_code></postal_code> <!-- **MANDATORY** Postal code of the laboratory --><city></city> <!-- **MANDATORY** City/locality of the laboratory --><region><![CDATA[]]></region>  <!-- Region, state, province, or county of the laboratory --><country_code></country_code> <!-- **ABS MANDATORY** 2-digit country code of the laboratory. Enum: {CH, DE, ES, FR, GB, HU, IT, PL, …} [norm ISO 3166-1 alpha-2] see  https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 --></address></addresses><!-- LABORATORY HISTORY --><date_begin></date_begin> <!-- Beginning date of the laboratory. [Format: ‘YYYY-MM-DD’] Ex: '1999-10-05' --><date_end></date_end> <!-- **COMPULSORY when lab stop activity** Ending date of the laboratory. [Format: ‘YYYY-MM-DD’] --><!-- LABORATORY WEB SITES --><links> <!-- **MANDATORY at least one** Link(s) to current web page(s) of the laboratory and organization(s) --><link><!-- multiple --> <name><![CDATA[]]></name> <!-- **MANDATORY** Name of the web page(s) --><url><![CDATA[]]></url> <!-- **MANDATORY** URL address (avoid non-perennial commercial URL) --></link></links><comments><![CDATA[]]></comments> <!-- Additional information on the laboratory (Tel, …) [blob] --></laboratory></import>"


# FUNCTIONS
# replacing special character
def accent_letters_replace(string_var):
    # A
    string_var = string_var.replace("À", "A")
    string_var = string_var.replace("Á", "A")
    string_var = string_var.replace("Â", "A")
    string_var = string_var.replace("Ã", "A")
    string_var = string_var.replace("Ä", "A")
    string_var = string_var.replace("Å", "A")
    string_var = string_var.replace("Æ", "Ae")
    # C
    string_var = string_var.replace("Ç", "C")
    # D
    string_var = string_var.replace("Ð", "D")
    # E
    string_var = string_var.replace("È", "E")
    string_var = string_var.replace("É", "E")
    string_var = string_var.replace("Ê", "E")
    string_var = string_var.replace("Ë", "E")
    # I
    string_var = string_var.replace("Ì", "I")
    string_var = string_var.replace("Í", "I")
    string_var = string_var.replace("Î", "I")
    string_var = string_var.replace("Ï", "I")
    # N
    string_var = string_var.replace("Ñ", "N")
    # O
    string_var = string_var.replace("Ò", "O")
    string_var = string_var.replace("Ó", "O")
    string_var = string_var.replace("Ô", "O")
    string_var = string_var.replace("Õ", "O")
    string_var = string_var.replace("Ö", "O")
    string_var = string_var.replace("Ø", "O")
    # T
    string_var = string_var.replace("Þ", "th")
    # U
    string_var = string_var.replace("Ù", "U")
    string_var = string_var.replace("Ú", "U")
    string_var = string_var.replace("Û", "U")
    string_var = string_var.replace("Ü", "U")
    # Y
    string_var = string_var.replace("Ý", "Y")
    # a
    string_var = string_var.replace("à", "a")
    string_var = string_var.replace("á", "a")
    string_var = string_var.replace("â", "a")
    string_var = string_var.replace("ã", "a")
    string_var = string_var.replace("ä", "a")
    string_var = string_var.replace("å", "a")
    string_var = string_var.replace("æ", "ae")
    # c
    string_var = string_var.replace("ç", "c")
    # d
    string_var = string_var.replace("ð", "d")
    # e
    string_var = string_var.replace("è", "e")
    string_var = string_var.replace("é", "e")
    string_var = string_var.replace("ê", "e")
    string_var = string_var.replace("ë", "e")
    # i
    string_var = string_var.replace("ì", "i")
    string_var = string_var.replace("í", "i")
    string_var = string_var.replace("î", "i")
    string_var = string_var.replace("ï", "i")
    # n
    string_var = string_var.replace("ñ", "n")
    # o
    string_var = string_var.replace("ò", "o")
    string_var = string_var.replace("ó", "o")
    string_var = string_var.replace("ô", "o")
    string_var = string_var.replace("õ", "o")
    string_var = string_var.replace("ö", "o")
    string_var = string_var.replace("ø", "o")
    # t
    string_var = string_var.replace("þ", "th")
    # s
    string_var = string_var.replace("ß", "ss")
    # u
    string_var = string_var.replace("ù", "u")
    string_var = string_var.replace("ú", "u")
    string_var = string_var.replace("û", "u")
    string_var = string_var.replace("û", "u")
    string_var = string_var.replace("ü", "u")
    # y
    string_var = string_var.replace("ý", "y")
    string_var = string_var.replace("ÿ", "y")
    # special chars
    string_var = string_var.replace(">", "")
    string_var = string_var.replace("<", "")
    string_var = string_var.replace("\\", "")
    string_var = string_var.replace("/", "")
    string_var = string_var.replace("'", "")
    string_var = string_var.replace('"', "")
    return string_var


# data together verification: function verifies if elements of elements_tuple are all empty or all filled
def data_together_verification(elements_tuple, elements_names):
    bool_and = bool(elements_tuple[0])
    bool_or = bool(elements_tuple[0])
    for index in range(1, len(elements_tuple)):
        bool_and = bool_and and bool(elements_tuple[index])
        bool_or = bool_or or bool(elements_tuple[index])
    if not bool_and and bool_or:
        index = 0
        for index in range(0, len(elements_tuple)):
            if elements_tuple[index] == '':
                break
        other_elements_str = ''
        for element in range(0, len(elements_tuple)):
            if element != index:
                if other_elements_str != '':
                    other_elements_str = other_elements_str + ' and/or '
                other_elements_str = other_elements_str + elements_names[element]
        print(f'focus on {elements_names[index]}')
        message = f'{elements_names[index]} is mandatory if {other_elements_str} ' \
                  f'{"is" if len(elements_tuple) == 2 else "are"} filled.' \
                  f'\nPlease, fill the missing data or delete values for {other_elements_str}'
        print(message)
        return (0, (elements_names[index], message))
    else:
        return (1, (None, None))


# function abs mandatory verification: one field
def abs_mandatory_one_field(field_value, field_name):
    if not field_value:
        print(f'focus on {field_name}')
        message = f'{field_name} is mandatory.\nPlease, fill the missing data'
        print(message)
        return (0, (field_name, message))
    else:
        return (1, (None, None))


# function country code verification
def country_code_verification(label, street, postal_code, city, region, country_code, country_code_field_name):
    if (bool(label) or bool(street) or bool(postal_code) or bool(city) or bool(region)) and not country_code:
        print(f'focus on {country_code_field_name}')
        message = 'Country code is mandatory.\nPlease, fill the missing data'
        print(message)
        return (0, (country_code_field_name, message))
    else:
        return (1, (None, None))


# address verification
def address_data_verification(address_1_label, address_1_street, address_1_postal_code, address_1_city,
                              address_1_region, address_1_country_code):
    there_is_a_message = 0
    # data together: address_street & address_postal_code & address_city
    verification_result = data_together_verification((address_1_street, address_1_postal_code, address_1_city),
                                                     ('street', 'postal code', 'city'))
    verification_Ok = verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # ABS mandatory: address_country_code
    # 1
    verification_result = country_code_verification(address_1_label, address_1_street, address_1_postal_code,
                                                    address_1_city, address_1_region, address_1_country_code,
                                                    'country code')
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    if verification_Ok:
        return (verification_Ok, (None, None))
    else:
        return (verification_Ok, (focus_element, message))


# addresses verification
def all_addresses_verification(address_1_label, address_1_street, address_1_postal_code,
                               address_1_city, address_1_region, address_1_country_code,
                               address_2_label, address_2_street, address_2_postal_code,
                               address_2_city, address_2_region, address_2_country_code,
                               address_3_label, address_3_street, address_3_postal_code,
                               address_3_city, address_3_region, address_3_country_code):
    there_is_a_message = 0
    # 1
    verification_result = address_data_verification(address_1_label, address_1_street, address_1_postal_code,
                                                    address_1_city, address_1_region, address_1_country_code)
    verification_Ok = verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # 2
    verification_result = address_data_verification(address_2_label, address_2_street, address_2_postal_code,
                                                    address_2_city, address_2_region, address_2_country_code)
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # 3
    verification_result = address_data_verification(address_3_label, address_3_street, address_3_postal_code,
                                                    address_3_city, address_3_region, address_3_country_code)
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    if verification_Ok:
        return (1, (None, None))
    else:
        return (0, (focus_element, message))


# global data verification
def global_data_verification(acronym, name, description, comments,
                             organization_1_acronym, organization_1_name,
                             organization_2_acronym, organization_2_name,
                             organization_3_acronym, organization_3_name,
                             organization_4_acronym, organization_4_name,
                             address_1_label, address_1_street, address_1_postal_code, address_1_city,
                             address_1_region, address_1_country_code,
                             address_2_label, address_2_street, address_2_postal_code, address_2_city,
                             address_2_region, address_2_country_code,
                             address_3_label, address_3_street, address_3_postal_code, address_3_city,
                             address_3_region, address_3_country_code,
                             date_begin, date_end,
                             link_1_name, link_1_url, link_2_name, link_2_url,
                             link_3_name, link_3_url, link_4_name, link_4_url,
                             link_5_name, link_5_url):
    there_is_a_message = 0
    # data types: no special data types
    # ABS mandatory
    # ABS mandatory: acronym
    verification_result = abs_mandatory_one_field(acronym, 'acronym')
    verification_Ok = verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # ABS mandatory: name
    verification_result = abs_mandatory_one_field(name, 'name')
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # ABS mandatory: at least 1 address
    if not (bool(address_1_country_code) or bool(address_2_country_code) or bool(address_3_country_code)):
        verification_Ok = 0
        if there_is_a_message == 0:
            there_is_a_message = 1
            focus_element = 'btn_address'
            message = 'At least one address is mandatory.\nPlease, fill the missing data'
            print(message)
    # data together: organization_acronym & organization_name
    # 1
    verification_result = data_together_verification((organization_1_acronym, organization_1_name),
                                                     ('acronym of organization 1', 'name of organization 1'))
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # 2
    verification_result = data_together_verification((organization_2_acronym, organization_2_name),
                                                     ('acronym of organization 2', 'name of organization 2'))
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # 3
    verification_result = data_together_verification((organization_3_acronym, organization_3_name),
                                                     ('acronym of organization 3', 'name of organization 3'))
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # 4
    verification_result = data_together_verification((organization_4_acronym, organization_4_name),
                                                     ('acronym of organization 4', 'name of organization 4'))
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # data together: link_name & link_url
    # 1
    verification_result = data_together_verification((link_1_name, link_1_url),
                                                     ('name of link 1', 'URL of link 1'))
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # 2
    verification_result = data_together_verification((link_2_name, link_2_url),
                                                     ('name of link 2', 'URL of link 2'))
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # 3
    verification_result = data_together_verification((link_3_name, link_3_url),
                                                     ('name of link 3', 'URL of link 3'))
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # 4
    verification_result = data_together_verification((link_4_name, link_4_url),
                                                     ('name of link 4', 'URL of link 4'))
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # 5
    verification_result = data_together_verification((link_5_name, link_5_url),
                                                     ('name of link 5', 'URL of link 5'))
    verification_Ok = verification_Ok and verification_result[0]
    if not verification_result[0] and there_is_a_message == 0:
        there_is_a_message = 1
        focus_element = verification_result[1][0]
        message = verification_result[1][1]
    # mandatory: organizations, address_street, address_postal_code, address_city, 1 link - do nothing, fill NULL
    if verification_Ok:
        return (verification_Ok, (None, None))
    else:
        return (verification_Ok, (focus_element, message))


# function to fill a child element with a given value
def simple_child_action(child_element, its_value):
    child_element.clear()
    if accent_letters_replace(its_value) == its_value:
        child_element.text = its_value
    else:
        child_element.text = etree.CDATA(its_value)


# function to add children to a given parent
def add_child_action(parent_element, sub_parent_name, children_tuple):
    # children_tuple structure: [0] child_name_str, [1] child_value, [2] child_special_value, [3] child_replace_value
    big_child_element = etree.SubElement(parent_element, sub_parent_name)
    for element in children_tuple:
        child_element = etree.SubElement(big_child_element, element[0])
        if element[2] == element[1]:
            child_element.text = element[3]
            if element[2] == "other":
                add_comment(child_element, " %%% TO VERIFY")
        else:
            if accent_letters_replace(element[1]) != element[1]:
                child_element.text = etree.CDATA(element[1])
            else:
                child_element.text = element[1]


# function to add a comment
def add_comment(child_element, comment_text):
    comment_verify = etree.Comment(comment_text)
    child_element.insert(0, comment_verify)


# function to add a given organization tag
def organization_fill_function(already_one_filled, child, organization_acronym, organization_name):
    if already_one_filled:
        add_child_action(child, 'organization', (('acronym', organization_acronym, 'none', 'none'),
                                                 ('name', organization_name, 'none', 'none')))
    else:
        for item in child.iter():
            if item.tag == "{http://sshade.eu/schema/import}organization":
                for inner_item in item.iter():
                    if inner_item.tag == "{http://sshade.eu/schema/import}acronym":
                        simple_child_action(inner_item, organization_acronym)
                        already_one_filled = 1
                    if inner_item.tag == "{http://sshade.eu/schema/import}name":
                        simple_child_action(inner_item, organization_name)
    return already_one_filled


# function to add a given address tag
def address_fill_function(already_one_filled, child, address_label, address_street, address_postal_code,
                          address_city, address_region, address_country_code):
    if already_one_filled:
        add_child_action(child, 'address', (('label', address_label, 'none', 'none'),
                                            ('street', address_street, '', 'NULL'),
                                            ('postal_code', address_postal_code, '', 'NULL'),
                                            ('city', address_city, '', 'NULL'),
                                            ('region', address_region, 'none', 'none'),
                                            ('country_code', address_country_code, 'other', 'other')))
    else:
        for item in child.iter():
            if item.tag == "{http://sshade.eu/schema/import}address":
                for inner_item in item.iter():
                    if inner_item.tag == "{http://sshade.eu/schema/import}label":
                        simple_child_action(inner_item, address_label)
                    if inner_item.tag == "{http://sshade.eu/schema/import}street":
                        if address_street == '':
                            simple_child_action(inner_item, 'NULL')
                        else:
                            simple_child_action(inner_item, address_street)
                    if inner_item.tag == "{http://sshade.eu/schema/import}postal_code":
                        if address_postal_code == '':
                            simple_child_action(inner_item, 'NULL')
                        else:
                            simple_child_action(inner_item, address_postal_code)
                    if inner_item.tag == "{http://sshade.eu/schema/import}city":
                        if address_city == '':
                            simple_child_action(inner_item, 'NULL')
                        else:
                            simple_child_action(inner_item, address_city)
                    if inner_item.tag == "{http://sshade.eu/schema/import}region":
                        simple_child_action(inner_item, address_region)
                    if inner_item.tag == "{http://sshade.eu/schema/import}country_code":
                        simple_child_action(inner_item, address_country_code)
                        if address_country_code == "other":
                            add_comment(inner_item, " %%% TO VERIFY ")
                        already_one_filled = 1
    return already_one_filled


# function to add a given link tag
def link_fill_function(already_one_filled, child, link_name, link_url):
    if already_one_filled:
        add_child_action(child, 'link', (('name', link_name, 'none', 'none'),
                                         ('url', link_url, 'none', 'none')))
    else:
        for item in child.iter():
            if item.tag == "{http://sshade.eu/schema/import}link":
                for inner_item in item.iter():
                    if inner_item.tag == "{http://sshade.eu/schema/import}name":
                        simple_child_action(inner_item, link_name)
                        already_one_filled = 1
                    if inner_item.tag == "{http://sshade.eu/schema/import}url":
                        simple_child_action(inner_item, link_url)
    return already_one_filled


# function to parse & fill the template
def xml_parse_and_fill(template, acronym, name, description, comments, organization_1_acronym, organization_1_name,
                       organization_2_acronym, organization_2_name, organization_3_acronym, organization_3_name,
                       organization_4_acronym, organization_4_name, address_1_label, address_1_street,
                       address_1_postal_code, address_1_city, address_1_region, address_1_country_code, address_2_label,
                       address_2_street, address_2_postal_code, address_2_city, address_2_region,
                       address_2_country_code, address_3_label, address_3_street, address_3_postal_code,
                       address_3_city, address_3_region, address_3_country_code, date_begin, date_end, link_1_name,
                       link_1_url, link_2_name, link_2_url, link_3_name, link_3_url, link_4_name, link_4_url,
                       link_5_name, link_5_url):
    # quantification
    organizations_qty = int(bool(organization_1_acronym)) + int(bool(organization_2_acronym)) + \
                        int(bool(organization_3_acronym)) + int(bool(organization_4_acronym))
    links_qty = int(bool(link_1_url)) + int(bool(link_2_url)) + int(bool(link_3_url))
    # parse & fill
    parser = etree.XMLParser(remove_blank_text=True)
    xml_root = etree.fromstring(template.encode("utf8"), parser)
    for child in xml_root.find("{http://sshade.eu/schema/import}laboratory").getchildren():
        # UID
        if child.tag == "{http://sshade.eu/schema/import}uid":
            simple_child_action(child,
                                "LAB_" + accent_letters_replace(acronym.strip()).upper().replace("-", "_").
                                replace(" ", "_"))
            add_comment(child, " %%% TO VERIFY ")
        # acronym
        if child.tag == "{http://sshade.eu/schema/import}acronym":
            simple_child_action(child, acronym)
        # name
        if child.tag == "{http://sshade.eu/schema/import}name":
            if name != '':
                simple_child_action(child, name)
            else:
                simple_child_action(child, 'NULL')
        # description
        if child.tag == "{http://sshade.eu/schema/import}description":
            simple_child_action(child, description)
        # organizations
        if child.tag == "{http://sshade.eu/schema/import}organizations":
            # there is no organizations
            if organizations_qty == 0:
                for item in child.iter():
                    if item.tag == "{http://sshade.eu/schema/import}organization":
                        for inner_item in item.iter():
                            if inner_item.tag == "{http://sshade.eu/schema/import}acronym":
                                simple_child_action(inner_item, 'NULL')
                            if inner_item.tag == "{http://sshade.eu/schema/import}name":
                                simple_child_action(inner_item, 'NULL')
            # there is one or more organizations
            else:
                already_one_filled = 0
                # 1
                if organization_1_acronym != "":
                    already_one_filled = organization_fill_function(already_one_filled, child,
                                                                    organization_1_acronym, organization_1_name)
                # 2
                if organization_2_acronym != "":
                    already_one_filled = organization_fill_function(already_one_filled, child,
                                                                    organization_2_acronym, organization_2_name)
                # 3
                if organization_3_acronym != "":
                    already_one_filled = organization_fill_function(already_one_filled, child,
                                                                    organization_3_acronym, organization_3_name)
                # 4
                if organization_4_acronym != "":
                    already_one_filled = organization_fill_function(already_one_filled, child,
                                                                    organization_4_acronym, organization_4_name)
        # addresses
        if child.tag == "{http://sshade.eu/schema/import}addresses":
            already_one_filled = 0
            # 1
            if address_1_country_code != "":
                already_one_filled = address_fill_function(already_one_filled, child, address_1_label,
                                                           address_1_street, address_1_postal_code,
                                                           address_1_city, address_1_region, address_1_country_code)
            # 2
            if address_2_country_code != "":
                already_one_filled = address_fill_function(already_one_filled, child, address_2_label,
                                                           address_2_street, address_2_postal_code,
                                                           address_2_city, address_2_region, address_2_country_code)
            # 3
            if address_3_country_code != "":
                already_one_filled = address_fill_function(already_one_filled, child, address_3_label,
                                                           address_3_street, address_3_postal_code,
                                                           address_3_city, address_3_region, address_3_country_code)
        # date_begin
        if child.tag == "{http://sshade.eu/schema/import}date_begin":
            simple_child_action(child, date_begin)
        # date_end
        if child.tag == "{http://sshade.eu/schema/import}date_end":
            simple_child_action(child, date_end)
        # links
        if child.tag == "{http://sshade.eu/schema/import}links":
            # there is no links
            if links_qty == 0:
                for item in child.iter():
                    if item.tag == "{http://sshade.eu/schema/import}link":
                        for inner_item in item.iter():
                            if inner_item.tag == "{http://sshade.eu/schema/import}name":
                                simple_child_action(inner_item, 'NULL')
                            if inner_item.tag == "{http://sshade.eu/schema/import}url":
                                simple_child_action(inner_item, 'NULL')
            # there is one or more link(s)
            else:
                already_one_filled = 0
                # 1
                if link_1_url != "":
                    already_one_filled = link_fill_function(already_one_filled, child, link_1_name, link_1_url)
                # 2
                if link_2_url != "":
                    already_one_filled = link_fill_function(already_one_filled, child, link_2_name, link_2_url)
                # 3
                if link_3_url != "":
                    already_one_filled = link_fill_function(already_one_filled, child, link_3_name, link_3_url)
                # 4
                if link_4_url != "":
                    already_one_filled = link_fill_function(already_one_filled, child, link_4_name, link_4_url)
                # 5
                if link_5_url != "":
                    already_one_filled = link_fill_function(already_one_filled, child, link_5_name, link_5_url)
        # comments
        if child.tag == "{http://sshade.eu/schema/import}comments":
            simple_child_action(child, comments)
    # from xml to byte
    str_to_upload = etree.tostring(xml_root, pretty_print=True, encoding="utf-8",
                                   xml_declaration=True, method="xml")
    return str_to_upload


def demo_F():
    # INPUTS
    # acronym, name, description, comments
    acronym = "FULL"
    name = "institut d'planeto et d'astro des montagnes"
    description = "In planetary sciences, IPAG studies planetary surfaces and subsurfaces, " \
                  "small bodies in the solar system, and the chemical evolution of primitive " \
                  "matter, as well as Sun-Earth interactions. IPAG also addresses stellar " \
                  "and planetary formation, from the initial phases of the core collapse " \
                  "where molecular complexity builds up, to the circumstellar disk physics " \
                  "and chemistry and planets formation.  IPAG also works on the physical " \
                  "processes implied in accretion-ejection phenomena around young stellar " \
                  "objects and compact objects where high energy and relativistic effects " \
                  "are involved."
    comments = "IPAG is the result of the merging of LPG and LAOG in January 2011. Postal address: IPAG, " \
               "UGA, CS 40700, F-38058 Grenoble Cédex 9, France"
    # organizations
    organization_1_acronym = "UGA"
    organization_1_name = "Université Grenoble Alpes"
    organization_2_acronym = "CNRS"
    organization_2_name = "Centre National de la Recherche Scientifique"  # field up to 100 chars!
    organization_3_acronym = ""
    organization_3_name = ""
    organization_4_acronym = "bla"
    organization_4_name = "bla-bla"
    # addresses
    address_1_label = ""
    address_1_street = "122-124 rue de la Piscine"
    address_1_postal_code = "38400"
    address_1_city = "Saint-Martin-d'Heres"
    address_1_region = ""
    address_1_country_code = "FR"
    address_2_label = "Bâtiments OSUG D"
    address_2_street = ""
    address_2_postal_code = ""
    address_2_city = ""
    address_2_region = "Rhône-Alpes d'Alpes"
    address_2_country_code = "FR"
    address_3_label = "Bâtiments PhITEM D"
    address_3_street = "122-124 rue de la Piscine"
    address_3_postal_code = "38400"
    address_3_city = "Saint-Martin-d'Heres"
    address_3_region = "Rhône-Alpes d'Alpes"
    address_3_country_code = "FR"
    # history
    date_begin = "2011-01-01"
    date_end = "2019-01-01"
    # links
    link_1_name = "IPAG web page 1"
    link_1_url = "http://ipag.osug.fr/"
    link_2_name = "IPAG web page 2"
    link_2_url = "http://ipag.osug.fr/"
    link_3_name = ""
    link_3_url = ""
    link_4_name = ""
    link_4_url = ""
    link_5_name = "dgd"
    link_5_url = "ss"

    # input verification
    verification_Ok = all_addresses_verification(address_1_label, address_1_street, address_1_postal_code,
                                                 address_1_city, address_1_region, address_1_country_code,
                                                 address_2_label, address_2_street, address_2_postal_code,
                                                 address_2_city, address_2_region, address_2_country_code,
                                                 address_3_label, address_3_street, address_3_postal_code,
                                                 address_3_city, address_3_region, address_3_country_code)[0]
    verification_Ok = verification_Ok and global_data_verification(acronym, name, description, comments,
                                                                   organization_1_acronym, organization_1_name,
                                                                   organization_2_acronym, organization_2_name,
                                                                   organization_3_acronym, organization_3_name,
                                                                   organization_4_acronym, organization_4_name,
                                                                   address_1_label, address_1_street,
                                                                   address_1_postal_code, address_1_city, address_1_region,
                                                                   address_1_country_code, address_2_label,
                                                                   address_2_street, address_2_postal_code,
                                                                   address_2_city, address_2_region,
                                                                   address_2_country_code, address_3_label,
                                                                   address_3_street, address_3_postal_code,
                                                                   address_3_city, address_3_region,
                                                                   address_3_country_code, date_begin, date_end,
                                                                   link_1_name, link_1_url, link_2_name, link_2_url,
                                                                   link_3_name, link_3_url, link_4_name, link_4_url,
                                                                   link_5_name, link_5_url)[0]
    # template filling
    if verification_Ok:
        # parsing & filling
        str_to_upload = xml_parse_and_fill(template, acronym, name, description, comments, organization_1_acronym,
                                           organization_1_name, organization_2_acronym, organization_2_name,
                                           organization_3_acronym, organization_3_name, organization_4_acronym,
                                           organization_4_name, address_1_label, address_1_street, address_1_postal_code,
                                           address_1_city, address_1_region, address_1_country_code, address_2_label,
                                           address_2_street, address_2_postal_code, address_2_city, address_2_region,
                                           address_2_country_code, address_3_label, address_3_street, address_3_postal_code,
                                           address_3_city, address_3_region, address_3_country_code, date_begin, date_end,
                                           link_1_name, link_1_url, link_2_name, link_2_url, link_3_name, link_3_url,
                                           link_4_name, link_4_url, link_5_name, link_5_url)
        # xml file saving
        file_name = f"laboratory_{acronym.strip()}.xml"
        if file_name:
            with open(file_name, 'wb') as file_output:
                file_output.write(str_to_upload)

#demo_F()