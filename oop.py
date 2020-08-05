# class Animal:

#     def talk(self):
#         print ("I have something to say!")
#     def walk(self):
#         print ("Hey! I am walking here!")
#     def clothes(self):
#         print ("I have nice clothes!")


# ##INITIALIZING 
# animal = Animal()
# dog = Animal()
# fish = Animal()
# animal.talk()
# animal.clothes()
# dog.clothes()
# dog.walk()

class Calculator:
    
    def sum(self, *args):
        print(sum(args))

    def subtract(self, a, b):
        print(a - b)


# basic_cal = Calculator()
# basic_cal.sum(23,43, 3,2,4,3,1,34,45,65,12)
# basic_cal.subtract(2300, 4500)

class Scientific_cal(Calculator):
    name = "default"

    def sqrt(self, number, power):
        print(number**power)

    def subtract(self,  *args):
        print(f"Hello this is {self.name} running")
        result = args[0]

        for i in range(len(args)):
            result = result - args[i-1]

        print(result)

sci_max = Scientific_cal()
sci_max2 = Scientific_cal()
sci_max2.name = "robo-power"

# sci_max.sum(212,34,12,43,132,34)
# sci_max.sqrt(3,3)
sci_max.subtract(2,4,1,4,45,2)
sci_max2.subtract(2,4,1,4,45,2)