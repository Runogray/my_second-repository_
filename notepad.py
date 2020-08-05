class Notepad():

    logged_user = ""

    def register(self):
        
        name = input("Please enter your name - ")
        password = input("Please enter your password - ")

        file_name = "oop/notes_pass.csv"
        file = open(file_name, "a")

        file.write(f"{name},{password}\n")
        print("Successfully created account \n")

    def login(self):

        name_input = input("Please enter your name - ")
        password_input = input("Please enter your password - ")

        file_name = "oop/notes_pass.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(",")
            name = splitted_line[0]
            password = splitted_line[1]

            if name == name_input:
                print("Username was correct ..!!")
                if password_input == password:
                    print("Loggin Successfull..!!")
                    
                    self.logged_user = name_input
                    break
                else:
                    print("Sorry your password was wrong")

        else :
            print("Username was wrong ..!!")

    def write_note(self):

        name = input("Please enter your name - ")
        title = input("Please enter your title - ")
        body = input("Please enter your body - ")

        file_name = "oop/notes.csv"
        file = open(file_name, "a")

        file.writelines(f"{name}:;{title}:;{body}\n")
        file.close()

    def read_data(self):
        
        file_name = "oop/notes.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(":;")
            name = splitted_line[0]
            title = splitted_line[1]
            body = splitted_line[2]

            print("###########################")
            print("Name :", name)
            print("Title :", title)
            print("- - - - - - - - - - - - - - ")
            print("\nBody :\n", body)
            print("###########################\n")


    def read_user_data(self):
        
        file_name = "oop/notes.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(":;")
            name = splitted_line[0]
            title = splitted_line[1]
            body = splitted_line[2]

            if name == self.logged_user:
                print("###########################")
                print("Name :", name)
                print("Title :", title)
                print("- - - - - - - - - - - - - - ")
                print("\nBody :\n", body)
                print("###########################\n")
    

    def transfer(self, transfer_to):

        file_name = "oop/notes.csv"
        file = open(file_name, "r")
        data = file.read()


        for index, line in enumerate(data.splitlines()):
            splitted_line = line.split(":;")
            
            title = splitted_line[1]
            name = splitted_line[0]
            
            if name == self.logged_user:
                print(index, title)

        note_to_del_index = int(input("Please what note would you like to delete : "))

        new_data = ""

        for index, line in enumerate(data.splitlines()):

            if index != note_to_del_index:

                new_data += line + "\n"
            
            elif index == note_to_del_index:


                splitted_line = line.split(":;")
                
                title = splitted_line[1]
                body = splitted_line[2]
                file.close()
                
                new_data += f"{transfer_to}:;{title}-from {self.logged_user}:;{body}\n"

            file_name = "oop/notes.csv"
            file = open(file_name, "w")
            file.write(new_data)
            file.close()
    
    
    def begin(self):

        is_registered = input("Do you have an account (y/n): ")

        if is_registered == "y":

            self.login()

        elif is_registered == "n":

            self.register()
            print("Please Sign In  to continue..\n")
            self.login()

        choice = input("Please what would you like to do : ")

        if choice == "r":

            self.read_user_data()

        elif choice == "w":

            self.write_note()
        
        elif choice == "t":

            transfer_to = input("Please enter beneficiary name: ")
            self.transfer(transfer_to)

Notepad().begin()