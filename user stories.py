import json 
import os

class DataLibrary: 
   """ 
   A class for saving and retrieving python dictionaries to and from disk. 
   """ 
   def __init__(self, data_path): 
       """ 
       Initialize the class with a data_path where the dictionaries will be saved. 
       """ 
       self.data_path = data_path 
       if not os.path.exists(data_path): 
           os.makedirs(data_path)

   def save(self, key, data): 
       """ 
       Save a python dictionary to disk with a given key. 
       """ 
       with open(os.path.join(self.data_path, key), 'w') as f: 
           json.dump(data, f)

   def retrieve(self, key): 
       """ 
       Retrieve a python dictionary from disk with a given key. 
       """ 
       with open(os.path.join(self.data_path, key), 'r') as f: 
           data = json.load(f) 
       return data
