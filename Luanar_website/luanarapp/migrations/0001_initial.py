# Generated by Django 5.0.1 on 2024-02-26 21:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrationOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_code', models.CharField(max_length=50)),
                ('office_name', models.CharField(max_length=100)),
                ('office_remarks', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('announcement_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('advert', models.FileField(blank=True, null=True, upload_to='announcements_files/')),
                ('application_form', models.FileField(blank=True, null=True, upload_to='announcements_files/')),
                ('file', models.FileField(blank=True, null=True, upload_to='announcements_files/')),
                ('category', models.CharField(choices=[('PUBLIC', 'Public'), ('STAFF', 'Staff'), ('STUDENTS', 'Students')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('college_id', models.AutoField(primary_key=True, serialize=False)),
                ('college_code', models.CharField(max_length=10, unique=True)),
                ('college_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.CharField(max_length=200)),
                ('event_description', models.TextField(blank=True, null=True)),
                ('event_photo', models.ImageField(blank=True, null=True, upload_to='events_photos/')),
                ('host', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Luanar4moreImpact',
            fields=[
                ('luanar4more_id', models.AutoField(primary_key=True, serialize=False)),
                ('luanar4more_title', models.CharField(max_length=200)),
                ('luanar4more_photo', models.ImageField(blank=True, null=True, upload_to='Luanar4moreImpact')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prospectus',
            fields=[
                ('prospectus_id', models.AutoField(primary_key=True, serialize=False)),
                ('prospectus_file', models.FileField(blank=True, null=True, upload_to='prospectus/')),
                ('prospectus_info', models.TextField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Prospectus',
            },
        ),
        migrations.CreateModel(
            name='QuickAnnouncement',
            fields=[
                ('quickannouncement', models.AutoField(primary_key=True, serialize=False)),
                ('announcement_title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Quick_announcement/')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchAndOutreach',
            fields=[
                ('research_id', models.AutoField(primary_key=True, serialize=False)),
                ('research_title', models.CharField(max_length=200)),
                ('research_photo', models.ImageField(blank=True, null=True, upload_to='ResearchAndOutreach')),
                ('research_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'ResearchAndOutreach',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('vacancy_id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.CharField(max_length=200)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('vacancy_file', models.FileField(blank=True, null=True, upload_to='vacancies/')),
            ],
            options={
                'verbose_name_plural': 'Vacancies',
            },
        ),
        migrations.CreateModel(
            name='AdministrationStaff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=100)),
                ('staff_position', models.CharField(choices=[('VICE CHANCELLOR', 'Vice chancellor'), ('DEPUTY VICE CHANCELLOR', 'Deputy Vice Chancellor'), ('UNIVERSITY REGISTRAR', 'University Registrar'), ('DEAN OF STUDENTS AFFAIRS', 'Dean of Students Affairs')], max_length=100)),
                ('staff_contacts', models.CharField(max_length=20)),
                ('staff_email', models.EmailField(max_length=254, unique=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('about_staff', models.TextField(blank=True, null=True)),
                ('office_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='luanarapp.administrationoffice')),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('campus_id', models.AutoField(primary_key=True, serialize=False)),
                ('campus_name', models.CharField(max_length=100)),
                ('campus_code', models.CharField(max_length=10, unique=True)),
                ('about_campus', models.TextField(blank=True, null=True)),
                ('campus_image', models.ImageField(blank=True, null=True, upload_to='campus_images')),
                ('college_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='luanarapp.college')),
            ],
            options={
                'verbose_name_plural': 'Campuses',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty_code', models.CharField(max_length=200, unique=True)),
                ('faculty_name', models.CharField(max_length=400)),
                ('faculty_mission', models.TextField(blank=True, null=True)),
                ('faculty_vision', models.TextField(blank=True, null=True)),
                ('faculty_description', models.TextField(blank=True, null=True)),
                ('faculty_image', models.ImageField(blank=True, null=True, upload_to='faculty')),
                ('campus_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='luanarapp.campus')),
            ],
            options={
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_code', models.CharField(max_length=50, unique=True)),
                ('department_name', models.CharField(max_length=500)),
                ('about_department', models.TextField(blank=True, null=True)),
                ('department_image', models.ImageField(blank=True, null=True, upload_to='department_images')),
                ('faculty_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='luanarapp.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicStaff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=100)),
                ('staff_position', models.CharField(choices=[('HEAD OF FACULTY', 'Head of FACULTY'), ('DEPUTY HEAD OF FACULTY', 'Deputy Head of FACULTY'), ('HEAD OF DEPARTMENT', 'Head of Department'), ('Lecturer', 'Lecturer'), ('Associate lecturer', 'Associate lecturer'), ('Part-Time Lecturer', 'Part Time Lecturer')], max_length=50)),
                ('staff_contacts', models.CharField(max_length=20)),
                ('staff_email', models.EmailField(max_length=254, unique=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('department_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='luanarapp.department')),
                ('faculty_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='luanarapp.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('images', models.ManyToManyField(related_name='gallery_images', to='luanarapp.galleryimage')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('news_title', models.CharField(max_length=200)),
                ('news_subtitle', models.CharField(blank=True, max_length=400, null=True)),
                ('news_body', models.TextField()),
                ('news_photo', models.ImageField(blank=True, null=True, upload_to='news_photos/')),
                ('photo_description', models.CharField(max_length=400)),
                ('tag', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('program_id', models.AutoField(primary_key=True, serialize=False)),
                ('program_code', models.CharField(max_length=10, unique=True)),
                ('program_name', models.CharField(max_length=500)),
                ('requirement', models.TextField(blank=True, null=True)),
                ('level', models.CharField(blank=True, max_length=50, null=True)),
                ('duration', models.IntegerField()),
                ('program_description', models.TextField(blank=True, null=True)),
                ('program_image', models.ImageField(blank=True, null=True, upload_to='programs/')),
                ('department_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='luanarapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Prospects',
            fields=[
                ('prospect_id', models.AutoField(primary_key=True, serialize=False)),
                ('prospect_name', models.CharField(blank=True, max_length=200, null=True)),
                ('program_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luanarapp.program')),
            ],
            options={
                'verbose_name_plural': 'Prospects',
            },
        ),
    ]
