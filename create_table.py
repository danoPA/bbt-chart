import psycopg2

from connect import connect_to_db

# add argparse for options via command line

# check if table has already been created

# create table for data
conn = connect_to_db()
cur = conn.cursor()
cur.execute("""CREATE TABLE BBT_CHART
        (DATE DATE   NOT NULL,
        TEMP REAL   NOT NULL);""")
print 'BBT chart table created successfully'
conn.commit()
conn.close()