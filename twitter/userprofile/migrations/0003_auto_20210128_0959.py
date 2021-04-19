# Generated by Django 3.1.5 on 2021-01-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20210128_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='/static/image/default-profile-avatar.png', null=True, upload_to='user-profile-photos/', verbose_name='profile image'),
        ),
    ]
