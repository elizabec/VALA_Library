import sys

def menu_select(menu):
    while menu:
        select = input("\nPlease select one of the following:\n1. Add a Book\n2. Show existing database\nQ. Exit\nPress enter to confirm\n")
        if select == "1":
            add_book()
        elif select == "2":
            show_database()
        elif select == "Q" or select == "q":
            print("Exiting...")
            exit()
        else:
            print("Please choose a valid option\n")

def add_book():
    title = input("Please enter the book title: ")
    author = input("Please enter the book author: ")
    isbn = input("Please enter the ISBN number: ")
    if len(isbn) < 13 or len(isbn) > 13:
        print("The given ISBN number is not the correct length, please enter a valid 13-digit ISBN number")
        isbn = input("Please enter the ISBN number: ")
    year = input ("Please enter the publishing year: ")

    print("\nYou have entered the following:\nTitle: " + title + "\nAuthor: " + author + "\nISBN: " + isbn + "\nPublished: " + year)
    add = input("\nWould you like to add this to the database? (Y/N)\n")
    if add == "Y" or add == "y":
        print("Adding to database!")
        app_file = title + "/" + author + "/" + isbn + "/" + year + "\n"
        with open(sys.argv[1], "a") as lib:
            lib.write(app_file)
        sort_database(sys.argv[1])
    elif add == "N" or add == "n":
        print("Returning to menu...")

def show_database():
    with open(sys.argv[1], "r") as lib:
        empty_check = lib.read(1) #ensuring that there is data to read in the database
        if not empty_check:
            print("There is nothing in the database!\n")
    with open(sys.argv[1], "r") as lib:
        print("\nThe following books are currently in the database:")
        for line in lib:
            strip_lines=line.strip()
            lib_line = strip_lines.split("/")
            print("\nTitle: "+ lib_line[0])
            print("Author: "+ lib_line[1])
            print("ISBN: "+ lib_line[2])
            print("Published: "+ lib_line[3])

def sort_database(filepath):
    temp_dict = {}
    with open(filepath, "r") as lib:
        for line in lib:
            lines = line.strip()
            dates = lines.split("/")
            lib_key = dates[0] + "/" + dates[1] + "/" + dates[2] + "/"
            lib_val = dates[3]
            temp_dict[lib_key] = lib_val
        temp = sorted(temp_dict.items(), key=lambda x:x[1])
        lib_dict = dict(temp)
    with open(filepath, "w") as lib:
        for k, v in lib_dict.items():
            sort_str = k + v + "\n"
            lib.write(sort_str)

if __name__ == '__main__':
    menu_select(menu=True)
    