from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=17)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)


User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
