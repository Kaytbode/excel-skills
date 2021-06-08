import os
import urllib.parse as up
import psycopg2 as pg

# connection to external database (elephantsql)
up.uses_netloc.append("postgres")

url = up.urlparse(os.environ["DB_URL"])

conn = pg.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)

