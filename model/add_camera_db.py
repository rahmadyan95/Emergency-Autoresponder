import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '.env')

load_dotenv(env_path)

class camera_db: 
    def __init__(self):
        link : str = os.getenv('DATABASE_URL')
        self.link = link
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(self.link)
            if self.connection :
                print('connection successfully')

        except Error as err :
            print(err)
    
    def close(self):
        if self.connection and self.connection.isexecuting:
            self.connection.close()
            print("Connection closed")

    def add_unit(self,id_camera,latitude,longitude):
        self.connect()
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO camera_data (id_camera, latitude, longitude) VALUES (%s, %s, %s)", 
                (id_camera,latitude, longitude)
            )
            self.connection.commit()
            print("User registered successfully")
        
        except Error as err:
            print(err)

        finally :
            if cursor:
                cursor.close()

    def get_all_camera_data(self):
        connection = psycopg2.connect(self.link)
        """Retrieves all camera data from the 'camera_data' table.

        Returns:
            list: A list of tuples containing camera data (id_camera, latitude, longitude).

        Raises:
            psycopg2.Error: If an error occurs during data retrieval.
        """
         # Connect to database
        if not connection:
            return None

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM camera_data")
            camera_data = cursor.fetchall()
            return camera_data
        except Error as err:
            print(f"Error retrieving camera data: {err}")
            raise
        finally:
            if cursor:
                cursor.close()
            

# instance = camera_db()
# camera_data = instance.get_all_camera_data()

# instance.add_unit('DMC34342488','-6.24223','4.32943034')
# instance.add_unit('DMC34wdwdwd','-6.24223','4.32946034')
# instance.add_unit('fMC34wdwdwd','-6.24223','4.32343034')
# for camera_tuple in camera_data:
#     camera_id, camera_code, latitude, longitude = camera_tuple
#     print(f"Camera ID: {camera_id}, Code: {camera_code}, Latitude: {latitude}, Longitude: {longitude}")