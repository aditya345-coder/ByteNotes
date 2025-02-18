# Generated by Django 5.0.6 on 2024-06-19 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0002_alter_note_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.CharField(choices=[('BUSINESS', 'Business'), ('PERSONAL', 'Personal'), ('IMPORTANT', 'Important')], default='PERSONAL', max_length=15),
        ),
    ]
