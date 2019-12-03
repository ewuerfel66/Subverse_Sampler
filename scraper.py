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

# The Hill
print("Scraping: The Hill")
scrapers.hill(sections.hill, hill_articleURLs)
# Get unique articles
hill_articleURLs = list(set(hill_articleURLs))


####################################################
################## Send to df ######################
####################################################

print("Compiling data for:")


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
dirty_rows = hill_df.values

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