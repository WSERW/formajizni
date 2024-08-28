# Generated by Django 4.2.5 on 2024-08-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_phone_contactinfo_phone1_contactinfo_phone2'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='Введите вопрос', max_length=255)),
                ('answer', models.TextField(help_text='Введите ответ')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
                'ordering': ['question'],
            },
        ),
    ]
