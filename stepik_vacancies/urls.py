'''stepik_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from vacancies.views import MainView, CompanyView, SpecialtyView, VacanciesView, VacancyView
from vacancies.views import custom_handler404, custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='home'),
    path('companies/<int:company_id>', CompanyView.as_view(), name='company'),
    path('vacancies/cat/<str:specialty>', SpecialtyView.as_view(), name='specialty'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view(), name='vacancy'),
]

handler404 = custom_handler404
handler500 = custom_handler500

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
