from django.http import HttpResponse
from django.shortcuts import render


from . import models



def index(request):
    latest_question_list = models.Question.objects.order_by()
    print(latest_question_list)
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



def register_user(requsert):
    if requsert.method=='post':
        nickName=requsert.POST.get('nickname')
        phoneNumber = requsert.POST.get('phoneNumber')
        username = requsert.POST.get('username')
        sex = requsert.POST.get('sex')
        age=requsert.POST.get('age')
        password = requsert.POST.get('password')

        models.User.phoneNumber=phoneNumber
        models.User.username=username
        models.User.password=password
        models.User.sex=sex
        models.User.nickName=nickName
        models.User.nickName=age