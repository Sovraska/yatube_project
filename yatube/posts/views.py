from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'Список мороженого слаг {slug}')
