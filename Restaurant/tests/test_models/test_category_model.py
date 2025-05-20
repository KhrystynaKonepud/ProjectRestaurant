import pytest
from Restaurant.models.category import Category

@pytest.mark.django_db
def test_category_str():
    cat = Category.objects.create(name="Салати", slug="salaty")
    assert str(cat) == "Салати"
