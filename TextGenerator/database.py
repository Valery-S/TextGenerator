import sqlite3

class DataBase:

    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance
    
    def __init__(self, db_name='db.sqllite') -> None:
        self._connection = sqlite3.connect(db_name)
        self._cursor = self._connection.cursor()

        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_history (
                id SERIAL PRIMARY KEY,
                prompt TEXT NOT NULL,
                output TEXT NOT NULL
            );
        ''')

        self._connection.commit()

    def save_message(self, prompt, message):
        sql = '''
            INSERT INTO chat_history(prompt, "output")
            VALUES 
                ('{}', '{}')
        '''.format(prompt, message)

        self._cursor.execute(sql)
        self._connection.commit()

    def __del__(self):
        self._cursor.close()
        self._connection.close()
