import sqlite3

class SQLiteDatabase:
    def __init__(self, db_name='app.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def add_object(self, obj):
        cls_name = obj.__class__.__name__.lower()
        columns = ', '.join(obj.__dict__.keys())
        placeholders = ', '.join('?' * len(obj.__dict__))
        values = tuple(obj.__dict__.values())
        self.cursor.execute(f'INSERT INTO {cls_name} ({columns}) VALUES ({placeholders})', values)
        self.connection.commit()

    def get_object(self, cls, obj_id):
        cls_name = cls.__name__.lower()
        self.cursor.execute(f'SELECT * FROM {cls_name} WHERE id = ?', (obj_id,))
        row = self.cursor.fetchone()
        if row:
            column_names = [description[0] for description in self.cursor.description]
            obj_data = dict(zip(column_names, row))
            return cls(**obj_data)
        return None

    def update_object(self, obj):
        cls_name = obj.__class__.__name__.lower()
        columns = ', '.join(f'{key} = ?' for key in obj.__dict__.keys())
        values = tuple(obj.__dict__.values())
        self.cursor.execute(f'UPDATE {cls_name} SET {columns} WHERE id = ?', (*values, obj.id))
        self.connection.commit()

    def delete_object(self, cls, obj_id):
        cls_name = cls.__name__.lower()
        self.cursor.execute(f'DELETE FROM {cls_name} WHERE id = ?', (obj_id,))
        self.connection.commit()
