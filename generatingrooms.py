import pymysql
import random

# Replace these values with your actual database connection details
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'system'
DB_NAME = 'pythonproject2'

# Sample data for room attributes
floor_choices = [1, 2, 3, 4, 5]
type_choices = ['AC', 'Non AC']
category_choices = ['Dulix', 'Luxurious','Normal','Suite']
status_choices = [0, 1]

# Function to generate random room data
def generate_random_room_data():
    number = random.randint(100, 999)
    floor = random.choice(floor_choices)
    description = f"Room {number} on floor {floor}"
    room_type = random.choice(type_choices)
    occupancy = random.randint(1, 5)
    category = random.choice(category_choices)
    price = round(random.uniform(50, 300), 2)
    status = random.choice(status_choices)
    return (number, floor, description, room_type, occupancy, category, price, status)

def insert_data():
    try:
        # Connect to the database
        connection = pymysql.connect(
        host='localhost',
        user='root',
        password='system',
        database='pythonproject2'
    )

        # Create a cursor to interact with the database
        cursor = connection.cursor()


        # SQL statement to insert data into the "rooms" table
        insert_query = "INSERT INTO rooms (name, floor, description, type, occupancy, category, price, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        # Generate and insert 50 rows of room data
        for _ in range(50):
            room_data = generate_random_room_data()
            cursor.execute(insert_query, room_data)

        # Commit the changes to the database
        connection.commit()

        print("Successfully inserted 50 rows.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if connection:
            connection.close()

if __name__ == "__main__":
    insert_data()
