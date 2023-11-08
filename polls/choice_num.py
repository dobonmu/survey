from .models import Question, Choice, Open_answer, User, UserResponse

class choice_num:
    def choice_num(choice_id):
        choice = Choice.objects.get(pk=choice_id)
        question_id = choice.question_id
        choice_list=list(Choice.objects.filter(question_id=question_id).values_list('id', flat=True))
        for i in range(len(choice_list)):
            if choice_list[i]==choice_id:
                return i+1