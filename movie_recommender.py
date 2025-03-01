# Prompt user for movie preferences
action = input("Do you like action movies? (yes/no):").lower() == "yes"
comedy = input("Do you like comedy movies? (yes/no):").lower() == "yes"
drama = input("Do you like drama movies? (yes/no):").lower() == "yes"

# Combine the booleans using logical operators to determine the movie genre
if action and comedy and not drama:
    genre = "Action-Comedy"
elif action and drama and not comedy:
    genre = "Action-Drama"
elif comedy and drama and not action:
    genre = "Comedy-Drama"
elif action:
    genre = "Action"
elif comedy:
    genre = "Comedy"
elif drama:
    genre = "Drama"
else:
    genre = "Unknown"

# Recommend movies based on the user's preferred genre using conditional statements
if genre == "Action-Comedy":
    print("Recommended movies: 'The Blue Brothers', 'Lock, Stock and Two Smoking Barrels', 'Bad Boys for Life'")
elif genre == "Action-Drama":
    print("Recommended movies: 'The Fugitive', 'Top Gun', 'Avengers End Game'")
elif genre == "Comedy-Drama":
    print("Recommended movies: 'Ted', 'Juno', 'Clueless'")
elif genre == "Action":
    print("Recommended movies: 'John Wick, 'The Dark Knight', 'Twister'")
elif genre == "Comedy":
    print("Recommended movies: 'Mouse Hunt', 'Night at the Museum', 'Airplane'")
elif genre == "Drama":
    print("Recommended movies: 'Erin Brockovich', 'Forest Gump', 'Bridget Jones's Diary'")
else:
    print("Sorry we couldn't determine your movie preferences.")


