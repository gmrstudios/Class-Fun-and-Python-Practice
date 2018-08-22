def display_message(chapter):
    print("I am learning about functions in chapter " + chapter + ".")

def favorite_book(title):
    print("One of my favorite books is " + title.title() + ".")

print("Type quit as message to exit the program.")
message = ""

while message != 'quit':
    print("Type 1 for chapter and 2 for book.")
    choice = input("Do you want to give a chapter or a book?")
    if choice == '1':
        message = input("What chapter are you learning about?")
        display_message(message)
    elif choice == '2':
        message = input("What is your favorite book?")
        favorite_book(message)
    else:
        print("You must type a 1 or 2 digit for your choice.")
