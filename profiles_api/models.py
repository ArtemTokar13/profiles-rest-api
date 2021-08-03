from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for User profiles"""

    def create_user(self, email, name, password=None):
        """Create a new User profile"""
        if not email:
            raise ValueError('User must hawe an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password):
        """Create superuser"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


"""Creating User model for represent email enstead username"""
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Model for Users"""
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS  = ['name']

    def get_full_name(self):
        """Retrive full name for User"""
        return self.name

    def get_short_name(self):
        """Retrive short name of User"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email
