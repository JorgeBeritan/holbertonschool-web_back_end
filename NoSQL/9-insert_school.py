#!/usr/bin/env python3
"""
    Made By Me
"""


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Documents ??
    """
    documents = mongo_collection.insert_one(kwargs)
    
    return documents.inserted_id
