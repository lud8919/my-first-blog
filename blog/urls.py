#plik został dodany

from django.conf.urls import url
from . import views   #importuje z bierzącego folderu widoki (views)


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #to wzorzec adresu URL, który przyporządkowuje widok (view) o nazwie post_list do adresu ^$. Ten wzorzec będzie wskazówką dla Django, że views.post_list jest właściwym miejscem dla każdego, kto wejdzie na stronę poprzez adres 'http://127.0.0.1:8000/'. Ostatni kawałek name='post_list jest nazwą adresu URL, która będzie używana do zidentyfikowania widoku.
    url(r'post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'), #zaraz po początku jest adres URL który będzie zawierać słowo post i / . (?P<pk>[0-9]+) -  Django pobierze wszystko, co będzie umieszczone w tym miejscu i przekaże to do widoku w zmiennej o nazwie pk. [0-9]  może to być tylko cyfra (czyli wszystko pomiędzy 0 a 9). + oznacza, że to musi być jedna lub więcej cyfr. Czyli coś takiego jest poprawne: http://127.0.0.1:8000/post/1234567890/
    url(r'post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]






