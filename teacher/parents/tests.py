from django.test import TestCase  
from .models import Recommendations  
from django.urls import reverse 

class RecommendationModelTest(TestCase):  
    def setUp(self):  
        # Подготовка данных перед каждым тестом  
        self.recommendation = Recommendations.objects.create(  
            title="Заголовок",  
            content="Содержание"  
        )  

    def test_post_creation(self):  
        """Проверяем, что пост создается корректно."""  
        self.assertEqual(self.recommendation.title, "Заголовок")  
        self.assertEqual(self.recommendation.content, "Содержание")   

    def test_str_method(self):  
        """Проверяем __str__ модели."""  
        self.assertEqual(str(self.recommendation), "Заголовок")  

class RecommendationListViewTest(TestCase):  
    def setUp(self):  
        # Создаем объект модели Recommendations
        self.precommendationost = Recommendations.objects.create(title="Заголовок", content="Содержание")  

    def test_view_url_exists(self):  
        """Проверяем, что URL работает."""  
        response = self.client.get(reverse("recommendation"))  
        self.assertEqual(response.status_code, 200)  

    def test_view_uses_correct_template(self):  
        """Проверяем, что используется правильный шаблон."""  
        response = self.client.get(reverse("recommendation"))  
        self.assertTemplateUsed(response, "parents/recommendation.html")  

    def test_view_contains_post(self):  
        """Проверяем, что пост отображается на странице."""  
        response = self.client.get(reverse("recommendation"))  
        self.assertContains(response, "Содержание") 