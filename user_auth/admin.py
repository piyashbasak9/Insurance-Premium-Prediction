
from django.contrib import admin
from .models import EmailVerification


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
	list_display = ('user', 'verification_code', 'is_verified', 'created_at')
