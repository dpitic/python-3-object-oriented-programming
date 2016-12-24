import sqlite3

"""
This script creates a database and populates it with sample data.
"""

conn = sqlite3.connect('sales.db')

conn.execute("CREATE TABLE Sales (salesperson TEXT, "
             "amt currency, year INTEGER, model TEXT, new BOOLEAN)")
conn.execute("INSERT INTO Sales VALUES"
             " ('Tim', 16000, 2010, 'Honda Fit', 'true')")
conn.execute("INSERT INTO Sales VALUES"
             " ('Tim', 9000, 2006, 'Ford Focus', 'false')")
conn.execute("INSERT INTO Sales VALUES"
             " ('Gayle', 8000, 2004, 'Dodge Neon', 'false')")
conn.execute("INSERT INTO Sales VALUES"
             " ('Gayle', 28000, 2009, 'Ford Mustang', 'true')")
conn.execute("INSERT INTO Sales VALUES"
             " ('Gayle', 50000, 2010, 'Lincoln Navigator', 'true')")
conn.execute("INSERT INTO Sales VALUES"
             " ('Don', 20000, 2008, 'Toyota Prius', 'false')")
conn.commit()
conn.close()
