# Generated by Django 2.2.5 on 2019-12-04 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20191031_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userarti',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Position'),
        ),
        migrations.AlterField(
            model_name='userarticle',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positionss', to='polls.Position'),
        ),
    ]
