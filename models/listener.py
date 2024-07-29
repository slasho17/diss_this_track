from models.person import Person
from models.playlist import Playlist

from typing import List
from datetime import datetime


class Listener(Person):
    def __init__(self, name: str, email: str, birth_date: datetime, biography: str):
        Person.__init__(self, name, email, birth_date, biography)
        self._playlists: List[Playlist] = []
        
    @property
    def playlists(self):
        """Getter for playlists"""
        return self._playlists
    
    @playlists.setter
    def playlists(self, value: List[Playlist]):
        """Setter for playlists"""
        self._playlists = value 

    def add_playlist(self, playlist: Playlist):
        if playlist not in self._playlists:
            self._playlists.append(playlist)
            
    def remove_playlist(self, playlist: Playlist):
        if playlist in self._playlists:
            self._playlists.remove(playlist)
