from app.models import Job


def main():
    jobs = []

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