from app.models import Job


def main():
    job1 = Job("Google", "Python Developer")
    job2 = Job("Microsoft", "Software Engineer", "Interview")

    print("===== JobTrack =====\n")

    job1.display()
    print()
    job2.display()


if __name__ == "__main__":
    main()