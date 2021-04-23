from django.shortcuts import render
from django.http import HttpResponse

from .models import News
# Create your views here.


def index(request):
    # print(dir(request))
    news = News.objects.all()
    # res = '<h1>Список новостей</h1>'
    # for item in news:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    # return(HttpResponse(res))
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})

 
def test(request):
    news1 = News.objects.filter(title='Новость 1')
    res = [i.title for i in news1]
    return(HttpResponse(f'<h1>{res}</h1>'))