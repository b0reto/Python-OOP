from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, poduct_name):
        p = self.find(poduct_name)
        if p:
            self.products.remove(p)

    def __repr__(self):
        result = [f'{p.name}: {p.quantity}' for p in self.products]
        return '\n'.join(result)