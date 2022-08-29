# Generated by Django 3.2.14 on 2022-08-02 11:54

from django.db import migrations, models
import openedx.core.djangoapps.discussions.models


class Migration(migrations.Migration):
    dependencies = [
        ('discussions', '0012_auto_20220511_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussionsconfiguration',
            name='provider_type',
            field=models.CharField(
                default=openedx.core.djangoapps.discussions.models.get_default_provider_type,
                help_text="The discussion tool/provider's id",
                max_length=100,
                verbose_name='Discussion provider',
            ),
        ),
        migrations.AlterField(
            model_name='historicaldiscussionsconfiguration',
            name='provider_type',
            field=models.CharField(
                default=openedx.core.djangoapps.discussions.models.get_default_provider_type,
                help_text="The discussion tool/provider's id",
                max_length=100,
                verbose_name='Discussion provider',
            ),
        ),
    ]