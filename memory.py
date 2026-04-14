import sqlite3

conn = sqlite3.connect("data/db.sqlite")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS chat(
id INTEGER PRIMARY KEY,
user TEXT,
bot TEXT
)
""")

def save(u, b):
    c.execute("INSERT INTO chat (user, bot) VALUES (?,?)", (u,b))
    conn.commit()