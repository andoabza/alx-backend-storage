from pymongo import MongoClient
list_all = __import__('8-all').list_all
update_topics = __import__('10-update_topics').update_topics

if __name__ == "__main__":
    client = MongoClient('mongodb+srv://mongouser:mongouser@cluster0.vsds4ez.mongodb.net/')
    school_collection = client.my_db.school
    update_topics(school_collection, "ando", ["Sys admin", "AI", "Algorithm"])