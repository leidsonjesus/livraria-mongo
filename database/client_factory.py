from pymongo.mongo_client import MongoClient
from pymongo.server_api  import ServerApi


class ClientFactory:

     def get_client(self):
        return MongoClient(
            'mongodb+srv://leidson:01Limite@cluster0.h3pv6bo.mongodb.net/?retryWrites=true&w=majority',
            server_api=ServerApi('1'))
