from models.person import Person
from models.album import Album
from models.genre import Genre

from typing import List
from datetime import datetime

class Artist(Person):
    def __init__(self, name: str, email: str, birth_date: datetime, biography: str):
        Person.__init__(self, name, email, birth_date, biography)
        self._albums: List[Album] = []
        self._genres: List[Genre] = []
        
    @property
    def albums(self):
        """Getter for albums"""
        return self._albums
    
    @albums.setter
    def albums(self, value: List[Album]):
        """Setter for albums"""
        self._albums = value 

    @property
    def genres(self):
        """Getter for genres"""
        return self._genres
    
    @genres.setter
    def genres(self, value: List[Genre]):
        """Setter for genres"""
        self._genres = value 
        
    def add_album(self, album: Album):
        if album not in self._albums:
            self._albums.append(album)
            
    def remove_album(self, album: Album):
        if album in self._albums:
            self._albums.remove(album)
                
    def add_genre(self, genre: Genre):
        if genre not in self._genres:
            self._genres.append(genre)
            
    def remove_genre(self, genre: Genre):
        if genre in self._genres:
            self._genres.remove(genre)
