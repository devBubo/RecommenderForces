# Generated by Django 5.0 on 2024-02-09 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_ratedproblems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='ratedProblems',
            new_name='rated_problems',
        ),
    ]
