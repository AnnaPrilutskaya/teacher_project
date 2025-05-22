from django.shortcuts import render, get_object_or_404
from .models import Recommendations, TestNew
from django.views.generic import DeleteView



def parent(request):
    template = 'parents/parents.html'
    return render(request, template) 

def recommendation(request):
    recommendations = Recommendations.objects.all()
    template = 'parents/recommendation.html'
    return render(request, template, {'list_of_recommendations': recommendations})

'''def test_view(request):
    # 1. Загружаем все вопросы и связанные варианты ответов ОДНИМ запросом
    questions = Question.objects.prefetch_related('options').all()
    
    # 2. Если пользователь отправил форму (POST-запрос)
    if request.method == 'POST':
        form_data = request.POST  # Получаем все данные формы
        total_score = 0  # Общий счёт
        
        # 3. Перебираем все вопросы для подсчёта баллов
        for question in questions:
            # Получаем ID выбранного варианта (например: 'question_1': '3')
            answer_id = form_data.get(f'question_{question.id}')
            
            if answer_id:  # Если ответ был выбран
                # 4. Находим объект AnswerOption по ID
                answer = Answer.objects.get(id=answer_id)
                # Добавляем баллы за ответ к общему счёту
                total_score += answer.points
        
        # 5. Рендерим страницу с результатами
        return render(request, 'parents/result.html', {
            'total_score': total_score,
            # Можно добавить детализацию ответов, если нужно
        })
    
    # 6. Если GET-запрос (первый заход на страницу)
    return render(request, 'parents/test.html', {
        'questions': questions  # Передаём вопросы в шаблон
    })'''

def test_list(request):
    tests = TestNew.objects.all()
    return render(request, 'parents/test_list.html', {'tests': tests})

def test_view(request, test_id):
    test = get_object_or_404(TestNew.objects.prefetch_related('questions__options'), id=test_id)
    
    if request.method == 'POST':  #если пользователь отправил форму
        total_score = 0
        for question in test.questions.all(): #проходим по всем вопросам
            answer_id = request.POST.get(f'question_{question.id}') # Получаем ID выбранного варианта
            if answer_id:
                answer = question.options.get(id=answer_id)
                total_score += answer.points
        # Переносим логику определения результата сюда
        result = next(
            (c.result_text for c in test.criteria.all() 
             if c.min_score <= total_score <= c.max_score),
            "Результат не определён"
        )
        return render(request, 'parents/result.html', {
            'test': test,
            'total_score': total_score,
            'result': result
        })
    
    return render(request, 'parents/test.html', {'test': test})
    
