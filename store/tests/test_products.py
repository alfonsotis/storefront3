import pytest
from rest_framework import status


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/',product)
    return do_create_product



@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, create_product):
        response = create_product({
        "title": "a",
        "description": "b",
        "slug": "c",
        "inventory": 2,
        "unit_price": 1,
        "collection": 2
    })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, create_product, authenticate_user):
        authenticate_user(is_staff=False)

        response = create_product({
        "title": "a",
        "description": "b",
        "slug": "c",
        "inventory": 2,
        "unit_price": 1,
        "collection": 2
    })
        
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, create_product, authenticate_user):
        authenticate_user(is_staff=True)

        response = create_product({
            "title": "a",
            "description": "b",
            "slug": "c",
            "inventory": 2,
            "unit_price": 1,
            "collection": 2
        })
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST