from django.conf.urls import patterns, url, include
from rango import views
from registration.backends.simple.views import RegistrationView


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(selfself,request, user):
        return '/rango/'


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page', views.add_page, name='add_page'),
    url(r'^add_category/', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/', views.category, name='category'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^restricted/', views.restricted, name='restricted'),
    (r'^accounts/', include('registration.backends.simple.urls')))