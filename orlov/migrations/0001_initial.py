# Generated by Django 4.0.4 on 2022-05-02 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datea', models.DateTimeField(auto_now_add=True, verbose_name='datea')),
                ('title', models.CharField(max_length=255, verbose_name='application_title')),
                ('details', models.TextField(verbose_name='application_details')),
            ],
            options={
                'db_table': 'application',
                'ordering': ['datea'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=64, verbose_name='surname')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('patronymic', models.CharField(blank=True, max_length=64, null=True, verbose_name='patronymic')),
                ('sex', models.CharField(choices=[('М', 'М'), ('Ж', 'Ж')], default='М', max_length=1, verbose_name='sex')),
                ('birthday', models.DateTimeField(verbose_name='birthday')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='address')),
                ('phone', models.CharField(blank=True, max_length=128, null=True, verbose_name='phone')),
            ],
            options={
                'db_table': 'employee',
                'ordering': ['surname', 'name', 'patronymic'],
            },
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datem', models.DateTimeField(verbose_name='datem')),
                ('status', models.CharField(max_length=128, verbose_name='movement_status')),
                ('details', models.TextField(blank=True, null=True, verbose_name='movement_details')),
            ],
            options={
                'db_table': 'movement',
                'ordering': ['datem'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daten', models.DateTimeField(verbose_name='daten')),
                ('title', models.CharField(max_length=256, verbose_name='title_news')),
                ('details', models.TextField(verbose_name='details_news')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='photo_news')),
            ],
            options={
                'db_table': 'news',
                'ordering': ['daten'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=64, verbose_name='phone')),
                ('address', models.CharField(max_length=128, verbose_name='address')),
            ],
            options={
                'db_table': 'person',
                'ordering': ['phone'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='position_title')),
            ],
            options={
                'db_table': 'position',
                'ordering': ['title'],
            },
        ),
        migrations.AddIndex(
            model_name='position',
            index=models.Index(fields=['title'], name='position_title_e0ff68_idx'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='news',
            index=models.Index(fields=['daten'], name='news_daten_a29edb_idx'),
        ),
        migrations.AddField(
            model_name='movement',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movement_application', to='orlov.application'),
        ),
        migrations.AddField(
            model_name='movement',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movement_employee', to='orlov.employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_position', to='orlov.position'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['phone'], name='person_phone_e491f7_idx'),
        ),
        migrations.AddIndex(
            model_name='movement',
            index=models.Index(fields=['application'], name='movement_applica_27871b_idx'),
        ),
        migrations.AddIndex(
            model_name='movement',
            index=models.Index(fields=['datem'], name='movement_datem_8708fe_idx'),
        ),
        migrations.AddIndex(
            model_name='movement',
            index=models.Index(fields=['employee'], name='movement_employe_435985_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['surname'], name='employee_surname_b85b55_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['name'], name='employee_name_7aabaa_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['patronymic'], name='employee_patrony_6290e8_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['position'], name='employee_positio_c649b1_idx'),
        ),
        migrations.AddIndex(
            model_name='application',
            index=models.Index(fields=['datea'], name='application_datea_198fe9_idx'),
        ),
        migrations.AddIndex(
            model_name='application',
            index=models.Index(fields=['user'], name='application_user_id_ba75f5_idx'),
        ),
    ]
