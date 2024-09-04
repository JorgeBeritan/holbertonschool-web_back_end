#!/usr/bin/env python3
"""
    Made By Me
"""


from pymongo import MongoClient


def school_by_topics(mongo_collection, topics):
    """
    Documnents???
    """

    documents = mongo_collection.find({"topics": topics})

    return documents
