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

# Fox
print("--- Fox News")
scrapers.fox(sections.fox, fox_articleURLs)
# Get unique articles
fox_articleURLs = list(set(fox_articleURLs))

print("")


####################################################
################## Send to df ######################
####################################################

print("Compiling data for:")


print("--- Fox News")
# Create lists for time and source
fox_source = ["fox" for i in range(len(fox_articleURLs))]
fox_days = [day for i in range(len(fox_articleURLs))]
fox_months = [month for i in range(len(fox_articleURLs))]
fox_years = [year for i in range(len(fox_articleURLs))]

# Instantiate df
fox_df = pd.DataFrame()

# add data to df
fox_df["article_URLs"] = fox_articleURLs
fox_df["source"] = fox_source
fox_df["day"] = fox_days
fox_df["month"] = fox_months
fox_df["year"] = fox_years


# Concatenate the dfs
df = pd.concat([fox_df])

print(len(fox_articleURLs))
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
