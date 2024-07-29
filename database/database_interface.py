from abc import ABC, abstractmethod
from database.database_csv import CSVDatabase
from database.database_sqlite import SQLiteDatabase

class DatabaseInterface(ABC):    
    def __init__(self, db_type: str) -> None:
        self.db_instance = self.create_database(db_type)
        
    def create_database(self, db_type: str):
        if db_type == "csv":
            return CSVDatabase()
        elif db_type == "sqlite":
            return SQLiteDatabase()
        else:
            raise ValueError(f"Unknown database type: {db_type}")

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def add_object(self, obj):
        pass

    @abstractmethod
    def get_object(self, cls, obj_id):
        pass

    @abstractmethod
    def update_object(self, obj):
        pass

    @abstractmethod
    def delete_object(self, cls, obj_id):
        pass
