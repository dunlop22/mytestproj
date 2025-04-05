import pytest
from django.urls import reverse
from django.test import Client
from .models import ModelAuto, Kuzov, Marka

@pytest.fixture
def client():
    """Фикстура для создания клиента Django"""
    return Client()

@pytest.fixture
def create_modelauto():
    kuzov = Kuzov.objects.create(tipkuzova="Sedan")
    marka = Marka.objects.create(naim="Toyota")
    model = ModelAuto.objects.create(
        naimenovanie="Toyota Corolla",
        kuzov=kuzov,
        marka=marka,
        price="15000",
        clirens=15.5,
        shirina=1.8,
        visota=1.45,
        dlina=4.3
    )
    return model

def test_model_index(client):
    """Тестирование главной страницы"""
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert 'eXCar' in response.content.decode()

@pytest.mark.django_db
def test_model_catalog(client, create_modelauto):
    """Тестирование каталога авто"""
    response = client.get(reverse('catalog'))
    assert response.status_code == 200
    assert 'Toyota Corolla' in response.content.decode()

@pytest.mark.django_db
def test_model_show(client, create_modelauto):
    """Тестирование страницы отображения авто"""
    model = create_modelauto
    response = client.get(reverse('show', args=[model.pk]))
    assert response.status_code == 200
    assert model.naimenovanie in response.content.decode()

@pytest.mark.django_db
def test_model_create(client):
    """Тестирование создания нового автомобиля"""
    kuzov = Kuzov.objects.create(tipkuzova="Coupe")
    marka = Marka.objects.create(naim="BMW")
    data = {
        'naimenovanie': 'BMW M3',
        'kuzov': kuzov.id,
        'marka': marka.id,
        'price': '50000',
        'clirens': 13.5,
        'shirina': 1.85,
        'visota': 1.4,
        'dlina': 4.5
    }
    response = client.post(reverse('new'), data)
    assert response.status_code == 302  # Ожидаем редирект на каталог
    assert ModelAuto.objects.count() == 0  # Убедимся, что объект сохранен
