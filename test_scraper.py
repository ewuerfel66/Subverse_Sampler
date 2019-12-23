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
bloom = Source("Bloomberg", "bloom", sections.bloom, scrapers.bloom)
breitbart = Source("Breitbart", "breitbart", sections.breitbart, scrapers.breitbart)
buzzfeed = Source("Buzzfeed News", "buzzfeed", sections.buzzfeed, scrapers.buzzfeed)
dailyWire = Source("The Daily Wire", "dailyWire", sections.dailyWire, scrapers.dailyWire)
examiner = Source("The Washington Examiner", "examiner", sections.examiner, scrapers.examiner)
fox = Source("Fox News", "fox", sections.fox, scrapers.fox)
hill = Source("The Hill", "hill", sections.hill, scrapers.hill)
huffpo = Source("The Huffington Post", "huffpo", sections.huffpo, scrapers.huffpo)
msnbc = Source("MSNBC", "msnbc", sections.msnbc, scrapers.msnbc)
nr = Source("National Review", "nr", sections.nr, scrapers.nr)
nypost = Source("The New York Post", "nypost", sections.nypost, scrapers.nypost)
nyt = Source("The New York Times", "nyt", sections.nyt, scrapers.nyt)
reason = Source("Reason", "reason", sections.reason, scrapers.reason)
vox = Source("Vox", "vox", sections.vox, scrapers.vox)
wapo = Source("The Washington Post", "wapo", sections.wapo, scrapers.wapo)
wsj = Source("The Wall Street Journal", "wsj", sections.wsj, scrapers.wsj)

# Create source list
sources = [ap, breitbart, buzzfeed, dailyWire, fox, hill, 
           huffpo, msnbc, nr, nypost, nyt, 
           reason, vox, examiner, wapo, wsj]


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

# Loop over sources
for source in sources:
    print(f"--- {source.name}")
    pull_data = """
    SELECT article_url FROM news_test
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

print("Compiling data for:")

# Loop over sources
for paper in sources:
    # Create lists for time and source
    print(f"--- {paper.name}")
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

print("Sending to DataBase:")

# Clean data for db insertion
print('--- Getting the data ready...')
dirty_rows = df.values

# Clean up rows
rows = []

for row in dirty_rows:
    rows.append(tuple(row))

print('--- Adding data to DataBase...')
# Loop over the array to write rows in the DB
for row in rows:
    insert = """
    INSERT INTO news_test
    (article_URL, source, day, month, year)
    VALUES 
    """ + str(row) + ';'
    
    pg_curs.execute(insert)

# Save and finish session
pg_curs.close()
pg_conn.commit()

print("")
print('all done!')