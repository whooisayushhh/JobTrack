import json
import os

from app.models import Job


DATA_FILE = "jobs.json"


def load_jobs():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        data = json.load(file)

    return [Job.from_dict(job) for job in data]


def save_jobs(jobs):
    data = [job.to_dict() for job in jobs]

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def main():
    jobs = load_jobs()

    print("===== JobTrack =====")

    while True:
        print("\n1. Add Job")
        print("2. View Jobs")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            company = input("Enter company name: ")
            position = input("Enter job position: ")
            status = input("Enter application status: ")

            job = Job(company, position, status)
            jobs.append(job)

            save_jobs(jobs)

            print("\nJob added successfully! ✅")

        elif choice == "2":
            if not jobs:
                print("\nNo jobs added yet.")
            else:
                print("\n===== Your Applications =====")

                for number, job in enumerate(jobs, start=1):
                    print(f"\nJob {number}")
                    job.display()

        elif choice == "3":
            print("\nThank you for using JobTrack! 👋")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()