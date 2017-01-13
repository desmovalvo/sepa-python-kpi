#!/usr/bin/python

# inner requirements
from KP import *

# global requiremets
import requests


# class Producer
class Producer(KP):

    """The Producer class - Inherits from KP"""

    # constructor
    def __init__(self, host, update):

        """Constructor for the Producer class"""

        # superclass constructor
        KP.__init__(self, host, None)

        # class attribute
        self.update = update
        

    # update
    def produce(self):

        """This method is used to update the KB"""
        
        # update
        r = requests.post(self.httphost, data=self.update, headers={"Content-type":"application/sparql-update"})
        print r

        # TODO: return value
