from models.body_of_art import BodyOfArt
from models.person import Person
from models.track import Track

from datetime import datetime
from typing import List

class Playlist(BodyOfArt):
    def __init__(self, title: str, owner: Person, debut_date: datetime = datetime.now, cover_art: str = None):
        BodyOfArt.__init__(self, title, debut_date, owner)
        self._cover_art = cover_art
        self._tracks: List[Track] = []

    @property
    def cover_art(self):
        """Getter for cover_art path"""
        return self._cover_art
    
    @cover_art.setter
    def cover_art(self, value: str):
        """Setter for cover_art path"""
        self._cover_art = value
    
    @property
    def tracks(self):
        """Getter for tracks"""
        return self._tracks
    
    @tracks.setter
    def tracks(self, value: List[Track]):
        """Setter for tracks"""
        self._tracks = value
        
    def add_track(self, track: Track):
        if track not in self._tracks:
            self._tracks.append(track)
    
    def remove_track(self, track: Track):
        if track in self._tracks:
            self._tracks.remove(track)