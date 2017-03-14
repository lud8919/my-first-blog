#plik został dodany

from django.conf.urls import url
from . import views   #importuje z bierzącego folderu widoki (views)


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #to wzorzec adresu URL, który przyporządkowuje widok (view) o nazwie post_list do adresu ^$. Ten wzorzec będzie wskazówką dla Django, że views.post_list jest właściwym miejscem dla każdego, kto wejdzie na stronę poprzez adres 'http://127.0.0.1:8000/'. Ostatni kawałek name='post_list jest nazwą adresu URL, która będzie używana do zidentyfikowania widoku.
]





