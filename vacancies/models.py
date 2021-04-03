from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()

    def __str__(self):
        return self.code


class Specialty(models.Model):
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return self.code


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=999)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.code


class Settings(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    setval = models.CharField(max_length=100)

    def __str__(self):
        return self.code
