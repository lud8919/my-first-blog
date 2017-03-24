# dodany  formularz dla modelu Post


from django import forms #importuje formularze z Django
from .models import Post  #to importuje model postu

class PostForm(forms.ModelForm): #PostForm będzie nazwą tego modelu formularza
    class Meta:
        model = Post # tu mówimy, że do stworzenia tego formularza będziemy urzywać modleu Post
        fields = ('title', 'text',)





