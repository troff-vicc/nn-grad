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
    #a = base.execute("""select imgData from imgs where id=3""").fetchall()[1][0]
    #base.execute(f"""DELETE FROM place WHERE id=3 AND imgData='{a}'""")
    
    with open('img.png', mode='rb') as img_file:
        image_64_encode = base64.b64encode(img_file.read())
    imgLen = int(base.execute("""SELECT id FROM imgs ORDER BY id DESC LIMIT 1;""").fetchone()[0]) + 1
    a = base.execute(
        f"""INSERT INTO imgs (id, imgData)
        VALUES ('{imgLen}', "{image_64_encode}")"""
    )
    
    img = [f'{imgLen}']
    img = json.dumps(img)
    
    name = 'В Нижнем Новгороде побывали гости из Луганска'
    description = """«Нижний Новгород - очень красивый древний город. Ему недавно исполнилось 800 лет. Место для нашей встречи выбрано не случайное – у собора Архангела Михаила, который считается самым древним в Нижнем Новгороде. Рядом – памятник основателям города. С территории Кремля открывается вид на Стрелку - слияние двух великих рек Оки и Волги. Надеюсь, за время пребывания в городе вы получите много впечатлений и захотите приехать к нам еще», - обратился к ребятам Юрий Шалабаев, добавив, что между Нижним Новгородом и Луганском в 2023 году было заключено соглашение о сотрудничестве, в рамках которого организованы мероприятия в различных сферах, в том числе образовательной.
    """
    base.execute(
        f"""INSERT INTO actions (id, name, description, date, type, photo_id)
                        VALUES('2', '{name}', '{description}', '28.10.24', '1', '{img}')"""
    )
    
    '''
    
    
    
    
    
    img = ['5']
    img = json.dumps(img)
    
    
    
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
    

    
    