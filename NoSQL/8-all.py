#!/usr/bin/env python3
"""
    Made By Me
"""


import pymongo
from typing import List

def list_all(mongo_collection: List) -> List:
    """
    Documented ???
    """
    documents = list(mongo_collection.find())
