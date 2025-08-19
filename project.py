records = []
def Add_Record():
    ID = int(input("\nEnter your ID : "))
    for record in records:
        if record["ID"] == ID:
            print("ID Already Exists")
            return
    Name = input("Enter your name : ")
    Age = int(input("Enter your age : "))
    Department = input("Enter your department : ")
    record = {"ID":ID , "Name":Name , "Age":Age , "Department":Department}
    records.append(record)
    print("\nRecord added successfully. \n")
    
def View_Record():
    if records :
        print("\n ------ All Records ------ \n")
        sorted_records = sorted(records, key=lambda x: x["ID"])
        for record in sorted_records :
            print(f"ID : {record['ID']} , Name : {record['Name']} , Age : {record['Age']} , Department : {record['Department']}")
    else :
        print("\nNo Record Found.")


def Search_Record():
    ID = int(input("\nEnter your ID : "))
    for record in records:
        if record["ID"] == ID:
            print(f"\nID : {record['ID']} , Name : {record['Name']} , Age : {record['Age']} , Department : {record['Department']}")
            return
    print("\nNo Record Found.")


def Update_Record():
    ID = int(input("\nEnter your ID : "))
    for record in records:
        if record["ID"] == ID:
            print("\nWhat would you like to update?")
            print("1. Name")
            print("2. Age")
            print("3. Department")

            choice = input("\nEnter your choice : ")

            if choice == '1':
                New_name = input("\nEnter updated name : ")
                record["Name"] = New_name
                print("\nName updated successfully")

            elif choice == '2':
                New_age = int(input("\nEnter updated age : "))
                record["Age"] = New_age
                print("\nAge updated successfully")

            elif choice == '3':
                New_department = input("\nEnter updated department : ")
                record["Department"] = New_department
                print("\nDepartment updated successfully")
            else :
                print("Invalid choice. Try again")
            break
    else :
        print("\nRecord Not Found.")


def Delete_Record():
    ID = int(input("\nEnter your ID : "))
    for record in records:
        if record["ID"] == ID:
            records.remove(record)
            print("\nRecord delete successfully")
            return
    else :
        print("\nRecord Not Found.")

def Show_Record_Count():
    print(f"\nTotal Number of records : {len(records)}")


def main_menu():
    while True :
        print("\n ------ Record Management System ------ \n")
        print("1. Add Record")
        print("2. View Record")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Show Record Count")
        print("7. Exit")
        
        choice = input("\nEnter your choice : ")

        if choice == '1' :
           Add_Record()

        elif choice == '2' :
            View_Record()

        elif choice == '3' :
            Search_Record()

        elif choice == '4' :
            Update_Record()

        elif choice == '5' :
            Delete_Record()

        elif choice == '6' :
            Show_Record_Count()

        elif choice == '7' :
            print("\nExiting Program. Goodbye!")
            break

        else :
            print("\nInvalid Choice. Please Try Again.")

main_menu()