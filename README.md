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

The results of the sampler are displayed on the [Subverse Sampler](https://odin-central.github.io/) site for review.


## Sources:
  - Left:
    * The Huffington Post
    * The Intercept
    * Jacobin Magazine
    * MSNBC
    * Vox
  - Center Left:
    * Buzzfeed News
    * CNN
    * The New York Times
    * Politico
    * The Washington Post
  - Center:
    * Associated Press
    * BBC
    * The Hill
    * NPR
    * Reuters
    * The Wall Street Journal
  - Center Right:
    * Fox News
    * Reason
    * The Washington Examiner
  - Right:
    * The Blaze
    * Breitbart
    * The Daily Mail
    * The Daily Wire
    * National Review
    * The New York Post