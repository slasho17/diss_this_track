from __future__ import annotations

from models.diss_this_track import DissThisTrack
from models.person import Person
from models.comment_section import CommentSection

from datetime import datetime
from typing import List

class BodyOfArt(DissThisTrack):
    def __init__(self, title: str, debut_date: datetime, owner: Person):
        DissThisTrack.__init__(self)
        self._title: str = title
        self._debut_date: datetime = debut_date
        self._owner: Person = owner
        
        self.likes_received: List[Person] = []
        self.number_of_likes_received: int = 0
        self.comment_section = CommentSection()
        
    @property
    def title(self):
        """Getter for title"""
        return self._title
    
    @title.setter
    def title(self, value: str):
        """Setter for owner"""

        self._title = value
        
    @property
    def debut_date(self):
        """Getter for debut_date"""
        return self._debut_date
    
    @debut_date.setter
    def debut_date(self, value: str):
        """Setter for debut_date"""
        self._debut_date = value

    @property
    def owner(self):
        """Getter for owner"""
        return self._owner
    
    @owner.setter
    def owner(self, value: str):
        """Setter for owner"""
        self._owner = value
        
    def liked_by(self, person: Person):
        """Increments likes in body of art"""
        if person not in self.likes_received:    
            self.number_of_likes_received +=1
            self.likes_received.append(person)
        else:
            #person already liked this
            pass
            
    def disliked_by(self, person: Person):
        """Decrements likes in body of art"""
        if person in self.likes_received:    
            self.number_of_likes_received -=1
            self.likes_received.remove(person)
        else:
            #person hasnt yet liked this
            pass
