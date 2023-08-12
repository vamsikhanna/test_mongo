import pymongo
client=pymongo.MongoClient("mongodb+srv://ineuron:ineuron@cluster0.eqx8ulg.mongodb.net/?retryWrites=true&w=majority")
db=client.test1477
print(db)


d={
    "name":"vamsi",
    "email":"khanna@gmail.com",
    "surname": "pallikonda"
}

db1=client['mongotest']
coll=db1['test1477']
coll.insert_one(d)
