import sqlite3

posts = (("Good", "I'm Good"),("Well", "I'm Well"),("Okay", "I'm Okay"),("Excellent", "I'm Excellent"),)
with sqlite3.connect("blog.db") as conn:
	cursor = conn.cursor()
	cursor.execute("DROP TABLE IF EXISTS posts")
	cursor.execute("CREATE TABLE posts (title TEXT, post TEXT)")
	cursor.executemany("INSERT INTO posts VALUES(?,?)", posts)