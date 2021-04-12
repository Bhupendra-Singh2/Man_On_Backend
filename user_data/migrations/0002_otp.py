# Generated by Django 4.0.4 on 2021-04-12 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(default=0)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]