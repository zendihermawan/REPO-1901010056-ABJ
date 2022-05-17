while True:
    def menuTrunk():
        print("*"*20)
        print("Menu Trunk")
        print("*"*20)
        print("a. Add Trunk \nb. Show Trunk \nz. Exit")
        print("*"*20)

    def addTrunk():
        while True:
            file = open("trunk-database.txt","a")
            x = input("Enter Switch or type z to stop: ")
            if x == 'z':
                break
            y = input("Enter Trunk Name: ")
            file.write("Trunk ID: "+x+", Trunk NAME: "+y+"\n")

    def showTrunk():
        file = open("trunk-database.txt","r")
        print("*"*50)
        for item in file:
            item = item.strip()
            print(item)
        print("*"*50)
        file.close()
        
# Main Apps
    menuTrunk()
    i = input("Enter the choice: ")
    print("*"*20)
    if i == 'a' :
        addTrunk()
        print("\n")
    elif i == 'b':
        print()
        showTrunk()
        print("\n")
    elif i == 'z':
        break
    else :
        print("Please provide valid input!")
        print("\n")