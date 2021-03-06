# Generated by Django 3.0.3 on 2020-03-28 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_departmet'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitsumoriservice',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contact.Departmet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contact.Departmet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicegroup',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contact.Departmet'),
            preserve_default=False,
        ),
    ]
