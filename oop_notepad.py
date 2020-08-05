class Notepad():

    def write_file(self, data):

        file_name = "functions/notes.csv"
        file = open(file_name, "a")
        file.write(data)

        return True

    def read_file(self):

        file_name = "functions/notes.csv"
        file = open(file_name, "r")
        data = file.read()

        return data

    def collect_data(self):

        name = input("Please enter your name : ")
        title = input("Please enter your note title : ")
        body = input("Please enter your Body : ")
        
        save_structure = f"{name};|{title};|{body}\n"

        return save_structure

    def process_and_display_data(self, data):

        for line in data.split("\n"):
            splitted_line = line.split(";|")
            name = splitted_line[0]
            title = splitted_line[1]
            body = splitted_line[2]

            print("##########################")
            print("Name :",  name)
            print()
            print("Title :", title)
            print()
            print("Body :", body)
            print("##########################")
            print()

    def start(self):

        choice = input("Welcome. \n\nEnter (w) to write and \n(r) to read : ")

        if choice == "w":

            data = self.collect_data()
            self.write_file(data)

        elif choice == "r":

            saved_notes = self.read_file()
            self.process_and_display_data(saved_notes)
            # print(saved_notes)


saturday_notepad = Notepad()
saturday_notepad.start()
