import hashlib

from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User class which extends built-in User. Presently, just adds a "bio"
# and a gravatar method. Feel free to add your own new fields here!


class User(AbstractUser):

    MEMBERSHIP_LEVELS = (
        ('Member', 'Member'),
        ('Plus', 'Plus'),
        ('Premium', 'Premium'),
        ('Professional', 'Professional'),
        ('Instructor', 'Instructor'),
        ('Student', 'Student')
    )

    membership = models.CharField(max_length=12,choices=MEMBERSHIP_LEVELS, default='Member')
    bio = models.TextField()

    def gravatar(self, size=None):
        GRAVATAR_URL = 'https://gravatar.com/avatar/%s?d=identicon%s'
        email = str(self.email).strip().lower()
        digest = hashlib.md5(email.encode('utf-8')).hexdigest()

        if size:
            size_str = '&s=%i' % size
        else:
            size_str = ''

        return GRAVATAR_URL % (digest, size_str)


class UserPrompt(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='allprompts'
    )

    text = models.CharField(max_length=45)

    created = models.DateTimeField(auto_now_add=True)
    revised = models.DateTimeField(auto_now=True)

    public = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=-100)

    class Meta:
        ordering = ['-upvotes']


class Vote(models.Model):
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='voted_on'
    )
    prompt = models.ForeignKey(UserPrompt,
        on_delete=models.CASCADE,
        related_name='vote'
    )
