from pymongo import MongoClient
import os

# Replace these variables with your MongoDB Atlas credentials and database name
username = "Your username"
password = "your password"
dbname = "Database name"
cluster_url = "db uri"  # e.g., "cluster.mongodb.net"

# Create the connection string
connection_string = f"mongodb+srv://{username}:{password}@{cluster_url}/{dbname}?retryWrites=true&w=majority"
#mongodb+srv://eftekhar:jam2003eft@jamcluster.mdng7.mongodb.net/

# Create a MongoClient to the MongoDB instance
client = MongoClient(connection_string)

# Access the database
db = client[dbname]

# Example: List collections in the database
collections = db.list_collection_names()
print("Collections in the database:", collections)
print("-----------------------------")

# Access a collection
movies = db.movies

#Example : List the first 10 movie in the collection
movies_list = movies.find().limit(2)
for movie in movies_list:
    print(movie)

print("-----------------------------")

# Example: Find a movie by title
movie = movies.find_one({"title": "The Godfather"})
print("Movie found by title:", movie)


# Remember to close the connection when done
client.close()
