import mysql.connector as mysql

try:
    db = mysql.connect(host="localhost", user="root", database="college")
    print("connected successfully")
except Exception as e:
    print("Impossible connection")
    # the cursor is what allows me to use the CRUD SQL commands
    # buffered means I can run multiple queries at a time without errors

command_handler = db.cursor(buffered=True)


def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print("5. Show all registered students")
        print("6. Show all registered teachers")
        print("7. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("\nRegister New Student")
            username = input(str("Student username : "))
            password = input(str("Student password : "))
            command_handler.execute(
                f"INSERT INTO users (username,password,privilege) VALUES ('{username}','{password}','student')")
            db.commit()
            print(username + " has been registered as a student")
        elif user_option == "2":
            print("\nRegister New Teacher")
            username = input(str("Teacher username : "))
            password = input(str("Teacher password : "))
            command_handler.execute(
                f"INSERT INTO users (username,password,privilege) VALUES ('{username}','{password}','teacher')")
            db.commit()
            print(username + " has been registered as a teacher")
        elif user_option == "3":
            print("\nRemove an existing student")
            username = input(str("Student username : "))
            command_handler.execute(f"DELETE FROM users WHERE username = '{username}' AND privilege = 'student'")
            db.commit()
            print(username + " - Student - HAS BEEN REMOVED FROM THE SYSTEM")
        elif user_option == "4":
            print("\nRemove an existing teacher")
            username = input(str("Teacher username : "))
            command_handler.execute(f"DELETE FROM users WHERE username = '{username}' AND privilege = 'teacher'")
            db.commit()
            print(username + " - Teacher - HAS BEEN REMOVED FROM THE SYSTEM")
        elif user_option == "5":
            print("All registered Students\n")
            select_all_students = "SELECT * FROM users WHERE privilege = 'student' "
            command_handler.execute(select_all_students)
            students = command_handler.fetchall()
            for student in students:
                print(student)
        elif user_option == "6":
            print("All registered Teacher\n")
            select_all_teachers = "SELECT * FROM users WHERE privilege = 'teacher' "
            command_handler.execute(select_all_teachers)
            teachers = command_handler.fetchall()
            for teacher in teachers:
                print(teacher)


def auth_admin():
    print("\nAdmin Login\n")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "1234":
        admin_session()
    elif username != "admin":
        print("wrong username")
    elif password != "1234":
        print("Incorrect password...")
    else:
        print("Login details not recognised")


def main():
    while 1:
        print("Welcome to the college system\n")
        print("1. Login as student")
        print("2. Login as Teacher")
        print("3. Login as ADMIN")

        user_option = input(str("Option: "))
        if user_option == '1':
            print("Student Login")
        elif user_option == '2':
            print("Teacher Login")
        elif user_option == '3':
            auth_admin()
            # print("ADMIN Login")
        else:
            print("No valid option was selected")


main()
