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

# Breitbart News
print("--- Breitbart")
scrapers.breitbart(sections.breitbart, breitbart_articleURLs)
# Get unique articles
breitbart_articleURLs = list(set(breitbart_articleURLs))

# The Washington Examiner
print("--- The Washington Examiner")
scrapers.examiner(sections.examiner, examiner_articleURLs)
# Get unique articles
examiner_articleURLs = list(set(examiner_articleURLs))

# The Hill
print("--- The Hill")
scrapers.hill(sections.hill, hill_articleURLs)
# Get unique articles
hill_articleURLs = list(set(hill_articleURLs))

# MSNBC
print("--- MSNBC")
scrapers.msnbc(sections.msnbc, msnbc_articleURLs)
# Get unique articles
msnbc_articleURLs = list(set(msnbc_articleURLs))

# The New York Times
print("--- The New York Times")
scrapers.nyt(sections.nyt, nyt_articleURLs)
# Get unique articles
nyt_articleURLs = list(set(nyt_articleURLs))

# Vox
print("--- Vox")
scrapers.vox(sections.vox, vox_articleURLs)
# Get unique articles
vox_articleURLs = list(set(vox_articleURLs))

# The Washington Post
print("--- The Washington Post")
scrapers.wapo(sections.wapo, wapo_articleURLs)
# Get unique articles
wapo_articleURLs = list(set(wapo_articleURLs))

# The Wall Street Journal
print("--- The Wall Street Journal")
scrapers.wsj(sections.wsj, wsj_articleURLs)
# Get unique articles
wsj_articleURLs = list(set(wsj_articleURLs))

print("")


####################################################
################## Send to df ######################
####################################################

print("Compiling data for:")


print("--- Breitbart")
# Create lists for time and source
breitbart_source = ["breitbart" for i in range(len(breitbart_articleURLs))]
breitbart_days = [day for i in range(len(breitbart_articleURLs))]
breitbart_months = [month for i in range(len(breitbart_articleURLs))]
breitbart_years = [year for i in range(len(breitbart_articleURLs))]

# Instantiate df
breitbart_df = pd.DataFrame()

# add data to df
breitbart_df["article_URLs"] = breitbart_articleURLs
breitbart_df["source"] = breitbart_source
breitbart_df["day"] = breitbart_days
breitbart_df["month"] = breitbart_months
breitbart_df["year"] = breitbart_years


print("--- The Washington Examiner")
# Create lists for time and source
examiner_source = ["examiner" for i in range(len(examiner_articleURLs))]
examiner_days = [day for i in range(len(examiner_articleURLs))]
examiner_months = [month for i in range(len(examiner_articleURLs))]
examiner_years = [year for i in range(len(examiner_articleURLs))]

# Instantiate df
examiner_df = pd.DataFrame()

# add data to df
examiner_df["article_URLs"] = examiner_articleURLs
examiner_df["source"] = examiner_source
examiner_df["day"] = examiner_days
examiner_df["month"] = examiner_months
examiner_df["year"] = examiner_years


print("--- The Hill")
# Create lists for time and source
hill_source = ["hill" for i in range(len(hill_articleURLs))]
hill_days = [day for i in range(len(hill_articleURLs))]
hill_months = [month for i in range(len(hill_articleURLs))]
hill_years = [year for i in range(len(hill_articleURLs))]

# Instantiate df
hill_df = pd.DataFrame()

# add data to df
hill_df["article_URLs"] = hill_articleURLs
hill_df["source"] = hill_source
hill_df["day"] = hill_days
hill_df["month"] = hill_months
hill_df["year"] = hill_years

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


print("--- The New York Times")
# Create lists for time and source
nyt_source = ["nyt" for i in range(len(nyt_articleURLs))]
nyt_days = [day for i in range(len(nyt_articleURLs))]
nyt_months = [month for i in range(len(nyt_articleURLs))]
nyt_years = [year for i in range(len(nyt_articleURLs))]

# Instantiate df
nyt_df = pd.DataFrame()

# add data to df
nyt_df["article_URLs"] = nyt_articleURLs
nyt_df["source"] = nyt_source
nyt_df["day"] = nyt_days
nyt_df["month"] = nyt_months
nyt_df["year"] = nyt_years


print("--- Vox")
# Create lists for time and source
vox_source = ["vox" for i in range(len(vox_articleURLs))]
vox_days = [day for i in range(len(vox_articleURLs))]
vox_months = [month for i in range(len(vox_articleURLs))]
vox_years = [year for i in range(len(vox_articleURLs))]

# Instantiate df
vox_df = pd.DataFrame()

# add data to df
vox_df["article_URLs"] = vox_articleURLs
vox_df["source"] = vox_source
vox_df["day"] = vox_days
vox_df["month"] = vox_months
vox_df["year"] = vox_years


print("--- The Washington Post")
# Create lists for time and source
wapo_source = ["wapo" for i in range(len(wapo_articleURLs))]
wapo_days = [day for i in range(len(wapo_articleURLs))]
wapo_months = [month for i in range(len(wapo_articleURLs))]
wapo_years = [year for i in range(len(wapo_articleURLs))]

# Instantiate df
wapo_df = pd.DataFrame()

# add data to df
wapo_df["article_URLs"] = wapo_articleURLs
wapo_df["source"] = wapo_source
wapo_df["day"] = wapo_days
wapo_df["month"] = wapo_months
wapo_df["year"] = wapo_years


print("--- The Wall Street Journal")
# Create lists for time and source
wsj_source = ["wsj" for i in range(len(wsj_articleURLs))]
wsj_days = [day for i in range(len(wsj_articleURLs))]
wsj_months = [month for i in range(len(wsj_articleURLs))]
wsj_years = [year for i in range(len(wsj_articleURLs))]

# Instantiate df
wsj_df = pd.DataFrame()

# add data to df
wsj_df["article_URLs"] = wsj_articleURLs
wsj_df["source"] = wsj_source
wsj_df["day"] = wsj_days
wsj_df["month"] = wsj_months
wsj_df["year"] = wsj_years


# Concatenate the dfs
df = pd.concat([hill_df, examiner_df, nyt_df, breitbart_df, 
                vox_df, wsj_df, wapo_df, msnbc_df])

print("")


####################################################
############## Send to ElephantSQL##################
####################################################

print("Sending to DataBase:")

print("--- Connecting...")
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
