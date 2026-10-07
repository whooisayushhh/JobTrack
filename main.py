from app.models import Job


def main():
    print("===== JobTrack =====")

    company = input("Enter company name: ")
    position = input("Enter job position: ")
    status = input("Enter application status: ")

    job = Job(company, position, status)

    print("\n===== Job Details =====")
    job.display()


if __name__ == "__main__":
    main()