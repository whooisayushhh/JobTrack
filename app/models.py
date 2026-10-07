class Job:
    def __init__(
        self,
        company,
        position,
        location,
        application_date,
        salary,
        job_type,
        work_mode,
        status="Applied"
    ):
        self.company = company
        self.position = position
        self.location = location
        self.application_date = application_date
        self.salary = salary
        self.job_type = job_type
        self.work_mode = work_mode
        self.status = status

    def display(self):
        print(f"Company: {self.company}")
        print(f"Position: {self.position}")
        print(f"Location: {self.location}")
        print(f"Application Date: {self.application_date}")
        print(f"Salary: {self.salary}")
        print(f"Job Type: {self.job_type}")
        print(f"Work Mode: {self.work_mode}")
        print(f"Status: {self.status}")

    def to_dict(self):
        return {
            "company": self.company,
            "position": self.position,
            "location": self.location,
            "application_date": self.application_date,
            "salary": self.salary,
            "job_type": self.job_type,
            "work_mode": self.work_mode,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Job(
            data["company"],
            data["position"],
            data["location"],
            data["application_date"],
            data["salary"],
            data["job_type"],
            data["work_mode"],
            data["status"]
        )