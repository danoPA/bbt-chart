import psycopg2

from connect import connect_to_db

# create table for data
conn = connect_to_db()
cur = conn.cursor()
cur.execute("""CREATE TABLE BBT_CHART
        (DATE DATE   NOT NULL,
        TEMP REAL   NOT NULL,
        CYCLE_DAY VARCHAR(4),
        LH_TEST CHAR(1));""")
print 'BBT chart table created successfully'
conn.commit()
conn.close()
