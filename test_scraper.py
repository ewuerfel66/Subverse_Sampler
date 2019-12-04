"""
News Sampler

- Scrape article URL, source, and timestamp from sources
- Compile data into DataFrame
- Send DataFrame to ElephantSQL DataBase
"""

print("")
print("-------------------------")
print("--- Test News Sampler ---")
print("-------------------------")
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


####################################################
################## Global Vars #####################
####################################################

# Create timestamp
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year

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

# msnbc
print("--- MSNBC")
scrapers.msnbc(sections.msnbc, msnbc_articleURLs)
# Get unique articles
msnbc_articleURLs = list(set(msnbc_articleURLs))

print("")


####################################################
################## Send to df ######################
####################################################

print("Compiling data for:")


print("--- MSNBC")
# Create lists for time and source
msnbc_source = ["msnbc" for i in range(len(msnbc_articleURLs))]
msnbc_days = [day for i in range(len(msnbc_articleURLs))]
msnbc_months = [month for i in range(len(msnbc_articleURLs))]
msnbc_years = [year for i in range(len(msnbc_articleURLs))]

# Instantiate df
msnbc_df = pd.DataFrame()

# add data to df
msnbc_df["article_URLs"] = msnbc_articleURLs
msnbc_df["source"] = msnbc_source
msnbc_df["day"] = msnbc_days
msnbc_df["month"] = msnbc_months
msnbc_df["year"] = msnbc_years


# Concatenate the dfs
df = pd.concat([msnbc_df])

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
