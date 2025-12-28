from django.db import models

# Create your models here.

class Hero(models.Model):
    hero_title = models.CharField(max_length=100)
    hero_position = models.CharField(max_length=100)
    hero_bgimage = models.ImageField(upload_to='static/')

class About(models.Model):
    about_details = models.TextField()
    about_title = models.CharField(max_length=100)
    about_sub_details = models.TextField()
    about_birthday = models.DateField()
    about_mobile = models.CharField(max_length=15)
    about_city = models.CharField(max_length=100)
    about_age = models.IntegerField()
    about_qualification = models.CharField(max_length=100)
    about_email = models.EmailField()
    about_image = models.ImageField(upload_to='static/',default='')

class  Skills(models.Model):
    skill_image = models.ImageField(upload_to='static/')

class Resume(models.Model):
    resume_summary = models.TextField()
    education_title = models.CharField(max_length=100) 
    education_year = models.CharField(max_length=100) 
    education_university = models.CharField(max_length=100) 
    project_name = models.CharField(max_length=100) 
    project_details = models.TextField()
    project_name2 = models.CharField(max_length=100,default='') 
    project_details2 = models.TextField(default='')  

class Portfolio(models.Model):
    app_image = models.ImageField(upload_to='static/')
    app_title = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='static/')
    product_title = models.CharField(max_length=100)
    gallery_image = models.ImageField(upload_to='static/')
    gallery_title = models.CharField(max_length=100)

class Testimonials(models.Model):
    client_review = models.TextField()
    client_image = models.ImageField(upload_to='static/')
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)

class Contact(models.Model):
    contact_address = models.TextField()
    contact_mobile = models.CharField(max_length=15)
    contact_email = models.EmailField()

class Message(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_subject = models.TextField()
    user_message = models.TextField()


