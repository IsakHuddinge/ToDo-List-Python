import os
# Clear console.
# cls for windows, clear for linux.
clear = lambda: os.system('cls' if os.name == "nt" else 'clear')


def displayList(myList):
    if len(myList) > 0:
        print("Your List:")
        # Go through all items in the list.
        for i in range(len(myList)):
            # Print index + 1 for readabiltiy.
            # No new line at end.
            print("[", i + 1, "] ", end="")
            
            print(myList[i]["title"] + ":")
            print(myList[i]["description"])
            # New Line for readability.
            print("\nDeadline:", myList[i]["deadline"])
    else:
        print("Your List is empty.")

# Creates a new dictionary and adds it to a list.
def addToList(myList, title, description, deadline):
    myDictionary = {
        "title": title.strip(),
        "description": description.strip(),
        "deadline": deadline.strip(),
        "done": False
    }
    myList.append(myDictionary)
    print("Added item to list.")


# Gets all necessary user input.
def newTaskInput():
    print("Creating new To doooooooooooo.!1@")
    title = input("Title: ")
    description = input("Description: ")
    deadline = input("Deadline: ")
    return title, description, deadline

# List
toDoList = []
# loop for repeated user input.
while True:
    # Clear console and display list
    clear()
    displayList(toDoList)
    userInput = input(">").lower().strip()
    # Create a new todo
    if userInput == "n":
        title, description, deadline = newTaskInput()
        addToList(toDoList, title, description, deadline)
    # Break out of loop, ending program
    elif userInput == "q":
        break