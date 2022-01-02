import sqlite3 as sql


def create_db():
    connection = sql.connect('beatles.db')
    connection.commit()
    connection.close()

def create_table():
    connection = sql.connect('beatles.db')
    cursor = connection.cursor()
    cursor.execute(
        """Create TABLE members (
            firstname text,
            lastname text,
            birthyear integer,
            main instrument text
        )"""
    )
    connection.commit()
    connection.close()

def insert_row(firstname, lastname, birthyear, maininstrument):
    connection = sql.connect('beatles.db')
    cursor = connection.cursor()
    instruction = f"INSERT INTO members VALUES ('{firstname}', '{lastname}', {birthyear}, '{maininstrument}')"
    cursor.execute(instruction)
    connection.commit()
    connection.close()

def ordered_by(field):
    connection = sql.connect('beatles.db')
    cursor = connection.cursor()
    instruction = f"SELECT * FROM members ORDER BY {field} DESC"
    cursor.execute(instruction)
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    print(data)

if __name__ == '__main__':
    # create_db()
    # create_table()
    # insert_row('John', 'Lennon', 1940, 'Rhythm Guitar')
    # insert_row('Paul', 'McCartney', 1942, 'Bass')
    # insert_row('George', 'Harrison', 1943, 'Lead Guitar')
    # insert_row('Ringo', 'Starr', 1940, 'Drums')
    #ordered_by('birthyear')
    #ordered_by('lastname')
    #ordered_by('firstname')
    ordered_by('main')



