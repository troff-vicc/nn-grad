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
    import base64, json
    
    description = """Sheraton Нижний Новгород Кремль расположен в историческом квартале города в окружении множества культурных достопримечательностей. К услугам гостей 176 роскошных комфортных номеров и люксов с первоклассными удобствами, в том числе фирменной кроватью Sweet Sleeper. Гости, останавливающиеся люксах, могут посетить эксклюзивный клубный лаундж Sheraton и насладиться бесплатным завтраком, напитками и закусками в течение дня. Великолепный фитнес-центр Sheraton и массаж в люксе гарантируют полное расслабление и восстановление энергии. Теплые оттенки общественных зон, интерьер которых спроектирован студией дизайна Жака Гарсиа, создают атмосферу уюта. Здесь любят собираться как путешественники, так и местные жители. К услугам гостей фирменного элегантного ресторана Smorodinn свежие сезонные блюда национальной кухни, а в баре в лобби можно провести время с друзьями за бокалом вкусного коктейля."""
    
    contact = {'tel': "8 (831) 431-70-00", 'link': 'www.starwood.com', 'email': 'reservation@sheraton-nn.com'}
    contact = json.dumps(contact)
    
    categories = ['0']
    categories = json.dumps(categories)
    
    img = ['6']
    img = json.dumps(img)
    
    base.execute(
        f"""INSERT INTO hotels (id, name, address, description, contacts, categories, district, stars, photo_id)
                VALUES('0', 'Отель "Sheraton Nizhny Novgorod Kremlin"', 'Нижний Новгород, пл. Театральная, д. 1', '{description}', '{contact}', '{categories}', '2', '5', '{img}')"""
    )
    
    with open('img.png', mode='rb') as img_file:
        image_64_encode = base64.b64encode(img_file.read())
    a = base.execute(
        f"""INSERT INTO imgs (id, imgData)
        VALUES ('6', "{image_64_encode}")"""
    )
    
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

    
    print(base.execute("PRAGMA table_info('hotels');").fetchall())

    
    
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
    

    
    