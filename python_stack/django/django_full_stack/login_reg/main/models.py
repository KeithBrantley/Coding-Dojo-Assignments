from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data('first_name')) < 2:
            errors['first_name'] = 'First name MUST be at least 3 characters long!'
        if len(post_data('last_name')) < 4:
            errors['last_name'] = 'Last name Must be at least 5 characters long!'
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'That doesnt look like an email!'
        if len(post_data['password']) < 7:
            errors['password'] = 'Password must contain at least 8 characters!'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()




    