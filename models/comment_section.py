from models.diss_this_track import DissThisTrack
from models.body_of_art import BodyOfArt
from models.comment import Comment

from typing import List

class CommentSection(DissThisTrack):
    def __init__(self, body_of_art: BodyOfArt):
        DissThisTrack.__init__(self)
        self._body_of_art:BodyOfArt = body_of_art
        self._comments: List[Comment] = []
        self._number_of_comments: int = 0
        self._average_stars: float = 0
            
    @property
    def body_of_art(self):
        """Getter for body_of_art"""
        return self._body_of_art
    
    @body_of_art.setter
    def body_of_art(self, value: BodyOfArt):
        """Setter for body_of_art"""
        self._body_of_art = value 
            
    @property
    def comments(self):
        """Getter for comments"""
        return self._comments
    
    @comments.setter
    def comments(self, value: list[Comment]):
        """Setter for comments"""
        self._comments = value 
            
    @property
    def number_of_comments(self):
        """Getter for number_of_comments"""
        return self._number_of_comments
    
    @number_of_comments.setter
    def number_of_comments(self, value: int):
        """Setter for number_of_comments"""
        self._number_of_comments = value 
            
    @property
    def average_stars(self):
        """Getter for average_stars"""
        return self._average_stars
    
    @average_stars.setter
    def average_stars(self, value: float):
        """Setter for average_stars"""
        self._average_stars = value 
        
    def add_comment(self, comment: Comment):
        if comment not in self._comments:
            self._comments.append(comment)
            self._number_of_comments +=1
            
    def delete_comment(self, comment: Comment):
        if comment in self._comments:
            self._comments.remove(comment)
            self._number_of_comments -=1
