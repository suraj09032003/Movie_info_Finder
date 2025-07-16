import requests

def get_movie_info(title):
    API_KEY = ""
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        print(f"Title: {data['Title']}")
        print(f"Year: {data['Year']}")
        print(f"Genre: {data['Genre']}")
        print(f"Director: {data['Director']}")
        print(f"Plot: {data['Plot']}")
    else:
        print("Movie not found!")

movie = input("Enter movie title: ")
get_movie_info(movie)