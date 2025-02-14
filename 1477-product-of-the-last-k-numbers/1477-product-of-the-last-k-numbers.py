class ProductOfNumbers:
    def __init__(self):
        self.prefix_products = [1]  # Store prefix products, starting with 1

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]  # Reset the prefix product list on zero
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_products):
            return 0  # If k extends beyond the last reset point (zero encountered), return 0
        return self.prefix_products[-1] // self.prefix_products[-k - 1]
