# MOVIE RECOMMENDATION SYSTEM - IN PROGRESS

import json
import tkinter as tk
import requests

def main():
    create_gui()

# fetch data from OMDB API
def fetch_movies(actor):
    url = "http://www.omdbapi.com/?i=tt3896198&apikey=27804dcc"
    params = {
        "s": actor if actor else "",
        "type":"movie",
          }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data ["Response"] == "True":
            return data
        else:
            return [], ("No movies found")
    else:
        return []

# takes user preferences and returns recommended movies
def recommend_movies(movies, actor=None):
    recommended = []
    for movie in movies:
        if isinstance(movie, dict) and "Title" in movie:
            if actor:
                if actor.lower() in movie["Title"].lower():
                    recommended.append(movie)
            else:
                recommended.append(movie)
    return recommended

# collects and return user preferences
def collect_preferences():
    actor_preference = actor.get()
    return actor_preference

# calls collect and recommend functions and creates list
def list_recommendations():
    actor_preference = collect_preferences()
    movie_data = fetch_movies(actor_preference)
    recommendations = recommend_movies(movie_data, actor_preference)
    movies.delete(0, tk.END)
    if recommendations:
        for movie in recommendations:
            movie_title = movie.get("Title","Unknown Title")
            movies.insert(tk.END, movie_title)
    else:
        movies.insert(tk.END,"Sorry, we couldn't find any movies.")


def create_gui():
    global actor, movies
    
    gui = tk.Tk()
    gui.title("PopcornGuru")
    gui.iconbitmap("popcorn.ico")
    gui.geometry("800x600")

    # user to type in actor/actress they want to search for (optional)
    actor_label = tk.Label(gui, text="Search actor/actress:")
    actor_label.pack()
    actor = tk.Entry(gui)
    actor.pack()

    # recommendations Label
    recommendations_label = tk.Label(gui, text="Recommendations:")
    recommendations_label.pack()

    # list of recommended movies to display
    movies = tk.Listbox(gui)
    movies.pack()

    # start search by clicking Start button
    start_button = tk.Button(gui, text="Start", command= list_recommendations)
    start_button.pack()

    gui.mainloop()
    
if __name__=="__main__":
    main()
