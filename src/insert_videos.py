from db_conn import conn
from sqlalchemy import text

sql = "INSERT INTO user_login (username, password, email) VALUES ('John Doe', 'password123', 'johndoe@example.com')"

conn.execute(text(sql))
conn.commit()

conn.close()
