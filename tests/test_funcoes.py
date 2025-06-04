import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import funcoes

@pytest.fixture(autouse=True)
def patch_dependencies(monkeypatch):
    # Simplify money formatting and reset caixa value
    monkeypatch.setattr(funcoes, "formatar_dinheiro", lambda v: f"R$ {v:.2f}")
    funcoes.valor_caixa = 0


def test_post_adiciona_valor():
    resultado = funcoes.requests_caixa(valor=10, request='post')
    assert resultado == "Valor de R$ 10.00 adicionado ao caixa. Total: R$ 10.00"
    assert funcoes.valor_caixa == 10


def test_get_retorna_valor_atual():
    funcoes.valor_caixa = 50
    resultado = funcoes.requests_caixa(request='get')
    assert resultado == "Valor atual do caixa: R$ 50.00"


def test_remove_valor():
    funcoes.valor_caixa = 100
    resultado = funcoes.requests_caixa(valor=40, request='remove')
    assert resultado == "Valor de R$ 40.00 removido do caixa. Total: R$ 60.00"
    assert funcoes.valor_caixa == 60
