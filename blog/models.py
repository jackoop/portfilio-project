from django.db import models

# Create A Blog models
class Blog(models.Model):
    # title
    title = models.CharField(max_length=255)
    # pub_date
    pub_date = models.DateTimeField()
    # body
    body = models.TextField()
    # image
    image = models.ImageField(upload_to='images/')




# Add the Blog app to the settings

# Creat a migration

# migrate

# add to admin
