import csv
import os 


#هنا قائمة العملاء الموجودين 
users={}

def add_user(user):
   name_user=input("Enter your name:")
   if name_user in users:
      print("User already exists ")
      return
   
   password=input("Enter your password: ")
   users[name_user]={"password":password, "balance":0.0 ,"transaction":[]}
   saving_users(users)
   print("User added successfuly !!!")

def load_users():
   users_acc=[]
   if not os.path.exists("users_account.csv"):   #اذا كان الملف غير موجود ننشئه براس الجدول فقط 
      with open("users_account.csv","w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["name_user","password","balance"])
      return users_acc

   with open("users_account.csv","r") as file:    #قراءة البيانات من الملف  
      reader=csv.DictReader(file)
      for row in reader:
         row["balance"]=float(row['balance'])   # تحويل الرصيد الى رقم 
         users_acc.append(row)
   return users_acc


users_list=load_users()
users={user["user_name"]: {"password": user["password"], "balance": user["balance"],"transaction":[]} for user in users_list} 

def saving_users(users):
   with open("users_account.csv","w",newline="") as file:
      writer=csv.DictWriter(file, fieldnames=["user_name","password","balance"])
      writer.writeheader()
      for name, data in users.items():
         writer.writerow({
            "user_name": name,
            "password": data["password"],
            "balance":data["balance"]
         })

def withdraw(name_user):
    try:
        amount=float(input('Enter the amount:'))
    except:
        print("Invaild input")
        return
   


    if amount <= 0:
        print('ERROR THE AMOUNT IS CAN NOT BE <= ZERO')
        return
    if amount >users[name_user]['balance']:
       print('ERROR : invalid amount')
       return

    users[name_user]['balance'] -= amount
    print('Done')
    users[name_user]['transactions'].append(f'withdraw, {amount}')
    saving_users(users)

    
def deposit(name_user):
    try:
       amount=float(input('Enter the amount:'))
    except:
       print("Invaild amount")
       return
       

    users[name_user]['balance'] += amount
    print('Done')
    users[name_user]['transactions'].append(f'deposit, {amount}')
    saving_users(users)

def print_transactions(name_user):     
    print(users[name_user]['transactions'])
    print('Done')

def print_balance(name_user):
    print(users[name_user]['balance'])
    print('Done')

#-----------------------------------------------------------------------------

#هنا بداية البرنامج 
print('Welcome to ATM')
name_user=input('Enter the user name :')

if name_user not in users:    #اذا كان العميل غير موجود 
   print('you are new user , create account')
   password=input('create your password:')
   users[name_user]={"password":password,"balance":0.0,"transactions":[]}
   saving_users(users)
   print('create account is done')

else:
   password=input('Enter your password here: ')
   if password!=users[name_user]['password']:
      print('the password is not correct')
      exit()


   



while True:
    
      #اختيار العميل العمليه المراده من القائمه
      print('\n1 - withdraw')
      print('2 - deposit')
      print('3 - show transactions')
      print('4 - show balance')
      print('5 - change my password')
      print('6 - Exit')
      choice=input('Enter your choice:')
      if choice =='1':
        withdraw(name_user)
      elif choice=='2':
        deposit(name_user)
      elif choice=='3':
        print_transactions(name_user)
      elif choice=='4':
        print_balance(name_user)
      elif choice=='5':
         new_password=input('Enter the new password here:')
         users[name_user]['password']=new_password
         saving_users(users)
         print('Done')
      elif choice=='6':
        print('good bay!!!')
        break
      else:
         print("Invaild choice")




