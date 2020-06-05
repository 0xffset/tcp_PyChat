import pymongo
import time


class MongoDB:
    def __init__(self):

        self.connection = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.connection['PyChat_tcp']
        self.col = self.db['clients']
        self.col_messages = self.db['messages']

    def save_client(self, address, port):
        try:
            data = {"address": address, "timestamp": time.time(), "port": port}

            x = self.col.find_one()
            if x['address'] == address:
                query = {"address": address}
                to_update = {"$set": {"timestamp": time.time(), "port": port}}
                self.col.update_one(query, to_update)
                self.col.find_one()
            else:
                self.col.insert_one(data)

        except Exception as excep:
            print(excep)

    def get_by_address(self, address):
        query = {"address": address}
        out = self.col.find_one(query)
        return out

    def save_message(self, address_from, address_to, message):
        try:
            data = {"address_from": address_from, "address_to": address_to,
                    "timestamp": time.time(), "message": message}
            self.col_messages.insert_one(data)

        except Exception as Excep:
            print(Excep)
