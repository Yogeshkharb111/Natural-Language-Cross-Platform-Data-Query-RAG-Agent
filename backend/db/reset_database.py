"""
Script to completely reset the MySQL database if needed
"""
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def reset_mysql_database():
    """
    Completely reset the MySQL database by dropping and recreating it
    """
    try:
        # Connect without specifying database
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD")
        )
        cursor = connection.cursor()

        # Drop and recreate database
        db_name = os.getenv("MYSQL_DB")
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cursor.execute(f"CREATE DATABASE {db_name}")
        
        print(f"✅ Database {db_name} reset successfully!")
        
        cursor.close()
        connection.close()
        
    except Exception as e:
        print(f"❌ Database reset failed: {e}")

if __name__ == "__main__":
    print("🔄 Resetting MySQL database...")
    reset_mysql_database()
    print("✅ Reset complete! Now run: python run_server.py")
