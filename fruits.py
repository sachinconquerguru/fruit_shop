"""
-Change fruit name and rate
-Add to cart(List the fruits with fruit_id->select id->store in cart list)
-Display
Properties: fruit_id,fruit_name,rate,imported_from,import_date,buy_price
"""



fruits = {}
while True:
    print("1.Add fruit")
    print("2.Delete fruit by name")
    print("3.Search fruit by name and rate")
    print("4.Change fruit name and rate")
    print("5.Add to cart")
    print("6.Display")
    print("7.Exit")
    choice = int(input("Enter your choice :"))

    if choice == 1:
        fruit_id = input("\tEnter fruit_id:")
        if fruit_id not in fruits.keys():

            name = input("\tEnter fruit name :")
            rate = input("\tenter the rate of this fruit :")
            imported_from = input("\tEnter imported_from :")
            import_date = input("\tEnter import_date (in DD/MM/YYYY) :")
            buy_price = int(input("\tEnter buy_price:"))
            temp ={
                "name":name,
                "rate":rate,
                "imported_from":imported_from,
                "import_date":import_date,
                "buy_price":buy_price
                }
            fruits[fruit_id] = temp        

    elif choice == 2:
        fruit_id = input("\tEnter fruit_id:")
        name = input("\tEnter fruit name :")
        flag = False
        if fruit_id in fruits.keys():
            for fruitid in fruits.values():
                if fruitid["name"] == name :
                    flag = True
        else:
            print("wrong id ")
        if flag == True:
            del fruits[fruit_id]
    
    elif choice == 3:
        print("1 .search by name ")
        print("2 .search by rate")
        choice1 = int(input("Enter your choice :"))

        if choice1 == 1:
            name = input("Enter name you want to search :")
            for i in fruits.values():
                if i["name"] == name:
                    print(f"\t{i['name']} | {i['rate']} | {i['imported_from']} | {i['import_date']} | {i['buy_price']} ")
                    flag = True
                    break
            if flag == False :
                print("\t Not Found")
        elif choice1 == 2 :
            rate = input("Enter rate you want search : ")
            for i in fruits.values():
                if i["rate"] == rate:
                    print(f"\t{i['name']} | {i['rate']} | {i['imported_from']} | {i['import_date']} | {i['buy_price']} ")
                    flag = True
                    break
            if flag == False :
                print("\tNot Found")


    elif choice == 4:
        print("1  .Change fruit name")
        print("2  .change rate")
        choice = int(input("\tenter your choice : "))
        if choice == 1:
            fruit_id = input("\tEnter fruit_id :")
            if fruit_id not in fruits.keys():
                print("\twrong fruit_id")
            else:
                fruits[fruit_id]['name'] = input("\tEnter new name")  
        elif choice == 2:
            fruit_id = input("\tEnter fruit id :")
            if fruit_id not in fruits.keys():
                print("\twrong fruit_id")
            else:
                fruits[fruit_id]['rate'] = input("\tEnter new rate")  

    elif choice == 5:

        cart_list = []
        for id,fruitname in fruits.items():
            cart_list.append(id + ":" + fruitname["name"])
        for i in cart_list:
            print(i)
        print("you can select from above list to add cart ")
        cart_l=[] 
        print("\tyou can enter fruit id to add cart")  
        cart_inp = int(input("enter the fruit_id to add cart : "))
        cart_l.append(cart_inp)
        print("\t your cart fruit ids",cart_inp)



    elif choice == 6:
        for frtid,fruit in fruits.items():
            print(f"\t{frtid} | {fruit['name']} | {fruit['rate']} | {fruit['imported_from']} | {fruit['import_date']} | {fruit['buy_price']} ")
     
              

    elif choice == 7:
        break;
    else:
        print("invalid choice")


