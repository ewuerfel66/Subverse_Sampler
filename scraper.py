"""
News Sampler

- Collect article URL, Source, timestamp into df
- Send df to ElephantSQL
"""

print("--- Subverse News Sampler ---")

####################################################
################### Imports ########################
####################################################

from datetime import datetime
import psycopg2
import pandas as pd

# Local Imports
import sections
import scrapers


####################################################
################## Global Vars #####################
####################################################

# Create timestamp
today = datetime.strftime(datetime.now(), '%m_%d_%y')

# Initialize URL lists
ap_articleURLs = []
breitbart_articleURLs = []
buzzfeed_articleURLs = []
dailyWire_articleURLs = []
examiner_articleURLs = []
fox_articleURLs = []
hill_articleURLs = []
msnbc_articleURLs = []
nyt_articleURLs = []
vox_articleURLs = []
wapo_articleURLs = []
wsj_articleURLs = []


####################################################
################# Scrape Sources ###################
####################################################

print("Scraping:")

# Breitbart News
print("--- Breitbart News")
scrapers.breitbart(sections.breitbart, breitbart_articleURLs)
# Get unique articles
breitbart_articleURLs = list(set(breitbart_articleURLs))

# The Hill
print("--- The Hill")
scrapers.hill(sections.hill, hill_articleURLs)
# Get unique articles
hill_articleURLs = list(set(hill_articleURLs))

# The New York Times
print("--- The New York Times")
scrapers.nyt(sections.nyt, nyt_articleURLs)
# Get unique articles
nyt_articleURLs = list(set(nyt_articleURLs))

# The Washington Examiner
print("--- The Washington Examiner")
scrapers.examiner(sections.examiner, examiner_articleURLs)
# Get unique articles
examiner_articleURLs = list(set(examiner_articleURLs))

# Vox
print("--- Vox")
scrapers.vox(sections.vox, vox_articleURLs)
# Get unique articles
vox_articleURLs = list(set(vox_articleURLs))


####################################################
################## Send to df ######################
####################################################

print("Compiling data for:")


print("--- Breitbart News")
# Create lists for time and source
breitbart_source = ["breitbart" for i in range(len(breitbart_articleURLs))]
breitbart_dates = [today for i in range(len(breitbart_articleURLs))]

# Instantiate df
breitbart_df = pd.DataFrame()

# add data to df
breitbart_df["article_URLs"] = breitbart_articleURLs
breitbart_df["source"] = breitbart_source
breitbart_df["date"] = breitbart_dates


print("--- The Hill")
# Create lists for time and source
hill_source = ["hill" for i in range(len(hill_articleURLs))]
hill_dates = [today for i in range(len(hill_articleURLs))]

# Instantiate df
hill_df = pd.DataFrame()

# add data to df
hill_df["article_URLs"] = hill_articleURLs
hill_df["source"] = hill_source
hill_df["date"] = hill_dates


print("--- The New York Times")
# Create lists for time and source
nyt_source = ["nyt" for i in range(len(nyt_articleURLs))]
nyt_dates = [today for i in range(len(nyt_articleURLs))]

# Instantiate df
nyt_df = pd.DataFrame()

# add data to df
nyt_df["article_URLs"] = nyt_articleURLs
nyt_df["source"] = nyt_source
nyt_df["date"] = nyt_dates


print("--- The Washington Examiner")
# Create lists for time and source
examiner_source = ["examiner" for i in range(len(examiner_articleURLs))]
examiner_dates = [today for i in range(len(examiner_articleURLs))]

# Instantiate df
examiner_df = pd.DataFrame()

# add data to df
examiner_df["article_URLs"] = examiner_articleURLs
examiner_df["source"] = examiner_source
examiner_df["date"] = examiner_dates


print("--- Vox")
# Create lists for time and source
vox_source = ["vox" for i in range(len(vox_articleURLs))]
vox_dates = [today for i in range(len(vox_articleURLs))]

# Instantiate df
vox_df = pd.DataFrame()

# add data to df
vox_df["article_URLs"] = vox_articleURLs
vox_df["source"] = vox_source
vox_df["date"] = vox_dates


# Concatenate the dfs
df = pd.concat([hill_df, examiner_df, nyt_df, breitbart_df, vox_df])


####################################################
############## Send to ElephantSQL##################
####################################################

print("Sending to DataBase:")

print("Connecting...")
# Credentials
dbname = "iuawmtcy"
user = "iuawmtcy"
password = "sEYOf2cgU7ieV-RreMPEHx0_5ypOZG6C" # Don't commit!!!
host = "salt.db.elephantsql.com"

# Establish connection
pg_conn = psycopg2.connect(dbname=dbname, user=user,
    password=password, host=host)

# Instantiate cursor
pg_curs = pg_conn.cursor()

# Clean data for db insertion
print('Getting the data ready...')
dirty_rows = df.values

# Clean up rows
rows = []

for row in dirty_rows:
    rows.append(tuple(row))

print('adding data to DataBase...')
# Loop over the array to write rows in the DB
for row in rows:
    insert = """
    INSERT INTO news
    (article_URL, source, date)
    VALUES 
    """ + str(row) + ';'
    
    pg_curs.execute(insert)

# Save and finish session
pg_curs.close()
pg_conn.commit()

print('all done!')