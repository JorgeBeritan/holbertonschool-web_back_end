#!/usr/bin/env python3
"""
    Made By Me
"""


from pymongo import MongoClient


def school_by_topics(mongo_collection, topic):
    """
    Documnents???
    """

    documents = mongo_collection.find({"topics": topic})

    return list(documents)
