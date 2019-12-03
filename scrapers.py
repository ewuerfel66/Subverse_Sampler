# Imports
import pandas as pd

import re

from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

# AP
def ap(ap_Sections, ap_ArticleURLs):
    for SectionURL in ap_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', {'class':'headline'}, href=re.compile('^/([a-z]+|[0-9]+)')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in ap_ArticleURLs:
                        # print(link.attrs['href'])
                        ap_ArticleURLs.append(link.attrs['href'])
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# Breitbart
def breitbart(breitbart_Sections, breitbart_ArticleURLs):
    for SectionURL in breitbart_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('([a-z]+-[a-z]+-[a-z]+-[a-z]+-[a-z]+/)$')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in breitbart_ArticleURLs:
                        newPage = 'https://www.breitbart.com' + link.attrs['href']
                        # print(newPage)
                        breitbart_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# Buzzfeed
def buzzfeed(buzzfeed_Sections, buzzfeed_ArticleURLs):
    for SectionURL in buzzfeed_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(https://www.buzzfeednews.com/article/)')):
                    if 'href' in link.attrs:
                        if link.attrs['href'] not in buzzfeed_ArticleURLs:
                            newPage = link.attrs['href']
                            # print(newPage)
                            buzzfeed_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# The Daily Wire
def dailyWire(dailyWire_Sections, dailyWire_ArticleURLs):
    # enter browser credentials
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0'}
    reg_url = 'https://www.dailywire.com/'
    req = Request(url=reg_url, headers=headers) 
    html = urlopen(req).read()

    try:
        # Initialize soup and article urls
        soup = BeautifulSoup(html, 'html.parser')
        dailyWire_EndArticleURLs = []

        # Scrape front page
        for link in soup.find_all('a', href=re.compile('^(/news/)')):
            if 'href' in link.attrs:
                if link.attrs['href'] not in dailyWire_EndArticleURLs:
                    # print(link.attrs['href'])
                    dailyWire_EndArticleURLs.append(link.attrs['href'])
                    
        # add prefix
        for ArticleURL in dailyWire_EndArticleURLs:
            FullArticleURL = 'https://www.dailywire.com'+ArticleURL
            dailyWire_ArticleURLs.append(FullArticleURL)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)


# Examiner
def examiner(examiner_Sections, examiner_ArticleURLs):
    for SectionURL in examiner_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)
    
        for link in soup.find_all('a', href=re.compile('([a-z]+-[a-z]+-[a-z]+-[a-z]+-[a-z]+)$')):
            if 'href' in link.attrs:
                if link.attrs['href'] not in examiner_ArticleURLs:
                    # print(link.attrs['href'])
                    examiner_ArticleURLs.append(link.attrs['href'])


# Fox News
def fox(fox_Sections, fox_ArticleURLs):
    for SectionURL in fox_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('([a-z]+-[a-z]+-[a-z]+-[a-z]+-[a-z]+)$')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in fox_ArticleURLs:
                        newPage = link.attrs['href']
                        # print(newPage)
                        fox_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# The Hill
def hill(hill_Sections, hill_ArticleURLs):
    for SectionURL in hill_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('([a-z]+-[a-z]+-[a-z]+-[a-z]+-[a-z]+)$')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in hill_ArticleURLs:
                        newPage = 'https://www.thehill.com' + link.attrs['href']
                        # print(newPage)
                        hill_ArticleURLs.append(newPage)
        # Handle potential errors
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# MSNBC
def msnbc(msnbc_Sections, msnbc_ArticleURLs):
    for SectionURL in msnbc_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('([a-z]+-[a-z]+-[a-z]+-[a-z]+-(n[0-9]+|ncna[0-9]+))$')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in msnbc_ArticleURLs:
                        # print(link.attrs['href'])
                        msnbc_ArticleURLs.append(link.attrs['href'])  
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# NYT
def nyt(nyt_Sections, nyt_ArticleURLs):
    for SectionURL in nyt_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html,'html.parser')
        
            for link in soup.find_all('a', href=re.compile('^(/2019/)')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in nyt_ArticleURLs:
                        # print(link.attrs['href'])
                        nyt_ArticleURLs.append(link.attrs['href'])
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# Vox
def vox(vox_Sections, vox_ArticleURLs):
    for SectionURL in vox_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
        
            for link in soup.find_all('a', href=re.compile('https://www.vox.com/')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in vox_ArticleURLs:
                        new_Page = link.attrs['href']
                        vox_ArticleURLs.append(new_Page)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# The Washington Post
def wapo(wapo_Sections, wapo_ArticleURLs):
    for SectionURL in wapo_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            
            for link in soup.find_all('a', href=re.compile('([a-z]+-[a-z]+-[a-z]+-[a-z]+-[a-z]+/)$')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in wapo_ArticleURLs:
                        if link.attrs['href'].startswith('https://'):
                            # print(link.attrs['href'])
                            wapo_ArticleURLs.append(link.attrs['href'])
                        elif link.attrs['href'].startswith('/'):
                            newPage = 'https://www.washingtonpost.com' + link.attrs['href']
                            # print(newPage)
                            wapo_ArticleURLs.append(newPage)
                        
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# WSJ
def wsj(wsj_Sections, wsj_ArticleURLs):
    for SectionURL in wsj_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html,'html.parser')
    
            for link in soup.find_all('a', href=re.compile('^(https://www.wsj.com/articles/)')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in wsj_ArticleURLs:
                        # print(link.attrs['href'])
                        wsj_ArticleURLs.append(link.attrs['href'])
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)