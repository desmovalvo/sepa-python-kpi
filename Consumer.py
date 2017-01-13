#!/usr/bin/python

# local requirements
from KP import *

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
    def query(self):

        """This method is used to query the KB"""
        
        # TODO
        pass


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
