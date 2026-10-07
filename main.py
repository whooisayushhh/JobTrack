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
        print("3. Update Status")
        print("4. Delete Job")
        print("5. Exit")

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
            if not jobs:
                print("\nNo jobs available to update.")
                continue

            print("\n===== Select Job =====")

            for number, job in enumerate(jobs, start=1):
                print(f"{number}. {job.company} - {job.position}")

            try:
                job_number = int(input("\nEnter job number: "))

                if 1 <= job_number <= len(jobs):
                    new_status = input("Enter new status: ")

                    jobs[job_number - 1].status = new_status

                    save_jobs(jobs)

                    print("\nStatus updated successfully! ✅")

                else:
                    print("\nInvalid job number.")

            except ValueError:
                print("\nPlease enter a valid number.")

        elif choice == "4":
            if not jobs:
                print("\nNo jobs available to delete.")
                continue

            print("\n===== Delete Job =====")

            for number, job in enumerate(jobs, start=1):
                print(f"{number}. {job.company} - {job.position}")

            try:
                job_number = int(input("\nEnter job number to delete: "))

                if 1 <= job_number <= len(jobs):
                    deleted_job = jobs.pop(job_number - 1)

                    save_jobs(jobs)

                    print(
                        f"\n{deleted_job.company} - "
                        f"{deleted_job.position} deleted successfully! 🗑️"
                    )

                else:
                    print("\nInvalid job number.")

            except ValueError:
                print("\nPlease enter a valid number.")

        elif choice == "5":
            print("\nThank you for using JobTrack! 👋")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()