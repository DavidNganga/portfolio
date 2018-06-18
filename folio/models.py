from django.db import models

# Create your models here.
class Project(models.Model):
     name = models.CharField(max_length=20)
     link_url = models.TextField(blank = True)
     description = models.CharField(max_length=200)
     project_screenshot = models.ImageField(upload_to ='images/',null = True )

     @classmethod
     def get_all(cls):
        projects = cls.objects.all()
        return projects

     def __str__(self):
        return self.name

     def save_project(self):
        self.save()

     def delete_project(self):
        self.delete()

     def get_Project_by_id(cls,id):
        names = cls.objects.get(id=id)
        return names
