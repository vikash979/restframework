# Generated by Django 2.2.5 on 2019-12-11 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_auto_20191211_0503'),
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
