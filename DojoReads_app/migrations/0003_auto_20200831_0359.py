# Generated by Django 2.2 on 2020-08-31 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DojoReads_app', '0002_auto_20200825_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='DojoReads_app.Author'),
        ),
    ]
