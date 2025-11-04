"""Delete legacy problemset models moved to problemlist app.

This migration removes the tables that were accidentally created under
`user_auth` (Category, Problem, Profile, Submission). The canonical models
now live in the `problemlist` app.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_auth", "0002_category_problem_profile_submission"),
    ]

    operations = [
        migrations.DeleteModel(name="Submission"),
        migrations.DeleteModel(name="Profile"),
        migrations.DeleteModel(name="Problem"),
        migrations.DeleteModel(name="Category"),
    ]
