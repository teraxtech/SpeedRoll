import pymongo

myclient = pymongo.MongoClient("mongodb://10.105.76.163:27017/")

mydb = myclient["Owlhacks-Project"]

mycol = mydb["scores"]


x = mycol.find_one()

print(x)
