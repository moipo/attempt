from django.urls import path #для использования urlpatters, в которой ищет django
from . import views #чтобы мочь связывать url с нашими представлениями приложения

urlpatterns = [
    path('', views.short, name = "short") ,
    path('wtf/',views.secondview, name='sec'),
    path('extend/',views.extend, name='extend'),
    path('checkmyform/',views.show_unnes_form, name='checkmyform'),
]

'''
path() be like: если клиент переходит по ссылке с
 названием "имя домена " + "ничего", то мы перенаправляем его на представление "short"
 в html (или в Django, я не знаю) будет это представление называться short
'''
