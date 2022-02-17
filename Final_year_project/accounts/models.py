from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_doctor(self, first_name, last_name, username, email, password, license):
        if len(license)!= 8:
            raise ValueError('Doctor must have a license valid number')

        user = self.create_doctor(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            license = license,
            password = password,
        )

        user.is_doctor= True
        user.is_active=True
        user.save(using=self._db)
        return user


    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        user.is_superuser= True
        user.is_active=True
        user.is_staff=True
        user.is_admin=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    # required 
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

# class Doctor(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     username = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     license_number = models.CharField(max_length=100, unique=True)

#     # required 
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email
    

#     def has_perm(self, perm, obj=None):
#         return self.is_admin
    
#     def has_module_perms(self, app_label):
#         return True
