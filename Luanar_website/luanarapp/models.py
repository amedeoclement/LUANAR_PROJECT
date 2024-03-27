from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    news_title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, null=True)
    news_subtitle = models.CharField(max_length= 400, null = True, blank = True)
    news_body = models.TextField()
    news_photo = models.ImageField(upload_to='news_photos/', blank=True, null=True)
    photo_description = models.CharField(max_length= 400)
    tag = models.CharField(max_length= 100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.news_title

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_title = models.CharField(max_length=200)
    event_description = models.TextField(null = True, blank = True)
    event_photo = models.ImageField(upload_to='events_photos/', blank=True, null=True)
    host = models.CharField(max_length= 200)
    venue = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null = True)
    end_time = models.TimeField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.event_title
class QuickAnnouncement(models.Model):
    quickannouncement = models.AutoField(primary_key=True)
    announcement_title = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(upload_to='Quick_announcement/', null = True, blank = True)

class Announcement(models.Model):
    announcement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)
    class Category(models.TextChoices):
        PUBLIC = "PUBLIC" , 'Public'
        STAFF = "STAFF", 'Staff'
        STUDENTS = "STUDENTS", 'Students'
    advert = models.FileField(upload_to='announcements_files/', blank=True, null=True)
    application_form = models.FileField(upload_to='announcements_files/', blank=True, null=True)
    file = models.FileField(upload_to='announcements_files/', blank=True, null=True)
    category = models.CharField(max_length= 50, choices = Category.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    college_code = models.CharField(max_length = 10, unique= True)
    college_name = models.CharField(max_length= 100)
    def __str__(self):
        return self.college_code

class Campus(models.Model):
    campus_id = models.AutoField(primary_key=True)
    campus_name = models.CharField(max_length = 100)
    campus_code = models.CharField(max_length= 10, unique = True)
    college_code = models.ForeignKey(College, on_delete = models.DO_NOTHING)
    about_campus = models.TextField(null= True, blank = True)
    campus_image = models.ImageField(upload_to='campus_images', null= True, blank = True)
    class Meta:
        verbose_name_plural = "Campuses"
    
    def __str__(self):
        return self.campus_code
    

class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_code = models.CharField(max_length=200, unique=True)
    faculty_name = models.CharField(max_length=400)
    faculty_mission = models.TextField(null = True, blank = True)
    faculty_vision = models.TextField(null = True, blank = True)
    faculty_description = models.TextField(null = True, blank = True)
    faculty_image = models.ImageField(upload_to='faculty', null = True, blank = True)

    campus_code = models.ForeignKey(Campus, on_delete = models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Faculties"
    def __str__(self):
        return self.faculty_code

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_code = models.CharField(max_length= 50, unique = True)
    department_name = models.CharField(max_length= 500)
    about_department = models.TextField(null=True, blank= True)
    faculty_code = models.ForeignKey(Faculty, on_delete = models.DO_NOTHING)
    department_image = models.ImageField(upload_to='department_images', blank=True, null=True)
    def __str__(self):
        return self.department_code
  

class ProgramNature(models.Model):
    programnature_id = models.AutoField(primary_key=True)
    programnature_name = models.CharField(max_length= 50, unique = True, null= False)
    def __str__(self):
        return self.programnature_name

class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_code = models.CharField(max_length=10, null= False, unique=True )
    program_name = models.CharField(max_length = 500)
    programnature_name = models.ForeignKey(ProgramNature, on_delete = models.DO_NOTHING, null = True, blank = True)
    requirement =  models.TextField(null=True, blank = True)
    duration = models.IntegerField()
    program_description = models.TextField(null=True, blank=True)
    program_image = models.ImageField(upload_to='programs/', blank= True, null=True)
    department_code = models.ForeignKey(Department, on_delete = models.DO_NOTHING)
    campus_code = models.ForeignKey(Campus, on_delete = models.DO_NOTHING, null = True, blank= True)
    prospects = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.program_code

class Luanar4moreImpact(models.Model):
    luanar4more_id  = models.AutoField(primary_key=True)
    luanar4more_title = models.CharField(max_length = 200)
    luanar4more_photo = models.ImageField(upload_to='Luanar4moreImpact', blank=True, null=True)
    description    = models.TextField(null = True, blank=True)
    def __str__(self):
        return self.luanar4more_title

class ResearchAndOutreach(models.Model):
    research_id = models.AutoField(primary_key=True)
    research_title = models.CharField(max_length=200)
    research_photo = models.ImageField(upload_to='ResearchAndOutreach', blank=True, null = True)
    research_description = models.TextField(blank = True, null= True)
    class Meta:
        verbose_name_plural = "ResearchAndOutreach"

    def __str__(self):
        return self.research_title

class AcademicStaff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=100)
    class Position(models.TextChoices):
        HEAD_OF_FACULTY = "HEAD OF FACULTY" , 'Head of FACULTY'
        DEPUTY_HEAD_OF_FACULTY = "DEPUTY HEAD OF FACULTY" , 'Deputy Head of FACULTY'
        HEAD_OF_DEPARTMENT = "HEAD OF DEPARTMENT" , 'Head of Department'
        LECTURER = "Lecturer" , 'Lecturer'
        ASSOCIATE_LECTURER = "Associate lecturer", 'Associate lecturer'
        PART_TIME_LECTURER = "Part-Time Lecturer", 'Part Time Lecturer'

    staff_position = models.CharField(max_length= 50, choices = Position.choices)
    staff_contacts = models.CharField(max_length= 20)
    staff_email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    department_code = models.ForeignKey(Department, on_delete = models.DO_NOTHING)
    faculty_code = models.ForeignKey(Faculty, on_delete = models.DO_NOTHING, to_field='faculty_code')
    def __str__(self):
        return self.staff_name

class AdministrationOffice(models.Model):
    office_code = models.CharField(max_length= 50)
    office_name = models.CharField(max_length= 100)
    office_remarks = models.TextField(null=True, blank = True)
    def __str__(self):
        return self.office_code

class AdministrationStaff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=100)
    class Position(models.TextChoices):
        VICE_CHANCELLOR = "VICE CHANCELLOR" , 'Vice chancellor'
        DEPUTY_VICE_CHANCELLOR = "DEPUTY VICE CHANCELLOR" , 'Deputy Vice Chancellor'
        UNIVERSITY_REGISTRAR = "UNIVERSITY REGISTRAR", 'University Registrar'
        DOSA = "DEAN OF STUDENTS AFFAIRS", 'Dean of Students Affairs'

    staff_position = models.CharField(max_length=100, choices= Position.choices)
    staff_contacts = models.CharField(max_length= 20)
    staff_email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    about_staff = models.TextField(blank=True, null = True)
    office_code = models.ForeignKey(AdministrationOffice, null=True, blank= False, on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.staff_name


class Vacancy(models.Model):
    vacancy_id = models.AutoField(primary_key = True)
    position = models.CharField(max_length = 200)
    job_description = models.TextField(null = True, blank=True)
    requirements = models.TextField(null=True, blank = True)
    vacancy_file = models.FileField(upload_to='vacancies/', blank=True, null=True, max_length=200)
    class Meta:
        verbose_name_plural = "Vacancies"
    def __str__(self):
        return self.position

class Gallery(models.Model):
    name = models.CharField(max_length= 200)
    images = models.ManyToManyField("GalleryImage", related_name ='gallery_images') 
    def __str__(self):
        return self.images

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    def __str__(self):
        return self.image
