class Job:
    def __init__(self, company, position, status="Applied"):
        self.company = company
        self.position = position
        self.status = status

    def display(self):
        print(f"Company: {self.company}")
        print(f"Position: {self.position}")
        print(f"Status: {self.status}")

    def to_dict(self):
        return {
            "company": self.company,
            "position": self.position,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Job(
            data["company"],
            data["position"],
            data["status"]
        )