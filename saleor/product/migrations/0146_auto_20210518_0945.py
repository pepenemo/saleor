# Generated by Django 3.2.2 on 2021-05-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0145_auto_20210511_1043"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categorytranslation",
            name="name",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="collectiontranslation",
            name="name",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="producttranslation",
            name="name",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
