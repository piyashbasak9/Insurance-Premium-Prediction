

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import random
import string

# Email verification (existing)
class EmailVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    @classmethod
    def generate_code(cls):
        return ''.join(random.choices(string.digits, k=6))

    def is_expired(self):
        from django.utils import timezone
        from datetime import timedelta
        return timezone.now() > self.created_at + timedelta(hours=24)

# Note: Category, Problem, Submission and Profile for problemset
# have been moved to the `problemlist` app. This file keeps
# only EmailVerification related to user registration.