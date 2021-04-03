from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from .models import Company, Specialty, Vacancy


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = Company.objects.annotate(vacancies_count=Count('vacancies'))
        context['specialties'] = Specialty.objects.annotate(vacancies_count=Count('vacancies'))
        return context


class CompanyView(TemplateView):
    template_name = 'company.html'

    def get_context_data(self, company_id, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = get_object_or_404(Company, id=company_id)
        context['vacancies'] = Vacancy.objects.filter(company__id=company_id)
        return context


class SpecialtyView(TemplateView):
    template_name = 'vacancies.html'

    def get_context_data(self, specialty, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_object_or_404(Specialty, code=specialty).title
        context['vacancies'] = Vacancy.objects.filter(specialty__code=specialty)
        return context


class VacanciesView(ListView):
    template_name = 'vacancies.html'
    model = Vacancy
    context_object_name = 'vacancies'
    queryset = Vacancy.objects.select_related('company').all().order_by('-published_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все вакансии'
        return context


class VacancyView(DetailView):
    template_name = 'vacancy.html'
    model = Vacancy
    pk_url_kwarg = 'vacancy_id'
    queryset = Vacancy.objects.select_related('company').all()


def custom_handler404(request, exception):
    response = render(request, '404.html')
    response.status_code = 404
    return response


def custom_handler500(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response
