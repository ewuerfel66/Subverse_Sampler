"""
News Sampler

- Scrape article URL, source, and timestamp from sources
- Compile data into DataFrame
- Send DataFrame to ElephantSQL DataBase
"""

print("")
print("-----------------------------")
print("--- Subverse News Sampler ---")
print("-----------------------------")
print("")

####################################################
################### Imports ########################
####################################################

from datetime import datetime
import psycopg2
import pandas as pd

# Local Imports
import sections
import scrapers
from sources import Source


####################################################
#################### Sources #######################
####################################################

ap = Source("Associated Press", "ap", sections.ap, scrapers.ap)
bbc = Source("The BBC", "bbc", sections.bbc, scrapers.bbc)
blaze = Source("The Blaze", "blaze", sections.blaze, scrapers.blaze)
breitbart = Source("Breitbart", "breitbart", sections.breitbart, scrapers.breitbart)
buzzfeed = Source("Buzzfeed News", "buzzfeed", sections.buzzfeed, scrapers.buzzfeed)
cnn = Source("CNN", "cnn", sections.cnn, scrapers.cnn)
dailyMail = Source("The Daily Mail", "dailyMail", sections.dailyMail, scrapers.dailyMail)
dailyWire = Source("The Daily Wire", "dailyWire", sections.dailyWire, scrapers.dailyWire)
examiner = Source("The Washington Examiner", "examiner", sections.examiner, scrapers.examiner)
fed = Source("The Federalist", "fed", sections.fed, scrapers.fed)
fox = Source("Fox News", "fox", sections.fox, scrapers.fox)
hill = Source("The Hill", "hill", sections.hill, scrapers.hill)
huffpo = Source("The Huffington Post", "huffpo", sections.huffpo, scrapers.huffpo)
intercept = Source("The Intercept", "intercept", sections.intercept, scrapers.intercept)
jacobin = Source("Jacobin Magazine", "jacobin", sections.jacobin, scrapers.jacobin)
msnbc = Source("MSNBC", "msnbc", sections.msnbc, scrapers.msnbc)
npr = Source("NPR", "npr", sections.npr, scrapers.npr)
nr = Source("National Review", "nr", sections.nr, scrapers.nr)
nypost = Source("The New York Post", "nypost", sections.nypost, scrapers.nypost)
nyt = Source("The New York Times", "nyt", sections.nyt, scrapers.nyt)
politico = Source("Politico", "politico", sections.politico, scrapers.politico)
reason = Source("Reason", "reason", sections.reason, scrapers.reason)
reuters = Source("Reuters", "reuters", sections.reuters, scrapers.reuters)
vox = Source("Vox", "vox", sections.vox, scrapers.vox)
wapo = Source("The Washington Post", "wapo", sections.wapo, scrapers.wapo)
wsj = Source("The Wall Street Journal", "wsj", sections.wsj, scrapers.wsj)

# Create source list (rows of 5)
sources = [ap, bbc, blaze, breitbart, buzzfeed, 
           cnn, dailyMail, dailyWire, fed, fox, 
           hill, huffpo, intercept, jacobin, msnbc, 
           npr, nr, nypost, nyt, politico, 
           reason, reuters, vox, examiner, wapo, 
           wsj]


####################################################
################## Global Vars #####################
####################################################

# Create timestamp
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year


####################################################
################# Load Old Data ####################
####################################################

print("Connecting to DataBase...")
print("")
# Credentials
dbname = "iuawmtcy"
user = "iuawmtcy"
password = "" # Don't commit!!!
host = "salt.db.elephantsql.com"

# Establish connection
pg_conn = psycopg2.connect(dbname=dbname, user=user,
    password=password, host=host)

# Instantiate cursor
pg_curs = pg_conn.cursor()

print("Pulling old data...")
print("")

# Loop over sources
for source in sources:
    pull_data = """
    SELECT article_url FROM news
    WHERE source='""" + str(source.codename) + "';"
    # Execute
    pg_curs.execute(pull_data)
    source.article_URLs = [url[0] for url in pg_curs.fetchall()]


####################################################
################# Scrape Sources ###################
####################################################

print("Scraping:")

# Loop over sources
for paper in sources:
    print(f"--- {paper.name}")
    fresh_articles = []
    paper.scraper(paper.sections, fresh_articles)
    paper.article_URLs = [x for x in fresh_articles if x not in paper.article_URLs]

print("")


####################################################
################## Send to df ######################
####################################################

print('Getting the data ready...')

# Loop over sources
for paper in sources:
    # Create lists for time and source
    paper.article_URLs = list(set(paper.article_URLs))
    paper_source = [paper.codename for i in range(len(paper.article_URLs))]
    paper_days = [day for i in range(len(paper.article_URLs))]
    paper_months = [month for i in range(len(paper.article_URLs))]
    paper_years = [year for i in range(len(paper.article_URLs))]

    # add data to df
    daily_df = pd.DataFrame()
    daily_df["article_URLs"] = paper.article_URLs
    daily_df["source"] = paper_source
    daily_df["day"] = paper_days
    daily_df["month"] = paper_months
    daily_df["year"] = paper_years
    paper.daily_df = daily_df

# Concat all together
df = pd.concat([paper.daily_df for paper in sources])

print("")


####################################################
############## Send to ElephantSQL##################
####################################################

# Clean data for db insertion
dirty_rows = df.values

# Clean up rows
rows = []

for row in dirty_rows:
    rows.append(tuple(row))

print('Adding data to DataBase...')
print("")
# Loop over the array to write rows in the DB
for row in rows:
    insert = """
    INSERT INTO news
    (article_URL, source, day, month, year)
    VALUES 
    """ + str(row) + ';'
    
    pg_curs.execute(insert)

# Save and finish session
pg_curs.close()
pg_conn.commit()

print('all done!')
print("")