class Job:
    def __init__(self, company, position, status="Applied"):
        self.company = company
        self.position = position
        self.status = status

    def display(self):
        print(f"Company: {self.company}")
        print(f"Position: {self.position}")
        print(f"Status: {self.status}")