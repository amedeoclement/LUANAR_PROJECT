
import datetime
from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import GalleryForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#create your views here

def loginPage(request):
    return redirect('/admin')
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     try:
    #         user = User.objects.get(username=username)
    #     except:
    #         messages.error(request, 'User does not exist')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #        login(request, user) 
    #        return redirect('home')
    #     else:
    #          messages.error(request, 'username or password incorrect')
    # context = {}
    # return render(request, 'luanarapp/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    announcements= Announcement.objects.all().order_by('-announcement_id')[:2]
    events = Event.objects.all().order_by('-event_id')[:2]
    faculties = Faculty.objects.all().order_by('faculty_id')[:3]
    news = News.objects.all().order_by('-news_id')[:6]
    luanar4moreimpacts = Luanar4moreImpact.objects.all().order_by('-luanar4more_id')[:1]
    context = {'faculties': faculties, 'news':news,'events':events, 'announcements':announcements,'luanar4moreimpacts':luanar4moreimpacts , 'prospectus':prospectus}
    return render(request, 'luanarapp/home.html', context)


def create_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GalleryForm()
        return render(request,'luanarapp/create_gallery.html', {'form':form})


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
    firstfaculty = Faculty.objects.get(faculty_id = 1)
    departments = Department.objects.filter(faculty_code_id = 3)
    faculties = Faculty.objects.all().order_by('faculty_code')[:6]
    context = {'faculties':faculties, 'firstfaculty':firstfaculty, 'departments':departments}
    
    return render(request, 'luanarapp/faculties.html', context)
   

def faculty_detailsView(request, code):
    firstfaculty = Faculty.objects.get(faculty_id= code)
    departments = Department.objects.filter(faculty_code_id = code)
    faculties = Faculty.objects.all().order_by('faculty_code')[:6]
    context = {'faculties':faculties, 'firstfaculty':firstfaculty, 'departments':departments}
    return render(request, 'luanarapp/faculties.html', context)

def department_detailsView(request, id):
    department = Department.objects.get(department_id = id)
    programs = Program.objects.filter(department_code_id = id)
    context={'department':department, 'programs':programs}
    return render(request, 'luanarapp/departments.html', context)

def program_detailsView(request, id):
    program = Program.objects.get(program_id = id)
    department = Department.objects.get(  department_id = program.department_code_id )
    context = {'program':program, 'department':department}
    return render(request, 'luanarapp/programs.html', context)

def campusesandmaps(request):
    return render(request, 'luanarapp/campusesandmaps.html')


def popularvideos(request):
    return render(request, 'luanarapp/about/popularvideos.html')

def newsandevents(request):
    news = News.objects.all().order_by('-news_id')
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
    return render(request, 'luanarapp/newsandevents.html', {'page': page, 'page_range': page_range})

def newsdetail(request, id):
    news = News.objects.all().order_by('?')[:4]
    new = News.objects.get(news_id = id )
    context = {'new': new , 'news':news}
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
    event = Event.objects.get(event_id = id )
    current_date = datetime.date.today()
    context = {'event': event , 'news':news, 'current_date':current_date}
    return render(request, 'luanarapp/event_details.html', context)


def vacancy_detailsView(request, id):
    vacancy = Vacancy.objects.get(vacancy_id = id)
    context = {'vacancy':vacancy}
    return render(request, 'luanarapp/vacancy_details.html', context)

def luanar4moreimpact(request):
    return render(request, 'luanarapp/luanar4moreimpact.html')

def undergraduate(request):
    return render(request, 'luanarapp/undergraduate.html')

def postgraduate(request):
    return render(request, 'luanarapp/postgraduate.html')

def message_from_vcView(request):
    return render(request,'luanarapp/about/message_from_vc.html')

def mission_vision_valuesView(request):
    return render(request, 'luanarapp/about/mission_vision_values.html')

def luanarhistoryView(request):
    return render(request, 'luanarapp/about/luanar_history.html')

def social_communityView(request):
    return render(request, 'luanarapp/about/social_community.html')

def new_partinershipsView(request):
    return render(request, 'luanarapp/about/new_partinerships.html')

#luanar campuses views
def bundacampus(request):
    programs = Program.objects.all()[:6]
    context = {'programs': programs}
    return render(request, 'luanarapp/campuses/bundacampus.html', context)

def citycampus(request):
    return render(request, 'luanarapp/campuses/citycampus.html')

def programs_at_cityView(request):
    programs = Program.objects.all()[:6]
    context = {'programs': programs}
    return render(request, 'luanarapp/campuses/programs_at_city.html', context)

def programs_at_odlView(request):
    programs = Program.objects.all()[:6]
    context = {'programs': programs}
    return render(request, 'luanarapp/campuses/programs_at_odl.html', context)

def odl(request):
    return render(request, 'luanarapp/campuses/odl.html')

def naturalresourcescollege(request):
    programs = Program.objects.all()[:6]
    context = {'programs': programs}
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
    return render(request, 'luanarapp/students/undergraduateprograms.html',  {'page': page, 'page_range': page_range})



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
    return render(request, 'luanarapp/students/postgraduateprograms.html',  {'page': page, 'page_range': page_range})

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
    announcement_detail = Announcement.objects.get(announcement_id=id)
    news = News.objects.all().order_by('?')[:4]
    context = {'news':news,'announcement_detail':announcement_detail}
    return render(request, 'luanarapp/announcement_details.html' , context)

def gallery(request):
    return render(request, 'luanarapp/gallery.html')

def social_media_links(request):
    return render(request, 'luanarapp/social_media_links.html')

def downloads(request):
    return render(request, 'luanarapp/downloads.html')

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
