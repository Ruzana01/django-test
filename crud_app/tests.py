from django.test import TestCase, Client
from django.urls import reverse
from .models import Item


class ItemCRUDTestCase(TestCase):
    def setUp(self):
        # Создаем тестового клиента для эмуляции запросов из браузера
        self.client = Client()
        # Создаем тестовую запись в базе данных
        self.item = Item.objects.create(
            title="Тестовый заголовок",
            content="Тестовое описание"
        )

    # 1. Тест READ (Просмотр списка элементов)
    def test_item_list_view(self):
        response = self.client.get(reverse('item_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовый заголовок")

    # 2. Тест CREATE (Создание элемента)
    def test_item_create_view(self):
        response = self.client.post(reverse('item_create'), {
            'title': 'Новый элемент',
            'content': 'Описание нового элемента'
        })
        # Проверяем перенаправление (редирект) после создания
        self.assertEqual(response.status_code, 302)
        # Проверяем, что объект действительно появился в базе данных
        self.assertTrue(Item.objects.filter(title='Новый элемент').exists())

    # 3. Тест DELETE (Удаление элемента)
    def test_item_delete_view(self):
        response = self.client.post(reverse('item_delete', args=[self.item.pk]))
        self.assertEqual(response.status_code, 302)
        # Проверяем, что объект удален из базы данных
        self.assertFalse(Item.objects.filter(pk=self.item.pk).exists())

    # 4. Тест EXPORT WORD (Скачивание Word-документа)
    def test_export_tests_to_word_view(self):
        response = self.client.get(reverse('export_tests'))
        self.assertEqual(response.status_code, 200)
        # Проверяем заголовки ответа (что отдается docx файл)
        self.assertIn('attachment; filename="django_tests_report.docx"', response['Content-Disposition'])
        self.assertEqual(
            response['Content-Type'],
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )