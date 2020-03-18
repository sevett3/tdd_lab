import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38


# Owner: Tommy Evett
# Test finding the most expensive product price
def test_CanCalculateMostExpensiveProductPrice(invoice, products):
    invoice.mostExpensiveProductPrice(products)
    assert invoice.mostExpensiveProductPrice(products) == 7.5


# Owner: Tommy Evett
# Test calculating the average impure price
def test_CanCalculateAverageImpurePrice(invoice, products):
    invoice.averageImpurePrice(products)
    assert invoice.averageImpurePrice(products) == 5
