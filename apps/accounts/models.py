from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from django.db.models import Q
from django.urls import reverse


class Role(models.TextChoices):
    # ADMIN = 'admin'
    STAFF = 'Staff'
    NORMAL = 'Normal'


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
        user.is_admin = True
        user.is_superuser = True
        return user

    def _default_set(self, **kwargs):
        user = self.model(**kwargs)
        password = kwargs.get('password', None)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True, editable=True)
    email = models.EmailField(unique=True)
    birth = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=8, choices=Role.choices, default=Role.NORMAL)
    deleted = models.BooleanField(default=False)

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


# Admin User
class AdminQuerySet(models.QuerySet):
    def active_user(self):
        return NormalUser.objects.filter(self._q_set())

    def active_staff(self):
        return StaffUser.objects.filter(self._q_set(user_role=Role.STAFF))

    def _q_set(self, user_role: str = Role.NORMAL):
        return (
                Q(role=user_role) &
                Q(is_active=True) &
                Q(deleted=False)
        )


class AdminManager(models.Manager):
    def get_queryset(self):
        return AdminQuerySet(self.model, using=self._db)

    def active_user(self):
        return self.get_queryset().active_user()

    def active_staff(self):
        return self.get_queryset().active_staff()


class AdminUser(User):
    role = models.CharField(max_length=6, choices=Role.choices, default='admin')
    is_superuser = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    admin_manager = AdminManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


# Staff User
class StaffQuerySet(models.QuerySet):
    def active_staff(self):
        return StaffUser.objects.filter(is_active=True)


class StaffManager(models.Manager):
    def get_queryset(self):
        return StaffQuerySet(self.model, using=self._db)

    def active_staff(self):
        return self.get_queryset().active_staff()

    # def all(self):
    #     return self.get_queryset().active_staff()


class StaffUser(User):
    role = models.CharField(max_length=6, choices=Role.choices, default=Role.STAFF)
    is_admin = models.BooleanField(default=True)

    staff_manager = StaffManager()


# Normal User
class NormalQuerySet(models.QuerySet):
    def active_user(self):
        return NormalUser.objects.filter(is_active=True)


class NormalManager(models.Manager):
    def get_queryset(self):
        return NormalQuerySet(self.model, using=self._db)

    def active_user(self):
        return self.get_queryset().active_user()


class NormalUser(User):
    is_superuser = models.BooleanField(default=False)

    normal_manager = NormalManager()

    def get_absolute_url(self):
        return reverse("accounts:detail_normal", kwargs={"pk": self.id})

    def get_api_url(self):
        return reverse("accounts_api:detail_normal", kwargs={"pk": self.id})
