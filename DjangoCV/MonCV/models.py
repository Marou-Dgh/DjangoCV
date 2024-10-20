from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    About_Me = models.TextField()
    Linkedin_url = models.URLField()
    Github_url = models.URLField()

    def __str__(self):
        return self.name

class Education(models.Model):
    School_name = models.CharField(max_length=100)
    Degree = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)

    def __str__(self):
        return self.School_name

class Work_Experience(models.Model):
    Name = models.CharField(max_length=100)
    Date = models.DateField()
    Tasks = models.TextField()
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class University_Projects(models.Model):
    Project_name = models.CharField(max_length=100)
    Date = models.DateField()
    Project_Description = models.TextField()
    Technology = models.CharField(max_length=100)

    def __str__(self):
        return self.Project_name

class Perronal_Projects(models.Model):
    Project_name = models.CharField(max_length=100)
    Date = models.DateField()
    Project_Description = models.TextField()
    Technology = models.CharField(max_length=100)

    def __str__(self):
        return self.Project_name

class Skills(models.Model):
    Skill = models.CharField(max_length=100)

    def __str__(self):
        return self.Skill

class Languages(models.Model):
    Language = models.CharField(max_length=100)
    Language_Level = models.CharField(max_length=100)

    def __str__(self):
        return self.Language
