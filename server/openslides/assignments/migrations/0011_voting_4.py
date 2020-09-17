# Generated by Django 2.2.9 on 2020-03-30 08:52

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assignments", "0010_voting_3"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignmentpoll",
            name="db_amount_global_abstain",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                default=Decimal("0"),
                max_digits=15,
                null=True,
                validators=[django.core.validators.MinValueValidator(Decimal("-2"))],
            ),
        ),
        migrations.AlterField(
            model_name="assignmentpoll",
            name="db_amount_global_no",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                default=Decimal("0"),
                max_digits=15,
                null=True,
                validators=[django.core.validators.MinValueValidator(Decimal("-2"))],
            ),
        ),
    ]