class Father:
    def skills(self):
        print("gardening, programming")


class Mother:
    def skills(self):
        print("cooking")


class Child(Father, Mother):
    def skills(self):
        print("sports")
        Father.skills(self)
        Mother.skills(self)


c = Child()
c.skills()