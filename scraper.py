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
breitbart = Source("Breitbart", "breitbart", sections.breitbart, scrapers.breitbart)
examiner = Source("The Washington Examiner", "examiner", sections.examiner, scrapers.examiner)
fox = Source("Fox News", "fox", sections.fox, scrapers.fox)
hill = Source("The Hill", "hill", sections.hill, scrapers.hill)
msnbc = Source("MSNBC", "msnbc", sections.msnbc, scrapers.msnbc)
nypost = Source("The New York Post", "nypost", sections.nypost, scrapers.nypost)
nyt = Source("The New York Times", "nyt", sections.nyt, scrapers.nyt)
vox = Source("Vox", "vox", sections.vox, scrapers.vox)
wapo = Source("The Washington Post", "wapo", sections.wapo, scrapers.wapo)
wsj = Source("The Wall Street Journal", "wsj", sections.wsj, scrapers.wsj)

# Create source list
sources = [ap, breitbart, fox, hill, msnbc, nypost, nyt, vox, examiner, wapo, wsj]


####################################################
################## Global Vars #####################
####################################################

# Create timestamp
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year


####################################################
################# Scrape Sources ###################
####################################################

print("Scraping:")

# Loop over sources
for paper in sources:
    print(f"--- {paper.name}")
    # print(paper.sections[0], paper.article_URLs[0])
    new_articles = []
    paper.scraper(paper.sections, new_articles)
    paper.article_URLs = new_articles

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

print("--- Connecting...")
# Credentials
dbname = "iuawmtcy"
user = "iuawmtcy"
password = "UnWCQ5-4ymEJCpY5Tly-F7ZXXONAEx7i" # Don't commit!!!
host = "salt.db.elephantsql.com"

# Establish connection
pg_conn = psycopg2.connect(dbname=dbname, user=user,
    password=password, host=host)

# Instantiate cursor
pg_curs = pg_conn.cursor()

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
    INSERT INTO news
    (article_URL, source, day, month, year)
    VALUES 
    """ + str(row) + ';'
    
    pg_curs.execute(insert)

# Save and finish session
pg_curs.close()
pg_conn.commit()

print("")
print('all done!')
