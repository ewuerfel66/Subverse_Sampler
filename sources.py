"""
A Class for each Source
"""

import pandas as pd

class Source:
    def __init__(self, name, codename, sections, scraper, article_URLs=[], section_URLs=[], daily_df=pd.DataFrame()):
        self.name = name
        self.codename = codename
        self.sections = sections
        self.scraper = scraper
        self.article_URLs = article_URLs
        self.daily_df = daily_df