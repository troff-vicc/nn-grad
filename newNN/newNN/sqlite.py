import sqlite3


class DateBase:
    def __init__(self):
        self.connection: sqlite3.Connection = sqlite3.connect('newNN/dataNN.db')#newNN
        self.cursor: sqlite3.Cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()
        
    def close(self):
        self.connection.close()

    def execute(self, request):
        self.cursor.execute(request)
        return self.cursor
    
    def create_function(self, name, cp, func):
        self.connection.create_function(name, cp, func)
        
        
if __name__ == '__main__':
    base = DateBase()
    import base64
    
    print(base.execute("PRAGMA table_info('hotels');").fetchall())
    
    
    
    '''
    
    with open('img.png', mode='rb') as img_file:
        image_64_encode = base64.b64encode(img_file.read())
    a = base.execute(
        f"""INSERT INTO imgs (id, imgData)
        VALUES ('1', "{image_64_encode}")"""
    )
    
    base.execute(
        f"""CREATE TABLE hotels (
            id INT,
            name TEXT,
            address TEXT,
            description TEXT,
            contacts TEXT,
            categories TEXT,
            district TEXT,
            stars INT,
            photo_id TEXT
        );""" [('actions',), ('places',), ('hotels',), ('imgs',)]
    )'''
    base.commit()
    base.close()
    

    
    