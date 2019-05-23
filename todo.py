def displayList(myList):
    print("Your List.")

#creates a new dictionary and adds it to a list.
def addToList(myList, title, description, deadline):
    myDictionary = {
        "title": title,
        "description": description,
        "deadline": deadline
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

#List
toDoList = []
# loop for repeated user input.
while True:
    displayList(toDoList)
    userInput = input(">")
    # Create a new todo
    if userInput.lower() == "n":
        title, description, deadline = newTaskInput()
        addToList(toDoList, title, description, deadline)
    # Break out of loop, ending program
    elif userInput.lower() == "q":
        break