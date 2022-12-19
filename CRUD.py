""" Jerry Barboza CS-340"""
from pymongo import MongoClient 
from bson.objectid import ObjectId

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:48284' % (username, password))
        self.database = self.client['AAC']
        
        # implement the C in CRUD. 
        
        def create(self, data): 
            if data is None: 
                self.database.animals.insert(data)
            else: 
                raise Exception("Nothing to save, because data parameter is empty")
                
        # method to implement the R in CRUD. 
        
        def read(self, readData):
            if readData:
                data = self.database.animals.find(data,{"_id":False})
            else: 
                data = self.database.animals.find({},{"_id":False})
            return data
        
        # method to implement the U in CRUD : update
        
        def update(self, query, data):
            if data is not None:
                updated = self.database.animals.update_one(query, data)
                return updated
            else:
                raise Exception("Nothing to save, because data parameter is empty")
                
        # method to implement the D in CRUD: Delete
        
        def delete(self,data):
            if data is not None:
                deleted = self.database.animals.delete_one(data)
                return deleted
            else:
                raise Exception("Nothing to save, because data parameter is empty")
                
                
            
        
       
        
        
