from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from Restaurant.models.beverage import Beverage
from Restaurant.models.dish import Dish
from Restaurant.models.category import Category
from django.core.files.uploadedfile import SimpleUploadedFile


class AdminPanelTests(TestCase):
    def setUp(self):
        # Створюємо суперкористувача
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='adminpass'
        )
        self.client.login(username='admin', password='adminpass')

        # Тестова категорія
        self.category = Category.objects.create(
            name="Напої", slug="napoi"
        )

    def test_admin_beverage_add(self):
        url = reverse("admin:beverage_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        photo = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")

        response = self.client.post(url, {
            'name': 'Кола',
            'slug': 'kola',
            'price': '25.00',
            'is_visible': True,
            'description': 'Газований напій',
            'volume': '0.5',
            'is_alcoholic': False,
            'ingredients': 'Вода, цукор, кофеїн',
            'photo': photo,
            'category': self.category.pk,
            'sort': 1,
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Beverage.objects.filter(name='Кола').exists())

    def test_admin_dish_list_view(self):
        # Додаємо страву
        Dish.objects.create(
            name='Суші',
            slug='sushi',
            price='120.00',
            is_visible=True,
            description='Смачні суші',
            weight='250',
            ingredients='Рис, риба',
            photo=SimpleUploadedFile("sushi.jpg", b"file_content", content_type="image/jpeg"),
            category=self.category,
            sort=1,
            is_vegetarian=False,
            is_spicy=True,
            cuisine_type='Японська'
        )

        url = reverse("admin:Restaurant_dish_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Суші")

    def test_admin_category_change(self):
        url = reverse("admin:Restaurant_category_change", args=[self.category.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Напої")

    def test_admin_category_delete(self):
        url = reverse("admin:Restaurant_category_delete", args=[self.category.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        post_response = self.client.post(url, {'post': 'yes'}, follow=True)
        self.assertEqual(post_response.status_code, 200)
        self.assertFalse(Category.objects.filter(pk=self.category.pk).exists())

    def test_admin_dish_add(self):
        url = reverse("admin:Restaurant_dish_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        photo = SimpleUploadedFile("dish.jpg", b"file_content", content_type="image/jpeg")

        response = self.client.post(url, {
            'name': 'Піца',
            'slug': 'pizza',
            'price': '150.00',
            'is_visible': True,
            'description': 'Смачна піца',
            'weight': '300',
            'ingredients': 'Тісто, сир, томати',
            'photo': photo,
            'category': self.category.pk,
            'sort': 2,
            'is_vegetarian': False,
            'is_spicy': False,
            'cuisine_type': 'Італійська'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Dish.objects.filter(name='Піца').exists())

    def test_admin_beverage_change(self):
        beverage = Beverage.objects.create(
            name='Пепсі',
            slug='pepsi',
            price='20.00',
            is_visible=True,
            description='Газований напій',
            volume='0.5',
            is_alcoholic=False,
            ingredients='Вода, цукор, кофеїн',
            category=self.category,
            sort=1,
        )

        url = reverse("admin:Restaurant_beverage_change", args=[beverage.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(url, {
            'name': 'Пепсі Лайт',
            'slug': 'pepsi-light',
            'price': '22.00',
            'is_visible': True,
            'description': 'Газований напій без цукру',
            'volume': '0.5',
            'is_alcoholic': False,
            'ingredients': 'Вода, підсолоджувачі, кофеїн',
            'category': self.category.pk,
            'sort': 1,
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        beverage.refresh_from_db()
        self.assertEqual(beverage.name, 'Пепсі Лайт')
        self.assertEqual(beverage.price, 22.00)

    def test_admin_dish_delete(self):
        dish = Dish.objects.create(
            name='Борщ',
            slug='borsch',
            price='80.00',
            is_visible=True,
            description='Традиційний український борщ',
            weight='350',
            ingredients="Буряк, капуста, м'ясо",
            category=self.category,
            sort=3,
            is_vegetarian=False,
            is_spicy=False,
            cuisine_type='Українська'
        )

        url = reverse("admin:Restaurant_dish_delete", args=[dish.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        post_response = self.client.post(url, {'post': 'yes'}, follow=True)
        self.assertEqual(post_response.status_code, 200)
        self.assertFalse(Dish.objects.filter(pk=dish.pk).exists())

    def test_admin_access_without_login(self):
        self.client.logout()
        url = reverse("admin:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertIn('/admin/login/', response.url)
