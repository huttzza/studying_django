from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

def index(request):
    #return HttpResponse("안녕하세요 pybo에 오셨끈여!")
    """
    pybo 목록 출력
    """
    page = request.GET.get('page','1')

    question_list = Question.objects.order_by('-create_date')#작성일자 역순으로

    paginator = Paginator(question_list, 10) #페이지당 10개씩
    page_obj = paginator.get_page(page)

    context = {'question_list':page_obj}
    return render(request,'pybo/question_list.html',context)

def detail(request, question_id) :
    """
    pybo 내용 출력
    """
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id) 
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html',context)

def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    
    """
    #request에 textarea에 입력된 데이터가 넘어옴
    question.answer_set.create(content=request.POST.get('content'),create_date=timezone.now())
    # request.POST.get('content')는 POST 형식으로 전송된 form 데이터 항목 중 name이 content인 값을 의미
    """

    """
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    이렇게 할 수도 있음
    """
    """
    #이동할 페이지 별칭, 해당 URL에 전달해야 하는 값
    return redirect('pybo:detail',question_id=question.id)
    """
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form=AnswerForm()
    context = {'question':question, 'form':form}
    return render(request, 'pybo/question_detail.html',context)

def question_create(request):
    """
    pybo 질문 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form':form}

    return render(request, 'pybo/question_form.html',context)