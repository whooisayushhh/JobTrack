from app.models import Job

job1 = Job(
    "Google",
    "Python Developer Intern",
    "Applied",
    "Bangalore"
)

print(job1.company)
print(job1.role)
print(job1.status)
print(job1.location)