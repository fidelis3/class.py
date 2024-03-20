class person:
    def __init__(self,name,age,gender):
        self.name=name 
        self.age=age 
        self.gender=gender
    def introduce(self):
        print(f"hello my name is {self.name}.I'm {self.age} years old and i'm {self.gender}.")
        #create an instance of the person class
        person2=person("John",30,"male")
        #call the introduce method to display the person's information
        person2.introduce()