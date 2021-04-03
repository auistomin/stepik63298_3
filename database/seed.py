import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stepik_vacancies.settings')
django.setup()

from vacancies.models import Company, Specialty, Vacancy, Settings  # noqa: E402.

import data  # noqa: E402.


def main():

    # companies
    Company.objects.all().delete()
    for company in data.companies:
        new_company = Company(id=company['id'],
                              name=company['title'],
                              location=company['location'],
                              logo=company['logo'],
                              description=company['description'],
                              employee_count=company['employee_count'],
                              )
        new_company.save()

    # specialties
    Specialty.objects.all().delete()
    for specialty in data.specialties:
        new_specialty = Specialty(code=specialty['code'],
                                  title=specialty['title'],
                                  picture='specty_' + specialty['code'] + '.png',
                                  )
        new_specialty.save()

    # vacancies
    Vacancy.objects.all().delete()
    for job in data.jobs:
        new_vacancy = Vacancy(id=job['id'],
                              title=job['title'],
                              specialty=Specialty.objects.get(code=job['specialty']),
                              company=Company.objects.get(id=job['company']),
                              skills=job['skills'],
                              description=job['description'],
                              salary_min=job['salary_from'],
                              salary_max=job['salary_to'],
                              published_at=job['posted'],
                              )
        new_vacancy.save()

    # settings
    Settings.objects.all().delete()
    new_setting = Settings(name='site_title', setval='Джуманджи')
    new_setting.save()
    new_setting = Settings(name='site_description', setval='Вакансии для <br>Junior-разработчиков')
    new_setting.save()


if __name__ == '__main__':
    main()
