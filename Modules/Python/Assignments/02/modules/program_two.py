#!/bin/python

from modules.constants import ERROR_MESSAGE
from modules.program import Program

import getpass
import hashlib


class DB:
    _echo=None
    _connected:bool = False

    _records:list[tuple]
    _auth:list[tuple] = [
        (1, "mahros", "5f4dcc3b5aa765d61d8327deb882cf99"),
        (2, "kali", "161ebd7d45089b3446ee4e0d86dbcf92"),
        (3, "root", "5f4dcc3b5aa765d61d8327deb882cf99"),
    ]
    
    def __init__(self, echo=None):
        self._echo = echo

    def echo(self, text:str):
        if self._echo == None:
            print(text)
        else:
            self._echo(text)


    def hash(self, text:str):
        return hashlib.md5(text.encode()).hexdigest()

    def auth(self, username, password):
        for record in self._auth:
            if record[1] == username:
                return record[2] == self.hash(password)
            
        return False
    
    def connect(self, username:str, password:str):
        auth:bool = self.auth(username, password)
        if auth:
            self._connected = True
            self.echo("Success! Your are connected.")
        else:
            self.echo("Sorry! Incorrect username or password.")

        return self

class ProgramTwo(Program):
    _name = "Auth Simulator"
    _desc = "Simulate a login cycle on a virtual db and checker"
    def __init__(self, id):
        super().__init__(id, self._name, self._desc)

    

    def process(self):
        self.echo("TIP: Password input is hidden!")
        self.echo("Record(u=mahros, p=password)")
        db = DB(echo=self.echo)

        # get username
        username = self.read("Username? ")

        # get password
        password = self.read("Password? ", hidden=True)

        # instance
        db.connect(username, password)
        
        


    def run(self):
        try:
            self.process()
        except Exception as Error:
            self.tryAgain(lambda:self.process(), before=ERROR_MESSAGE)