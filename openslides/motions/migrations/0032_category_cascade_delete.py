# Generated by Django 2.2.3 on 2019-08-05 10:50

from django.db import migrations, models

import openslides.utils.models


class Migration(migrations.Migration):

    dependencies = [("motions", "0031_state_css_classes_2")]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=openslides.utils.models.CASCADE_AND_AUTOUPDATE,
                related_name="children",
                to="motions.Category",
            ),
        )
    ]
