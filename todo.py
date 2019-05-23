import os
# Clear console
# cls for windows, clear for linux
clear = lambda: os.system('cls' if os.name == "nt" else 'clear')

# Prints a nice looking list
def displayList(myList):
    if len(myList) > 0:
        print("Your List:")
        # Go through all items in the list
        for i in range(len(myList)):
            if myList[i]["done"]:
                print("[X]", end="")
            else:
                print("[-]", end="")

            # Print index + 1 for readabiltiy
            # No new line at end
            print("[" + str(i + 1) + "]", end=" ")
            
            print(myList[i]["title"] + ":")
            print(myList[i]["description"])
            # New Line for readability
            print("\nDeadline:", myList[i]["deadline"])
            # Extra line for readability.
            print()
    else:
        print("Your List is empty.")

# Creates a new dictionary and adds it to a list
def addToList(myList, title, description, deadline):
    myDictionary = {
        "title": title.strip(),
        "description": description.strip(),
        "deadline": deadline.strip(),
        "done": False
    }
    myList.append(myDictionary)
    print("Added item to list.")


# Gets all necessary user input
def newTaskInput():
    clear()
    print("Creating new To doooooooooooo.!1@")
    title = input("Title: ")
    description = input("Description: ")
    deadline = input("Deadline: ")
    return title, description, deadline

def displayControls(noOfItems):
    print("[N]ew task")
    if noOfItems == 1:
        print("[1] Change done status for task.")
    elif noOfItems > 1:
        print("[1-" + str(noOfItems) + "] Change done status for task")
    print("[Q]uit")
    
# List
toDoList = []
# Loop for repeated user input
while True:
    # Clear console and display list
    clear()
    displayList(toDoList)
    displayControls(len(toDoList))
    userInput = input("> ").lower().strip()
    # Create a new todo
    if userInput == "n":
        # Get input
        title, description, deadline = newTaskInput()
        # Add to list
        addToList(toDoList, title, description, deadline)
    # Break out of loop, ending program
    elif userInput == "q":
        break
    # Check if user inputed a number to toggle done status
    else:
        # Try to convert user input string to int
        try:
           int(userInput)
        except:
            userInput = 0
        else:
            userInput = int(userInput)
            # If it succeds, check if it's within list length
            if userInput >= 1 and userInput <= len(toDoList):
                # toogle done status
                toDoList[userInput - 1]["done"] = not toDoList[userInput - 1]["done"]

            
