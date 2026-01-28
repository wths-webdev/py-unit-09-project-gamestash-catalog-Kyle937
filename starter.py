
import time
import random
import os
import sys

def clear_terminal():
    if sys.platform.startswith('win32'):
        os.system('cls')
    else:
        os.system('clear')
clear_terminal()
games = {
    "GTA V": 2013,
    "Ratchet & Clank": 2021,
    "Spider-Man: Miles Morales": 2020,
    "God of War Ragnarok": 2022,
    "The Legend of Zelda: Tears of the Kingdom": 2023,
    "Super Mario Odyssey": 2017,
    "Princess Peach": 2024,
    "Mario Kart 8 Deluxe": 2017
}

# get_inventory_count(): Returns how many total games there are in a readable format.
def inventory():
    slot = 1
    for item in games:
        slot +=1
    print("there are " + slot + " games")

# add_game(title, year): Adds a game to the inventory.
def addGame(title, year):
    games.update({title: year})

# remove_game(title): Removes a game from the inventory.
def removeGame(title):
    if title in games:
        games.pop(title)
        print(title + " was removed successfully.")
    else:
        print(title + " is not in the list")
# display_inventory()
def showInventory():
    slot = 1
    for item in games:
        print(slot, item)
        slot +=1

# search_year(year)
def searchYear(year):
    print(f"All games from {year}:")
    for game in games:
        if games[game] == year:
            print(f"   {game}")

# search_title(title)
def searchTitle(title):
    print(title, "was made in",games[title])


# Welcome message
print("\nWelcome to...")
print(" _____________________________  \n"
    "/        _____________        \\\n"
    "| == .  |             |     o |\n"
    "|   _   |             |    B  |\n"
    "|  / \\  |   Game      | A   O |\n"
    "| | O | |      Stash  |  O    |\n"
    "|  \\_/  |             |       |\n"
    "|  :::  |_____________| . . . |\n"
    "\\_____________________________/")

while True:
    clear_terminal()
    # Display menu to user
    print()
    print("----------- Menu ----------")
    print("Add game (add)")
    print("Remove game (remove)")
    print("Show inventory (show)")
    print("Search by year (year)")
    print("Search for a title (title)")
    print("Quit (q)\n")
    user_selection = input("What would you like to do? ").lower()
    clear_terminal()
    # Use conditional statements to call functions based on user input
    if user_selection == "add":
        print("What game would you like to add?")
        title = input("Title: ")
        year = input("Year released: ")

        # update() will add to the dictionary if the key does not exist
        addGame(title, year)

    elif user_selection == "remove":
        if len(games) > 0:
            game = input("What title would you like to remove? ")

            removeGame(game)
    
    elif user_selection == "show":
        if len(games)>0:
            print("There are " + str(len(games)) + " games in your inventory.")
            showInventory()
        else:
            print("there is currently no games in the list")

    elif user_selection == "year":
        if len(games)>0:
            year = int(input("Which year would you like to seach for? "))

            searchYear(year)
        else:
            print("theres no games currently")
    elif user_selection == "title":
        if len(games)>0:
            title = input("Which title would you like to search for? ")
            searchTitle(title)
        else:
            print("there are no games currently")
    elif user_selection == "q":
        print("Bye bye!")
        break # out of the loop

    else:
        print("Error: That was not an option.\n")

print("")