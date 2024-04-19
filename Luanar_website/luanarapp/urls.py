from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
path('', views.home, name= ""),
path('login/', views.loginPage, name="login"),
path('logout/', views.logoutUser, name="logout"),
path('create-gallery/', views.create_gallery, name="create-gallery"),
path('about', views.about, name = "about"),
path('vacancies', views.vacancies, name = "vacancies"),
path('vacancy_details/<str:id>', views.vacancy_detailsView, name = "vacancy_details"),
path('newsandevents', views.newsandevents, name = "newsandevents"),
path('newsdetail/<str:id>', views.newsdetail, name = "newsdetail"),
path('events', views.events, name = "events"),
path('eventsdetail/<str:id>', views.eventsdetail, name = "eventsdetail"),
path('campusesandmaps', views.campusesandmaps, name = "campusesandmaps"),
path('luanarholdings', views.luanarholdings, name = "luanarholdings"),
path('faculties', views.faculties, name = "faculties"),
path('faculty_details/<str:code>', views.faculty_detailsView, name="faculty_details"),
path('department_details/<str:id>', views.department_detailsView, name = "department_details"),
path('program_details/<str:id>', views.program_detailsView, name= "program_details"),

path('search/', views.search_view, name='search_view'),



path('partinerships', views.partinerships, name = "partinerships"),
path('luanar4moreimpact', views.luanar4moreimpact, name = "luanar4moreimpact"),
path('managementandgovernance', views.managementandgovernance, name = "managementandgovernance"),
path('policies', views.policies, name="policies"),
path('postgraduate', views.postgraduate, name = "postgraduate"),
path('undergraduate',views.undergraduate, name ="undergraduate"),
path('howtoapply', views.howtoapplyView , name = "howtoapply"),
path('message_from_vc', views.message_from_vcView, name = 'message_from_vc'),
path('mission_vision_values', views.mission_vision_valuesView, name="mission_vision_values"),
path('luanar_history', views.luanarhistoryView, name= "luanar_history"),
path('social_community', views.social_communityView, name = "social_community"),
path('new_partinerships', views.new_partinershipsView, name = "new_partinerships"),

#students routes
path('undergraduateprograms', views.undergraduateprograms , name = "undergraduateprograms"),
path('postgraduateprograms', views.postgraduateprograms , name = "postgraduateprograms"),
path('alumnisportlight', views.alumnisportlight , name = "alumnisportlight"),
path('luanarcalendar', views.luanarcalendar , name = "luanarcalendar"),
path('shortcourses', views.shortcourses , name = "shortcourses"),
path('internationalstudents', views.internationalstudents , name = "internationalstudents"),
path('summerprograms', views.summerprograms , name = "summerprograms"),
path('bundacampus', views.bundacampus , name = "bundacampus"),
path('citycampus', views.citycampus , name = "citycampus"),
path('programs_at_city', views.programs_at_cityView, name = "programs_at_city"),
path('programs_at_odl', views.programs_at_odlView, name = "programs_at_odl"),

path('odl', views.odl , name = "odl"),
path('naturalresourcescollege', views.naturalresourcescollege , name = "naturalresourcescollege"),
path('whychooseluanar', views.whychooseluanar , name = "whychooseluanar"),
path('virtualcampus', views.virtualcampus , name = "virtualcampus"),
path('onlineregistration', views.onlineregistration , name = "onlineregistration"),
path('sportsandrecreation', views.sportsandrecreation , name = "sportsandrecreation"),
path('summerschools', views.summerschools , name = "summerschools"),
path('applicationsNche', views.applicationsNche , name = "applicationsNche"),
path('whattostudy', views.whattostudy , name = "whattostudy"),
path('accommodation', views.accommodation , name = "accommodation"),
path('safetyoncampus', views.safetyoncampus , name = "safetyoncampus"),
path('prospectus', views.prospectus , name = "prospectus"),
path('immigration', views.immigrationView, name = "immigration"),
path('gbv', views.gbv, name="gbv"),



#staff profiles


path('aboutvc', views.aboutvc, name = "aboutvc"),
path('aboutdvc', views.aboutdvc, name = "aboutdvc"),
path('aboutur', views.aboutur, name = "aboutur"),


#postgraduate routes
path('feesandfunding', views.feesandfunding , name = "feesandfunding"),
path('applicationprocess', views.applicationprocess , name = "applicationprocess"),
path('fundingopportunities', views.fundingopportunities , name = "fundingopportunities"),
path('student_rules_and_regulations', views.student_rules_and_regulations , name = "student_rules_and_regulations"),



#campus life routes
path('wheretoeat', views.wheretoeat , name = "wheretoeat"),
path('healthandwellbeing', views.healthandwellbeing , name = "healthandwellbeing"),
path('studentsgovernance', views.studentsgovernance , name = "studentsgovernance"),
path('thingstodo', views.thingstodo , name = "thingstodo"),
path('researchandoutreach', views.researchandoutreach , name = "researchandoutreach"),
path('campus_life', views.campus_life, name= "campus_life"),
path('studentunion', views.studentunion, name= "studentunion"),
path('studentorientation', views.studentorientation, name="studentorientation"),
path('supportnetworks', views.supportnetworks, name = "supportnetworks"),
path('studentclubsandsociety', views.studentclubsandsociety, name="studentclubsandsociety"),
path('popularvideos', views.popularvideos , name = "popularvideos"),
path('staff_sports', views.staff_sports, name = "staff_sports"),
path('support_services', views.support_services, name = 'support_services'),



#luanar administrative offices' routes
path('office_of_vc', views.office_of_vc , name = "office_of_vc"),
path('office_of_dvc', views.office_of_dvc , name = "office_of_dvc"),
path('office_of_dosa', views.office_of_dosa , name = "office_of_dosa"),
path('office_of_ar', views.office_of_ar , name = "office_of_ar"),
path('office_of_ur', views.office_of_ur , name = "office_of_ur"),
path('office_of_doqa', views.office_of_doqa , name = "office_of_doqa"),
path('office_of_hr', views.office_of_hr, name = "office_of_hr"),
path('marketing', views.marketing, name ="marketing"),



path('announcements', views.announcements , name = "announcements"),
path('announcement_detail/<str:id>', views.announcement_detail, name = 'announcement_detail'),
path('gallery', views.gallery , name = "gallery"),
path('social_media_links', views.social_media_links , name = "social_media_links"),
path('downloads', views.downloads , name = "downloads"),
 
]
