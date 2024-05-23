import mysql.connector as sqlcon
from mysql.connector import Error
from dotenv import load_dotenv
import os
import hashlib

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '.env')

load_dotenv(env_path)


class DatabaseConnection:
    def __init__(self):

        host: str = os.getenv('HOST')
        user: str = os.getenv('USER')
        password: str = os.getenv('PASSWORD')
        database: str = os.getenv('DATABASE')
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlcon.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to the database")
        except sqlcon.Error as err:
            print(f"Error: {err}")

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connection closed")

    def create_database(self):
        try:
            self.connection = sqlcon.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = self.connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            cursor.execute(f"USE {self.database}")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS dispatcher (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL,
                    user_name VARCHAR(255) NOT NULL,
                    job_position VARCHAR(255) NOT NULL
                )
            """)
            self.connection.commit()
            print("Database and table created")
        except Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()


    def register_user(self, username, password, nama_user, jabatan):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO dispatcher (username, password, user_name, job_position) VALUES (%s, %s, %s, %s)", 
                (username, hashed_password, nama_user, jabatan)
            )
            self.connection.commit()
            print("User registered successfully")
        except Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()

    # def login_user(self, username, password):
    #     hashed_password = hashlib.sha256(password.encode()).hexdigest()
    #     cursor = None
    #     try:
    #         cursor = self.connection.cursor()
    #         cursor.execute("SELECT * FROM dispatcher WHERE username = %s AND password = %s", (username, hashed_password))
    #         user = cursor.fetchone()
    #         if user:
    #             print("Login successful")
    #             return True
    #         else:
    #             print("Invalid username or password")
    #             return False
    #     except Error as err:
    #         print(f"Error: {err}")
    #     finally:
    #         if cursor:
    #             cursor.close()

    def login_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = None
        try:
            if self.connection and self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM dispatcher WHERE username = %s AND password = %s", (username, hashed_password))
                user = cursor.fetchone()
                if user:
                    print("Login successful")
                    return True
                else:
                    print("Invalid username or password")
                    return False
            else:
                print("No database connection available for logging in")
                return False
        except Error as err:
            print(f"Error: {err}")
            return False
        finally:
            if cursor:
                cursor.close()

# Usage
if __name__ == "__main__":
    
    db = DatabaseConnection()
    db.create_database()
    db.connect()

    # username = input("Enter username for registration: ")
    # password = input("Enter password for registration: ")
    # nama_user = input("Enter name for registration: ")
    # jabatan = input("Enter position for registration: ")
    # db.register_user(username, password, nama_user, jabatan)

    # Login with the registered user
    username = input("Enter username for login: ")
    password = input("Enter password for login: ")
    db.login_user(username, password)
    
   
