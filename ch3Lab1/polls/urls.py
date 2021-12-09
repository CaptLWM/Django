from django.urls import path
from polls import views

# mysite->urls.py를 통해 polls 들어오면
app_name = 'polls'
urlpatterns = [ #polls 뒤에 오는 항목에 따라 해당 html로 이동
    path('', views.index, name='index'), # /polls/ view 안에 있는 idex함수 호출 / 
    path('<int:question_id>/', views.detail, name='detail'), # /polls/5/
    path('<int:question_id>/results/', views.results, name='results'), # /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # /polls/5/vote/
]   