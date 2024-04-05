from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os
from django.contrib.auth.models import User

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    news_title = models.CharField(max_length=200)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Field to store the name of the staff member who added the news
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
    
    # Override save method to handle file replacement
    def save(self, *args, **kwargs):
    # Check if the instance has a primary key (i.e., it's an existing object)
      if self.pk:
        old_instance = News.objects.get(pk=self.pk)
        # Check if the file field has changed
        if old_instance.news_photo != self.news_photo:
            old_instance.news_photo.delete(False)
      else:
        # If it's a new instance, no need to delete old file
        pass
      super().save(*args, **kwargs)

# Signal to delete file before model instance is deleted
@receiver(pre_delete, sender=News)

def delete_file_on_delete(sender, instance, **kwargs):
         instance.news_photo.delete(False)

# Signal to delete old file if replaced by a new one
@receiver(pre_save, sender=News)
def delete_old_file_on_change(sender, instance, **kwargs):
    if instance.pk:
       old_instance = News.objects.get(pk=instance.pk)
       if old_instance.news_photo != instance.news_photo:
            old_instance.news_photo.delete(False)
    

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
    
             # Override delete method to delete associated file
    def delete(self, *args, **kwargs):
        # Delete the file when the object is deleted
        storage, path = self.event_photo.storage, self.event_photo.path
        storage.delete(path)
        super().delete(*args, **kwargs)

    # Override save method to handle file replacement
    def save(self, *args, **kwargs):
    # Check if the instance has a primary key (i.e., it's an existing object)
      if self.pk:
        old_instance = Event.objects.get(pk=self.pk)
        # Check if the file field has changed
        if old_instance.event_photo != self.event_photo:
            old_instance.event_photo.delete(False)
      else:
        # If it's a new instance, no need to delete old file
        pass
      super().save(*args, **kwargs)

# Signal to delete file before model instance is deleted
@receiver(pre_delete, sender=Event)

def delete_file_on_delete(sender, instance, **kwargs):
         instance.event_photo.delete(False)

# Signal to delete old file if replaced by a new one
@receiver(pre_save, sender=Event)
def delete_old_file_on_change(sender, instance, **kwargs):
    if instance.pk:
       old_instance = Event.objects.get(pk=instance.pk)
       if old_instance.event_photo != instance.event_photo:
            old_instance.event_photo.delete(False)
    

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
    application_form = models.FileField(upload_to='announcements_files/', blank=True, null=True)
    file = models.FileField(upload_to='announcements_files/', blank=True, null=True)
    category = models.CharField(max_length= 50, choices = Category.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    # Override delete method to delete associated file
    def delete(self, *args, **kwargs):
        # Delete the file when the object is deleted
        storage, path = self.file.storage, self.file.path
        storage.delete(path)
        super().delete(*args, **kwargs)

    # Override save method to handle file replacement
    def save(self, *args, **kwargs):
    # Check if the instance has a primary key (i.e., it's an existing object)
      if self.pk:
        old_instance = Announcement.objects.get(pk=self.pk)
        # Check if the file field has changed
        if old_instance.file != self.file:
            old_instance.file.delete(False)
      else:
        # If it's a new instance, no need to delete old file
        pass
      super().save(*args, **kwargs)


# Signal to delete file before model instance is deleted
@receiver(pre_delete, sender=Announcement)

def delete_file_on_delete(sender, instance, **kwargs):
         instance.file.delete(False)

# Signal to delete old file if replaced by a new one
@receiver(pre_save, sender=Announcement)
def delete_old_file_on_change(sender, instance, **kwargs):
    if instance.pk:
       old_instance = Announcement.objects.get(pk=instance.pk)
       if old_instance.file != instance.file:
            old_instance.file.delete(False)
    

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
    
         # Override delete method to delete associated file
    def delete(self, *args, **kwargs):
        # Delete the file when the object is deleted
        storage, path = self.faculty_image.storage, self.faculty_image.path
        storage.delete(path)
        super().delete(*args, **kwargs)

    # Override save method to handle file replacement
    def save(self, *args, **kwargs):
    # Check if the instance has a primary key (i.e., it's an existing object)
      if self.pk:
        old_instance = Faculty.objects.get(pk=self.pk)
        # Check if the file field has changed
        if old_instance.faculty_image != self.faculty_image:
            old_instance.faculty_image.delete(False)
      else:
        # If it's a new instance, no need to delete old file
        pass
      super().save(*args, **kwargs)

# Signal to delete file before model instance is deleted
@receiver(pre_delete, sender=Faculty)

def delete_file_on_delete(sender, instance, **kwargs):
         instance.faculty_image.delete(False)

# Signal to delete old file if replaced by a new one
@receiver(pre_save, sender=Faculty)
def delete_old_file_on_change(sender, instance, **kwargs):
    if instance.pk:
       old_instance = Faculty.objects.get(pk=instance.pk)
       if old_instance.faculty_image != instance.faculty_image:
            old_instance.faculty_image.delete(False)
    


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_code = models.CharField(max_length= 50, unique = True)
    department_name = models.CharField(max_length= 500)
    about_department = models.TextField(null=True, blank= True)
    faculty_code = models.ForeignKey(Faculty, on_delete = models.DO_NOTHING)
    department_image = models.ImageField(upload_to='department_images', blank=True, null=True)
    def __str__(self):
        return self.department_code
    
     # Override delete method to delete associated file
    def delete(self, *args, **kwargs):
        # Delete the file when the object is deleted
        storage, path = self.department_image.storage, self.department_image.path
        storage.delete(path)
        super().delete(*args, **kwargs)

    # Override save method to handle file replacement
    def save(self, *args, **kwargs):
    # Check if the instance has a primary key (i.e., it's an existing object)
      if self.pk:
        old_instance = Department.objects.get(pk=self.pk)
        # Check if the file field has changed
        if old_instance.department_image != self.department_image:
            old_instance.department_image.delete(False)
      else:
        # If it's a new instance, no need to delete old file
        pass
      super().save(*args, **kwargs)

# Signal to delete file before model instance is deleted
@receiver(pre_delete, sender=Department)

def delete_file_on_delete(sender, instance, **kwargs):
         instance.department_image.delete(False)

# Signal to delete old file if replaced by a new one
@receiver(pre_save, sender=Department)
def delete_old_file_on_change(sender, instance, **kwargs):
    if instance.pk:
       old_instance = Department.objects.get(pk=instance.pk)
       if old_instance.department_image != instance.department_image:
            old_instance.department_image.delete(False)

  

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
    
     # Override delete method to delete associated file
    def delete(self, *args, **kwargs):
        # Delete the file when the object is deleted
        storage, path = self.program_image.storage, self.program_image.path
        storage.delete(path)
        super().delete(*args, **kwargs)

    # Override save method to handle file replacement
    def save(self, *args, **kwargs):
    # Check if the instance has a primary key (i.e., it's an existing object)
      if self.pk:
        old_instance = Program.objects.get(pk=self.pk)
        # Check if the file field has changed
        if old_instance.program_image != self.program_image:
            old_instance.program_image.delete(False)
      else:
        # If it's a new instance, no need to delete old file
        pass
      super().save(*args, **kwargs)

# Signal to delete file before model instance is deleted
@receiver(pre_delete, sender=Program)

def delete_file_on_delete(sender, instance, **kwargs):
         instance.program_image.delete(False)

# Signal to delete old file if replaced by a new one
@receiver(pre_save, sender=Program)
def delete_old_file_on_change(sender, instance, **kwargs):
    if instance.pk:
       old_instance = Program.objects.get(pk=instance.pk)
       if old_instance.program_image != instance.program_image:
            old_instance.program_image.delete(False)


class Luanar4moreImpact(models.Model):
    luanar4more_id  = models.AutoField(primary_key=True)
    luanar4more_title = models.CharField(max_length = 200)
    description    = models.TextField(null = True, blank=True)
    luanar4more_photo = models.ImageField(upload_to='Luanar4moreImpact', blank=True, null=True)

    # Override delete method to delete associated file
    def delete(self, *args, **kwargs):
        # Delete the file when the object is deleted
        storage, path = self.luanar4more_photo.storage, self.luanar4more_photo.path
        storage.delete(path)
        super().delete(*args, **kwargs)

    # Override save method to handle file replacement
    def save(self, *args, **kwargs):
    # Check if the instance has a primary key (i.e., it's an existing object)
      if self.pk:
        old_instance = Luanar4moreImpact.objects.get(pk=self.pk)
        # Check if the file field has changed
        if old_instance.luanar4more_photo != self.luanar4more_photo:
            old_instance.luanar4more_photo.delete(False)
      else:
        # If it's a new instance, no need to delete old file
        pass
      super().save(*args, **kwargs)

# Signal to delete file before model instance is deleted
@receiver(pre_delete, sender=Luanar4moreImpact)

def delete_file_on_delete(sender, instance, **kwargs):
         instance.luanar4more_photo.delete(False)

# Signal to delete old file if replaced by a new one
@receiver(pre_save, sender=Luanar4moreImpact)
def delete_old_file_on_change(sender, instance, **kwargs):
    if instance.pk:
       old_instance = Luanar4moreImpact.objects.get(pk=instance.pk)
       if old_instance.luanar4more_photo != instance.luanar4more_photo:
            old_instance.luanar4more_photo.delete(False)


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
    

      # Override delete method to delete associated file
    def delete(self, *args, **kwargs):
        # Delete the file when the object is deleted
        storage, path = self.research_photo.storage, self.research_photo.path
        storage.delete(path)
        super().delete(*args, **kwargs)
    
   # Override save method to handle file replacement
    def save(self, *args, **kwargs):
    # Check if the instance has a primary key (i.e., it's an existing object)
      if self.pk:
        old_instance = ResearchAndOutreach.objects.get(pk=self.pk)
        # Check if the file field has changed
        if old_instance.research_photo != self.research_photo:
            old_instance.research_photo.delete(False)
      else:
        # If it's a new instance, no need to delete old file
        pass
      super().save(*args, **kwargs)

# Signal to delete file before model instance is deleted
@receiver(pre_delete, sender=ResearchAndOutreach)

def delete_file_on_delete(sender, instance, **kwargs):
         instance.research_photo.delete(False)

# Signal to delete old file if replaced by a new one
@receiver(pre_save, sender=ResearchAndOutreach)
def delete_old_file_on_change(sender, instance, **kwargs):
    if instance.pk:
       old_instance = ResearchAndOutreach.objects.get(pk=instance.pk)
       if old_instance.research_photo != instance.research_photo:
            old_instance.research_photo.delete(False)
    

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
    about_staff = models.TextField(blank = True, null = True)
    staff_contacts = models.CharField(max_length= 20)
    staff_email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    department_code = models.ForeignKey(Department, on_delete = models.DO_NOTHING)
    faculty_code = models.ForeignKey(Faculty, on_delete = models.DO_NOTHING, to_field='faculty_code')
    def __str__(self):
        return self.staff_name
    
      # Override delete method to delete associated file
    def delete(self, *args, **kwargs):
        # Delete the file when the object is deleted
        storage, path = self.profile_pic.storage, self.profile_pic.path
        storage.delete(path)
        super().delete(*args, **kwargs)
    

    # Override save method to handle file replacement
    def save(self, *args, **kwargs):
    # Check if the instance has a primary key (i.e., it's an existing object)
      if self.pk:
        old_instance = AcademicStaff.objects.get(pk=self.pk)
        # Check if the file field has changed
        if old_instance.profile_pic != self.profile_pic:
            old_instance.profile_pic.delete(False)
      else:
        # If it's a new instance, no need to delete old file
        pass
      super().save(*args, **kwargs)

# Signal to delete file before model instance is deleted
@receiver(pre_delete, sender=AcademicStaff)

def delete_file_on_delete(sender, instance, **kwargs):
         instance.profile_pic.delete(False)

# Signal to delete old file if replaced by a new one
@receiver(pre_save, sender=AcademicStaff)
def delete_old_file_on_change(sender, instance, **kwargs):
    if instance.pk:
       old_instance = AcademicStaff.objects.get(pk=instance.pk)
       if old_instance.profile_pic != instance.profile_pic:
            old_instance.profile_pic.delete(False)

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
    
      # Override delete method to delete associated file
    def delete(self, *args, **kwargs):
        # Delete the file when the object is deleted
        storage, path = self.profile_pic.storage, self.profile_pic.path
        storage.delete(path)
        super().delete(*args, **kwargs)
    
    # Override save method to handle file replacement
    def save(self, *args, **kwargs):
    # Check if the instance has a primary key (i.e., it's an existing object)
      if self.pk:
        old_instance = AdministrationStaff.objects.get(pk=self.pk)
        # Check if the file field has changed
        if old_instance.profile_pic != self.profile_pic:
            old_instance.profile_pic.delete(False)
      else:
        # If it's a new instance, no need to delete old file
        pass
      super().save(*args, **kwargs)

# Signal to delete file before model instance is deleted
@receiver(pre_delete, sender=AdministrationStaff)

def delete_file_on_delete(sender, instance, **kwargs):
         instance.profile_pic.delete(False)

# Signal to delete old file if replaced by a new one
@receiver(pre_save, sender=AdministrationStaff)
def delete_old_file_on_change(sender, instance, **kwargs):
    if instance.pk:
       old_instance = AdministrationStaff.objects.get(pk=instance.pk)
       if old_instance.profile_pic != instance.profile_pic:
            old_instance.profile_pic.delete(False)

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