# Generated by Django 2.2.5 on 2019-12-06 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dabout', '0003_aboutpagebody_id_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpagebody',
            name='id_about',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
