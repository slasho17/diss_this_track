from __future__ import annotations

from models.diss_this_track import DissThisTrack
from models.comment import Comment
from models.comment_section import CommentSection
from models.body_of_art import BodyOfArt

from typing import List
from datetime import datetime

class Person(DissThisTrack):
    def __init__(self, name: str, email: str, birth_date: datetime, biography: str):
        DissThisTrack.__init__(self)
        self._name: str = name
        self._email: str = email
        self._birth_date: datetime = birth_date
        self._biography: str = biography
        self._comments_made: List[Comment] = []
        self._comments_liked: List[Comment] = []
        self._followers: List[Person] = []
        self._follows: List[Person]  = []
        self._bodies_of_art_liked: List[BodyOfArt]  = []

    @property
    def name(self):
        """Getter for name"""
        return self._name
    
    @name.setter
    def name(self, value: str):
        """Setter for name"""
        self._name = value 
        
    @property
    def email(self):
        """Getter for email"""
        return self._email
    
    @email.setter
    def email(self, value: str):
        """Setter for email"""
        self._email = value
        
    @property
    def birth_date(self):
        """Getter for birth_date"""
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value: datetime):
        """Setter for birth_date"""
        self._birth_date = value 
        
    @property
    def biography(self):
        """Getter for biography"""
        return self._biography
    
    @biography.setter
    def biography(self, value: str):
        """Setter for biography"""
        self._biography = value 
        
    @property
    def comments_made(self):
        """Getter for comments_made"""
        return self._comments_made
    
    @comments_made.setter
    def comments_made(self, value: List[Comment]):
        """Setter for comments_made"""
        self._comments_made = value 
        
    @property
    def comments_liked(self):
        """Getter for comments_liked"""
        return self._comments_liked
    
    @comments_liked.setter
    def comments_liked(self, value: List[Comment]):
        """Setter for comments_liked"""
        self._comments_liked = value 
        
    @property
    def followers(self):
        """Getter for followers"""
        return self._followers
    
    @followers.setter
    def followers(self, value: List[Person]):
        """Setter for followers"""
        self._followers = value 
        
    @property
    def follows(self):
        """Getter for follows"""
        return self._follows
    
    @followers.setter
    def follows(self, value: List[Person]):
        """Setter for follows"""
        self._follows = value 
        
    @property
    def bodies_of_art_liked(self):
        """Getter for bodies_of_art_liked"""
        return self._bodies_of_art_liked
    
    @bodies_of_art_liked.setter
    def bodies_of_art_liked(self, value: List[BodyOfArt]):
        """Setter for bodies_of_art_liked"""
        self._bodies_of_art_liked = value 
        
    def make_a_comment(self, comment_section: CommentSection, comment_text: str, number_of_stars: float):
        new_comment = Comment(self, comment_section, comment_text, number_of_stars)
        comment_section.add_comment(new_comment)
        self._comments_made.append(new_comment)

    def delete_comment(self, comment: Comment):
        if comment in self._comments_made:
            comment.comment_section.delete_comment(self)
            self._comments_made.remove(comment)
    
    def like_comment(self, comment: Comment):
        if comment not in self._comments_liked:
            comment.get_liked_by(self)
            self.comments_liked.append(comment)

    def dislike_comment(self, comment: Comment):
        if comment in self._comments_liked:
            comment.get_disliked_by(self)
            self.comments_liked.remove(comment)
    
    def follow_someone(self, someone: Person):
        if someone not in self._follows:
            self._follows.append(someone)
            someone.get_followed_by(self)

    def unfollow_someone(self, someone: Person):
        if someone in self._follows:
            self._follows.remove(someone)
            someone.get_unfollowed_by(self)

    def get_followed_by(self, someone: Person):
        if someone not in self._followers:
            self._followers.append(someone)

    def get_unfollowed_by(self, someone: Person):
        if someone in self._followers:
            self._followers.remove(someone)

    def like_body_of_art(self, body_of_art: BodyOfArt):
        if body_of_art not in self._bodies_of_art_liked:
            self._bodies_of_art_liked.append(body_of_art)
            body_of_art.liked_by(self)
            
    def dislike_body_of_art(self, body_of_art: BodyOfArt):
        if body_of_art in self._bodies_of_art_liked:
            self._bodies_of_art_liked.remove(body_of_art)
            body_of_art.disliked_by(self)