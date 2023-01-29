class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self): 
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("Welcome, new member!")
        else:
            print("User already a member")
    def spend_points(self,amount):
        if amount > self.gold_card_points:
            print("Not enough points")
        else:
            self.gold_card_points - amount


user_richard = User('Richard', 'Padilla', 'r.p@gmail', 25)

user_richard.display_info()

user_richard.enroll()

user_anthony = User("Anthony", "Padilla", 'a.p@gmail.com', 21)

user_sarah = User("Sarah", "Johnson", 's.j@gmail.com', 23)

user_richard.spend_points(50)

user_anthony.enroll()

user_anthony.spend_points(80)

user_richard.display_info()

user_anthony.display_info()

user_sarah.display_info()

user_richard.enroll()

user_sarah.spend_points(40)

