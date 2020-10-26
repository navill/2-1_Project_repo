from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from accounts.models import StaffUser

User = get_user_model()


# Staff = get_staff_model()
# Admin = get_admin_model()

class BaseProfile(models.Model):
    address = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=12, default='')
    call_number = models.CharField(max_length=12, default='')

    class Meta:
        abstract = True


class NormalUserProfile(BaseProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descriptions = models.TextField(default='')


class StaffUserProfile(BaseProfile):
    staff = models.OneToOneField(StaffUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, default='')
