import sqlite3


class DateBase:
    def __init__(self):
        self.connection: sqlite3.Connection = sqlite3.connect('../dataNN.db')#newNN
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
    import base64, json
    print(base.execute("PRAGMA table_info('actions');").fetchall())
    #a = base.execute("""select imgData from imgs where id=3""").fetchall()[1][0]
    #base.execute(f"""DELETE FROM place WHERE id=3 AND imgData='{a}'""")
    '''
    
    
    with open('img.png', mode='rb') as img_file:
        image_64_encode = base64.b64encode(img_file.read())
    a = base.execute(
        f"""INSERT INTO imgs (id, imgData)
        VALUES ('3', "{image_64_encode}")"""
    )
    
    contact = {'tel': "8 (831) 216-01-00", 'link': 'https://tempcoffee.ru'}
    contact = json.dumps(contact)
    
    categories = ['1']
    categories = json.dumps(categories)
    
    img = ['5']
    img = json.dumps(img)
    
    base.execute(
        f"""INSERT INTO places (id, name, address, description, contacts, categories, district, photo_id)
            VALUES('5', 'Кофейня ТЕМП', 'ул. Пискунова, 24', '{description}', '{contact}', '{categories}', '2', '{img}')"""
    )

    
    print(base.execute("PRAGMA table_info('actions');").fetchall())

    
    
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
    

    
    