from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Not to disclose')
)

class UserManager(BaseUserManager):
    # 함수명에 _를 사용항으로서 이 class안에서만 사용하겠다는 것을 명시적으로 표시한거
    def _create_user(self, email, username, password, gender=2, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, 'blogs/like_section.html',  password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=256, unique=True)
    username = models.CharField(max_length=32)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES)

    objects = UserManager()
    # 고유 식별자로 사용되는 사용자 모델의 필드 이름을 설명하는 문자열입니다.
    USERNAME_FIELD = 'email'
    # createsuperuser관리 명령을 통해 사용자를 생성할 때 묻는 필드 이름 목록입니다 .
    REQUIRED_FIELDS = []

    def __str__(self):
        # return "<%d %s>" % (self.pk,self.email)
        return "%s" % (self.email)
