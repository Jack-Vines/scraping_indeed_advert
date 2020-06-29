"""
Main app to run job advert scrape.
"""
import time

from helpers import parse_html, extract_features, load_scrape


URL = "https://www.indeed.co.uk/viewjob?cmp=Harringtons-Sales-%26-Lettings&t=Account+Assistant&jk=9a2565f2b076b6f0&vjs=3"


def main(url):
    """Main function to run full scrape.

    Parameters
    ----------
    url : str
       Text URL of an indeed.co.uk job advert
    """
    parsed_html = parse_html(url)
    feature_dict = extract_features(parsed_html)
    print(load_scrape(feature_dict))


if __name__ == "__main__":
    start_time = time.time()
    main(URL)
    print("--- Time taken: %s seconds ---" % (time.time()-start_time))
    