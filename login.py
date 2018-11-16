import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["employee"]
collection = db["login"]


username = input("Enter Username:")
password = input("Enter Password:")
for x in collection.find({},{"username":1,"password":1}):
    name=str(x["Username"])
    password=str(x["Password"])
if username==name and password==password:
    print("Login Successful")
else:
    print("Login Failed")

