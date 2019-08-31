#!/usr/bin/env python3.6
from user import User
from user import Account

def create_user(firstname,lastname,username,password):
    '''
    function to create new user
    '''
    new_user = User(firstname,lastname,username,password)
    return new_user

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    function to delete user
    '''
    user.delete_user()

def find_user(username):
    '''
    function to search for users
    '''
    return User.find_by_username(username)

def display_user():
    return User.display_userInfo()