from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb+srv://mongouser:mongouser@cluster0.vsds4ez.mongodb.net/')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    # for school in schools:
    #     print("[{}] {}".format(school.get('_id'), school.get('name')))
    print(schools)