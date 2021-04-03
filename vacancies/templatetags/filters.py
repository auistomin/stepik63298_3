from django.template import Library

register = Library()


def count_str(count, base, suffixes):
    count_int = int(count) if count else 0
    suffix = suffixes[2]
    if (2 <= count_int % 10 <= 4) and (count_int % 100 // 10 != 1):
        suffix = suffixes[1]
    elif (count_int % 10 == 1) and (count_int % 100 // 10 != 1):
        suffix = suffixes[0]
    return base + suffix


@register.filter
def vacancies_count_str(vacancies_count):
    return count_str(vacancies_count, 'ваканси', ['я', 'и', 'й'])


@register.filter
def employee_count_str(employee_count):
    return count_str(employee_count, 'человек', ['', 'а', ''])


@register.filter
def separated_list(strlist):
    return ' • '.join([item.strip() for item in strlist.split(',')])
