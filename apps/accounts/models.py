from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.


class Role(models.TextChoices):
    ADMIN = 'admin'
    STAFF = 'staff'
    NORMAL = 'normal'


class UserManager(BaseUserManager):
    """
    [kwargs]
    username: str
    email: str
    birth: str
    password: str
    """
    def create_user(self, **kwargs):
        user = self._default_set(**kwargs)
        return user

    def create_superuser(self, **kwargs):
        user = self._default_set(**kwargs)
        return user

    def _default_set(self, **kwargs):
        user = self.model(**kwargs)
        password = kwargs.get('password', None)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    birth = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=6, choices=Role.choices, default=Role.NORMAL)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = ['email']
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return False

    def has_module_perms(self, app_label):
        return False

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        abstract = True


class AdminUser(User):
    role = models.CharField(max_length=6, choices=Role.choices, default=Role.ADMIN)
    is_admin = models.BooleanField(default=True)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class NormalUser(User):
    is_superuser = models.BooleanField(default=False)
