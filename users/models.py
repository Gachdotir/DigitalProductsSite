from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user manager to handle users with email as the unique identifier.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model where email is the unique identifier
    for authentication instead of usernames.
    """
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


class Device(models.Model):
    WEB = 1
    ANDROID = 2
    IOS = 3
    DEVICE_TYPE_CHOICES = (
        (WEB, 'WEB'),
        (ANDROID, 'ANDROID'),
        (IOS, 'IOS'),
    )

    user = models.ForeignKey(User, related_name='devices', on_delete=models.CASCADE)
    device_uuid = models.UUIDField(_('device UUID'), null=True)
    last_login = models.DateTimeField(_('last login'), null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES, default=WEB)
    device_os = models.CharField(_('device os'), max_length=20, null=True)
    device_model = models.CharField(_('device model'), max_length=20, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Mete:
        db_table = 'user_devices'
        verbose_name = _('device')
        verbose_name_plural = _('devices')
        unique_together = ('user', 'device_uuid')


class Province(models.Model):
    name = models.CharField(max_length=30)
    is_valid = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'provinces'
        verbose_name = _('province')
        verbose_name_plural = _('provinces')
