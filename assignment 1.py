"""
Replace the contents of this module docstring with your own details
Name: Zimin Li
Date started: 2021/8/9
GitHub URL:
"""
FILENAME = "assignment 1.txt"
print("Travel Tracker 1.0 -By Zimin Li 3 places loaded from places.csv")
menu="""
Menu:
L - List places
R - Recommend random place
A - Add new place
M - Mark a place as visited
Q - Quit"""

def main():
    places = []
    place_file = open(FILENAME, "r") #open csv file and keep all the line into list
    places=get_places_form_file(place_file) #strip and split then string into the file
    print(menu)
    choice = input("Enter your choice:")
    while choice !="":

        if choice=="L": #show the list of the place
            show_place_list(places)
            print(menu)
            choice = input("Enter your choice:")
        elif choice=="R": #recommend an unvisited place to the customer
            show_random_place(places)
            print(menu)
            choice = input("Enter your choice:")
        elif choice=="A": #add a new place to the list
            add_new_place(places)
            print(menu)
            choice = input("Enter your choice:")
        elif choice=="M": #Mark a place where a tourist has been
            # 更新 某旅游地 为 已去过状态
            mark_place(places)
            print(menu)
            choice = input("Enter your choice:")
        elif choice=="Q": #quit option,also load how many place in csv
            with open(FILENAME,"w") as f:
                for place in places:
                    f.write(place[0]+','+place[1]+','+place[2]+','+place[3]+'\r\n')
            print("{} places saved to places.csv".format(len(places)))
            print("Have a nice day :)")
            exit()
        else:
            # Invaild choice for wrong input
            print("Invalid menu choice")
            print(menu)
            choice = input("Enter your choice:")

def get_places_form_file(place_file):
    list = []
    for line in place_file:
        line=line.strip()
        place=line.split(',')
        list.append(place)
    return list

def get_unvisited(place_lists): #caculate the unvisited place
    unvisited=0
    for line in place_lists:
        if line[3]=="n":
            unvisited+=1
    return unvisited

def show_place_list(place_list): #show the list of visited place and unvisited place
    place_num = 0
    n_place = 0
    Sort_Priority(place_list)#Covert the str to integer
    for line in place_list:
        if line[3] == "v": #find out v place in csv
            place_num = place_num + 1
            print("  {}. {} in {} {}".format(place_list.index(line) + 1, line[0].ljust(15, ' '), line[1].ljust(15, ' '), line[2]))

        else: #find out n place in csv
            n_place = n_place + 1
            place_num = place_num + 1
            print(("* {}. {} in {} {}".format(place_list.index(line) + 1, line[0].ljust(15, ' '), line[1].ljust(15, ' '), line[2])))
    print("  {} places. You still want to visit {} places".format(place_num, n_place))

def Sort_Priority(place_list):
    from operator import itemgetter
    for x in place_list:
        x[2] = int(x[2]) #convert a str number to an integer
    place_list.sort(key = itemgetter(3,2)) #sort the list, 'n' and 'v' as priority sort, number will sort after it.

def show_random_place(places): #recommend an unvisited place to the customer
    unvisited_places = []
    for place_item in places:
        if place_item[3] == "n":
            unvisited_places.append(place_item)

    import random
    unvisited_place = len(unvisited_places) #get a random index number
    if unvisited_place == 0:#if the location is visited, loop back to get a new location until it is not visited.
        print("No places left to visit!Why not add a new place?")
    else:
        place_result=unvisited_places[random.randint(0, unvisited_place-1)]
        print("Not sure where to visit next?\nHow about ...{} in {}".format(place_result[0],place_result[1]))

def add_new_place(places):  #add new places to the file
    new_place = []
    name = input("Name:")
    while name==" ": #location name input error check
        print("Input can not be blank")
        name = input("Name:")
    else:
        new_place.append(name)

    country = input("Country:")
    while country==" ":#country input error check
        print("Input can not be blank")
        country = input("Country:")
    else:
        new_place.append(country)

    priority = input("Priority:")
    while priority == " ":#priority input error check
        print("Input can not be blank")
        priority = input("Priority:")
    else:
        new_place.append(priority)
        new_place.append('n')
        places.append(new_place)
    print("{} in {} (priority {}) added to Travel Tracker".format(name,country,priority))

def mark_place(places): #find out the location information base on the input index
    unvisited_place = get_unvisited(places)
    if unvisited_place == 0: #check for the unvisited place
        print("No unvisited places")
    else:
        visited_places = []
        unvisited_places = []
        for key,place in enumerate(places):
            place_key = key+1
            unvisited_places.append(place_key)
            if place[3]=="v":
                visited_places.append(place_key)
        show_place_list(places)
        print("Enter the number of a place to mark as visited")

        place_num = input(">>> ")
        while place_num !=" ":   #error checking for the loop
                print("Input can not be blank")
                if place_num.isdigit():
                    place_num = int(place_num)
                    if place_num <= 0:
                        print("Number must be > 0")
                    elif (place_num not in unvisited_places):
                        print("Invalid place number")
                    elif (place_num in visited_places):
                        print("You have already visited {}".format(places[place_num-1][0]))
                    else:
                        break
                else:
                    print("Invalid input;enter a valid number")
        places[place_num-1][3] = 'v'
        print("{} in {} visited!".format(places[place_num-1][0],places[place_num-1][1]))



main()
