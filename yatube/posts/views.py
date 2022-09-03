from django.shortcuts import render


def index(request):

    template = 'posts/index.html'

    title = 'Yatube'

    text = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }

    return render(request, template, context)


def group_posts(request, slug):

    template = 'posts/group_list.html'

    title = 'Yatube'

    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
