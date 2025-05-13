import psycopg2
import os
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
# Replace these with your actual database connection details
conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
cursor = conn.cursor()  # Use RealDictCursor to fetch data as a dictionary
cursor.execute("ALTER TABLE expenselog ADD category varchar(20);")
#rows = cursor.fetchall()
#print(rows)  # Print the first 10 rows to the console
conn.commit()
conn.close()
