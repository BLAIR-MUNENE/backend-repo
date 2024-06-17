import sqlite3

class Event:
    TABLE_NAME = "events"

    def __init__(self, id, image, description, location, time, price) -> None:
        self.id = None
        self.image = image
        self.description = description
        self.location = location
        self.time = time
        self.price = price

    def save(self):
        # Create table if it doesn't exist
        create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image BLOB NOT NULL,
                description TEXT,
                location TEXT,
                time REAL,
                price INTEGER
            )
        """
        with sqlite3.connect('db.sqlite') as conn:  # Replace 'your_database.db' with your actual database file name
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
            conn.commit()
            self.id = cursor.lastrowid 

            # Insert event details
            insert_values_sql = f"""
                INSERT INTO {self.TABLE_NAME} (image, description, location, time, price) 
                VALUES (?,?,?,?,?)
            """
            cursor.execute(insert_values_sql, (self.image, self.description, self.location, self.time, self.price))
            conn.commit()

    def to_dict(self):
        return {
            "id" : self.id,
            "image": self.image,
            "description" : self.description,
            "location ": self.location,
            "time": self.time,
            "price" : self.price
        }

    @classmethod
    def find_all(cls):
        with sqlite3.connect('db.sqlite') as conn:  # Ensure a new connection is made here
            cursor = conn.cursor()
            sql = f"""
                 SELECT * FROM {cls.TABLE_NAME}
            """
            rows = cursor.execute(sql).fetchall()
            
            return [
                cls.row_to_instance(row).to_dict() for row in rows
            ]

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None
        return cls(row[0], row[1], row[2], row[3], row[4], row[5])

# Example usage

career_day = Event(1,"https://example.com/image.jpg","Description","Location","10:30",500)
career_day.save()
print(Event.find_all())
