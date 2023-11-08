from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.contrib import messages
import pandas as pd
import os

from .models import Question, Choice, Open_answer, User, UserResponse
from .random_photo import RandomPhoto
from .choice_num import choice_num
def index(request):
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    file_paths=RandomPhoto.get_photo_paths()
    r_photo_1,r_photo_2= RandomPhoto.choose(file_paths)
    context={'question': question, 'r_photo_1':r_photo_1, 'r_photo_2':r_photo_2}
    choices = Choice.objects.filter(question=question)
    if not choices:
        return render(request, 'polls/answer.html', context)
    else:
        return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question=question)
    if not choices:
        user_answers = Open_answer.objects.filter(question=question)
        return render(request, 'polls/answer_results.html', {'question': question,'user_answers': user_answers})
    else:
        return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question=question)
    if not choices:
        if request.method == 'POST':
            submitted_answer = request.POST.get('choice_text')
            open_answer_obj = Open_answer.objects.create(
                question=question,
                user_answer=submitted_answer
            )
            open_answer_obj.save()
            return render(request, 'polls/end.html')
        else:
            return render(request, 'polls/answer.html')
    else:
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            file_paths=RandomPhoto.get_photo_paths()
            r_photo_1,r_photo_2= RandomPhoto.choose(file_paths)
            context={'question': question, 'r_photo_1':r_photo_1, 'r_photo_2':r_photo_2,'error_message': "You didn't select a choice."}
            return render(request, 'polls/detail.html', context)
        else:

            selected_choice.votes += 1
            selected_choice.save()
        
        next_question_id = question_id + 1
        try:
            next_question = Question.objects.get(pk=next_question_id)
        except Question.DoesNotExist:
            return render(request, 'polls/end.html')
        
        return HttpResponseRedirect(reverse('polls:detail', args=(next_question_id,)))
    
def test(request):
    open_question_id_list=[13,19]
    open_question_list=[]
    for question_id in open_question_id_list:
        question = get_object_or_404(Question, pk=question_id)
        open_question_list.append(question)
    question_id_list=[20,21,22,16,17,18]
    question_list=[]
    randomPhoto=RandomPhoto()
    photo_list=randomPhoto.get_photo_paths()
    r_photo_1,r_photo_2=RandomPhoto.choose(photo_list)
    for question_id in question_id_list:
        question = get_object_or_404(Question, pk=question_id)
        question.photo_1=r_photo_1
        question.photo_2=r_photo_2
        question_list.append(question)
    context={'open_question_list':open_question_list,'question_list':question_list,'r_photo_1':r_photo_1,'r_photo_2':r_photo_2}
    return render(request,'polls/test.html', context)


# def test(request):
#     question_list=[13,16,17,18]
#     question_object_list=[]
#     for i in range(len(question_list)):
#         question_id=question_list[i]
#         question = get_object_or_404(Question, pk=question_id)
#         choices = Choice.objects.filter(question=question_id)
#         if not choices:
#             pass
#         else:
#             file_paths=RandomPhoto.get_photo_paths()
#             r_photo_1,r_photo_2= RandomPhoto.choose(file_paths)
#             question.photo_1=r_photo_1
#             question.photo_2=r_photo_2
#         question_object_list.append(question)
#     context={'question_list':question_object_list}
#     return render(request, 'polls/test_1.html', context)

# def test_vote(request):
#     if request.method == 'POST':
#         open_question_list = [13, 19]
#         question_list =[16,17,18]
#         for question_id in open_question_list:
#             choice_text = request.POST.get('choice_text', None)
#             question=get_object_or_404(Question, pk=question_id)
#             open_answer_obj = Open_answer.objects.create(
#                     question=question,
#                     user_answer=choice_text
#                 )
#             open_answer_obj.save()


#             question_id = question.id
#             selected_choice_id = request.POST.get(f'choice_{question_id}', None)
#             choice_text = request.POST.get('choice_text', None)

#             if selected_choice_id:
#                 
#                 selected_choice = get_object_or_404(Choice, pk=selected_choice_id)
#                 selected_choice.votes += 1
#                 selected_choice.save()
#             else:
#                 open_answer_obj = Open_answer.objects.create(
#                     question=question,
#                     user_answer=choice_text
#                 )
#                 open_answer_obj.save()

#         return redirect('polls:test')  
#     else:
#         return redirect('polls:test')  
    
def test_vote(request):
    question_id_list=[16,17,18]
    question_list=[]
    df=pd.DataFrame()
    df = df.reset_index()
    for questoin_id in question_id_list:
        question=get_object_or_404(Question, pk=questoin_id)
        question_list.append(question)
    if request.method == 'POST':
        name = request.POST.get('choice_text_13', None)
        phone_num = request.POST.get('choice_text_19', None)
        gender_choice =  request.POST.get('choice_20', None)
        gender=choice_num.choice_num(int(gender_choice))
        age_choice =  request.POST.get('choice_21', None)
        age=choice_num.choice_num(int(age_choice))
        earing_choice =  request.POST.get('choice_22', None)
        earing=choice_num.choice_num(int(earing_choice))
        r_photo_1 = request.POST.get('r_photo_1', None)
        r_photo_2 = request.POST.get('r_photo_2', None)
        choice_list=[]
        user = User.objects.create(
                     name=name,
                     phone_num=phone_num,
                     gender=gender,
                     age=age,
                     earing=earing,
                     photo_1=r_photo_1,
                     photo_2=r_photo_2
                 )
        data = {
        'name': [user.name],
        'phone_num': [user.phone_num],
        'gender': [int(user.gender)],
        'age': [int(user.age)],
        'earing': [int(user.earing)],
        'photo_1': [user.photo_1],
        'photo_2': [user.photo_2]
    }

        new_row = pd.DataFrame(data)

        df = pd.concat([df, new_row], ignore_index=True)
        # df = df.append({
        #     'name': user.name,
        #     'phone_num': user.phone_num,
        #     'gender': int(user.gender),
        #     'age': int(user.age),
        #     'earing': int(user.earing),
        #     'photo_1': user.photo_1,
        #     'photo_2': user.photo_2
        # }, ignore_index=True)
        for question_id in question_id_list:
            question=Question.objects.get(pk=question_id)
            choice = request.POST.get(f'choice_{question_id}', None)
            choice_list.append(choice)
            selected_choice = Choice.objects.get(pk=choice).__str__()
            userResponse=UserResponse(user=user,question=question,selected_answer=int(selected_choice))
            df[str(question_id)]=[selected_choice]
        #     data = {
        #     str(question_id): [selected_choice]
        # }

        #     new_row = pd.DataFrame(data)

        #     df = pd.concat([df, new_row], ignore_index=True)


            # df=df.append({
            #     str(question_id):selected_choice
            # },ignore_index=True)
            userResponse.save()
        file_name = f'{user.name}_{user.phone_num}.csv'
        new_file_name = get_incremented_filename(file_name)
        df.to_csv(new_file_name, index=False, encoding='utf-8')
        return render(request, 'polls/end.html')
        
def get_incremented_filename(file_name):
    base, ext = os.path.splitext(file_name)
    if not os.path.exists(file_name):
        return file_name

    file_counter = 1
    while True:
        incremented_name = f"{base}_{file_counter}{ext}"
        if not os.path.exists(incremented_name):
            return incremented_name
        file_counter += 1

    

def test_result(request):
    user_responses = UserResponse.objects.select_related('user').all()
    return render(request, 'polls/test_results.html', {'user_responses': user_responses})

# def result_download(request):
