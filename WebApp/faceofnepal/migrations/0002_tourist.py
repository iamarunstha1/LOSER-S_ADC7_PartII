# Generated by Django 3.0.1 on 2020-01-20 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faceofnepal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add', to='faceofnepal.Freelancer')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='faceofnepal.Freelancer')),
            ],
        ),
    ]
