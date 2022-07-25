# Generated by Django 4.0.6 on 2022-07-25 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_feedback_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(verbose_name='Feedback Date'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='score',
            field=models.CharField(choices=[('G', 'Great'), ('O', 'Okay'), ('T', 'Terrible')], default='G', max_length=1, verbose_name='Score Here'),
        ),
    ]
