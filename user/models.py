from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from appointments.models import Appointment
# from feedback.models import Feedback
# from django.db.models.manager import Manager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None, phone=None, address=None, years=None, image=None):
            
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            name=name,
            phone=phone,
            address=address,
            years=years,
            image=image
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_dentist(self, email, name, password=None, phone=None, address=None, years=None, image=None):
        user = self.create_user(email, name, password, phone=phone, address=address, years=years, image=image)

        user.is_dentist = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):

    # appointments: Manager[Appointment]
    # feedback: Manager[Feedback]

    email = models.EmailField(max_length=40, unique=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    years = models.IntegerField(default=0)
    image = models.ImageField(upload_to='user/assets/images', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_dentist = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self) -> str:
        if self.is_dentist:
            return f'{self.name}, working as a dentist for {self.years}'
        
        return f'{self.name}, {self.years}, lives in {self.address}'
