import pytest
from tests.modelss import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()  # Создание экземпляра Cart


class TestProducts:

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        product.buy(1)
        assert product.quantity == 999

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    def test_add_product(self, cart, product):
        cart.add_product(product, 1)  # Добавление продукта в корзину
        assert cart.products[product] == 1
        cart.add_product(product, 1)
        assert cart.products[product] == 2

    def test_remove_product(self, cart, product):
        cart.add_product(product, 2)  # Сначала добавим продукт в корзину
        cart.remove_product(product, 1)  # Затем удалим один продукт
        assert cart.products[product] == 1
        cart.remove_product(product, 1)
        assert product not in cart.products

    def test_clear(self, cart, product):
        cart.add_product(product, 1)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self,cart,product):
        cart.add_product(product, 4)
        assert cart.get_total_price() == 400

    def test_buy(self, cart, product):
        cart.add_product(product, 5)
        cart.buy()
        assert product.quantity == 995
        assert len(cart.products) == 0

    def test_buy_insufficient_stock(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()