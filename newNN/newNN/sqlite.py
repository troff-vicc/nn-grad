import sqlite3


class DateBase:
    def __init__(self):
        self.connection: sqlite3.Connection = sqlite3.connect('../dataNN.db')#tudaSuda/
        self.cursor: sqlite3.Cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()
        
    def close(self):
        self.connection.close()

    def execute(self, request):
        self.cursor.execute(request)
        return self.cursor
        
        
if __name__ == '__main__':
    base = DateBase()
    base.execute(
        f"""CREATE TABLE actions (
            id INT,
            name TEXT,
            description TEXT,
            data TEXT,
            photo_id TEXT
        );"""
                     )
    base.commit()
    base.close()
    
    