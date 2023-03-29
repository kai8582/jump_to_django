from django.contrib import admin
from .models import Question, Answer, test

# Register your models here.


admin.site.register(Answer)

#제목(subject)로 질문 데이터 검색해보기
class QuestionAdmin(admin.ModelAdmin):
    search_fields=["subject"]
    
admin.site.register(Question,QuestionAdmin)

admin.site.register(test)