# Create your views here.
# Widok jest miejscem, w którym umieszczamy "logikę" naszej aplikacji. Pobierze on informacje od modelu, który wcześniej utworzyłaś, a następnie przekaże je do szablonu (template).



from django.shortcuts import render, get_object_or_404 # get_object_or_404 - bierze stronę 404 z Django
from django.utils import timezone  #Czas jest potrzebny bo wyświatlamy tylko opublikowane posty a te mają datę publikacji
from .models import Post    #By modele zapisane w bazie danych się wyświetliły na stronie musimy pobrać te modele i przekazać je do szablonu. Więc tutaj importujemy nazwę modelu (Post) z pliku models.py (kropka oznacza bieżący katalog)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #Ten QuerySet zwraca listę wpisów, które zostały opublikowane (mają datę publikacji) i są uporządkowane według daty publikacji (published_date). Tu więcej o QuerySet https://docs.djangoproject.com/en/1.8/ref/models/querysets/
    return render(request, 'blog/post_list.html', {'posts': posts})  #to jest funkcja (def) o nazwie post_list, która przyjmuje zapytanie (request) i zwraca (return) funkcję zwaną render, której zadaniem jest wyrenderowanie (złożenie w całość) naszego szablonu blog/post_list.html. Skałada i z HTML-a i z obiektów Post



def post_detail(request, pk): #widok dla detali wpisu otrzymuje dodatkowy parametr pk
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


