from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
   path('',views.index,name="index"),
    path('index.html',views.index,name="index"),
    path("jobs.html", views.jobs,name="jobs"),
    path("candidate.html", views.candidate,name="candidate"),
    path("job_details.html", views.jobdetails,name="job_details"),
    path("elements.html", views.element,name="elements"),
    path("blog.html", views.blog,name="blog"),
    path("single-blog.html",views.singleblog,name="singleblog"),
    path("contact.html", views.contact,name="contact"),
    path("login.html", views.login,name="login"),
    path("sign_up.html", views.signup,name="sign_up"),
    path("resume.html", views.resume,name="resume"),
    path("aftersignUp.html", views.aftersignUp,name="aftersignUp"),
    path("aftercontact.html", views.aftercontact,name="aftercontact"),
    path("subscribed.html", views.subscribed,name="subscribed"),
    path("digitalmarketer.html", views.digitalmarketer,name="digitalmarketer"),
    path("wordpress.html", views.wordpress,name="wordpress"),
    path("visual.html", views.visual,name="visual"),
    path("creative.html", views.creative,name="creative"),
    path("applicationDone.html", views.application,name="application")
      

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)