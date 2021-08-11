fruits = []
while True:
    print("1.Add fruit")
    print("2.Delete fruit")
    print("3.Search fruit")
    print("4.Change fruit name and rate")
    print("5.Display Employee name : ")
    print("6.exit")
    choice = int(input("Enter your choice :"))

    if choice == 1:
        
        name = input("Enter fruit name :")
        rate = int(input("enter the rate of this fruit :"))
        if name:
            fruits.append([name,rate])
            print(fruits)   

    elif choice == 2:
        print("choose fruits name from this ")
        name = input("Enter fruits name to delete : ")
        for i in fruits:
            if (fruits[fruits.index(i)][0] == name):
                fruits.pop(fruits.index(i))
        print(fruits)        
            

    
    elif choice == 3:
        print("1 .search by name ")
        print("2 .search by rate")
        choice1 = int(input("Enter your choice :"))

        if choice1 == 1:
            name = input("Enter name you want to search :")
            for i in fruits:
                if (fruits[fruits.index(i)][0] == name):
                    print("fruit " + name +" showing in the list ")

        elif choice1 == 2:
            rate = int(input("Enter the rate you want search : "))
            for i in fruits:
                if (fruits[fruits.index(i)][1] == rate):
                    print("fruit rate showing in the list ")

    

    elif choice == 4:
        print("1 .update name of the fruit ")
        print("2 .update rate of the fruit")
        choice2 = int(input("Enter your choice :"))
        if choice2 == 1:
            name = input("Enter name you want to update :")
            new_name = input("Enter the new name:")
            for i in fruits:
                if (fruits[fruits.index(i)][0] == name):
                    fruits[fruits.index(i)][0]=new_name
                    
        elif choice2 == 2:
            rate = int(input("Enter the rate you want update : "))
            new_rate = int(input("Enter new rate for update : "))
            for i in fruits:
                if (fruits[fruits.index(i)][1] == rate):
                    fruits[fruits.index(i)][1]=new_rate
                                           
        
    elif choice == 5:
        print(fruits)
            

    elif choice == 6:
        break;
    else:
        print("invalid choice")


