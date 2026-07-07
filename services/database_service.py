# handles reading and writing to db.json
import json
DATABASE_FILE = "db.json"

def load_database():
    #Load all data from db.json
    with open(DATABASE_FILE,"r") as file:
        return json.load(file)
    
def save_database(data):
    #save updated data back to db.json.
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file)