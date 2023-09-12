from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.assignment
movies = db.movies

while True:
    choice = int(input("Do you wish to:\n 1 - Add movie \n 2 - Show movie details \n 3 - Show movies \n"))
    if choice == 1:
        name = input("Enter movie name:\n")
        genre = input("Enter movie genre:\n")
        year = int(input("Enter release year:\n"))
        movie_details = {
            'name': name,
            'genre': genre,
            'year Publicare': year
        }
        movies.insert_one(movie_details)
    elif choice == 2:
        name_retrieve = input("Introduceti namele filmului pe care il cautati:\n")
        result = movies.find_one({'name': name_retrieve})
        print(f"\n name: {result['name']}\n genre: {result['genre']}\n year publicare: {result['year Publicare']} \n")
    elif choice == 3:
        result = movies.find()
        print("\n")
        for r in result:
            print(f"name:{r['name']} \n genre: {r['genre']} \n year publicare: {r['year Publicare']} \n")


