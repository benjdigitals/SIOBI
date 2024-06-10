from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=False, blank=True, default='')
    bio = models.TextField(null=False, blank=True)
    likes = models.TextField(max_length=500, null=False, default='')
    dislikes = models.TextField(max_length=500, null=False, default='')
    reason = models.TextField(null=False, blank=True)
    school = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name