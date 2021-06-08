from db.db_config import conn

# Pull data from database to excel

def fetch_data(query):
    cur = conn.cursor()

    cur.execute(query)

    records = cur.fetchall()

    return records



