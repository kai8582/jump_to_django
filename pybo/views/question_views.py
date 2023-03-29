from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from ..forms import QuestionForm
from ..models import Question

@login_required(login_url="common:login")
def question_create(request):
    if request.method=='POST':
        form=QuestionForm(request.POST)
        #post request를 받으면 request.POST를 argument로 subject,content 값이 QuestionForm의 subject,content속성에 저장되어 객체가 생성된다
        if form.is_valid():
            question=form.save(commit=False)
            question.author=request.user
            question.create_date=timezone.now()
            question.save()
            return redirect("pybo:index")
        else:
            context={'form':form}
            return render(request,'pybo/question_form.html',context)
    
    else:
        form=QuestionForm()
        context={'form':form}
        return render(request, 'pybo/question_form.html',context)    
 
 
@login_required(login_url="common:login")
def question_modify(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    if request.user != question.author:
        messages.error(request,'수정권한이 없습니다')
        return redirect('pybo:detail',question_id=question.id)
    if request.method=='POST':
        form=QuestionForm(request.POST,instance=question)
        if form.is_valid():
            question=form.save(commit=False)
            question.modify_date=timezone.now()
            question.save()
            return redirect('pybo:detail',question_id=question.id)
        else:
            form=QuestionForm(request.POST)
            context={"form":form}
            return render(request,'pybo/question_form.html',context)
    else:
        form=QuestionForm(instance=question)
        context={'form':form}
        return render(request,'pybo/question_form.html',context)

@login_required(login_url="common:login")
def question_delete(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    if request.user != question.author:
        messages.error(request,'삭제권한이 없습니다')
        return redirect('pybo:detail',question_id=question.id)
    else:
        question.delete()
        return redirect('pybo:index')
    
@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)