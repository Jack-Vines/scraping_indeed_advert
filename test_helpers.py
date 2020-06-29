"""
Tests for helper functions.
"""
import logging
from helpers import parse_html, extract_features, load_scrape


TEST_URL = "https://www.indeed.co.uk/viewjob?jk=0c09a0b6ce363465"
FALSE_TEST_URL = "https://www.indeed.co.uk/viewINVALID_URLcount6b6f0&vjs=3"

html = parse_html(TEST_URL)
feature_dict = extract_features(html)


def test_parse_html(caplog):
    """
    Test function to ensure function returns correct logs dependant on
    whether parse was successful.
    """
    with caplog.at_level(logging.INFO):
        test_valid_soup = parse_html(TEST_URL)
    assert "Page parsed" in caplog.text
    with caplog.at_level(logging.WARNING):
        test_invalid_soup = parse_html(FALSE_TEST_URL)
    assert "Invalid URL used" in caplog.text


def test_extract_features():
    """
    Test function to ensure features are extracted successfully.
    """
    assert feature_dict['title'] == 'Paralegal/Legal Assistant'
    assert feature_dict['company_name'] == 'Medical Solicitors'
    assert feature_dict['location'] == 'Sheffield, South Yorkshire'
    assert feature_dict['id'] == '971f8ceb7a7c159b2295'
    assert feature_dict['url'] == 'https://www.indeed.co.uk/viewjob?jk=0c09a0b6ce363465'
    assert feature_dict['description'][:50] == 'We currently have a fantastic opportunity for a Pa'
    

def test_load_scrape():
    """
    Test function to ensure load function returns correct print.
    """
    assert load_scrape(feature_dict) == "Job: Paralegal/Legal Assistant has been extracted."
