from django.contrib import admin
from django.db.models import fields

# Register your models here.
from polls.models import Question, Choice

#class QuestionAdmin(admin.ModelAdmin): # 필드 순서 변경
    #fields = ['pub_date','question_text'] 
'''
class QuestionAdmin(admin.ModelAdmin): #필드를 분리해서 보여주기
    fieldsets = [ #첫번째 인자가 해당 필드의 제목
        ('Question Statement',{'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date'],'classes':['collapse']}), #collapse:필드 접기
    ]
'''
'''
class ChoiceInline(admin.StackedInline): #스택형태로 보여주기
    model = Choice
    extra = 2
'''
class ChoiceInline(admin.TabularInline): #테이블 형태로 보여주기
    model=Choice
    extra=2


class QuestionAdmin(admin.ModelAdmin): 
    fieldsets = [ 
        (None,              {'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date'],'classes':['collapse']}), #collapse:필드 접기
    ]
    inlines=[ChoiceInline] #Choice 모델 클래스 같이 보기
    list_display = ('question_text','pub_date') #레코드 리스트 칼럼 지정 / date published
    list_filter = ['pub_date'] #필터 사이드바 추가 / 날짜기준 정렬 / 장고에서 알아서 지원
    search_fields = ['question_text'] #검색박스 추가


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

