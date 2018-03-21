from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager
)
from schoolmanagement.models import School
class UserManager(BaseUserManager):
    def create_user(self, email,full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("User must have an email ID")
        if not password:
            raise ValueError("User must have a password")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        if full_name:
            user_obj.full_name = full_name
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            full_name=full_name,
        )
        return user

    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=200) 
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    schoolid = models.ForeignKey(School, blank=True,null=True, on_delete=models.CASCADE)
    registered = models.TimeField(auto_now_add=True, auto_now=False)
    updated = models.TimeField(auto_now=True, auto_now_add=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name.split(' ')[0:1]
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
