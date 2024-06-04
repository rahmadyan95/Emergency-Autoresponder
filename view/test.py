DATABASE_URL = "postgres://default:vxaClStN9b6w@ep-wandering-bonus-a1vnxdai.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
import psycopg2

# Replace with your Vercel database connection details


# Create a connection to the Vercel database
try:
    connection = psycopg2.connect(DATABASE_URL)
    print("Connected to Vercel database successfully")
except psycopg2.Error as e:
    print("Error connecting to Vercel database:", e)
    exit()

# Create the dispatcher table
cursor = connection.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS dispatcher (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  user_name VARCHAR(255) NOT NULL,
  job_position VARCHAR(255) NOT NULL
);
"""
cursor.execute(create_table_query)
connection.commit()
print("Dispatcher table created successfully")

# Close the database connection
connection.close()
print("Database connection closed")
