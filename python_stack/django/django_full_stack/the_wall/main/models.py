from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name MUST be at least 3 characters long!"
        if len(post_data['last_name']) < 4:
            errors['last_name'] = "Last name MUST be at least 5 characters long!"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "That doesn't look like an email!"
        if len(post_data['password']) < 2:
            errors['password'] = "Pasword MUST be at least 3 characters long!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=255)
    commented_on = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




