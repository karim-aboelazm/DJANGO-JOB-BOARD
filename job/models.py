from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Job(models.Model): # ===> table in database called Jobs
    title = models.CharField(max_length=100) # ===> column in Job table in database 
    #location
    job_type = models.CharField(max_length=15,choices = JOB_TYPE)
    description = models.TextField(max_length=5000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


