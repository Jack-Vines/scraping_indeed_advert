# Basic indeed.co.uk Web Scraper

## Overview

This repo contains code to scrape basic information from an indeed.co.uk job advert.

Though basic, the structure is designed to be able to increment iteratively as new features are defined.

There are certain functions that are currently empty that exist as an example of further enhancements that could be made.

## How to Run

To run the scraper, firstly ensure all requirements in the [requirements.txt](requirements.txt) file are met, then run `python run.py` from the command line.

Currently this will just print the title of the extracted job, and time taken to run the function in lieu of actual database load.

## Tests

Each helper function has an associated test. Running `pytest test_helpers.py` will show current status of test.

## TODO

Due to time constraints, certain functions are included but undeveloped, as a demonstrative framework for potential future enhancements. 
