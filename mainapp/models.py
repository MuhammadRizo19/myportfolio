from django.db import models
import uuid
from ckeditor.fields import RichTextField    

class Skill(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    skill_name = models.CharField(max_length=20, unique=True)
    percent = models.CharField(max_length=3)

    def __str__(self):
        return self.skill_name
    
class Experience(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    job_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    job_desc = models.TextField()

    def __str__(self):
        return self.company_name    


class AboutMe(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=50)
    text = models.TextField()
    
    def __str__(self):
        return self.title

class Graduation(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    degree_name = models.CharField(max_length=30)
    university_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    desc = models.TextField()

    def __str__(self):
        return self.degree_name

class Service(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=30)
    desc = models.TextField()
    icon = models.CharField(max_length=30)

    def __str__(self):
        return self.title
 
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    email = models.EmailField()
    title = models.CharField(max_length=50)
    message = models.TextField()
    sent_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-sent_time']

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    post_title = models.CharField(max_length=70)
    post_body = RichTextField(null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title