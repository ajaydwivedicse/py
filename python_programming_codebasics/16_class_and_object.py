class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == 'actor':
            print(self.name, 'shoots a film')
        elif self.occupation == 'cricketer':
            print(self.name, 'plays cricket')

tom = Human('tom cruise', 'actor')
virat = Human('virat kohli', 'cricketer')
tom.do_work()
virat.do_work()
