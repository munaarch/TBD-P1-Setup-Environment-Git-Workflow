from pymongo import MongoClient

uri = "mongodb+srv://munaolya:Muna1147@cluster0.wsssukb.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print(client.list_database_names())
except Exception as e:
    print("Koneksi gagal:",e)