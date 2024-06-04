import mysql.connector as sqlcon
# from mysql.connector import Error
from dotenv import load_dotenv
import os
import hashlib
import psycopg2
from psycopg2 import Error

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '.env')

DATABASE_URL = "postgres://default:vxaClStN9b6w@ep-wandering-bonus-a1vnxdai.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
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
        """
        Establishes a connection to the MySQL database using the credentials provided during initialization.
        Prints a message if the connection is successful, otherwise prints the error message.
        """

        try:
            # self.connection = sqlcon.connect(
            #     host=self.host,
            #     user=self.user,
            #     password=self.password,
            #     database=self.database
            # )

            self.connection = psycopg2.connect(DATABASE_URL)
            if self.connection:
                print("Connected to the database")
        except sqlcon.Error as err:
            print(f"Error: {err}")

    def close(self):

        """
        Closes the database connection if it is open.
        Prints a message if the connection is successfully closed.
        """

        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connection closed")

    def create_database(self):
        
        """
        Creates a database and a table (dispatcher) if they do not exist. 
        The dispatcher table is designed to store user information.
        Prints a message if the operation is successful, otherwise prints the error message.
        """
        

        try:
            self.connection = psycopg2.connect(DATABASE_URL)

            cursor = self.connection.cursor()
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


    def register_user(self, username, password, name, job_position):
        
        """
        Registers a new user by inserting their information into the dispatcher table.
        The password is hashed using SHA-256 before storage.
        
        Parameters:
            username (str): The user's username.
            password (str): The user's password.
            name (str): The user's name.
            job_position (str): The user's job position.
        
        Returns:
            bool: True if the user is successfully registered, False if an error occurs during registration.
        
        Prints a message if the operation is successful, otherwise prints the error message.
        """
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO dispatcher (username, password, user_name, job_position) VALUES (%s, %s, %s, %s)", 
                (username, hashed_password, name, job_position)
            )
            self.connection.commit()
            print("User registered successfully")
            return True
        except Error as err:
            print(f"Error: {err}")
            return False
        finally:
            if cursor:
                cursor.close()


    def login_user(self, username, password):

        """
        Authenticates a user by checking their username and hashed password against the records in the dispatcher table.
        
        Parameters:
            username (str): The user's username.
            password (str): The user's password.
        
        Returns:
            bool: True if the username and password match a record in the database, False otherwise or if an error occurs.
        
        Prints a message if the authentication is successful, otherwise prints the error message.
        """

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = None
        try:
            if self.connection and self.connection.status == psycopg2.extensions.STATUS_READY:
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
# if __name__ == "__main__":
    
    # db = DatabaseConnection()
    # # db.create_database()
    # db.connect()

    # username = input("Enter username for registration: ")
    # password = input("Enter password for registration: ")
    # nama_user = input("Enter name for registration: ")
    # jabatan = input("Enter position for registration: ")
    # db.register_user(username, password, nama_user, jabatan)

# Login with the registered user
    # username = input("Enter username for login: ")
    # password = input("Enter password for login: ")
    # db.login_user(username, password)
    
   
