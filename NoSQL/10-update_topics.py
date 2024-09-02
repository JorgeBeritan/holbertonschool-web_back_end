#!/usr/bin/env python3
"""
    Made By Me
"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Document??
    """

    documents = mongo_collection.update_many({
        {"name": name},
        {"$set": {"topics": topics}}
    })

    return documents.modified_count