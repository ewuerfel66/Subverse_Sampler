# Subverse Sampler

![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)


## Project Overview
The Subverse Sampler is comprised of two parts:
  * The Daily News Scraper
  * The News Sampler
  
### The Daily News Scraper
The Daily News Scraper scrapes `article URL`, `source` and `date` from each of the sources listed in the **Sources** section.

This is set up to run daily at 10 AM EST.

### The News Sampler
The News Sampler selects a simple random sample of 100 articles for each source.


## Sources:
  - Left:
    * Vox
  - Center Left:
    * The New York Times
  - Center:
    * The Hill
  - Center Right:
    * The Washington Examiner
  - Right:
    * Breitbart
