class Job:
    def __init__(
        self,
        company,
        position,
        location,
        application_date,
        status="Applied"
    ):
        self.company = company
        self.position = position
        self.location = location
        self.application_date = application_date
        self.status = status

    def display(self):
        print(f"Company: {self.company}")
        print(f"Position: {self.position}")
        print(f"Location: {self.location}")
        print(f"Application Date: {self.application_date}")
        print(f"Status: {self.status}")

    def to_dict(self):
        return {
            "company": self.company,
            "position": self.position,
            "location": self.location,
            "application_date": self.application_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Job(
            data["company"],
            data["position"],
            data["location"],
            data["application_date"],
            data["status"]
        )