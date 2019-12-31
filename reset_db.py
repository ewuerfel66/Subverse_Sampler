import psycopg2

print("Connecting...")
# Credentials
dbname = "jfblqfwt"
user = "jfblqfwt"
password = "" # Don't commit!!!
host = "rajje.db.elephantsql.com"

# Establish connection
pg_conn = psycopg2.connect(dbname=dbname, user=user,
    password=password, host=host)

# Instantiate cursor
pg_curs = pg_conn.cursor()

# Statements
drop = """
DROP TABLE news_test;
"""

create = """
CREATE TABLE news_test (
    id SERIAL PRIMARY KEY,
    article_URL VARCHAR(500),
    source VARCHAR(20),
    day INTEGER,
    month INTEGER,
    year INTEGER
)
"""

# Execute statements
print("Droppin old `news_test` table...")
pg_curs.execute(drop)
print("Creating new `news_test` table...")
pg_curs.execute(create)

# Close up
pg_curs.close()
pg_conn.commit()

print('--- All done! ---')
print("")