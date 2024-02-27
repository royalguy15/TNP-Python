from pymongo import MongoClient

client = MongoClient()

db_name = client["Sample_db"]
collection_name = db_name["students"]

class location:
    def __init__(self, state="Odisha", pin=765022, country="India"):
        self.state = state
        self.pin = pin
        self.country = country

class student(location):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        # self.location = vars(location())

    def update_location(self, state, pin, country):
        super().__init__(state, pin, country)

data = student("Dharani", "mechanical")
data.update_location("Odhisa",00000,"India")
# print(vars(data))
collection_name.insert_one(vars(data))