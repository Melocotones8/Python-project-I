import sqlite3
import datetime

from menus_input import user_input

def table(func):
    def wrapper_table(*args):

        connection = sqlite3.connect("saves.db")
        cursor = connection.cursor()

        try:
            createTable = """CREATE TABLE TEST (
            save_name VARCHAR(20) PRIMARY KEY,
            name VARCHAR(20),
            gender VARCHAR(20),
            level INTEGER,
            class VARCHAR(10),
            hp INTEGER,
            attack INTEGER,
            defense INTEGER,
            ability INTEGER,
            last_play TIMESTAMP); """
            cursor.execute(createTable)
        except:
            pass

        return func(*args)
        
    return wrapper_table

@table
def save_game(name, gender, level, h_class, hp, attack, defense, ability):

    print("Enter save_name")
    save_name = user_input()

    try:
        connection = sqlite3.connect("saves.db")
        cursor = connection.cursor()
        last_play = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        insertQuery = """INSERT INTO TEST
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """

        cursor.execute(insertQuery, 
        (save_name, name, gender, level, h_class, hp, attack, defense, ability, last_play))
        connection.commit()
        print("Succesfully saved")
    except:
        print("Error")

    cursor.close()
    connection.close()

@table
def saves():

    connection = sqlite3.connect("saves.db")
    cursor = connection.cursor()

    results = cursor.execute("SELECT save_name, name, level, class, last_play FROM TEST")
    rows = 0

    print("SAVES:")
    for row in results:
        rows += 1
        print("Save name: {} || hero name: {} || level: {} || class: {} || last play: {}".format(row[0], row[1], row[2], row[3], row[4]))
        print("-" * 30)

    cursor.close()
    connection.close()

    return rows

@table
def load_game():

    connection = sqlite3.connect("saves.db")
    cursor = connection.cursor()

    print("Enter save name:")
    save_name = user_input()

    try:
        result = cursor.execute("""SELECT name, gender, class, hp, attack, defense, level, ability FROM TEST 
                                WHERE save_name = '{}'; """.format(save_name))
        save = result.fetchone()

        return save
    
    except:
        print("Wrong save name")
    
    cursor.close()
    connection.close()
