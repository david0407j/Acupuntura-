import pytest
from django.urls import reverse

from acupuntura.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:base'))
    return resp


# testes do cabeçalho da página
def test_status_code(resp):
    assert resp.status_code == 200