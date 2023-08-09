from decimal import Decimal
import pytest
from rest_framework import status
from model_bakery import baker
from store.models import Collection, Product


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, create_product):
        response = create_product({
            "title": "a",
            "description": "b",
            "slug": "-",
            "inventory": 2,
            "unit_price": 1,
            "collection": 2
        })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, create_product, authenticate_user):
        authenticate_user(is_staff=False)
        collection = baker.make(Collection)

        response = create_product({
            "title": "a",
            "description": "b",
            "slug": "-",
            "inventory": 2,
            "unit_price": 1,
            "collection": collection.id
        })

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, create_product, authenticate_user):
        authenticate_user(is_staff=True)

        response = create_product({
            "description": "b",
            "slug": "-",
            "inventory": 2,
            "unit_price": 1,
            "collection": 2
        })

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_data_is_valid_returns_201(self, create_product, authenticate_user):
        authenticate_user(is_staff=True)
        collection = baker.make(Collection)

        response = create_product({
            "title": "Sample Product",
            "description": "This is a sample product.",
            "slug": "sample-product",
            "inventory": 10,
            "unit_price": 9.99,
            "collection": collection.id
        })

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] is not None


@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_product_exists_returns_200(self, api_client):
        collection = baker.make(Collection)
        product = baker.make(Product, collection=collection)

        response = api_client.get(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': product.id,
            'title': product.title,
            'description': product.description,
            'slug': product.slug,
            'inventory': product.inventory,
            'unit_price': product.unit_price,
            'collection': collection.id,
            'images': [],
            'price_with_tax': product.unit_price * Decimal(1.1)
        }