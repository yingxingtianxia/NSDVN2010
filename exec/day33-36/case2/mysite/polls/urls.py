from django.urls import path
from polls import views

urlpatterns = [
    #匹配http://x.x.x.x/polls/
    path('', views.index,name='index')
]
