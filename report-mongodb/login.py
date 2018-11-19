import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["employee"]
collection = db["login"]


username = input("Enter Username:")
Password = input("Enter Password:")
for x in collection.find({},{"username":1,"password":1}):
    name=str(x["username"])
    password=str(x["password"])
if username==name and Password==password:
    print("Login Successful")
else:
    print("Login Failed")

