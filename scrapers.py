# Imports
import pandas as pd

import re
import time

from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

# AP
def ap(ap_Sections, ap_ArticleURLs):
    stragglers = ["/termsofservice", "/privacystatement"]
    
    for SectionURL in ap_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile("^/[a-z0-9]+$")):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in stragglers:
                        if link.attrs['href'] not in ap_ArticleURLs:
                            newPage = "https://apnews.com" + str(link.attrs['href'])
                            # print(newPage)
                            ap_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# BBC
def bbc(bbc_Sections, bbc_ArticleURLs):
    for SectionURL in bbc_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(/news/).*([0-9]+)$')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in bbc_ArticleURLs:
                        newPage = 'https://www.bbc.com' + link.attrs['href']
                        # print(newPage)
                        bbc_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# The Blaze
def blaze(blaze_Sections, blaze_ArticleURLs):
    for SectionURL in blaze_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(https://www.theblaze.com/news/)')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in blaze_ArticleURLs:
                        newPage = link.attrs['href']
                        # print(newPage)
                        blaze_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# # Bloomberg
# def bloom(bloom_Sections, bloom_ArticleURLs):
    
#     for SectionURL in bloom_Sections:
#         try:
#             html = urlopen(SectionURL)
#             soup = BeautifulSoup(html, 'html.parser')
#             for link in soup.find_all('a'):
#                 if 'href' in link.attrs:
#                     if link.attrs['href'] not in bloom_ArticleURLs:
#                         newPage = "https://www.bloomberg.com" + str(link.attrs['href'])
#                         print(newPage)
#                         bloom_ArticleURLs.append(newPage)
#         except HTTPError as e:
#             print(e)
#         except URLError as e:
#             print(e)


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


# CNN
def cnn(cnn_Sections, cnn_ArticleURLs):
    for SectionURL in cnn_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(/[0-9]+/[0-9]+/[0-9]+/)')):
                    if 'href' in link.attrs:
                        if link.attrs['href'] not in cnn_ArticleURLs:
                            newPage = "https://www.cnn.com" + str(link.attrs['href'])
                            # print(newPage)
                            cnn_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# # The Daily Caller
# def dailyCaller(dailyCaller_Sections, dailyCaller_ArticleURLs):
#     headers = {'User-Agent': 'Mozilla/5.0'}
    
#     for SectionURL in dailyCaller_Sections:
#         try:
#             req = Request(url=SectionURL, headers=headers)
#             html = urlopen(req).read()
#             soup = BeautifulSoup(html, 'html.parser')
#             for link in soup.find_all('a', href=re.compile('^(/news/).*([0-9]+)$')):
#                 if 'href' in link.attrs:
#                     if link.attrs['href'] not in dailyCaller_ArticleURLs:
#                         newPage = 'https://dailycaller.com' + link.attrs['href']
#                         print(newPage)
#                         dailyCaller_ArticleURLs.append(newPage)
#         except HTTPError as e:
#             print(e)
#         except URLError as e:
#             print(e)


# The Daily Mail
def dailyMail(dailyMail_Sections, dailyMail_ArticleURLs):

    for SectionURL in dailyMail_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(/news/).*([a-z]+-[a-z]+.html)$')):
                if 'href' in link.attrs:
                        if link.attrs['href'] not in dailyMail_ArticleURLs:
                            newPage = 'https://www.dailymail.co.uk' + link.attrs['href']
                            # print(newPage)
                            dailyMail_ArticleURLs.append(newPage)
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


# The Federalist
def fed(fed_Sections, fed_ArticleURLs):
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for SectionURL in fed_Sections:
        try:
            req = Request(url=SectionURL, headers=headers)
            html = urlopen(req).read()
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(https://thefederalist.com/[0-9]+/[0-9]+/[0-9]+/)')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in fed_ArticleURLs:
                        newPage = link.attrs['href']
                        # print(newPage)
                        fed_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


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


# The Huffington Post
def huffpo(huffpo_Sections, huffpo_ArticleURLs):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0'}
    
    for SectionURL in huffpo_Sections:
        try:
            req = Request(url=SectionURL, headers=headers)
            html = urlopen(req).read()
            soup = BeautifulSoup(html, 'html.parser')
        
            for link in soup.find_all('a', href=re.compile("^(https://www.huffpost.com/entry/)")):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in huffpo_ArticleURLs:
                        newPage = link.attrs['href']
                        # print(newPage)
                        huffpo_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# The Intercept
def intercept(intercept_Sections, intercept_ArticleURLs):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0'}
    
    for section in intercept_Sections:
        try:
            req = Request(url=section, headers=headers) 
            html = urlopen(req).read()
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^https://theintercept.com/[0-9]+/[0-9]+/[0-9]+/')):
                    if 'href' in link.attrs:
                        if link.attrs['href'] not in intercept_ArticleURLs:
                            newPage = link.attrs['href']
                            # print(newPage)
                            intercept_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# Jacobin
def jacobin(jacobin_Sections, jacobin_ArticleURLs):
    for SectionURL in jacobin_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(/[0-9]+/[0-9]+/)')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in jacobin_ArticleURLs:
                        newPage = 'https://www.jacobinmag.com' + link.attrs['href']
                        # print(newPage)
                        jacobin_ArticleURLs.append(newPage)
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


# NPR
def npr(npr_Sections, npr_ArticleURLs):
    for SectionURL in npr_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(https).*([a-z0-9]+-[a-z0-9]+-[a-z0-9]+)$')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in npr_ArticleURLs:
                        # print(link.attrs['href'])
                        npr_ArticleURLs.append(link.attrs['href'])
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# National Review
def nr(nr_Sections, nr_ArticleURLs):
    for SectionURL in nr_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(https://www.nationalreview).*([a-z]+-[a-z]+-[a-z]+/)$')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in nr_ArticleURLs:
                        # print(link.attrs['href'])
                        nr_ArticleURLs.append(link.attrs['href'])
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# The New York Post
def nypost(nypost_Sections, nypost_ArticleURLs):
    for SectionURL in nypost_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(https://nypost.com/20)')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in nypost_ArticleURLs:
                        # print(link.attrs['href'])
                        nypost_ArticleURLs.append(link.attrs['href'])  
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
                        newPage = "https://www.nytimes.com" + str(link.attrs['href'])
                        nyt_ArticleURLs.append(newPage)
        except HTTPError as e:
            pass
        except URLError as e:
            pass


# Politico
def politico(politico_Sections, politico_ArticleURLs):
    for SectionURL in politico_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(https://www.politico.com/news/[0-9]+/[0-9]+/[0-9]+/)')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in politico_ArticleURLs:
                        newPage = link.attrs['href']
                        # print(newPage)
                        politico_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# Reason
def reason(reason_Sections, reason_ArticleURLs):
    for SectionURL in reason_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
        
            for link in soup.find_all('a', href=re.compile('^(https://reason.com/[0-9]+)')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in reason_ArticleURLs:
                        newPage = link.attrs['href']
                        # print(newPage)
                        reason_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# Reuters
def reuters(reuters_Sections, reuters_ArticleURLs):
    for SectionURL in reuters_Sections:
        try:
            html = urlopen(SectionURL)
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=re.compile('^(https://www.reuters.com/article/)')):
                    if 'href' in link.attrs:
                        if link.attrs['href'] not in reuters_ArticleURLs:
                            newPage = link.attrs['href']
                            # print(newPage)
                            reuters_ArticleURLs.append(newPage)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)


# Vox
def vox(vox_Sections, vox_ArticleURLs):
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for SectionURL in vox_Sections:
        try:
            req = Request(url=SectionURL, headers=headers)
            html = urlopen(req).read()
            soup = BeautifulSoup(html, 'html.parser')
        
            for link in soup.find_all('a', href=re.compile('^https://www.vox.com/.*[0-9]+/[0-9]+/[0-9]+/[0-9]+/')):
                # time.sleep(2)
                if 'href' in link.attrs:
                    if link.attrs['href'] not in vox_ArticleURLs:
                        newPage = link.attrs['href']
                        # print(f"---{newPage}")
                        vox_ArticleURLs.append(newPage)
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


# # The Washington Times
# def watimes(watimes_Sections, watimes_ArticleURLs):
#     for SectionURL in watimes_Sections:
#         try:
#             html = urlopen(SectionURL)
#             soup = BeautifulSoup(html, 'html.parser')
        
#             for link in soup.find_all('a', href=re.compile('^(/[a-z]+/[0-9]+/[a-z]+/[0-9]+/)|^(https://www.washingtontimes.com/[a-z]+/[0-9]+/[a-z]+/[0-9]+/)')):
#                 if 'href' in link.attrs:
#                     if link.attrs['href'] not in watimes_ArticleURLs:
#                         new_Page = link.attrs['href']
#                         watimes_ArticleURLs.append(new_Page)
#         except HTTPError as e:
#             print(e)
#         except URLError as e:
#             print(e)


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