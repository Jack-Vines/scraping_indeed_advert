"""
Helper functions for job advert scrape.
"""
import logging 
import requests
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


def parse_html(url):
    """Function to parse html from a URL.

    Parameters
    ----------
    url : str
        String URL

    Returns
    ----------
    soup : bs4.BeautifulSoup
       Resulting HTML as a bs4 object

    """
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "lxml")
        logging.info("Page parsed")
        return soup
    else:
        logging.warning("Invalid URL used")


def extract_features(soup):
    """Function to extract relevant features from job advert.

    Parameters
    ----------
    soup : bs4.BeautifulSoup

    Returns:
    ----------
    feature_dict : dict
        Dictionary of extracted features

    """
    title = soup.find('span',{'class':'indeed-apply-widget'})['data-indeed-apply-jobtitle']
    company_name = soup.find('span',{'class':'indeed-apply-widget'})['data-indeed-apply-jobcompanyname']
    location = soup.find('span',{'class':'indeed-apply-widget'})['data-indeed-apply-joblocation']
    _id = soup.find('span',{'class':'indeed-apply-widget'})['data-indeed-apply-jobid']
    url = soup.find('span',{'class':'indeed-apply-widget'})['data-indeed-apply-joburl']
    description = soup.find(id='jobDescriptionText').text
    feature_dict = {'title':title,
                    'company_name':company_name,
                    'location':location,
                    'id':_id,
                    'url':url,
                    'description':description
                    }
    return feature_dict


def load_scrape(feature_dict):
    """Placeholder function that returns advert title as formatted string.

    Parameters
    ----------
    feature_dict : dict
        dictionary of advert features

    """
    title = feature_dict['title']
    return f'Job: {title} has been extracted.'


def extract_skills():
    """
    Placeholder function intended to categorize advert into recognized taxonomy.
    """
    pass


def categorize_job():
    """
    Placeholder function intended to categorize skills into recognized taxonomy.
    """


def geocode_location():
    """
    Placeholder function intended to geocode location.
    """
