import psycopg2

print("Connecting...")
# Credentials
dbname = "iuawmtcy"
user = "iuawmtcy"
<<<<<<< HEAD
password = "uZH51Pcq9N6jamL5our1dz9PoZGTRK9r" # Don't commit!!!
=======
password = "" # Don't commit!!!
>>>>>>> 05b32abddf1eaf6c9a32e450eb9b458595d88fd0
host = "salt.db.elephantsql.com"

# Establish connection
pg_conn = psycopg2.connect(dbname=dbname, user=user,
    password=password, host=host)

# Instantiate cursor
pg_curs = pg_conn.cursor()

# Statements
drop = """
DROP TABLE news;
"""

create = """
CREATE TABLE news (
    id SERIAL PRIMARY KEY,
    article_URL VARCHAR(500),
    source VARCHAR(20),
    date VARCHAR(12)
)
"""

# Execute statements
print("Droppin old `news` table...")
pg_curs.execute(drop)
print("Creating new `news` table...")
pg_curs.execute(create)

# Close up
pg_curs.close()
pg_conn.commit()

print('all done!')
