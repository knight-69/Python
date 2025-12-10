class Programmer:
    company = "Microsoft"

    def __init__(self, name ,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Lakshit",130000,24201)
print(p.name,p.pin,p.salary,p.company)
r = Programmer("Arjun",110000,21201)
print(r.name,r.pin,r.salary,r.company)

        