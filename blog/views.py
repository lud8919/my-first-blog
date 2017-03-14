# Create your views here.
# Widok jest miejscem, w którym umieszczamy "logikę" naszej aplikacji. Pobierze on informacje od modelu, który wcześniej utworzyłaś, a następnie przekaże je do szablonu (template).

from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})  #to jest metoda (def) o nazwie post_list, która przyjmuje zapytanie (request) i zwraca (return) metodę zwaną render, której zadaniem jest wyrenderowanie (złożenie w całość) naszego szablonu blog/post_list.html.


