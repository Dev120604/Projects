import random
import matplotlib.pyplot as plt
south = {
    "Thriller": ["KGF-2", "RRR", "Pushpa - The Rise", "KGF", "Vikram", "Magadheera", "Bahubali - The Conclusion", "Bahubali - The Beginning"],
    "Lovestory": ["Geetha Govindam", "Sita Ramam", "Dear Comrade", "Radhe Shyam", "Tholi Prema", "Fidaa", "Dumdaar Khiladi", "Super Khiladi 4", "World Famous Lover", "The Super Khiladi 3"],
    "Horror": ["U Turn", "Pizza", "Aranmanai", "Bhaagamathie", "Karvva", "Ezra", "Kanchhana"]
}
bollywood = {
    "Thriller": ["Lagaan", "Dangal", "Chak De! India", "M. S. Dhoni: The Untold Story", "Mary Kom", "Gold"],
    "Lovestory": ["Shiddat", "Yeh Jawaani Hai Deewani", "Dil To Pagal Hai", "Jab Tak Hai Jaan", "Aashiqui 2", "Mohabbatein", "Kuch Kuch Hota Hai", "DDLJ"],
    "Horror": ["Bhool Bhulaiya", "Bhoot", "1920 London", "Raaz", "Stree"]
}
hollywood = {
    "Thriller": ["Inception", "Avatar", "Avatar 2", "Glass Onion", "The Blind side", "I Am Legend", "The Village", "The Sixth Sense", "The Matrix"],
    "Lovestory": ["After We Fell", "After We Collided", "Your Place or Mine", "Sqaured Love All Over again", "Love Today", "Fifty Shades Grey", "The Perfect Date", "The Kissing Booth", "After Ever Happy", "Purple Hearts"],
    "Horror": ["The Cursed", "The Conjuring", "Annabelle", "You Are Not My Mother", "Veronica", "The Night House", "IT", "The Exorcist"]
}
marvel = ["Avengers-Infinity War", "Avengers-End Game", "Ironman", "The Avengers", "Thor-The Darkwolrd",
    "Captain America", "Doctor Strange", "Spider Man-No Way Home", "AntMan", "Avengers Age of Ultron", "Black Panther"]
dc = ["Aquaman", "Batman", "Superman", "Black Adam",
    "Shazam", "Justice league", "Joker", "Wonder Woman"]
iMDB_top_10 = {
    "The Shawshank Redemption":9.3,
    "The Godfather":9.2,
    "John Wick:Chapter 4":8.7,
    "Interstellar":8.6,
    "Air":8.6,
    "Parasite":8.3,
    "The Dark Knight":8.0,
    "RRR":7.9,
    "Avatar: The Way of Water":7.8,
    "The Batman":7.8,
        }
like_movie = []
liked_movies = {}
def liked_movies_1():
    global like_movie
    global liked_movies
    lst_2 = list(set(like_movie))
    for i in range(len(lst_2)):
        count = 0
        for j in range(len(like_movie)):
            if like_movie[j] == lst_2[i]:
                count += 1
        liked_movies[lst_2[i]] = count
    print(liked_movies)
def liked_movies_bar():
    name = liked_movies.keys()
    data = liked_movies.values()
    plt.bar(name,data,color = "cyan")
    plt.xlabel("Name of the movies.")
    plt.ylabel("Liked by our users.")
    plt.title("Most liked movies.")
    plt.tight_layout()
    plt.show()
    
def Add_movie(Mname,Mlocation,Mplace):
    """Adds a movie in the data base by the manager"""
    if Mlocation == "hollywood":
        if Mplace == "Thriller":
            for i in hollywood["Thriller"]:
                if Mname == i:
                        print("It's already in the databse.")
                else:
                        hollywood["Thriller"].append(Mname)
            return (f"Movie {Mname} is already exists in database.")
        elif Mplace == "lovestory":
            for i in hollywood["Lovestory"]:
                if Mname == i:
                    print("It's already in the databse.")
                else:
                    hollywood["Lovestory"].append(Mname)
            return f"Movie {Mname} is already exists in database."
        elif Mplace == "horror":
            for i in hollywood["Horror"]:
                if Mname == i:
                    print("It's already in the databse.")
                else:
                    hollywood["Horror"].append(Mname)
            return f"Movie {Mname} is already exists in database."
    elif Mlocation == "bollywood":
        if Mplace == "Thriller":
            for i in bollywood["Thriller"]:
                if Mname == i:
                    print("It's already in the databse.")
                else:
                    bollywood["Thriller"].append(Mname)
            return f"Movie {Mname} is already exists in database."
        elif Mplace == "lovestory":
            for i in bollywood["Lovestory"]:
                if Mname == i:
                    print("It's already in the databse.")
                else:
                    bollywood["Lovestory"].append(Mname)
            return f"Movie {Mname} is already exists in database."
        elif Mplace == "horror":
            for i in bollywood["Horror"]:
                if Mname == i:
                    print("It's already in the databse.")
                else:
                    bollywood["Horror"].append(Mname)
            return f"Movie {Mname} is already exists in database."
    elif Mlocation == "south":
        if Mplace == "Thriller":
            for i in south["Thriller"]:
                if Mname == i:
                    print("It's already in the databse.")
                else:
                    south["Thriller"].append(Mname)
            return f"Movie {Mname} is already exists in database."
        elif Mplace == "lovestory":
            for i in south["Lovestory"]:
                if Mname == i:
                    print("It's already in the databse.")
                else:
                    south["Lovestory"].append(Mname)
            return f"Movie {Mname} is already exists in database."
        elif Mplace == "horror":
            for i in south["Horror"]:
                if Mname == i:
                    print("It's already in the databse.")
                else:
                    south["Horror"].append(Mname)
            return f"Movie {Mname} is already exists in database."
    elif Mlocation == "marvel":
        for i in marvel:
            if Mname == i:
                print("It's already in the databse.")
            else:
                marvel.append(Mname)
    elif Mlocation == "dc":
        for i in dc:
            if Mname == i:
                print("It's already in the databse.")
            else:
                dc.append(Mname)
    else:
            return "Enter Valid Loction To Add To Database."
def Movie_Finder(Mside):
    """It will suggest a movie randomly from the database."""
    if Mside == "hollywood" or Mside == "south" or Mside == "bollywood":
        Mtype = input("Enter the type of movie(thriller/lovestory/horror)").lower()
    if Mside == "hollywood":
        if Mtype == "thriller":
            movie = random.choice(hollywood["Thriller"])
            print(movie)
            like = input("Did you like this suggestion.(Yes/No)").lower()
            if like == "yes":
                like_movie.append(movie)
                print("Appriatiacted.")
            else:
                print("We will improve our recommendation.")
        elif Mtype == "lovestory":
            movie =  random.choice(hollywood["Lovestory"])
            print(movie)
            like = input("Did you like this suggestion.(Yes/No)").lower()
            if like == "yes":
                like_movie.append(movie)
                print("Appriatiacted.")
            else:
                print("We will improve our recommendation.")
        elif Mtype == "horror":
            movie = random.choice(hollywood["Horror"])
            print(movie)
            like = input("Did you like this suggestion.(Yes/No)").lower()
            if like == "yes":
                like_movie.append(movie)
                print("Appriatiacted.")
            else:
                print("We will improve our recommendation.")
        else:
            return "Please,Enter valid choice."
    elif Mside == "bollywood":
        if Mtype == "thriller":
            movie = random.choice(bollywood["Thriller"])
            print(movie)
            like = input("Did you like this suggestion.(Yes/No)").lower()
            if like == "yes":
                like_movie.append(movie)
                print("Appriatiacted.")
            else:
                print("We will improve our recommendation.")
        elif Mtype == "lovestory":
            movie = random.choice(bollywood["Lovestory"])
            print(movie)
            like = input("Did you like this suggestion.(Yes/No)").lower()
            if like == "yes":
                like_movie.append(movie)
                print("Appriatiacted.")
            else:
                print("We will improve our recommendation.")
        elif Mtype == "horror":
            movie = random.choice(bollywood["Horror"])
            print(movie)
            like = input("Did you like this suggestion.(Yes/No)").lower()
            if like == "yes":
                like_movie.append(movie)
                print("Appriatiacted.")
            else:
                print("We will improve our recommendation.")
        else:
            return "Please,Enter valid choice."
    elif Mside == "south":
        if Mtype == "thriller":
            movie = random.choice(south["Thriller"])
            print(movie)
            like = input("Did you like this suggestion.(Yes/No)").lower()
            if like == "yes":
                like_movie.append(movie)
                print("Appriatiacted.")
            else:
                print("We will improve our recommendation.")
        elif Mtype == "lovestory":
            movie = random.choice(south["Lovestory"])
            print(movie)
            like = input("Did you like this suggestion.(Yes/No)").lower()
            if like == "yes":
                like_movie.append(movie)
                print("Appriatiacted.")
            else:
                print("We will improve our recommendation.")
        elif Mtype == "horror":
            movie = random.choice(south["Horror"])
            print(movie)
            like = input("Did you like this suggestion.(Yes/No)").lower()
            if like == "yes":
                like_movie.append(movie)
                print("Appriatiacted.")
            else:
                print("We will improve our recommendation.")
        else:
            return "Please,Enter valid choice."
    elif Mside == "marvel":
        movie = random.choice(marvel)
        print(movie)
        like = input("Did you like this suggestion.(Yes/No)").lower()
        if like == "yes":
            like_movie.append(movie)
            print("Appriatiacted.")
        else:
            print("We will improve our recommendation.")
    elif Mside == "dc":
        movie = random.choice(dc)
        print(movie)
        like = input("Did you like this suggestion.(Yes/No)").lower()
        if like == "yes":
            like_movie.append(movie)
            print("Appriatiacted.")
        else:
            print("We will improve our recommendation.")
    else:
        return "Please,Enter valid choice."

def based_on_iMDB():
    """Top 10 movies based on iMDB and make pie chart."""
    labels = []
    ratings = []
    for lable,rate in iMDB_top_10.items():
        labels.append(lable)
        ratings.append(rate)
    plt.pie(ratings,labels=labels,autopct='%1.f%%',explode=[0.2,0.2,0.05,0.05,0.05,0.05,0.05,0.01,0.01,0.01])
#     plt.legend(title="iMDB top 10 movies.",loc="lower right")
    plt.show()
is_on = True
temp = input("Welcome to the chatbot.What can i do for you?(to find a movie - Enter 'Find')").lower()
while is_on:
    if temp == "find":
        Mside = input("Enter the film industry(hollywood/bollywood/south/dc/marvel)").lower()
        Movie_Finder(Mside)
        choice = input("Do you want to continue.(Yes/No)").lower()
        if choice == "yes":
            is_on = True
        elif choice == "no":
            is_on = False
            recommend = input("Do you want to take a glimpse to our top recommended movies(Yes/No) or based on iMDB rating(Enter 'iMDB')").lower()
            if recommend == "yes":
                liked_movies_1()
                liked_movies_bar()
            elif recommend == "imdb":
                based_on_iMDB()
    elif temp == "add":
        Mname = input("Enter the name of movie : ")
        Mlocation = input("Enter the location(hollywood/bollywood/south/marvel/dc)").lower()
        Mplace = input("Enter the place(goosebumps/lovestory/horror)").lower()
        Add_movie(Mname,Mlocation,Mplace)
    else:
        print("Enter valid choice")