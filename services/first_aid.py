
from pymongo import MongoClient

client = MongoClient('mongodb://localhost/')

first_aid = client['twilio']['first_aid']


def search_injury(search_word):
    """
    This function performs a full text search based on the index we created earlier
    :param search_word:
    :return:
    """
    cursor = first_aid.find({'$text': {'$search': search_word}})
    result = []
    for data in cursor:
        result.append(data)
    return result