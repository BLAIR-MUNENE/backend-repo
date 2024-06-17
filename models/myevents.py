import sqlite3

class MyEvents:
    
    TABLE_NAME = "myevents"

    def __init__(self,id, image, description, location, time) -> None:
        self.id = None
        self.image = image
        self.description = description
        self.location = location
        self.time = time

    def save(self):
        
        create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image BLOB NOT NULL,
                description TEXT,
                location TEXT,
                time REAL
            )
        """
        with sqlite3.connect('db.sqlite') as conn: 
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
            conn.commit()
            self.id = cursor.lastrowid

            insert_values_sql = f"""
                INSERT INTO {self.TABLE_NAME} (image, description, location, time) 
                VALUES (?,?,?,?)
            """
            cursor.execute(insert_values_sql, (self.image, self.description, self.location, self.time))
            conn.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "image": self.image,
            "description": self.description,
            "location": self.location,
            "time": self.time,
        }

    @classmethod
    def find_all(cls):
        with sqlite3.connect('db.sqlite') as conn:  
            cursor = conn.cursor()
            sql = f"""
                 SELECT * FROM {cls.TABLE_NAME}
            """
            rows = cursor.execute(sql).fetchall()
            
            return [
                cls(row[0], row[1], row[2], row[3]).to_dict() for row in rows
            ]

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None
        return cls(row[1], row[2], row[3], row[4])

