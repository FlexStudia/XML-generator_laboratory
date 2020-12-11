# coding: utf-8

# IMPORTS
import pytest
import XMLgenerator_laboratory

# GLOBALS
text_array = ['test', 'TeST', 'téSt', 'T-éSt test', '']
url_array = ['http://ipag.osug.fr/', '']
data_array = ['2011-01-01', '']

acronym = "FuLL"
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


# tests of FUNCTIONS
def test_data_together_verification():
    for element1 in text_array:
        for element2 in text_array:
            if (element1 != '' and element2 == '') or (element1 == '' and element2 != ''):
                assert XMLgenerator_laboratory.data_together_verification((element1, element2),
                                                                          ('element1', 'element2'))[0] == 0, \
                    f"test failed for the elements: {element1}, {element2}"
            else:
                assert XMLgenerator_laboratory.data_together_verification((element1, element2),
                                                                          ('element1', 'element2'))[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}"


def test_abs_mandatory_one_field():
    for element in text_array:
        if element == '':
            assert XMLgenerator_laboratory.abs_mandatory_one_field(element, 'element')[0] == 0, \
                f"test failed for the element: {element}"
        else:
            assert XMLgenerator_laboratory.abs_mandatory_one_field(element, 'element')[0] == 1, \
                f"test failed for the element: {element}"


def test_country_code_verification():
    for element1 in text_array:
        for element2 in text_array:
            for element3 in text_array:
                for element4 in text_array:
                    for element5 in text_array:
                        for element6 in text_array:
                            if (bool(element1) or bool(element2) or bool(element3) or bool(element4) or bool(
                                    element5)) and not element6:
                                assert XMLgenerator_laboratory.country_code_verification(element1, element2,
                                                                                         element3, element4,
                                                                                         element5, element6,
                                                                                         'element')[0] == 0, \
                                    f"test failed for the elements: {element1}, {element2}, {element3}, " \
                                    f"{element4}, {element5}, {element6}"
                            else:
                                assert XMLgenerator_laboratory.country_code_verification(element1, element2,
                                                                                         element3, element4,
                                                                                         element5, element6,
                                                                                         'element')[0] == 1, \
                                    f"test failed for the elements: {element1}, {element2}, {element3}, " \
                                    f"{element4}, {element5}, {element6}"


def test_address_data_verification():
    # street, postal code & city 1
    for element1 in text_array:
        for element2 in text_array:
            for element3 in text_array:
                if not (bool(element1) and bool(element2) and bool(element3)) and (
                        bool(element1) or bool(element2) or bool(element3)):
                    assert XMLgenerator_laboratory.address_data_verification(address_1_label, element1, element2,
                                                                             element3, address_1_region,
                                                                             address_1_country_code)[0] == 0, \
                        f"test failed for the elements: {element1}, {element2}, {element3}"
                else:
                    assert XMLgenerator_laboratory.address_data_verification(address_1_label, element1, element2,
                                                                             element3, address_1_region,
                                                                             address_1_country_code)[0] == 1, \
                        f"test failed for the elements: {element1}, {element2}, {element3}"
    # street, postal code & city 2
    for element1 in text_array:
        for element2 in text_array:
            for element3 in text_array:
                if not (bool(element1) and bool(element2) and bool(element3)) and (
                        bool(element1) or bool(element2) or bool(element3)):
                    assert XMLgenerator_laboratory.address_data_verification(address_2_label, element1, element2,
                                                                             element3, address_2_region,
                                                                             address_2_country_code)[0] == 0, \
                        f"test failed for the elements: {element1}, {element2}, {element3}"
                else:
                    assert XMLgenerator_laboratory.address_data_verification(address_2_label, element1, element2,
                                                                             element3, address_2_region,
                                                                             address_2_country_code)[0] == 1, \
                        f"test failed for the elements: {element1}, {element2}, {element3}"
    # street, postal code & city 3
    for element1 in text_array:
        for element2 in text_array:
            for element3 in text_array:
                if not (bool(element1) and bool(element2) and bool(element3)) and (
                        bool(element1) or bool(element2) or bool(element3)):
                    assert XMLgenerator_laboratory.address_data_verification(address_3_label, element1, element2,
                                                                             element3, address_3_region,
                                                                             address_3_country_code)[0] == 0, \
                        f"test failed for the elements: {element1}, {element2}, {element3}"
                else:
                    assert XMLgenerator_laboratory.address_data_verification(address_3_label, element1, element2,
                                                                             element3, address_3_region,
                                                                             address_3_country_code)[0] == 1, \
                        f"test failed for the elements: {element1}, {element2}, {element3}"
    # country code 1
    for element1 in text_array:
        if element1 == '':
            assert XMLgenerator_laboratory.address_data_verification(address_1_label, address_1_street,
                                                                     address_1_postal_code, address_1_city,
                                                                     address_1_region, element1)[0] == 0, \
                f"test failed for the elements: {element1}"
        else:
            assert XMLgenerator_laboratory.address_data_verification(address_1_label, address_1_street,
                                                                     address_1_postal_code, address_1_city,
                                                                     address_1_region, element1)[0] == 1, \
                f"test failed for the elements: {element1}"
    # country code 2
    for element1 in text_array:
        if element1 == '':
            assert XMLgenerator_laboratory.address_data_verification(address_2_label, address_2_street,
                                                                     address_2_postal_code, address_2_city,
                                                                     address_2_region, element1)[0] == 0, \
                f"test failed for the elements: {element1}"
        else:
            assert XMLgenerator_laboratory.address_data_verification(address_2_label, address_2_street,
                                                                     address_2_postal_code, address_2_city,
                                                                     address_2_region, element1)[0] == 1, \
                f"test failed for the elements: {element1}"
    # country code 3
    for element1 in text_array:
        if element1 == '':
            assert XMLgenerator_laboratory.address_data_verification(address_3_label, address_3_street,
                                                                     address_3_postal_code, address_3_city,
                                                                     address_3_region, element1)[0] == 0, \
                f"test failed for the elements: {element1}"
        else:
            assert XMLgenerator_laboratory.address_data_verification(address_3_label, address_3_street,
                                                                     address_3_postal_code, address_3_city,
                                                                     address_3_region, element1)[0] == 1, \
                f"test failed for the elements: {element1}"


def test_global_data_verification():
    # organization 1
    for element1 in text_array:
        for element2 in text_array:
            if (element1 != '' and element2 == '') or (element1 == '' and element2 != ''):
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        element1, element2,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 0, \
                    f"test failed for the elements: {element1}, {element2}"
            else:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        element1, element2,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}"
    # organization 2
    for element1 in text_array:
        for element2 in text_array:
            if (element1 != '' and element2 == '') or (element1 == '' and element2 != ''):
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        element1, element2,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 0, \
                    f"test failed for the elements: {element1}, {element2}"
            else:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        element1, element2,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}"
    # organization 3
    for element1 in text_array:
        for element2 in text_array:
            if (element1 != '' and element2 == '') or (element1 == '' and element2 != ''):
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        element1, element2,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 0, \
                    f"test failed for the elements: {element1}, {element2}"
            else:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        element1, element2,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}"
    # organization 4
    for element1 in text_array:
        for element2 in text_array:
            if (element1 != '' and element2 == '') or (element1 == '' and element2 != ''):
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym,
                                                                        organization_1_name,
                                                                        organization_2_acronym,
                                                                        organization_2_name,
                                                                        organization_3_acronym,
                                                                        organization_3_name,
                                                                        element1, element2,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region,
                                                                        address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region,
                                                                        address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region,
                                                                        address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 0, \
                    f"test failed for the elements: {element1}, {element2}"
            else:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym,
                                                                        organization_1_name,
                                                                        organization_2_acronym,
                                                                        organization_2_name,
                                                                        organization_3_acronym,
                                                                        organization_3_name,
                                                                        element1, element2,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region,
                                                                        address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region,
                                                                        address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region,
                                                                        address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}"
    # street, postal code & city 1
    for element1 in text_array:
        for element2 in text_array:
            for element3 in text_array:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, element1, element2,
                                                                        element3,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}, {element3}"
    # street, postal code & city 2
    for element1 in text_array:
        for element2 in text_array:
            for element3 in text_array:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, element1, element2,
                                                                        element3,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}, {element3}"
    # street, postal code & city 3
    for element1 in text_array:
        for element2 in text_array:
            for element3 in text_array:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, element1, element2,
                                                                        element3,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}, {element3}"
    # link 1
    for element1 in text_array:
        for element2 in text_array:
            if not (bool(element1) and bool(element2)) and (bool(element1) or bool(element2)):
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        element1, element2, link_2_name, link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 0, \
                    f"test failed for the elements: {element1}, {element2}"
            else:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        element1, element2, link_2_name, link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}"
    # link 2
    for element1 in text_array:
        for element2 in text_array:
            if not (bool(element1) and bool(element2)) and (bool(element1) or bool(element2)):
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, element1, element2,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 0, \
                    f"test failed for the elements: {element1}, {element2}"
            else:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, element1, element2,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        link_5_name, link_5_url)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}"
    # link 3
    for element1 in text_array:
        for element2 in text_array:
            if not (bool(element1) and bool(element2)) and (bool(element1) or bool(element2)):
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        element1, element2, link_4_name, link_4_url,
                                                                        link_5_name, link_5_url)[0] == 0, \
                    f"test failed for the elements: {element1}, {element2}"
            else:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        element1, element2, link_4_name, link_4_url,
                                                                        link_5_name, link_5_url)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}"
    # link 4
    for element1 in text_array:
        for element2 in text_array:
            if not (bool(element1) and bool(element2)) and (bool(element1) or bool(element2)):
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, element1, element2,
                                                                        link_5_name, link_5_url)[0] == 0, \
                    f"test failed for the elements: {element1}, {element2}"
            else:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, element1, element2,
                                                                        link_5_name, link_5_url)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}"
    # link 5
    for element1 in text_array:
        for element2 in text_array:
            if not (bool(element1) and bool(element2)) and (bool(element1) or bool(element2)):
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        element1, element2)[0] == 0, \
                    f"test failed for the elements: {element1}, {element2}"
            else:
                assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                        organization_1_acronym, organization_1_name,
                                                                        organization_2_acronym, organization_2_name,
                                                                        organization_3_acronym, organization_3_name,
                                                                        organization_4_acronym, organization_4_name,
                                                                        address_1_label, address_1_street,
                                                                        address_1_postal_code, address_1_city,
                                                                        address_1_region, address_1_country_code,
                                                                        address_2_label, address_2_street,
                                                                        address_2_postal_code, address_2_city,
                                                                        address_2_region, address_2_country_code,
                                                                        address_3_label, address_3_street,
                                                                        address_3_postal_code, address_3_city,
                                                                        address_3_region, address_3_country_code,
                                                                        date_begin, date_end,
                                                                        link_1_name, link_1_url, link_2_name,
                                                                        link_2_url,
                                                                        link_3_name, link_3_url, link_4_name,
                                                                        link_4_url,
                                                                        element1, element2)[0] == 1, \
                    f"test failed for the elements: {element1}, {element2}"
    # acronym
    for element1 in text_array:
        if element1 == '':
            assert XMLgenerator_laboratory.global_data_verification(element1, name, description, comments,
                                                                    organization_1_acronym, organization_1_name,
                                                                    organization_2_acronym, organization_2_name,
                                                                    organization_3_acronym, organization_3_name,
                                                                    organization_4_acronym, organization_4_name,
                                                                    address_1_label, address_1_street,
                                                                    address_1_postal_code, address_1_city,
                                                                    address_1_region, address_1_country_code,
                                                                    address_2_label, address_2_street,
                                                                    address_2_postal_code, address_2_city,
                                                                    address_2_region, address_2_country_code,
                                                                    address_3_label, address_3_street,
                                                                    address_3_postal_code, address_3_city,
                                                                    address_3_region, address_3_country_code,
                                                                    date_begin, date_end,
                                                                    link_1_name, link_1_url, link_2_name, link_2_url,
                                                                    link_3_name, link_3_url, link_4_name, link_4_url,
                                                                    link_5_name, link_5_url)[0] == 0, \
                f"test failed for the elements: {element1}"
        else:
            assert XMLgenerator_laboratory.global_data_verification(element1, name, description, comments,
                                                                    organization_1_acronym, organization_1_name,
                                                                    organization_2_acronym, organization_2_name,
                                                                    organization_3_acronym, organization_3_name,
                                                                    organization_4_acronym, organization_4_name,
                                                                    address_1_label, address_1_street,
                                                                    address_1_postal_code, address_1_city,
                                                                    address_1_region, address_1_country_code,
                                                                    address_2_label, address_2_street,
                                                                    address_2_postal_code, address_2_city,
                                                                    address_2_region, address_2_country_code,
                                                                    address_3_label, address_3_street,
                                                                    address_3_postal_code, address_3_city,
                                                                    address_3_region, address_3_country_code,
                                                                    date_begin, date_end,
                                                                    link_1_name, link_1_url, link_2_name, link_2_url,
                                                                    link_3_name, link_3_url, link_4_name, link_4_url,
                                                                    link_5_name, link_5_url)[0] == 1, \
                f"test failed for the elements: {element1}"
    # name
    for element1 in text_array:
        if element1 == '':
            assert XMLgenerator_laboratory.global_data_verification(acronym, element1, description, comments,
                                                                    organization_1_acronym, organization_1_name,
                                                                    organization_2_acronym, organization_2_name,
                                                                    organization_3_acronym, organization_3_name,
                                                                    organization_4_acronym, organization_4_name,
                                                                    address_1_label, address_1_street,
                                                                    address_1_postal_code, address_1_city,
                                                                    address_1_region, address_1_country_code,
                                                                    address_2_label, address_2_street,
                                                                    address_2_postal_code, address_2_city,
                                                                    address_2_region, address_2_country_code,
                                                                    address_3_label, address_3_street,
                                                                    address_3_postal_code, address_3_city,
                                                                    address_3_region, address_3_country_code,
                                                                    date_begin, date_end,
                                                                    link_1_name, link_1_url, link_2_name, link_2_url,
                                                                    link_3_name, link_3_url, link_4_name, link_4_url,
                                                                    link_5_name, link_5_url)[0] == 0, \
                f"test failed for the elements: {element1}"
        else:
            assert XMLgenerator_laboratory.global_data_verification(acronym, element1, description, comments,
                                                                    organization_1_acronym, organization_1_name,
                                                                    organization_2_acronym, organization_2_name,
                                                                    organization_3_acronym, organization_3_name,
                                                                    organization_4_acronym, organization_4_name,
                                                                    address_1_label, address_1_street,
                                                                    address_1_postal_code, address_1_city,
                                                                    address_1_region, address_1_country_code,
                                                                    address_2_label, address_2_street,
                                                                    address_2_postal_code, address_2_city,
                                                                    address_2_region, address_2_country_code,
                                                                    address_3_label, address_3_street,
                                                                    address_3_postal_code, address_3_city,
                                                                    address_3_region, address_3_country_code,
                                                                    date_begin, date_end,
                                                                    link_1_name, link_1_url, link_2_name, link_2_url,
                                                                    link_3_name, link_3_url, link_4_name, link_4_url,
                                                                    link_5_name, link_5_url)[0] == 1, \
                f"test failed for the elements: {element1}"
    # at least 1 address
    for element1 in text_array:
        for element2 in text_array:
            for element3 in text_array:
                if not (bool(element1) or bool(element2) or bool(element3)):
                    assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                            organization_1_acronym, organization_1_name,
                                                                            organization_2_acronym, organization_2_name,
                                                                            organization_3_acronym, organization_3_name,
                                                                            organization_4_acronym, organization_4_name,
                                                                            address_1_label, address_1_street,
                                                                            address_1_postal_code, address_1_city,
                                                                            address_1_region, element1,
                                                                            address_2_label, address_2_street,
                                                                            address_2_postal_code, address_2_city,
                                                                            address_2_region, element2,
                                                                            address_3_label, address_3_street,
                                                                            address_3_postal_code, address_3_city,
                                                                            address_3_region, element3,
                                                                            date_begin, date_end,
                                                                            link_1_name, link_1_url, link_2_name,
                                                                            link_2_url,
                                                                            link_3_name, link_3_url, link_4_name,
                                                                            link_4_url,
                                                                            link_5_name, link_5_url)[0] == 0, \
                        f"test failed for the elements: {element1}, {element2}, {element3}"
    # description
    for element1 in text_array:
        assert XMLgenerator_laboratory.global_data_verification(acronym, name, element1, comments,
                                                                organization_1_acronym, organization_1_name,
                                                                organization_2_acronym, organization_2_name,
                                                                organization_3_acronym, organization_3_name,
                                                                organization_4_acronym, organization_4_name,
                                                                address_1_label, address_1_street,
                                                                address_1_postal_code, address_1_city,
                                                                address_1_region, address_1_country_code,
                                                                address_2_label, address_2_street,
                                                                address_2_postal_code, address_2_city,
                                                                address_2_region, address_2_country_code,
                                                                address_3_label, address_3_street,
                                                                address_3_postal_code, address_3_city,
                                                                address_3_region, address_3_country_code,
                                                                date_begin, date_end,
                                                                link_1_name, link_1_url, link_2_name, link_2_url,
                                                                link_3_name, link_3_url, link_4_name, link_4_url,
                                                                link_5_name, link_5_url)[0] == 1, \
            f"test failed for the elements: {element1}"
    # comments
    for element1 in text_array:
        assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, element1,
                                                                organization_1_acronym, organization_1_name,
                                                                organization_2_acronym, organization_2_name,
                                                                organization_3_acronym, organization_3_name,
                                                                organization_4_acronym, organization_4_name,
                                                                address_1_label, address_1_street,
                                                                address_1_postal_code, address_1_city,
                                                                address_1_region, address_1_country_code,
                                                                address_2_label, address_2_street,
                                                                address_2_postal_code, address_2_city,
                                                                address_2_region, address_2_country_code,
                                                                address_3_label, address_3_street,
                                                                address_3_postal_code, address_3_city,
                                                                address_3_region, address_3_country_code,
                                                                date_begin, date_end,
                                                                link_1_name, link_1_url, link_2_name, link_2_url,
                                                                link_3_name, link_3_url, link_4_name, link_4_url,
                                                                link_5_name, link_5_url)[0] == 1, \
            f"test failed for the elements: {element1}"
    # label & region 1
    for element1 in text_array:
        for element2 in text_array:
            assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                    organization_1_acronym, organization_1_name,
                                                                    organization_2_acronym, organization_2_name,
                                                                    organization_3_acronym, organization_3_name,
                                                                    organization_4_acronym, organization_4_name,
                                                                    element1, address_1_street, address_1_postal_code,
                                                                    address_1_city,
                                                                    element2, address_1_country_code,
                                                                    address_2_label, address_2_street,
                                                                    address_2_postal_code, address_2_city,
                                                                    address_2_region, address_2_country_code,
                                                                    address_3_label, address_3_street,
                                                                    address_3_postal_code, address_3_city,
                                                                    address_3_region, address_3_country_code,
                                                                    date_begin, date_end,
                                                                    link_1_name, link_1_url, link_2_name, link_2_url,
                                                                    link_3_name, link_3_url, link_4_name, link_4_url,
                                                                    link_5_name, link_5_url)[0] == 1, \
                f"test failed for the elements: {element1}, {element2}"
    # label & region 2
    for element1 in text_array:
        for element2 in text_array:
            assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                    organization_1_acronym, organization_1_name,
                                                                    organization_2_acronym, organization_2_name,
                                                                    organization_3_acronym, organization_3_name,
                                                                    organization_4_acronym, organization_4_name,
                                                                    address_1_label, address_1_street,
                                                                    address_1_postal_code, address_1_city,
                                                                    address_1_region, address_1_country_code,
                                                                    element1, address_2_street, address_2_postal_code,
                                                                    address_2_city,
                                                                    element2, address_2_country_code,
                                                                    address_3_label, address_3_street,
                                                                    address_3_postal_code, address_3_city,
                                                                    address_3_region, address_3_country_code,
                                                                    date_begin, date_end,
                                                                    link_1_name, link_1_url, link_2_name, link_2_url,
                                                                    link_3_name, link_3_url, link_4_name, link_4_url,
                                                                    link_5_name, link_5_url)[0] == 1, \
                f"test failed for the elements: {element1}, {element2}"
    # label & region 3
    for element1 in text_array:
        for element2 in text_array:
            assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                    organization_1_acronym, organization_1_name,
                                                                    organization_2_acronym, organization_2_name,
                                                                    organization_3_acronym, organization_3_name,
                                                                    organization_4_acronym, organization_4_name,
                                                                    address_1_label, address_1_street,
                                                                    address_1_postal_code, address_1_city,
                                                                    address_1_region, address_1_country_code,
                                                                    address_2_label, address_2_street,
                                                                    address_2_postal_code, address_2_city,
                                                                    address_2_region, address_2_country_code,
                                                                    element1, address_3_street, address_3_postal_code,
                                                                    address_3_city,
                                                                    element2, address_3_country_code,
                                                                    date_begin, date_end,
                                                                    link_1_name, link_1_url, link_2_name, link_2_url,
                                                                    link_3_name, link_3_url, link_4_name, link_4_url,
                                                                    link_5_name, link_5_url)[0] == 1, \
                f"test failed for the elements: {element1}, {element2}"
    # date_begin & date_end
    for element1 in data_array:
        for element2 in data_array:
            assert XMLgenerator_laboratory.global_data_verification(acronym, name, description, comments,
                                                                    organization_1_acronym, organization_1_name,
                                                                    organization_2_acronym, organization_2_name,
                                                                    organization_3_acronym, organization_3_name,
                                                                    organization_4_acronym, organization_4_name,
                                                                    address_1_label, address_1_street,
                                                                    address_1_postal_code, address_1_city,
                                                                    address_1_region, address_1_country_code,
                                                                    address_2_label, address_2_street,
                                                                    address_2_postal_code, address_2_city,
                                                                    address_2_region, address_2_country_code,
                                                                    address_3_label, address_3_street,
                                                                    address_3_postal_code, address_3_city,
                                                                    address_3_region, address_3_country_code,
                                                                    element1, element2,
                                                                    link_1_name, link_1_url, link_2_name, link_2_url,
                                                                    link_3_name, link_3_url, link_4_name, link_4_url,
                                                                    link_5_name, link_5_url)[0] == 1, \
                f"test failed for the elements: {element1}, {element2}"


def test_xml_parse_and_fill():
    # acronym
    for element1 in text_array:
        if element1:
            str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, element1, name,
                                                                      description, comments,
                                                                      organization_1_acronym, organization_1_name,
                                                                      organization_2_acronym, organization_2_name,
                                                                      organization_3_acronym, organization_3_name,
                                                                      organization_4_acronym, organization_4_name,
                                                                      address_1_label, address_1_street,
                                                                      address_1_postal_code,
                                                                      address_1_city, address_1_region,
                                                                      address_1_country_code,
                                                                      address_2_label, address_2_street,
                                                                      address_2_postal_code,
                                                                      address_2_city, address_2_region,
                                                                      address_2_country_code,
                                                                      address_3_label, address_3_street,
                                                                      address_3_postal_code,
                                                                      address_3_city, address_3_region,
                                                                      address_3_country_code,
                                                                      date_begin, date_end,
                                                                      link_1_name, link_1_url,
                                                                      link_2_name, link_2_url,
                                                                      link_3_name, link_3_url,
                                                                      link_4_name, link_4_url,
                                                                      link_5_name, link_5_url).decode("utf-8")
            assert str_from_xml.find(
                f"<uid>{'LAB_' + XMLgenerator_laboratory.accent_letters_replace(element1.strip()).upper().replace('-', '_').replace(' ', '_')}<!-- %%% TO VERIFY --></uid>") != -1, \
                f"test failed for the element: {element1}"
    # name
    for element1 in text_array:
        str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym,
                                                                  element1, description, comments,
                                                                  organization_1_acronym, organization_1_name,
                                                                  organization_2_acronym, organization_2_name,
                                                                  organization_3_acronym, organization_3_name,
                                                                  organization_4_acronym, organization_4_name,
                                                                  address_1_label, address_1_street,
                                                                  address_1_postal_code,
                                                                  address_1_city, address_1_region,
                                                                  address_1_country_code,
                                                                  address_2_label, address_2_street,
                                                                  address_2_postal_code,
                                                                  address_2_city, address_2_region,
                                                                  address_2_country_code,
                                                                  address_3_label, address_3_street,
                                                                  address_3_postal_code,
                                                                  address_3_city, address_3_region,
                                                                  address_3_country_code,
                                                                  date_begin, date_end,
                                                                  link_1_name, link_1_url,
                                                                  link_2_name, link_2_url,
                                                                  link_3_name, link_3_url,
                                                                  link_4_name, link_4_url,
                                                                  link_5_name, link_5_url).decode("utf-8")
        if not element1:
            assert str_from_xml.find("<name>NULL</name>") != -1, f"test failed for the element: {element1}"
        elif XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
            assert str_from_xml.find(f"<name><![CDATA[{element1}]]></name>") != -1, \
                f"test failed for the element: {element1}"
        else:
            assert str_from_xml.find(f"<name>{element1}</name>") != -1, f"test failed for the element: {element1}"
    # description
    for element1 in text_array:
        str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym, name,
                                                                  element1, comments,
                                                                  organization_1_acronym, organization_1_name,
                                                                  organization_2_acronym, organization_2_name,
                                                                  organization_3_acronym, organization_3_name,
                                                                  organization_4_acronym, organization_4_name,
                                                                  address_1_label, address_1_street,
                                                                  address_1_postal_code,
                                                                  address_1_city, address_1_region,
                                                                  address_1_country_code,
                                                                  address_2_label, address_2_street,
                                                                  address_2_postal_code,
                                                                  address_2_city, address_2_region,
                                                                  address_2_country_code,
                                                                  address_3_label, address_3_street,
                                                                  address_3_postal_code,
                                                                  address_3_city, address_3_region,
                                                                  address_3_country_code,
                                                                  date_begin, date_end,
                                                                  link_1_name, link_1_url,
                                                                  link_2_name, link_2_url,
                                                                  link_3_name, link_3_url,
                                                                  link_4_name, link_4_url,
                                                                  link_5_name, link_5_url).decode("utf-8")
        if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
            assert str_from_xml.find(f"<description><![CDATA[{element1}]]></description>") != -1, \
                f"test failed for the element: {element1}"
        else:
            assert str_from_xml.find(f"<description>{element1}</description>") != -1, \
                f"test failed for the element: {element1}"
    # comments
    for element1 in text_array:
        str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym, name,
                                                                  description, element1,
                                                                  organization_1_acronym, organization_1_name,
                                                                  organization_2_acronym, organization_2_name,
                                                                  organization_3_acronym, organization_3_name,
                                                                  organization_4_acronym, organization_4_name,
                                                                  address_1_label, address_1_street,
                                                                  address_1_postal_code,
                                                                  address_1_city, address_1_region,
                                                                  address_1_country_code,
                                                                  address_2_label, address_2_street,
                                                                  address_2_postal_code,
                                                                  address_2_city, address_2_region,
                                                                  address_2_country_code,
                                                                  address_3_label, address_3_street,
                                                                  address_3_postal_code,
                                                                  address_3_city, address_3_region,
                                                                  address_3_country_code,
                                                                  date_begin, date_end,
                                                                  link_1_name, link_1_url,
                                                                  link_2_name, link_2_url,
                                                                  link_3_name, link_3_url,
                                                                  link_4_name, link_4_url,
                                                                  link_5_name, link_5_url).decode("utf-8")
        if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
            assert str_from_xml.find(f"<comments><![CDATA[{element1}]]></comments>") != -1, \
                f"test failed for the element: {element1}"
        else:
            assert str_from_xml.find(f"<comments>{element1}</comments>") != -1, \
                f"test failed for the element: {element1}"
    # organizations
    # no organization
    str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(
        XMLgenerator_laboratory.template, acronym, name,
        description, comments,
        '', '',
        '', '',
        '', '',
        '', '',
        address_1_label, address_1_street,
        address_1_postal_code,
        address_1_city, address_1_region,
        address_1_country_code,
        address_2_label, address_2_street,
        address_2_postal_code,
        address_2_city, address_2_region,
        address_2_country_code,
        address_3_label, address_3_street,
        address_3_postal_code,
        address_3_city, address_3_region,
        address_3_country_code,
        date_begin, date_end,
        link_1_name, link_1_url,
        link_2_name, link_2_url,
        link_3_name, link_3_url,
        link_4_name, link_4_url,
        link_5_name, link_5_url).decode("utf-8")
    assert str_from_xml.find("<acronym>NULL</acronym>") != -1
    assert str_from_xml.find("<name>NULL</name>") != -1, \
        f"test failed for no organization"
    # organization_1
    for element1 in text_array:
        for element2 in text_array:
            if element1 != '' and element2 != '':
                str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym,
                                                                          name,
                                                                          description, comments,
                                                                          element1, element2,
                                                                          organization_2_acronym, organization_2_name,
                                                                          organization_3_acronym, organization_3_name,
                                                                          organization_4_acronym, organization_4_name,
                                                                          address_1_label, address_1_street,
                                                                          address_1_postal_code,
                                                                          address_1_city, address_1_region,
                                                                          address_1_country_code,
                                                                          address_2_label, address_2_street,
                                                                          address_2_postal_code,
                                                                          address_2_city, address_2_region,
                                                                          address_2_country_code,
                                                                          address_3_label, address_3_street,
                                                                          address_3_postal_code,
                                                                          address_3_city, address_3_region,
                                                                          address_3_country_code,
                                                                          date_begin, date_end,
                                                                          link_1_name, link_1_url,
                                                                          link_2_name, link_2_url,
                                                                          link_3_name, link_3_url,
                                                                          link_4_name, link_4_url,
                                                                          link_5_name, link_5_url).decode("utf-8")
                if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                    assert str_from_xml.find(f"<acronym><![CDATA[{element1}]]></acronym>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<acronym>{element1}</acronym>") != -1, \
                        f"test failed for the element: {element1}"
                if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                    assert str_from_xml.find(f"<name><![CDATA[{element2}]]></name>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<name>{element2}</name>") != -1, \
                        f"test failed for the element: {element1}"
    # organization_2
    for element1 in text_array:
        for element2 in text_array:
            if element1 != '' and element2 != '':
                str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym,
                                                                          name, description, comments,
                                                                          organization_1_acronym, organization_1_name,
                                                                          element1, element2,
                                                                          organization_3_acronym, organization_3_name,
                                                                          organization_4_acronym, organization_4_name,
                                                                          address_1_label, address_1_street,
                                                                          address_1_postal_code,
                                                                          address_1_city, address_1_region,
                                                                          address_1_country_code,
                                                                          address_2_label, address_2_street,
                                                                          address_2_postal_code,
                                                                          address_2_city, address_2_region,
                                                                          address_2_country_code,
                                                                          address_3_label, address_3_street,
                                                                          address_3_postal_code,
                                                                          address_3_city, address_3_region,
                                                                          address_3_country_code,
                                                                          date_begin, date_end,
                                                                          link_1_name, link_1_url,
                                                                          link_2_name, link_2_url,
                                                                          link_3_name, link_3_url,
                                                                          link_4_name, link_4_url,
                                                                          link_5_name, link_5_url).decode("utf-8")
                if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                    assert str_from_xml.find(f"<acronym><![CDATA[{element1}]]></acronym>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<acronym>{element1}</acronym>") != -1, \
                        f"test failed for the element: {element1}"
                if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                    assert str_from_xml.find(f"<name><![CDATA[{element2}]]></name>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<name>{element2}</name>") != -1, \
                        f"test failed for the element: {element1}"
    # organization_3
    for element1 in text_array:
        for element2 in text_array:
            if element1 != '' and element2 != '':
                str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym,
                                                                          name, description, comments,
                                                                          organization_1_acronym, organization_1_name,
                                                                          organization_2_acronym, organization_2_name,
                                                                          element1, element2,
                                                                          organization_4_acronym, organization_4_name,
                                                                          address_1_label, address_1_street,
                                                                          address_1_postal_code,
                                                                          address_1_city, address_1_region,
                                                                          address_1_country_code,
                                                                          address_2_label, address_2_street,
                                                                          address_2_postal_code,
                                                                          address_2_city, address_2_region,
                                                                          address_2_country_code,
                                                                          address_3_label, address_3_street,
                                                                          address_3_postal_code,
                                                                          address_3_city, address_3_region,
                                                                          address_3_country_code,
                                                                          date_begin, date_end,
                                                                          link_1_name, link_1_url,
                                                                          link_2_name, link_2_url,
                                                                          link_3_name, link_3_url,
                                                                          link_4_name, link_4_url,
                                                                          link_5_name, link_5_url).decode("utf-8")
                if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                    assert str_from_xml.find(f"<acronym><![CDATA[{element1}]]></acronym>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<acronym>{element1}</acronym>") != -1, \
                        f"test failed for the element: {element1}"
                if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                    assert str_from_xml.find(f"<name><![CDATA[{element2}]]></name>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<name>{element2}</name>") != -1, \
                        f"test failed for the element: {element1}"
    # organization_4
    for element1 in text_array:
        for element2 in text_array:
            if element1 != '' and element2 != '':
                str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym,
                                                                          name, description, comments,
                                                                          organization_1_acronym, organization_1_name,
                                                                          organization_2_acronym, organization_2_name,
                                                                          organization_3_acronym, organization_3_name,
                                                                          element1, element2,
                                                                          address_1_label, address_1_street,
                                                                          address_1_postal_code,
                                                                          address_1_city, address_1_region,
                                                                          address_1_country_code,
                                                                          address_2_label, address_2_street,
                                                                          address_2_postal_code,
                                                                          address_2_city, address_2_region,
                                                                          address_2_country_code,
                                                                          address_3_label, address_3_street,
                                                                          address_3_postal_code,
                                                                          address_3_city, address_3_region,
                                                                          address_3_country_code,
                                                                          date_begin, date_end,
                                                                          link_1_name, link_1_url,
                                                                          link_2_name, link_2_url,
                                                                          link_3_name, link_3_url,
                                                                          link_4_name, link_4_url,
                                                                          link_5_name, link_5_url).decode("utf-8")
                if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                    assert str_from_xml.find(f"<acronym><![CDATA[{element1}]]></acronym>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<acronym>{element1}</acronym>") != -1, \
                        f"test failed for the element: {element1}"
                if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                    assert str_from_xml.find(f"<name><![CDATA[{element2}]]></name>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<name>{element2}</name>") != -1, \
                        f"test failed for the element: {element1}"
    # addresses
    # address_1
    for element1 in text_array:
        for element2 in text_array:
            for element3 in text_array:
                for element4 in text_array:
                    for element5 in text_array:
                        for element6 in text_array:
                            if element6:
                                if not (bool(element2) and bool(element3) and bool(element4)) \
                                        and (bool(element2) or bool(element3) or bool(element4)):
                                    str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(
                                        XMLgenerator_laboratory.template, acronym, name,
                                        description, comments,
                                        organization_1_acronym, organization_1_name,
                                        organization_2_acronym, organization_2_name,
                                        organization_3_acronym, organization_3_name,
                                        organization_4_acronym, organization_4_name,
                                        element1, element2, element3, element4, element5, element6,
                                        address_2_label, address_2_street,
                                        address_2_postal_code,
                                        address_2_city, address_2_region,
                                        address_2_country_code,
                                        address_3_label, address_3_street,
                                        address_3_postal_code,
                                        address_3_city, address_3_region,
                                        address_3_country_code,
                                        date_begin, date_end,
                                        link_1_name, link_1_url,
                                        link_2_name, link_2_url,
                                        link_3_name, link_3_url,
                                        link_4_name, link_4_url,
                                        link_5_name, link_5_url).decode("utf-8")
                                    # label
                                    if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                                        assert str_from_xml.find(f"<label><![CDATA[{element1}]]></label>") != -1, \
                                            f"test failed for the element: {element1}"
                                    else:
                                        assert str_from_xml.find(f"<label>{element1}</label>") != -1, \
                                            f"test failed for the element: {element1}"
                                    # street
                                    if element2:
                                        if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                                            assert str_from_xml.find(f"<street><![CDATA[{element2}]]></street>") != -1, \
                                                f"test failed for the element: {element2}"
                                        else:
                                            assert str_from_xml.find(f"<street>{element2}</street>") != -1, \
                                                f"test failed for the element: {element2}"
                                    else:
                                        assert str_from_xml.find(f"<street>NULL</street>") != -1, \
                                            f"test failed for no street"
                                    # postal_code
                                    if element3:
                                        if XMLgenerator_laboratory.accent_letters_replace(element3) != element3:
                                            assert str_from_xml.find(f"<postal_code>"
                                                                     f"<![CDATA[{element3}]]></postal_code>") != -1, \
                                                f"test failed for the element: {element3}"
                                        else:
                                            assert str_from_xml.find(f"<postal_code>{element3}</postal_code>") != -1, \
                                                f"test failed for the element: {element3}"
                                    else:
                                        assert str_from_xml.find(f"<postal_code>NULL</postal_code>") != -1, \
                                            f"test failed for no postal_code"
                                    # city
                                    if element4:
                                        if XMLgenerator_laboratory.accent_letters_replace(element4) != element4:
                                            assert str_from_xml.find(f"<city>"
                                                                     f"<![CDATA[{element4}]]></city>") != -1, \
                                                f"test failed for the element: {element4}"
                                        else:
                                            assert str_from_xml.find(f"<city>{element4}</city>") != -1, \
                                                f"test failed for the element: {element4}"
                                    else:
                                        assert str_from_xml.find(f"<city>NULL</city>") != -1, \
                                            f"test failed for no city"
                                    # region
                                    if XMLgenerator_laboratory.accent_letters_replace(element5) != element5:
                                        assert str_from_xml.find(f"<region><![CDATA[{element5}]]></region>") != -1, \
                                            f"test failed for the element: {element5}"
                                    else:
                                        assert str_from_xml.find(f"<region>{element5}</region>") != -1, \
                                            f"test failed for the element: {element5}"
                                    # country_code
                                    if XMLgenerator_laboratory.accent_letters_replace(element6) != element6:
                                        assert str_from_xml.find(
                                            f"<country_code><![CDATA[{element6}]]></country_code>") != -1, \
                                            f"test failed for the element: {element6}"
                                    else:
                                        assert str_from_xml.find(f"<country_code>{element6}</country_code>") != -1, \
                                            f"test failed for the element: {element6}"
    # address_2
    for element1 in text_array:
        for element2 in text_array:
            for element3 in text_array:
                for element4 in text_array:
                    for element5 in text_array:
                        for element6 in text_array:
                            if element6:
                                if not (bool(element2) and bool(element3) and bool(element4)) \
                                        and (bool(element2) or bool(element3) or bool(element4)):
                                    str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(
                                        XMLgenerator_laboratory.template, acronym, name,
                                        description,
                                        comments,
                                        organization_1_acronym, organization_1_name,
                                        organization_2_acronym, organization_2_name,
                                        organization_3_acronym, organization_3_name,
                                        organization_4_acronym, organization_4_name,
                                        address_1_label, address_1_street,
                                        address_1_postal_code,
                                        address_1_city, address_1_region,
                                        address_1_country_code,
                                        element1, element2, element3, element4, element5, element6,
                                        address_3_label, address_3_street,
                                        address_3_postal_code,
                                        address_3_city, address_3_region,
                                        address_3_country_code,
                                        date_begin, date_end,
                                        link_1_name, link_1_url,
                                        link_2_name, link_2_url,
                                        link_3_name, link_3_url,
                                        link_4_name, link_4_url,
                                        link_5_name, link_5_url).decode("utf-8")
                                    # label
                                    if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                                        assert str_from_xml.find(f"<label><![CDATA[{element1}]]></label>") != -1, \
                                            f"test failed for the element: {element1}"
                                    else:
                                        assert str_from_xml.find(f"<label>{element1}</label>") != -1, \
                                            f"test failed for the element: {element1}"
                                    # street
                                    if element2:
                                        if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                                            assert str_from_xml.find(
                                                f"<street><![CDATA[{element2}]]></street>") != -1, \
                                                f"test failed for the element: {element2}"
                                        else:
                                            assert str_from_xml.find(f"<street>{element2}</street>") != -1, \
                                                f"test failed for the element: {element2}"
                                    else:
                                        assert str_from_xml.find(f"<street>NULL</street>") != -1, \
                                            f"test failed for no street"
                                    # postal_code
                                    if element3:
                                        if XMLgenerator_laboratory.accent_letters_replace(element3) != element3:
                                            assert str_from_xml.find(f"<postal_code>"
                                                                     f"<![CDATA[{element3}]]></postal_code>") != -1, \
                                                f"test failed for the element: {element3}"
                                        else:
                                            assert str_from_xml.find(
                                                f"<postal_code>{element3}</postal_code>") != -1, \
                                                f"test failed for the element: {element3}"
                                    else:
                                        assert str_from_xml.find(f"<postal_code>NULL</postal_code>") != -1, \
                                            f"test failed for no postal_code"
                                    # city
                                    if element4:
                                        if XMLgenerator_laboratory.accent_letters_replace(element4) != element4:
                                            assert str_from_xml.find(f"<city>"
                                                                     f"<![CDATA[{element4}]]></city>") != -1, \
                                                f"test failed for the element: {element4}"
                                        else:
                                            assert str_from_xml.find(f"<city>{element4}</city>") != -1, \
                                                f"test failed for the element: {element4}"
                                    else:
                                        assert str_from_xml.find(f"<city>NULL</city>") != -1, \
                                            f"test failed for no city"
                                    # region
                                    if XMLgenerator_laboratory.accent_letters_replace(element5) != element5:
                                        assert str_from_xml.find(f"<region><![CDATA[{element5}]]></region>") != -1, \
                                            f"test failed for the element: {element5}"
                                    else:
                                        assert str_from_xml.find(f"<region>{element5}</region>") != -1, \
                                            f"test failed for the element: {element5}"
                                    # country_code
                                    if XMLgenerator_laboratory.accent_letters_replace(element6) != element6:
                                        assert str_from_xml.find(
                                            f"<country_code><![CDATA[{element6}]]></country_code>") != -1, \
                                            f"test failed for the element: {element6}"
                                    else:
                                        assert str_from_xml.find(f"<country_code>{element6}</country_code>") != -1, \
                                            f"test failed for the element: {element6}"
    # address_3
    for element1 in text_array:
        for element2 in text_array:
            for element3 in text_array:
                for element4 in text_array:
                    for element5 in text_array:
                        for element6 in text_array:
                            if element6:
                                if not (bool(element2) and bool(element3) and bool(element4)) \
                                        and (bool(element2) or bool(element3) or bool(element4)):
                                    str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(
                                        XMLgenerator_laboratory.template, acronym, name,
                                        description,
                                        comments,
                                        organization_1_acronym, organization_1_name,
                                        organization_2_acronym, organization_2_name,
                                        organization_3_acronym, organization_3_name,
                                        organization_4_acronym, organization_4_name,
                                        address_1_label, address_1_street,
                                        address_1_postal_code,
                                        address_1_city, address_1_region,
                                        address_1_country_code,
                                        address_2_label, address_2_street,
                                        address_2_postal_code,
                                        address_2_city, address_2_region,
                                        address_2_country_code,
                                        element1, element2, element3, element4, element5, element6,
                                        date_begin, date_end,
                                        link_1_name, link_1_url,
                                        link_2_name, link_2_url,
                                        link_3_name, link_3_url,
                                        link_4_name, link_4_url,
                                        link_5_name, link_5_url).decode("utf-8")
                                    # label
                                    if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                                        assert str_from_xml.find(f"<label><![CDATA[{element1}]]></label>") != -1, \
                                            f"test failed for the element: {element1}"
                                    else:
                                        assert str_from_xml.find(f"<label>{element1}</label>") != -1, \
                                            f"test failed for the element: {element1}"
                                    # street
                                    if element2:
                                        if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                                            assert str_from_xml.find(
                                                f"<street><![CDATA[{element2}]]></street>") != -1, \
                                                f"test failed for the element: {element2}"
                                        else:
                                            assert str_from_xml.find(f"<street>{element2}</street>") != -1, \
                                                f"test failed for the element: {element2}"
                                    else:
                                        assert str_from_xml.find(f"<street>NULL</street>") != -1, \
                                            f"test failed for no street"
                                    # postal_code
                                    if element3:
                                        if XMLgenerator_laboratory.accent_letters_replace(element3) != element3:
                                            assert str_from_xml.find(f"<postal_code>"
                                                                     f"<![CDATA[{element3}]]></postal_code>") != -1, \
                                                f"test failed for the element: {element3}"
                                        else:
                                            assert str_from_xml.find(
                                                f"<postal_code>{element3}</postal_code>") != -1, \
                                                f"test failed for the element: {element3}"
                                    else:
                                        assert str_from_xml.find(f"<postal_code>NULL</postal_code>") != -1, \
                                            f"test failed for no postal_code"
                                    # city
                                    if element4:
                                        if XMLgenerator_laboratory.accent_letters_replace(element4) != element4:
                                            assert str_from_xml.find(f"<city>"
                                                                     f"<![CDATA[{element4}]]></city>") != -1, \
                                                f"test failed for the element: {element4}"
                                        else:
                                            assert str_from_xml.find(f"<city>{element4}</city>") != -1, \
                                                f"test failed for the element: {element4}"
                                    else:
                                        assert str_from_xml.find(f"<city>NULL</city>") != -1, \
                                            f"test failed for no city"
                                    # region
                                    if XMLgenerator_laboratory.accent_letters_replace(element5) != element5:
                                        assert str_from_xml.find(f"<region><![CDATA[{element5}]]></region>") != -1, \
                                            f"test failed for the element: {element5}"
                                    else:
                                        assert str_from_xml.find(f"<region>{element5}</region>") != -1, \
                                            f"test failed for the element: {element5}"
                                    # country_code
                                    if XMLgenerator_laboratory.accent_letters_replace(element6) != element6:
                                        assert str_from_xml.find(
                                            f"<country_code><![CDATA[{element6}]]></country_code>") != -1, \
                                            f"test failed for the element: {element6}"
                                    else:
                                        assert str_from_xml.find(f"<country_code>{element6}</country_code>") != -1, \
                                            f"test failed for the element: {element6}"
    # dates
    for element1 in data_array:
        for element2 in data_array:
            str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym, name,
                                                                      description, comments,
                                                                      organization_1_acronym, organization_1_name,
                                                                      organization_2_acronym, organization_2_name,
                                                                      organization_3_acronym, organization_3_name,
                                                                      organization_4_acronym, organization_4_name,
                                                                      address_1_label, address_1_street,
                                                                      address_1_postal_code,
                                                                      address_1_city, address_1_region,
                                                                      address_1_country_code,
                                                                      address_2_label, address_2_street,
                                                                      address_2_postal_code,
                                                                      address_2_city, address_2_region,
                                                                      address_2_country_code,
                                                                      address_3_label, address_3_street,
                                                                      address_3_postal_code,
                                                                      address_3_city, address_3_region,
                                                                      address_3_country_code,
                                                                      element1, element2,
                                                                      link_1_name, link_1_url,
                                                                      link_2_name, link_2_url,
                                                                      link_3_name, link_3_url,
                                                                      link_4_name, link_4_url,
                                                                      link_5_name, link_5_url).decode("utf-8")
            assert str_from_xml.find(f"<date_begin>{element1}</date_begin>") != -1, \
                f"test failed for the element: {element1}"
            assert str_from_xml.find(f"<date_end>{element2}</date_end>") != -1, \
                f"test failed for the element: {element2}"
    # links
    # no links
    str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym, name,
                                                              description,
                                                              comments,
                                                              organization_1_acronym, organization_1_name,
                                                              organization_2_acronym, organization_2_name,
                                                              organization_3_acronym, organization_3_name,
                                                              organization_4_acronym, organization_4_name,
                                                              address_1_label, address_1_street,
                                                              address_1_postal_code,
                                                              address_1_city, address_1_region,
                                                              address_1_country_code,
                                                              address_2_label, address_2_street,
                                                              address_2_postal_code,
                                                              address_2_city, address_2_region,
                                                              address_2_country_code,
                                                              address_3_label, address_3_street,
                                                              address_3_postal_code,
                                                              address_3_city, address_3_region,
                                                              address_3_country_code,
                                                              date_begin, date_end,
                                                              '', '',
                                                              '', '',
                                                              '', '',
                                                              '', '',
                                                              '', '').decode("utf-8")
    assert str_from_xml.find("<name>NULL</name>") != -1
    assert str_from_xml.find("<url>NULL</url>") != -1, \
        f"test failed for no links"
    # link_1
    for element1 in text_array:
        for element2 in url_array:
            if element1 != '' and element2 != '':
                str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym,
                                                                          name, description, comments,
                                                                          organization_1_acronym, organization_1_name,
                                                                          organization_2_acronym, organization_2_name,
                                                                          organization_3_acronym, organization_3_name,
                                                                          organization_4_acronym, organization_4_name,
                                                                          address_1_label, address_1_street,
                                                                          address_1_postal_code,
                                                                          address_1_city, address_1_region,
                                                                          address_1_country_code,
                                                                          address_2_label, address_2_street,
                                                                          address_2_postal_code,
                                                                          address_2_city, address_2_region,
                                                                          address_2_country_code,
                                                                          address_3_label, address_3_street,
                                                                          address_3_postal_code,
                                                                          address_3_city, address_3_region,
                                                                          address_3_country_code,
                                                                          date_begin, date_end,
                                                                          element1, element2,
                                                                          link_2_name, link_2_url,
                                                                          link_3_name, link_3_url,
                                                                          link_4_name, link_4_url,
                                                                          link_5_name, link_5_url).decode("utf-8")
                if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                    assert str_from_xml.find(
                        f"<name><![CDATA[{element1}]]></name>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<name>{element1}</name>") != -1, \
                        f"test failed for the element: {element1}"
                if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                    assert str_from_xml.find(
                        f"<url><![CDATA[{element2}]]></url>") != -1, \
                        f"test failed for the element: {element2}"
                else:
                    assert str_from_xml.find(f"<url>{element2}</url>") != -1, \
                        f"test failed for the element: {element2}"
    # link_2
    for element1 in text_array:
        for element2 in url_array:
            if element1 != '' and element2 != '':
                str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym,
                                                                          name,
                                                                          description,
                                                                          comments,
                                                                          organization_1_acronym, organization_1_name,
                                                                          organization_2_acronym, organization_2_name,
                                                                          organization_3_acronym, organization_3_name,
                                                                          organization_4_acronym, organization_4_name,
                                                                          address_1_label, address_1_street,
                                                                          address_1_postal_code,
                                                                          address_1_city, address_1_region,
                                                                          address_1_country_code,
                                                                          address_2_label, address_2_street,
                                                                          address_2_postal_code,
                                                                          address_2_city, address_2_region,
                                                                          address_2_country_code,
                                                                          address_3_label, address_3_street,
                                                                          address_3_postal_code,
                                                                          address_3_city, address_3_region,
                                                                          address_3_country_code,
                                                                          date_begin, date_end,
                                                                          link_1_name, link_1_url,
                                                                          element1, element2,
                                                                          link_3_name, link_3_url,
                                                                          link_4_name, link_4_url,
                                                                          link_5_name, link_5_url).decode("utf-8")
                if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                    assert str_from_xml.find(
                        f"<name><![CDATA[{element1}]]></name>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<name>{element1}</name>") != -1, \
                        f"test failed for the element: {element1}"
                if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                    assert str_from_xml.find(
                        f"<url><![CDATA[{element2}]]></url>") != -1, \
                        f"test failed for the element: {element2}"
                else:
                    assert str_from_xml.find(f"<url>{element2}</url>") != -1, \
                        f"test failed for the element: {element2}"
    # link_3
    for element1 in text_array:
        for element2 in url_array:
            if element1 != '' and element2 != '':
                str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym,
                                                                          name,
                                                                          description,
                                                                          comments,
                                                                          organization_1_acronym, organization_1_name,
                                                                          organization_2_acronym, organization_2_name,
                                                                          organization_3_acronym, organization_3_name,
                                                                          organization_4_acronym, organization_4_name,
                                                                          address_1_label, address_1_street,
                                                                          address_1_postal_code,
                                                                          address_1_city, address_1_region,
                                                                          address_1_country_code,
                                                                          address_2_label, address_2_street,
                                                                          address_2_postal_code,
                                                                          address_2_city, address_2_region,
                                                                          address_2_country_code,
                                                                          address_3_label, address_3_street,
                                                                          address_3_postal_code,
                                                                          address_3_city, address_3_region,
                                                                          address_3_country_code,
                                                                          date_begin, date_end,
                                                                          link_1_name, link_1_url,
                                                                          link_2_name, link_2_url,
                                                                          element1, element2,
                                                                          link_4_name, link_4_url,
                                                                          link_5_name, link_5_url).decode("utf-8")
                if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                    assert str_from_xml.find(
                        f"<name><![CDATA[{element1}]]></name>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<name>{element1}</name>") != -1, \
                        f"test failed for the element: {element1}"
                if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                    assert str_from_xml.find(
                        f"<url><![CDATA[{element2}]]></url>") != -1, \
                        f"test failed for the element: {element2}"
                else:
                    assert str_from_xml.find(f"<url>{element2}</url>") != -1, \
                        f"test failed for the element: {element2}"
    # link_4
    for element1 in text_array:
        for element2 in url_array:
            if element1 != '' and element2 != '':
                str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym,
                                                                          name,
                                                                          description,
                                                                          comments,
                                                                          organization_1_acronym, organization_1_name,
                                                                          organization_2_acronym, organization_2_name,
                                                                          organization_3_acronym, organization_3_name,
                                                                          organization_4_acronym, organization_4_name,
                                                                          address_1_label, address_1_street,
                                                                          address_1_postal_code,
                                                                          address_1_city, address_1_region,
                                                                          address_1_country_code,
                                                                          address_2_label, address_2_street,
                                                                          address_2_postal_code,
                                                                          address_2_city, address_2_region,
                                                                          address_2_country_code,
                                                                          address_3_label, address_3_street,
                                                                          address_3_postal_code,
                                                                          address_3_city, address_3_region,
                                                                          address_3_country_code,
                                                                          date_begin, date_end,
                                                                          link_1_name, link_1_url,
                                                                          link_2_name, link_2_url,
                                                                          link_3_name, link_3_url,
                                                                          element1, element2,
                                                                          link_5_name, link_5_url).decode("utf-8")
                if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                    assert str_from_xml.find(
                        f"<name><![CDATA[{element1}]]></name>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<name>{element1}</name>") != -1, \
                        f"test failed for the element: {element1}"
                if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                    assert str_from_xml.find(
                        f"<url><![CDATA[{element2}]]></url>") != -1, \
                        f"test failed for the element: {element2}"
                else:
                    assert str_from_xml.find(f"<url>{element2}</url>") != -1, \
                        f"test failed for the element: {element2}"
    # link_5
    for element1 in text_array:
        for element2 in url_array:
            if element1 != '' and element2 != '':
                str_from_xml = XMLgenerator_laboratory.xml_parse_and_fill(XMLgenerator_laboratory.template, acronym,
                                                                          name,
                                                                          description,
                                                                          comments,
                                                                          organization_1_acronym, organization_1_name,
                                                                          organization_2_acronym, organization_2_name,
                                                                          organization_3_acronym, organization_3_name,
                                                                          organization_4_acronym, organization_4_name,
                                                                          address_1_label, address_1_street,
                                                                          address_1_postal_code,
                                                                          address_1_city, address_1_region,
                                                                          address_1_country_code,
                                                                          address_2_label, address_2_street,
                                                                          address_2_postal_code,
                                                                          address_2_city, address_2_region,
                                                                          address_2_country_code,
                                                                          address_3_label, address_3_street,
                                                                          address_3_postal_code,
                                                                          address_3_city, address_3_region,
                                                                          address_3_country_code,
                                                                          date_begin, date_end,
                                                                          link_1_name, link_1_url,
                                                                          link_2_name, link_2_url,
                                                                          link_3_name, link_3_url,
                                                                          link_4_name, link_4_url,
                                                                          element1, element2).decode("utf-8")
                if XMLgenerator_laboratory.accent_letters_replace(element1) != element1:
                    assert str_from_xml.find(
                        f"<name><![CDATA[{element1}]]></name>") != -1, \
                        f"test failed for the element: {element1}"
                else:
                    assert str_from_xml.find(f"<name>{element1}</name>") != -1, \
                        f"test failed for the element: {element1}"
                if XMLgenerator_laboratory.accent_letters_replace(element2) != element2:
                    assert str_from_xml.find(
                        f"<url><![CDATA[{element2}]]></url>") != -1, \
                        f"test failed for the element: {element2}"
                else:
                    assert str_from_xml.find(f"<url>{element2}</url>") != -1, \
                        f"test failed for the element: {element2}"
