from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)    
    uploader = models.ForeignKey(User,related_name = "uploaded_books")
    liked_users = models.ManyToManyField(User, related_name = "liked_books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)



# For your assignment:

# Create the appropriate models and the appropriate relationship.  Design your models so that the following command would be supported
# Book.objects.first().uploader - this should return the user who uploaded the book
# User.objects.first().uploaded_books - this should return all the books that are uploaded by the first user
# Book.objects.first().liked_users - this should return all the users who liked the first book
# User.objects.first().liked_books - this should return all the books that were liked by the first user
# Create 3 different user accounts
# Have the first user create 2 books.
# Have the second user create 2 other books.
# Have the third user create 2 other books.
# Have the first user like the last book and the first book
# Have the second user like the first book and the third book
# Have the third user like all books
# Display all users who like the first book
# Display the user who uploaded the first book
# Display all users who like the second book
# Display the user who uploaded the second book