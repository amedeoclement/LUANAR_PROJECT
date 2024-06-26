from django.contrib import admin
from .models import  Event, News, Announcement, ProgramNature, AcademicStaff,Calendar, Program, Faculty, ResearchAndOutreach, QuickAnnouncement, AdministrationStaff,Luanar4moreImpact,Vacancy, Department, College,Campus, AdministrationOffice

#Register your models here.

from .models import Subscriber, Newsletter

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_subscribed']
    search_fields =('email','date_subscribed')
    list_per_page = 5

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']
    search_fields =('title', 'uploaded_at')
    list_per_page = 5

class EventAdmin(admin.ModelAdmin):
    list_display= ('event_title','host','venue', 'event_description','event_photo', 'date')
    list_display_links = ('event_title','host','venue', 'event_description','event_photo', 'date')
    search_fields =('event_title','host', 'venue', 'tag')
    list_per_page = 5
    
class NewAdmin(admin.ModelAdmin):
    list_display= ('news_title', 'news_subtitle', 'added_by_full_name', 'news_body')
    list_display_links = ('news_title', 'news_subtitle','news_body')
    search_fields =('news_title', 'news_header')
    list_per_page = 5
    readonly_fields = ['added_by']

    def save_model(self, request, obj, form, change):
        if not obj.added_by_id:
            obj.added_by = request.user  # Assign the currently logged-in staff member to the added_by field if it's not already set
        super().save_model(request, obj, form, change)

    def added_by_full_name(self, obj):
        if obj.added_by:
            return f"{obj.added_by.first_name} {obj.added_by.last_name}"
        return "Unknown"
    added_by_full_name.short_description = 'Added By'

class AnnouncementAdmin(admin.ModelAdmin):
    list_display= ('title', 'description', 'created_at')
    list_display_links = ('title', 'description', 'created_at')
    search_fields =('title', 'description')
    list_per_page = 5

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('position', 'job_description','requirements')
    list_display_links = ('position', 'job_description','requirements')
    search_fields = ('position', 'job_description', 'requirements')
    list_per_page = 5

class FacultyAdmin(admin.ModelAdmin):
    list_display= ('faculty_code','faculty_name','faculty_mission', 'faculty_description')
    list_display_links = ('faculty_code','faculty_name','faculty_mission', 'faculty_description')
    search_fields =('faculty_code','faculty_name')
    list_per_page = 5

class CampusAdmin(admin.ModelAdmin):
    list_display= ('campus_code','campus_name','about_campus')
    list_display_links = ('campus_code','campus_name','about_campus')
    search_fields =('campus_code','campus_name')
    list_per_page = 5

class AdministrationStaffAdmin(admin.ModelAdmin):
    list_display= ('staff_name','staff_position','staff_email', 'about_staff')
    list_display_links = ('staff_name','staff_position','staff_email', 'about_staff')
    search_fields =('staff_name','staff_position', 'staff_email')
    list_per_page = 5

class ProgramNatureAdmin(admin.ModelAdmin):
    list_display= ('programnature_id','programnature_name')
    list_display_links= ('programnature_id', 'programnature_name')
    search_fields =('programnature_id','programnature_name')
    list_per_page = 2

class ProgramAdmin(admin.ModelAdmin):
    list_display= ('program_code','program_name', 'duration')
    list_display_links= ('program_code','program_name', 'duration')
    search_fields =('program_code','program_name')
    list_per_page = 10

class AcademicStaffAdmin(admin.ModelAdmin):
    list_display= ('staff_name','staff_position','staff_email')
    list_display_links = ('staff_name','staff_position','staff_email')
    search_fields =('staff_name','staff_position', 'staff_email')
    list_per_page = 5

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_code','department_name')
    search_fields = ('department_code','department_name')
    list_per_page = 10

class CollegeAdmin(admin.ModelAdmin):
    list_display= ('college_code','college_name')
    list_display_links = ('college_code','college_name')
    search_fields =('college_code','college_name')
    list_per_page = 5

class Luanar4moreImpactAdmin(admin.ModelAdmin):
    list_display= ('luanar4more_title','luanar4more_photo','description')
    list_display_links = ('luanar4more_title','luanar4more_photo','description')
    search_fields =('luanar4more_title','description')
    list_per_page = 5

class ResearchAndOutreachAdmin(admin.ModelAdmin):
    list_display= ('research_title','research_description','research_photo')
    list_display_links = ('research_title','research_description','research_photo')
    search_fields =('research_title','research_description')
    list_per_page = 5

class AdministrationOfficeAdmin(admin.ModelAdmin):
    list_display= ('office_code','office_name','office_remarks')
    list_display_links = ('office_code','office_name','office_remarks')
    search_fields =('office_code','office_name')
    list_per_page = 5
class QuickAnnouncementAdmin(admin.ModelAdmin):
    list_display= ('announcement_title','description')
    list_display_links = ('announcement_title','description')
    search_fields =('announcement_title','description')
    list_per_page = 5

class CalendarAdmin(admin.ModelAdmin):
    list_display= ('calendar_date','calendar_event','venue')
    list_display_links = ('calendar_date','calendar_event','venue')
    search_fields =('calendar_event','venue')
    
admin.site.register(QuickAnnouncement, QuickAnnouncementAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(News, NewAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(AdministrationStaff, AdministrationStaffAdmin)
admin.site.register(AcademicStaff, AcademicStaffAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(Luanar4moreImpact, Luanar4moreImpactAdmin)
admin.site.register(ResearchAndOutreach, ResearchAndOutreachAdmin)
admin.site.register(AdministrationOffice, AdministrationOfficeAdmin)
admin.site.register(ProgramNature, ProgramNatureAdmin)
admin.site.register(Calendar, CalendarAdmin)