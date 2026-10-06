import datetime
dt = datetime.datetime.now()
print(dt)


class journal:

    def __init__(self):

        with open("journal.txt","x")as file:
         print(file)

    def add_new_entery():
       
       try:
            new_entery = input("Enter your journal entry: ")
            with open("journal","a")as file:
                file.write(str(dt) + new_entery +"\n")
                print("entery add successfully!")
       except:
              print("error in add entry")
           

    def view_all_entery():
        print("your journal entries")
        print("-------------------------------")

        try:
            with open("journal","r")as file:
                data = file.read()
                print(data)
        except:
            print("no journal entries found. start by adding a new entery")   

    def search_entery():
       
       try:
            with open("journal","r")as file:
                entery = input("enter the keyword or data search")
                for x in file:
                    if entery.lower() in x.lower():
                        print(f"{x} [{dt}]")
                        break
                else:
                        print("not found data")
       except:      
       
           print(f"No entris were fond for the keyword:{entery}.")         


    def delete_entery():
       try:
          a = input("are you sure you want to delete all entrise?(yes/no):yes")
          if a == "yes":
            with open("journal","w")as file:
                file.write("")

          elif  a == "no":
                print("your choice no") 

          else:
                print("select(yes/no)")
       except:   
            print("No journal entries to delete")                       
obj = journal

while True:
   print("welcome to personal journal Manager")   
   print("Please select an option: ")
   print("1. Add a new entery: ")
   print("2. View all entery: ")
   print("3. Search for an entery: ")
   print("4. Delete all entery: ")
   print("5. Exit: ")           

   choice = int(input("Entery your choice number: "))

   if choice == 1:
       obj.add_new_entery()

   elif choice == 2:
        obj.view_all_entery()

   elif choice == 3:
         obj.search_entery()

   elif choice == 4:
         obj.delete_entery()

   elif choice == 5:
        print("Thank you for using Personal Journal Manager . Goodbye!")   
        break
   else:
       print("Invalid Choice Number")                

    