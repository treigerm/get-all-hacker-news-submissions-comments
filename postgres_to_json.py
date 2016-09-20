import json
import psycopg2
import os
from psycopg2.extras import RealDictCursor

host = os.environ['DB']
dbname = "hacker_news"
user = "treigerm"
password = "1234"

conn_string = "host=%s dbname=%s user=%s password=%s" % (host, dbname, user, password)
db = psycopg2.connect(conn_string)
cur = db.cursor(cursor_factory=RealDictCursor)
cur.execute("SELECT * FROM hn_submissions;")

result = []
for row in cur.fetchall():
    row["created_at"] = row["created_at"].isoformat()
    result.append(row)

with open("json/hn_submissions.json", 'w+') as f:
    json.dump(result, f)
