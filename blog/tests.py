from django.test import TestCase, Client
from django.urls import reverse
from .models import Blog

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Создаем запись, у которой точно есть поле title
        self.blog = Blog.objects.create(
            title="Тестовая статья"
        )

    # 5 вариантов проверок для List и Detail 

    def test_1_list_view_status_code(self):
        """1. Проверка доступности списка статей (Код 200)"""
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)

    def test_2_list_view_contains_title(self):
        """2. Проверка наличия заголовка статьи в списке"""
        response = self.client.get(reverse('blog_list'))
        self.assertContains(response, "Тестовая статья")

    def test_3_detail_view_status_code(self):
        """3. Проверка доступности детальной страницы статьи (Код 200)"""
        response = self.client.get(reverse('blog_detail', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)

    def test_4_detail_view_contains_id_and_content(self):
        """4. Проверка получения правильного заголовка на детальной странице"""
        response = self.client.get(reverse('blog_detail', args=[self.blog.id]))
        self.assertContains(response, "Тестовая статья")

    def test_5_detail_view_not_found(self):
        """5. Проверка перехода по несуществующему ID (Код 404)"""
        response = self.client.get(reverse('blog_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)

    # Учет популярности (лайков) 

    def test_initial_likes_is_zero(self):
        """Проверка: у нового блога количество лайков изначально равно нулю"""
        new_blog = Blog.objects.create(title="Новый блог")
        self.assertEqual(new_blog.likes, 0)

    def test_likes_increment_on_detail_request(self):
        """Проверка: GET-запрос к детальной странице увеличивает лайки на 1"""
        self.client.get(reverse('blog_detail', args=[self.blog.id]))
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.likes, 1)