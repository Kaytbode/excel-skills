from db_config import conn

query1 = "CREATE TABLE sers (id serial PRIMARY KEY, name VARCHAR, location VARCHAR, age INT)"

query2 = "CREATE TABLE department (dept_id serial PRIMARY KEY, student INT references users(id), department VARCHAR)"

users_values = (("Kayode", "Lagos", 34), ("Seyi", "Lagos", 45), ("Uche", "Imo", 45), ("Adamu", "Kano", 13), ("Bill", "Atlanta", 100))

dept_values = ((2, "Sociology"), (3, "Sociology"), (1, "Biology"), (5, "Computer science"))

cur = conn.cursor()

cur.execute(query1)
cur.execute(query2)
cur.executemany("INSERT INTO sers (name, location, age) VALUES (%s, %s, %s)", users_values)
cur.executemany("INSERT INTO department (student, department) VALUES (%s, %s)", dept_values)

# Needed for changes to be persistent
conn.commit()
cur.close()
conn.close()