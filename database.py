import psycopg2
from dotenv import load_dotenv 
import os

# Load environment variables from .env file
load_dotenv()

#Database credentials from .env file
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def connect_to_database():
    try:
        #Establish connection to PostgreSQL
        connection = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        
        print("Connected to the PostgreSQL database successfully!")
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        
def create_tables():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        try:
            # Creating tables (Movies and Customers)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                genre VARCHAR(100),
                release_year INT,
                available_copies INT DEFAULT 1,
                total_copies INT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS customers (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                phone VARCHAR(15),
                membership_status VARCHAR(20) DEFAULT 'Active'
            );
            """)

            connection.commit()
            print("✅ Tables created successfully!")
        except Exception as e:
            print("❌ Error creating tables:", e)
        finally:
            cursor.close()
            connection.close()
    else:
        print("❌ Could not connect to the database.")

# Test the connection and table creation
if __name__ == "__main__":
    create_tables()