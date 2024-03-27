# from django import forms
# from .models import News, Event, Announcement,Staff, Program, Faculty, ProgramNature, Department, College,Campus

# class NewsForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = ['title', 'description', 'first_photo','second_photo','third_photo','news_date']

# class EventsForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['title', 'description', 'first_photo','second_photo', 'third_photo','forth_photo', 'host', 'venue','start_date','end_date','files']

# class AnnouncementForm(forms.ModelForm):
#     class Meta:
#         model = Announcement
       
# class ProgramForm(forms.ModelForm):
#     class Meta:
#         model = Program
#         fields = ['program_code','program_name','requirement','duration','program_description']

# class ProgramNatureForm(forms.ModelForm):
#     class Meta:
#         model = ProgramNature
#         fields = ['programnature_name']

# class FacultyForm(forms.ModelForm):
#     class Meta:
#         model = Faculty
#         fields = ['faculty_code','faculty_name']

# class StaffForm(forms.ModelForm):
#     class Meta:
#         model = Staff
#         fields = ['staff_name','staff_position','phone','staff_email','staff_about','profile_pic']

# class DepartmentForm(forms.ModelForm):
#     class Meta:
#         model = Department
#         fields = ['faculty_code','faculty_name']

# class CollegeForm(forms.ModelForm):
#     class Meta:
#         model = College
#         fields = ['college_code','college_name']


# class CampusForm(forms.ModelForm):
#     class Meta:
#         model = Campus
#         fields = ['_code','faculty_name']

from django import forms
from .models import Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name','images']
    