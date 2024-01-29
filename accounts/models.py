from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.contrib.auth.base_user import BaseUserManager
import uuid
from django.contrib.auth.models import AbstractUser

class AccontManager(BaseUserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email field cannot be empty!")
        if not password:
            raise ValueError("password fiel cannot be empty!")

        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    

class AccountHolder(AbstractUser):
    class Gender:
        MALE = "Male"
        FEMALE = "Female"
        OTHER = "Other"

        choice = (
            (MALE, "Male"),
            (FEMALE, "Female"),
            (OTHER, "Other")
        )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.CharField(
        max_length=50,
        help_text="Enter username",
        null=False,
        unique=True,
        validators=[MinLengthValidator(3, "Username must not be less than three")]
    )

    email = models.EmailField(
        help_text="User's Email",
        null=False,
        unique=True
    )

    password = models.CharField(
        help_text="User's password",
        null=False,
        max_length=50,
        validators=[MinLengthValidator(6, "Password should not be less than six characters")]
    )

    gender = models.CharField(max_length=25, choices=Gender.choice, default=Gender.OTHER)
    is_active = models.BooleanField(default=False, null=False)

    objects = AccontManager()
    # USERNAME_FIELD = 'email'
    # EMAIL_FIELD = 'email'

