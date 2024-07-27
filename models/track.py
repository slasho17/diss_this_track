from body_of_art import BodyOfArt
from artist import Artist
from album import Album

from datetime import datetime
from typing import List

class Track(BodyOfArt):
    def __init__(self, title: str, owner: Artist, album: Album, debut_date: datetime = datetime.now):
        BodyOfArt.__init__(self, title, debut_date, owner)
        self._album: Album = album
        self._features: List[Artist] = []
        self._duration_in_seconds: int = None
        self._lyrics: str = None

    @property
    def album(self):
        """Getter for album"""
        return self._album
    
    @album.setter
    def album(self, value: Album):
        """Setter for album"""
        self._album = value
        
    @property
    def features(self):
        """Getter for features"""
        return self._features
    
    @features.setter
    def features(self, value: List[Artist]):
        """Setter for features"""
        self._features = value
        
    @property
    def duration_in_seconds(self):
        """Getter for features"""
        return self._duration_in_seconds
    
    @duration_in_seconds.setter
    def duration_in_seconds(self, value: int):
        """Setter for duration_in_seconds"""
        self._duration_in_seconds = value
        
    @property
    def lyrics(self):
        """Getter for lyrics"""
        return self._lyrics
    
    @lyrics.setter
    def lyrics(self, value: str):
        """Setter for lyrics"""
        self._lyrics = value
        
        