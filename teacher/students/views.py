from django.shortcuts import render
from .models import Articles, Memos, Recommendations
from django.views.generic import DeleteView
from .utils import generate_problem, set_difficulty
from django.http import JsonResponse

def index(request):
    template = 'students/index.html'
    return render(request, template) 

def student(request):
    for_students = Articles.objects.all()
    mem = Memos.objects.all()
    recom = Recommendations.objects.all()
    template = 'students/student.html'
    return render(request, template, {'article': for_students, 'new_mem': mem, 'new_recom': recom}) 

class ForStudentView(DeleteView):
    model = Articles
    template_name= 'students/detail.html'
    context_object_name = 'article'

def memo(request):
    memos = Memos.objects.all()
    template = 'students/memo.html'
    return render(request, template, {'list_of_memos': memos}) 

def recommendation(request):
    recommendations = Recommendations.objects.all()
    template = 'students/recommendation.html'
    return render(request, template, {'list_of_recommendations': recommendations})

# Главная страница с примером
def math_game(request):
    # Получаем уровень сложности из GET-параметра или используем текущий
    current_difficulty = 'first_class' # если честно, не понимаю, как это работает. по идее должно работать
                                        # и без этой строки, но без нее не работает. говорит, что я ссылаюсь
                                        # на эту переменную не определив ее. хотя она вроде как глобальная...
    difficulty = request.GET.get('difficulty', current_difficulty)
    
    # Устанавливаем новую сложность, если она передана
    if difficulty != current_difficulty:
        current_difficulty = set_difficulty(difficulty)

    # Проверяем, что сложность из допустимых значений
    #valid_difficulties = ['first_class', 'second_class', 'third_class', 'forth_class']
    #if difficulty not in valid_difficulties:
     #   difficulty = 'first_class'  # Значение по умолчанию, если прислали что-то странное

    
    
    problem, correct_answer = generate_problem()
    return render(request, 'students/game.html', {
        'problem': problem,
        'initial_correct_answer': correct_answer,  
        'current_difficulty': current_difficulty  # Передаем в шаблон
    })

# Проверка ответа (AJAX)
def check_answer(request):
    
    if request.method == 'POST':
        user_answer = int(request.POST.get('answer', 0))
        correct_answer = int(request.POST.get('correct_answer'))
        is_correct = (user_answer == correct_answer)


        return JsonResponse({
            'is_correct': is_correct,
            'correct_answer': correct_answer,
        })

# Генерация нового примера (AJAX)
def get_new_problem(request):
    problem, correct_answer = generate_problem()
    return JsonResponse({
        'problem': problem,
        'correct_answer': correct_answer,
    })
