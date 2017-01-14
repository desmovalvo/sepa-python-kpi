#!/usr/bin/python

# local requirements
from KP import *

# global requiremets
import json
import requests


# class Consumer
class Consumer(KP):

    """The Consumer class - Inherits from KP"""

    # constructor
    def __init__(self, httphost, wshost, query):

        """Constructor for the Consumer class"""

        # superclass constructor
        KP.__init__(self, httphost, wshost)

        # class attribute
        self.query = query


    # query
    def consume(self):

        """This method is used to query the KB"""
        
        # update
        r = requests.post(self.httphost, data=self.query, headers={"Content-type":"application/sparql-query"})

        # return status and results
        if r.status == 200:
            return True, json.loads(r.text)
        else:
            return False, None
        

        
    # subscribe
    def subscribe(self):

        """This method is used to subscribe to the KB"""
        
        # TODO
        pass


    # unsubscribe
    def unsubscribe(self):

        """This method is used to unsubscribe from the KB"""
        
        # TODO
        pass
