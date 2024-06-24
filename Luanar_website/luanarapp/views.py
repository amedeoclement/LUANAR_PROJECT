
import datetime
from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import SearchForm, SubscriberForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#create your views here

def loginPage(request):
    return redirect('/admin')

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    announcements= Announcement.objects.all().order_by('-announcement_id')[:3]
    events = Event.objects.all().order_by('-event_id')[:3]
    faculties = Faculty.objects.all().order_by('faculty_code')[:3]
    news = News.objects.all().order_by('-news_id')[:3]
    form = SearchForm()
    context = {'faculties': faculties, 'news':news,'events':events, 'announcements':announcements, 'prospectus':prospectus, 'form':form}
    return render(request, 'luanarapp/home.html', context)


#luanar in general
def about(request):
    return render(request, 'luanarapp/about.html')

def partinerships(request):
    return render(request, 'luanarapp/partinerships.html')

def managementandgovernance(request):
    
    return render(request, 'luanarapp/managementandgovernance.html')

def policies(request):
    return render(request, 'luanarapp/policies.html')

def faculties(request):
    firstfaculty = Faculty.objects.get(faculty_code = 'BUNDA_FAG')
    news = News.objects.all().order_by( '-news_id')[1]
    departments = Department.objects.filter(faculty_code_id = 3)
    faculties = Faculty.objects.all().order_by('faculty_code')[:6]
    staff = AcademicStaff.objects.filter(faculty_code_id = "BUNDA_FAG", staff_position = "HEAD OF FACULTY")
    context = {'faculties':faculties, 'firstfaculty':firstfaculty, 'departments':departments, 'news':news, 'staff':staff}
    return render(request, 'luanarapp/faculties.html', context)


def faculty_detailsView(request, code):
    firstfaculty = Faculty.objects.get(faculty_id= code)
    departments = Department.objects.filter(faculty_code_id = code)
    faculties = Faculty.objects.all().order_by('faculty_code')[:6]
    news = News.objects.all().order_by( '-news_id')[1]
    staff = AcademicStaff.objects.filter(faculty_code_id = firstfaculty.faculty_code, staff_position = "HEAD OF FACULTY")
    context = {'faculties':faculties, 'firstfaculty':firstfaculty, 'departments':departments, 'staff':staff, 'news':news}
    return render(request, 'luanarapp/faculties.html', context)

def campus_faculties(request, code):
    firstfaculty = Faculty.objects.filter(campus_code_id = code)[1]
    faculties = Faculty.objects.filter(campus_code_id = code).order_by('faculty_code')
    news = News.objects.all().order_by( '-news_id')[1]
    staff = AcademicStaff.objects.filter(faculty_code_id = firstfaculty.faculty_code, staff_position = "HEAD OF FACULTY")
    context = {'faculties':faculties, 'firstfaculty':firstfaculty, 'staff':staff, 'news':news}
    return render(request, 'luanarapp/faculties.html', context)


def department_detailsView(request, id):
    department = Department.objects.get(department_id = id)
    programs = Program.objects.filter(department_code_id = id)
    context={'department':department, 'programs':programs}
    return render(request, 'luanarapp/departments.html', context)

def program_detailsView(request, id):
    program = Program.objects.get(program_id = id)
    department = Department.objects.get(department_id = program.department_code_id )
    faculty = Faculty.objects.get(faculty_id = department.faculty_code_id)
    context = {'program':program, 'department':department,'faculty':faculty}
    return render(request, 'luanarapp/programs.html', context)

def campusesandmaps(request):
    return render(request, 'luanarapp/campusesandmaps.html')


def popularvideos(request):
    return render(request, 'luanarapp/about/popularvideos.html')

def newsandevents(request):
    news = News.objects.all().order_by('-news_id')
    staff = AdministrationStaff.objects.order_by('?').first()
    # Your queryset

    # Number of items per page
    items_per_page = 4

    # Create a Paginator object
    paginator = Paginator(news, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')

    try:
        # Get the specified page
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)

    # Get the current page number
    current_page = page.number

    # Get the total number of pages
    total_pages = paginator.num_pages

    # Calculate the range of pages to display
    if total_pages <= 10:
        page_range = paginator.page_range
    else:
        if current_page <= 5:
            page_range = range(1, 11)
        elif current_page >= total_pages - 4:
            page_range = range(total_pages - 9, total_pages + 1)
        else:
            page_range = range(current_page - 4, current_page + 5)

    # Pass the page object and page range to the template
    return render(request, 'luanarapp/newsandevents.html', {'page': page, 'page_range': page_range, 'staff': staff})

def newsdetail(request, id):
    news = News.objects.all().order_by('?')[:4]
    new = News.objects.get(news_title = id )
    events = Event.objects.all().order_by('-event_id')[:2]
    added_by_user = new.added_by  # Retrieve the user who added the news
    context = {'new': new , 'news':news, 'added_by_user':added_by_user,'events':events}
    return render(request, 'luanarapp/newsdetail.html', context)

def events(request):
    event = Event.objects.all().order_by('-event_id')
    # Your queryset

    # Number of items per page
    items_per_page = 6

    # Create a Paginator object
    paginator = Paginator(event, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')

    try:
        # Get the specified page
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)

    # Get the current page number
    current_page = page.number

    # Get the total number of pages
    total_pages = paginator.num_pages

    # Calculate the range of pages to display
    if total_pages <= 10:
        page_range = paginator.page_range
    else:
        if current_page <= 5:
            page_range = range(1, 11)
        elif current_page >= total_pages - 4:
            page_range = range(total_pages - 9, total_pages + 1)
        else:
            page_range = range(current_page - 4, current_page + 5)

    # Pass the page object and page range to the template
    return render(request, 'luanarapp/events.html', {'page': page, 'page_range': page_range})



def luanarholdings(request):
    return render(request, 'luanarapp/luanarholdings.html')

def vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-vacancy_id')
    announcements = Announcement.objects.all().order_by('-announcement_id')[:2]
 # Number of items per page
    items_per_page = 3

    # Create a Paginator object
    paginator = Paginator(vacancies, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')

    try:
        # Get the specified page
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)

    # Get the current page number
    current_page = page.number

    # Get the total number of pages
    total_pages = paginator.num_pages

    # Calculate the range of pages to display
    if total_pages <= 10:
        page_range = paginator.page_range
    else:
        if current_page <= 5:
            page_range = range(1, 11)
        elif current_page >= total_pages - 4:
            page_range = range(total_pages - 9, total_pages + 1)
        else:
            page_range = range(current_page - 4, current_page + 5)
    return render(request, 'luanarapp/vacancies.html', {'page': page, 'page_range': page_range,'announcements':announcements})

def eventsdetail(request, id):
    news = News.objects.all().order_by('?')[:4]
    event = Event.objects.get(event_title = id )
    current_date = datetime.date.today()
    context = {'event': event , 'news':news, 'current_date':current_date}
    return render(request, 'luanarapp/event_details.html', context)


def vacancy_detailsView(request, id, title):
    vacancy = Vacancy.objects.get(vacancy_id = id, position = title)
    hr = AdministrationStaff.objects.get(staff_position = "Human Resources Manager")
    context = {'vacancy':vacancy, 'hr':hr}
    return render(request, 'luanarapp/vacancy_details.html', context)

def luanar4moreimpact(request):
    luanar4moreimpacts = Luanar4moreImpact.objects.all().order_by('-luanar4more_id')[:1]
    return render(request, 'luanarapp/luanar4moreimpact.html', {'luanar4moreimpacts':luanar4moreimpacts})

def undergraduate(request):
    return render(request, 'luanarapp/undergraduate.html')

def postgraduate(request):
    return render(request, 'luanarapp/postgraduate.html')

def message_from_vcView(request):
    return render(request,'luanarapp/about/message_from_vc.html')

def mission_vision_valuesView(request):
    vc = AdministrationStaff.objects.filter(office_code_id = 2)
  
    return render(request, 'luanarapp/about/mission_vision_values.html', {'vc':vc})

def luanarhistoryView(request):
    return render(request, 'luanarapp/about/luanar_history.html')

def social_communityView(request):
    return render(request, 'luanarapp/about/social_community.html')

def new_partinershipsView(request):
    return render(request, 'luanarapp/about/new_partinerships.html')

#luanar campuses views
def bundacampus(request):
    announcements= Announcement.objects.filter(tag = "Bunda").order_by('-announcement_id')[:2]
    events = Event.objects.filter(tag = "Bunda").order_by('-event_id')[:2]
    faculties = Faculty.objects.filter(campus_code_id = 1).order_by('faculty_code')[:3]
    news = News.objects.filter(tag = 'Bunda').order_by('-news_id')[:3]
    context = {'faculties': faculties, 'news':news,'events':events, 'announcements':announcements}
    return render(request, 'luanarapp/campuses/bundacampus.html', context)

def citycampus(request):
    announcements= Announcement.objects.filter(tag = "CITY").order_by('-announcement_id')[:2]
    events = Event.objects.filter(tag = "CITY").order_by('-event_id')[:2]
    faculties = Faculty.objects.filter(campus_code_id = 4).order_by('faculty_code')[:3]
    news = News.objects.filter(tag = 'CITY').order_by('-news_id')[:3]
    context = {'faculties': faculties, 'news':news,'events':events, 'announcements':announcements}
    return render(request, 'luanarapp/campuses/citycampus.html',context)

def programs_at_cityView(request):
    programs = Program.objects.all()[:6]
    context = {'programs': programs}
    return render(request, 'luanarapp/campuses/programs_at_city.html', context)

def odl(request):
    announcements= Announcement.objects.filter(tag = "ODL").order_by('-announcement_id')[:2]
    events = Event.objects.filter(tag = "ODL").order_by('-event_id')[:2]
    faculties = Faculty.objects.filter(campus_code_id = 3).order_by('faculty_code')[:3]
    news = News.objects.filter(tag = 'ODL').order_by('-news_id')[:3]
    context = {'faculties': faculties, 'news':news,'events':events, 'announcements':announcements}
    return render(request, 'luanarapp/campuses/odl.html', context)

def naturalresourcescollege(request):
    announcements= Announcement.objects.filter(tag = "NRC").order_by('-announcement_id')[:2]
    events = Event.objects.filter(tag = "NRC").order_by('-event_id')[:2]
    faculties = Faculty.objects.filter(campus_code_id = 2).order_by('faculty_code')[:3]
    news = News.objects.filter(tag = 'NRC').order_by('-news_id')[:3]
    context = {'faculties': faculties, 'news':news,'events':events, 'announcements':announcements}
    return render(request, 'luanarapp/campuses/naturalresourcescollege.html', context)


def virtualcampus(request):
    return render(request, 'luanarapp/campuses/virtualcampus.html')


#luanar students views

def undergraduateprograms(request):
    undergraduate_programs = Program.objects.filter(programnature_name_id = 1)
    # Number of items per page
    items_per_page = 6

    # Create a Paginator object
    paginator = Paginator(undergraduate_programs, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')

    try:
        # Get the specified page
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)

    # Get the current page number
    current_page = page.number

    # Get the total number of pages
    total_pages = paginator.num_pages

    # Calculate the range of pages to display
    if total_pages <= 10:
        page_range = paginator.page_range
    else:
        if current_page <= 5:
            page_range = range(1, 11)
        elif current_page >= total_pages - 4:
            page_range = range(total_pages - 9, total_pages + 1)
        else:
            page_range = range(current_page - 4, current_page + 5)
    
    form = SearchForm()
    return render(request, 'luanarapp/students/undergraduateprograms.html',  {'page': page, 'page_range': page_range,'form':form})



def postgraduateprograms(request):

    postgraduate_programs = Program.objects.filter(programnature_name_id = 2)
    # Number of items per page
    items_per_page = 6

    # Create a Paginator object
    paginator = Paginator(postgraduate_programs, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')

    try:
        # Get the specified page
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)

    # Get the current page number
    current_page = page.number

    # Get the total number of pages
    total_pages = paginator.num_pages

    # Calculate the range of pages to display
    if total_pages <= 10:
        page_range = paginator.page_range
    else:
        if current_page <= 5:
            page_range = range(1, 11)
        elif current_page >= total_pages - 4:
            page_range = range(total_pages - 9, total_pages + 1)
        else:
            page_range = range(current_page - 4, current_page + 5)
    form = SearchForm()
    return render(request, 'luanarapp/students/postgraduateprograms.html',  {'page': page, 'page_range': page_range, 'form':form})

def howtoapplyView(request):
    return render(request, 'luanarapp/students/howtoapply.html')

def alumnisportlight(request):
    return render(request, 'luanarapp/students/alumnisportlight.html')

def office_of_doqa(request):
    return render(request, 'luanarapp/office/office_of_doqa.html')

def luanarcalendar(request):
    return render(request, 'luanarapp/students/luanarcalendar.html')

def whychooseluanar(request):
    return render(request, 'luanarapp/students/whychooseluanar.html')

def campus_life(request):
    return render(request, 'luanarapp/students/campus_life.html')

def studentunion(request):
    return render(request, 'luanarapp/students/students_union.html')

def studentaccommodation(request):
    return render(request, 'luanarapp/students/students_accommodation.html')

def studentclubsandsociety(request):
    return render(request, 'luanarapp/campus_life/studentclubsandsociety.html')

def supportnetworks(request):
    return render(request, 'luanarapp/campus_life/supportnetworks.html')

def studentorientation(request):
    return render(request, 'luanarapp/students/studentorientation.html')

def shortcourses(request):
    return render(request, 'luanarapp/students/shortcourses.html')

def internationalstudents(request):
    return render(request, 'luanarapp/students/internationalstudents.html')

def summerprograms(request):
    return render(request, 'luanarapp/students/summerprograms.html')

def onlineregistration(request):
    return render(request, 'luanarapp/students/onlineregistration.html')

def sportsandrecreation(request):
    return render(request, 'luanarapp/students/sportsandrecreation.html')

def summerschools(request):
    return render(request, 'luanarapp/students/summerschools.html')

def applicationsNche(request):
    return render(request, 'luanarapp/students/applicationsNche.html')

def whattostudy(request):
    return render(request, 'luanarapp/students/whattostudy.html')

def accommodation(request):
    return render(request, 'luanarapp/students/accommodation.html')

def gbv(request):
    return render(request, 'luanarapp/gbv.html')

def safetyoncampus(request):
    return render(request, 'luanarapp/students/safetyoncampus.html')

def prospectus(request):
    return render(request, 'luanarapp/students/prospectus.html')

def immigrationView(request):
    return render(request, 'luanarapp/students/immigration.html')

def student_rules_and_regulations(request):
    return render(request, 'luanarapp/students/student_rules_and_regulations.html')

#postgraduate views

def feesandfunding(request):
    return render(request, 'luanarapp/students/feesandfunding.html')

def applicationprocess(request):
    return render(request, 'luanarapp/students/applicationprocess.html')

def fundingopportunities(request):
    return render(request, 'luanarapp/students/fundingopportunities.html')

#campuslife views

def wheretoeat(request):
    return render(request, 'luanarapp/campus_life/wheretoeat.html')

def healthandwellbeing(request):
    return render(request, 'luanarapp/campus_life/healthandwellbeing.html')

def studentsgovernance(request):
    return render(request, 'luanarapp/campus_life/studentsgovernance.html')

def thingstodo(request):
    return render(request, 'luanarapp/campus_life/thingstodo.html')


def researchandoutreach(request):
    return render(request, 'luanarapp/campus_life/researchandoutreach.html')

def staff_sports(request):
    return render(request, 'luanarapp/campus_life/staff_sports.html')

def support_services(request):
    return render(request, 'luanarapp/campus_life/support_services.html')

#luanar administrative offices' views

def office_of_vc(request):
    vc = AdministrationStaff.objects.get(office_code_id = 2)
    new = News.objects.filter().order_by('-news_id')[0]
    return render(request, 'luanarapp/office/office_of_vc.html', {'vc':vc,'new':new}) 

def office_of_dvc(request):

    dvc = AdministrationStaff.objects.get(office_code_id = 3)
    new = News.objects.filter().order_by('-news_id')[0]
    return render(request, 'luanarapp/office/office_of_dvc.html', {'dvc':dvc,'new':new})

def office_of_dosa(request):
    return render(request, 'luanarapp/office/office_of_dosa.html')

def office_of_ar(request):
    return render(request, 'luanarapp/office/office_of_ar.html')

def office_of_ur(request):
    return render(request, 'luanarapp/office/office_of_ur.html')

def office_of_hr(request):
    return render(request, 'luanarapp/office/office_of_hr.html')

def marketing(request):
    return render(request, 'luanarapp/office/marketing_office.html')

def announcements(request):
    announcements = Announcement.objects.all().order_by('-updated_at')
     # Number of items per page
    items_per_page = 6

    # Create a Paginator object
    paginator = Paginator(announcements, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')

    try:
        # Get the specified page
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)

    # Get the current page number
    current_page = page.number

    # Get the total number of pages
    total_pages = paginator.num_pages

    # Calculate the range of pages to display
    if total_pages <= 10:
        page_range = paginator.page_range
    else:
        if current_page <= 5:
            page_range = range(1, 11)
        elif current_page >= total_pages - 4:
            page_range = range(total_pages - 9, total_pages + 1)
        else:
            page_range = range(current_page - 4, current_page + 5)

    # Pass the page object and page range to the template
    return render(request, 'luanarapp/announcements.html', {'page': page, 'page_range': page_range})

def announcement_detail(request, id):
    announcement_detail = Announcement.objects.get(title =id)
    news = News.objects.all().order_by('?')[:4]
    context = {'news':news,'announcement_detail':announcement_detail}
    return render(request, 'luanarapp/announcement_details.html' , context)

def social_media_links(request):
    return render(request, 'luanarapp/social_media_links.html')

def downloads(request):
            
            announcements = Announcement.objects.all().order_by('-announcement_id')
            newsletter = Newsletter.objects.all().order_by('-id')
            vacancies = Vacancy.objects.all().order_by('-vacancy_id')
            # Combine querysets from both models
            combined_results = list(announcements) + list(newsletter) + list(vacancies)

            # Number of items per page
            items_per_page = 10

            # Create a Paginator object
            paginator = Paginator(combined_results, items_per_page)

            # Get the page number from the request
            page_number = request.GET.get('page')

            try:
                # Get the specified page
                page = paginator.page(page_number)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                page = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                page = paginator.page(paginator.num_pages)

            # Get the current page number
            current_page = page.number

            # Get the total number of pages
            total_pages = paginator.num_pages

            # Calculate the range of pages to display
            if total_pages <= 6:
                page_range = paginator.page_range
            else:
                if current_page <= 3:
                    page_range = range(1, 7)
                elif current_page >= total_pages - 2:
                    page_range = range(total_pages - 5, total_pages + 1)
                else:
                    page_range = range(current_page - 2, current_page + 3)

            # Pass the page object and page range to the template
            context =  {'page': page, 'page_range': page_range}
            return render(request, 'luanarapp/downloads.html', context)

# staff profiles

def aboutvc(request):
    vc = AdministrationStaff.objects.get(office_code_id = 2)
    return render(request, 'luanarapp/staff/vc.html', {'vc':vc})

def aboutdvc(request):
    dvc = AdministrationStaff.objects.get(office_code_id = 3)
    return render(request, 'luanarapp/staff/dvc.html', {'dvc':dvc})

def aboutur(request):
    ur = AdministrationStaff.objects.get(office_code_id = 4)
    new = News.objects.filter().order_by('-news_id')[0]
    return render(request, 'luanarapp/staff/ur.html', {'ur':ur,'new':new})


def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            # Perform search in the database
            results = Program.objects.filter(program_name__icontains=query)
            form = SearchForm()
            # Number of items per page
            items_per_page = 6

            # Create a Paginator object
            paginator = Paginator(results, items_per_page)

            # Get the page number from the request
            page_number = request.GET.get('page')

            try:
                # Get the specified page
                page = paginator.page(page_number)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                page = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                page = paginator.page(paginator.num_pages)

            # Get the current page number
            current_page = page.number

            # Get the total number of pages
            total_pages = paginator.num_pages

            # Calculate the range of pages to display
            if total_pages <= 6:
                page_range = paginator.page_range
            else:
                if current_page <= 3:
                    page_range = range(1, 7)
                elif current_page >= total_pages - 2:
                    page_range = range(total_pages - 5, total_pages + 1)
                else:
                    page_range = range(current_page - 2, current_page + 3)

            # Pass the page object and page range to the template
            context =  {'query': query,'form':form, 'page': page, 'page_range': page_range}
            return render(request, 'luanarapp/search_results.html', context)
    else:
        form = SearchForm()

    return render(request, 'luanarapp/students/undergraduateprograms.html', {'form': form})


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data.get('email')
            if Subscriber.objects.filter( email = email).exists():
                messages.info(request, 'This email is already subscribed.')
            else:
                form.save()
                messages.success(request, 'You have successfully subscribed to the newsletter.')
                return redirect('')
            
        else:
           form = SubscriberForm()
           messages.info(request, 'The email has already been used on this site!!!')

    else:
        form = SubscriberForm()
        messages.info(request, 'Check the form if it is properly configured')
    return redirect('')


def search_page(request):
    return render(request, 'luanarapp/search.html')


def general_search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Perform search across different models
            faculties = Faculty.objects.filter(faculty_name__icontains=query) | Faculty.objects.filter(faculty_description__icontains=query)
            news = News.objects.filter(news_title__icontains=query) | News.objects.filter(news_body__icontains=query)
            events = Event.objects.filter(event_title__icontains=query) | Event.objects.filter(event_description__icontains=query) | Event.objects.filter(host__icontains=query)
            announcements = Announcement.objects.filter(title__icontains=query) | Announcement.objects.filter(description__icontains=query)
            programs = Program.objects.filter(program_name__icontains=query) | Program.objects.filter(program_description__icontains=query)


            #administrationOffices = AdministrationOffice.objects.filter(office_name__icontains=query) | AdministrationOffice.objects.filter(office_remarks__icontains=query)
            academicStaffs = AcademicStaff.objects.filter(staff_name__icontains=query) | AcademicStaff.objects.filter(staff_position__icontains=query)
            adminstrationStaffs = AdministrationStaff.objects.filter(staff_name__icontains=query) | AdministrationStaff.objects.filter(staff_position__icontains=query)
            # Combine querysets from both models
            combined_results = list(faculties) + list(news) + list(events) + list(announcements) + list(academicStaffs)+ list(adminstrationStaffs) + list(programs)

            # Number of items per page
            items_per_page = 6

            # Create a Paginator object
            paginator = Paginator(combined_results, items_per_page)

            # Get the page number from the request
            page_number = request.GET.get('page')

            try:
                # Get the specified page
                page = paginator.page(page_number)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                page = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                page = paginator.page(paginator.num_pages)

            # Get the current page number
            current_page = page.number

            # Get the total number of pages
            total_pages = paginator.num_pages

            # Calculate the range of pages to display
            if total_pages <= 6:
                page_range = paginator.page_range
            else:
                if current_page <= 3:
                    page_range = range(1, 7)
                elif current_page >= total_pages - 2:
                    page_range = range(total_pages - 5, total_pages + 1)
                else:
                    page_range = range(current_page - 2, current_page + 3)

            # Pass the page object and page range to the template
            context =  {'query': query, 'form': form, 'page': page, 'page_range': page_range}
            return render(request, 'luanarapp/general_search.html', context)
    else:
        form = SearchForm()
    return render(request, 'luanarapp/general_search.html', {'form': form})

def adminstrative_staff_view(request, id):
    staff = AdministrationStaff.objects.get(staff_id =id)
    return render(request, 'luanarapp/staff/administrative_staff.html', {'staff':staff})

def academic_staff_view(request, id):
    staff = AcademicStaff.objects.get(staff_id =id)
    return render(request, 'luanarapp/staff/academic_staff.html', {'staff':staff})