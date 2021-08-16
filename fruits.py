
fruits = {}
cart_list = []
cart_l=[]


def print_fruit_menu():
    print("1.Add fruit")
    print("2.Delete fruit by name")
    print("3.Search fruit by name and rate")
    print("4.Change fruit name and rate")
    print("5.Display and Buy")
    print("6.Display")
    print("7.Exit")


def add_fruit_details():
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

def delete_fruit():
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

def search_menu():
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


def change__fruit_menu():
    print("1  .Change fruit name")
    print("2  .change rate")
    choice = int(input("\tenter your choice : "))
    if choice == 1:
        fruit_id = input("\tEnter fruit_id :")
        if fruit_id not in fruits.keys():
            print("\twrong fruit_id")
        else:
            fruits[fruit_id]['name'] = input("\tEnter new name : ")  
    elif choice == 2:
        fruit_id = input("\tEnter fruit id :")
        if fruit_id not in fruits.keys():
            print("\twrong fruit_id")
        else:
            fruits[fruit_id]['rate'] = input("\tEnter new rate : ")  

def add_to_cart():
    print("........................Adding to cart..........................................")
    fru_id = input("\tEnter the fruit id : ")
    if fru_id in fruits.keys():
        cart_list.append(fru_id)
        print(cart_list)
    else:
        print("\tWrong fruit id")

def del_fruit_id_from_cart():
    fruit_id = input("\tenter the fruit id for delete : ")
    for i in cart_list:
        if i == fruit_id:
            cart_list.remove(fruit_id)
            print(cart_list)
        else:
            print("\twrong fruit id")

def display_bill():
    print("\t-fruit_id-----fruit name -----fruit rate --")
    for i in cart_list:
        
        print(f"\t{i} | {fruits[i]['name']} | {fruits[i]['rate']}")

def manage_add_cart():
    print("\t1 . Add fruits to cart")
    print("\t2 . Delete fruit from")
    print("\t3 . cart Bill")
    print("\t4 . exit")

def main_manage_add_cart(): 
    manage_add_cart()
    while True:
        ch = int(input("\tEnter the choice  : "))
        if ch == 1:
            add_to_cart()
        elif ch == 2:
            del_fruit_id_from_cart()
        elif ch == 3:
            display_bill()
        elif ch == 4:
            break;  

        else:
            print("\tinvalid fruit id")
        

def display_fruit_details():
    for frtid,fruit in fruits.items():
        print(f"\t{frtid} | {fruit['name']} | {fruit['rate']} | {fruit['imported_from']} | {fruit['import_date']} | {fruit['buy_price']} ")

while True :
    print_fruit_menu()
    ch = int(input("\tEnter the choice  : "))
    if ch == 1 :
        print("-----Add fruit-------")
        add_fruit_details()
    elif ch == 2 :
        print("-----Delete fruit by name-----")
        delete_fruit()
    elif ch == 3:
        print("--------Search fruit by name and rate------")
        search_menu()
    elif ch == 4:
        print("-------Change fruit name and rate------")
        change__fruit_menu()
    elif ch == 5:
        print("---------Add to cart------")
        main_manage_add_cart()
    elif ch == 6:
        print("-----------Display fruit details --------")
        display_fruit_details()
    elif ch == 7:
        print("Exit")
        break
    else:
        print("Invalid choice")
