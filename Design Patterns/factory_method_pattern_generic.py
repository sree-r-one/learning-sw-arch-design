from abc import ABC, abstractmethod


class Product(ABC):
    """
    Product interface declares the operations that all concrete products must implement
    """

    @abstractmethod
    def operation(self) -> str:
        """
        Operation method that all concrete products must implement
        """
        pass


class ConcreteProduct1(Product):
    """
    ConcreteProduct1 is a concrete product that implements the Product interface
    """

    def operation(self) -> str:
        return "Result of ConcreteProduct1"


class ConcreteProduct2(Product):
    """
    ConcreteProduct2 is a concrete product that implements the Product interface
    """

    def operation(self) -> str:
        return "Result of ConcreteProduct2"


class Creator(ABC):
    """
    Creator class declares the factory method that returns a new product object
    """

    @abstractmethod
    def factory_method(self) -> Product:
        """
        Factory method that returns a new product object
        """
        pass

    def some_operation(self) -> str:
        """
        Some operation that uses the factory method to create a product object
        """
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class ConcreteCreator1(Creator):
    """
    ConcreteCreator1 is a concrete creator that implements the Creator interface
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    """
    ConcreteCreator2 is a concrete creator that implements the Creator interface
    """

    def factory_method(self) -> Product:
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:
    """
    Client code that uses the creator object to create a product object
    """
    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n{creator.some_operation()}",
        end="",
    )


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
    print("\n")
