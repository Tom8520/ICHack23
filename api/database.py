import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connect():
    return mysql.connector.connect(
        user=os.getenv("DATABASE_USERNAME"),
        password=os.getenv("DATABASE_PASSWORD"),
        host='fi1.billigerhost.com',
        port=3306,
        database='s163_ICHack'
    )