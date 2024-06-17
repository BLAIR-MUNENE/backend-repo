import sqlite3
TABLE_NAME = "bookings"
class Booking:
    
    def __init__(self, id, name , age, phoneNumber, email, Paymentdetails, eventid) -> None:
        self.id = None
        self.name = name
        self.age = age
        self.phoneNumber = phoneNumber
        self.email = email
        self.Paymentdetails = Paymentdetails
        self.eventid = eventid 
    
    def save(self):
        insert_values_sql = f"""
            INSERT INTO {TABLE_NAME} (name, age, phoneNumber, email, Paymentdetails, eventid) 
            VALUES (?,?,?,?,?,?)
        """
        with sqlite3.connect('db.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute(insert_values_sql, (self.name, self.age, self.phoneNumber, self.email, self.Paymentdetails, self.eventid))
            conn.commit()
        return self
    def to_dict(self):
        return {
            "id" : self.id,
            "name" :self.name,
            "age": self.age,
            "phoneNumber": self.phoneNumber,
            "email": self.email,
            "Paymentdetails": self.Paymentdetails,
            
        }