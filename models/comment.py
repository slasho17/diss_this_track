from diss_this_track import DissThisTrack
from comment_section import CommentSection
from person import Person

from typing import List
from __future__ import annotations

class Comment(DissThisTrack):
    def __init__(self, author: Person, comment_section: CommentSection, comment_text: str, number_of_stars: float):
        DissThisTrack.__init__(self)
        self._author: Person = author
        self._comment_section = comment_section
        self._comment_text: str = comment_text
        self._number_of_stars: float = number_of_stars
        self._likes_received: List[Person] = []
        self._number_of_likes_received: int = 0
    
    @property
    def author(self):
        """Getter for author"""
        return self._author
    
    @author.setter
    def author(self, value: Person):
        """Setter for author"""
        self._author = value 
    
    @property
    def comment_section(self):
        """Getter for comment_section"""
        return self._comment_section
    
    @comment_section.setter
    def comment_section(self, value: CommentSection):
        """Setter for comment_section"""
        self._comment_section = value 
    
    @property
    def comment_text(self):
        """Getter for comment_text"""
        return self._comment_text
    
    @comment_text.setter
    def comment_text(self, value: str):
        """Setter for comment_text"""
        self._comment_text = value 
    
    @property
    def number_of_stars(self):
        """Getter for number_of_stars"""
        return self._number_of_stars
    
    @number_of_stars.setter
    def number_of_stars(self, value: float):
        """Setter for number_of_stars"""
        self._number_of_stars = value 
    
    @property
    def likes_received(self):
        """Getter for likes_received"""
        return self._likes_received
    
    @likes_received.setter
    def likes_received(self, value: List[Person]):
        """Setter for likes_received"""
        self._likes_received = value 
    
    @property
    def number_of_likes_received(self):
        """Getter for number_of_likes_received"""
        return self._number_of_likes_received
    
    @number_of_likes_received.setter
    def number_of_likes_received(self, value: int):
        """Setter for number_of_likes_received"""
        self._number_of_likes_received = value 

    def get_liked_by(self, person: Person):
        if person not in self._likes_received:
            self._likes_received.append(person)
            self._number_of_likes_received +=1

    def get_disliked_by(self, person: Person):
        if person in self._likes_received:
            self._likes_received.remove(person)
            self._number_of_likes_received -=1
    
    def delete_comment(self, person: Person):
        if person == self._author:
            self._comment_section.delete_comment(self)
            