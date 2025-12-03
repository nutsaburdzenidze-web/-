import json, os

path = "data.json" # ფაილი სადაც შეინახება ინფორმაცია
def get_data():
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            try :
                data = json.loads(f.read())
            except json.JSONDecodeError:
                data = []
    else:
        data = []
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    return data

def balance_check(first_name, last_name): # ბალანსის შემოწმება
    data = get_data()
    for user in data:
        if user["first_name"] == first_name and user["last_name"] == last_name:
            return round(user["balance"], 2)
    return 0
        
def get_user_info(): # მომხმარებლის სახელი და გვარის შეყვანა
    first_name = input("please enter yout first name: ")
    last_name = input("please enter last name: ")
    return first_name, last_name
# ავტორიზახია
def user_authenfication(first_name, last_name):
    data = get_data()
    user_exists = False
    for user in data:
        if  user["first_name"] == first_name and user["last_name"] == last_name:
            user_exists = True
            break
# მომხმარებლის დმატება თუ არ არსებობს
    if not user_exists:
        data.append({"first_name":first_name, "last_name":last_name, "balance":0})
        with open(path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, indent=2))
        print(f"New user {first_name} {last_name} cretaed!")
    else:
        print(f"Welcome back {first_name} {last_name}!")
 # დეპოზიტი
def make_deposit(first_name, last_name, amount):
    print(f"You are making deposit of {amount} GEL")
    balance = balance_check(first_name, last_name)
    update_data(first_name, last_name, balance + amount)
    print(f"Operation Successfull!\nYour balance now is {balance_check(first_name, last_name)}")
# ახალი მონაცემების შენხვა 
def update_data( first_name, last_name, new_bal):
        data = get_data()
        for user in data:
            if user['first_name'] == first_name and user['last_name'] == last_name:
                user['balance'] = round(new_bal, 2)
        with open(path, mode='w', encoding='utf-8') as f:
                f.write(json.dumps(data, indent=2))
 #გამოტანა               
def withdraw_money(first_name, last_name , amount):
    balance = balance_check(first_name, last_name)
    commision = round(amount*0.01, 2) #  საკომისიო თანხის 1 პროცენტი
    total = round(amount + commision, 2)
    if balance >= total:
        print(f"You are withdrawing amount of {amount} GEL, the commision is {commision}")
        update_data(first_name, last_name, balance-total)
        print(f"Operation Successfull!\nYour balance now is {balance_check(first_name, last_name)}")
    else:
        print("You dont have enough money on your balance")


# მენიუ
def print_options():
    print("1. balance check")
    print("2. make deposit")
    print("3. withdraw money")
    print("4. Exit")


first_name, last_name = get_user_info()
print("Authenticating user....")
user_authenfication(first_name, last_name)
while True:
    print_options()
    try:
        op = int(input())
        if op == 1:
            print(balance_check(first_name, last_name))
        elif op == 2:
            amount = float(input("Enter amount you want to deposit!: "))
            if amount > 0:
             make_deposit(first_name, last_name, amount)
        elif op == 3:
            amount = float(input("Enter amount you want to withdraw!: "))
            if amount > 0:
             withdraw_money(first_name, last_name, amount)
        elif op == 4:
            print("Goodbye👋🏻!")
            break
        else:
            print("please enter valid choice")
            continue
    except ValueError:
        print("invalid input. enter a number 1-4")
