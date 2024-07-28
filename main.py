# from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import Any
#
#
# class Builder(ABC):
#
#
#     @property
#     @abstractmethod
#     def product(self) -> None:
#         pass
#
#     @abstractmethod
#     def produce_part_a(self) -> None:
#         pass
#
#     @abstractmethod
#     def produce_part_b(self) -> None:
#         pass
#
#     @abstractmethod
#     def produce_part_c(self) -> None:
#         pass
#
#
# class ConcreteBuilder1(Builder):
#
#
#     def __init__(self) -> None:
#
#         self.reset()
#
#     def reset(self) -> None:
#         self._product = Product1()
#
#     @property
#     def product(self) -> Product1:
#
#         product = self._product
#         self.reset()
#         return product
#
#     def produce_part_a(self) -> None:
#         self._product.add("PartA1")
#
#     def produce_part_b(self) -> None:
#         self._product.add("PartB1")
#
#     def produce_part_c(self) -> None:
#         self._product.add("PartC1")
#
#
# class Product1():
#
#
#     def __init__(self) -> None:
#         self.parts = []
#
#     def add(self, part: Any) -> None:
#         self.parts.append(part)
#
#     def list_parts(self) -> None:
#         print(f"Product parts: {', '.join(self.parts)}", end="")
#
#
# class Director:
#
#
#     def __init__(self) -> None:
#         self._builder = None
#
#     @property
#     def builder(self) -> Builder:
#         return self._builder
#
#     @builder.setter
#     def builder(self, builder: Builder) -> None:
#
#         self._builder = builder
#
#
#
#     def build_minimal_viable_product(self) -> None:
#         self.builder.produce_part_a()
#
#     def build_full_featured_product(self) -> None:
#         self.builder.produce_part_a()
#         self.builder.produce_part_b()
#         self.builder.produce_part_c()
#
#
# if __name__ == "_main_":
#
#     director = Director()
#     builder = ConcreteBuilder1()
#     director.builder = builder
#
#     print("Standard basic product: ")
#     director.build_minimal_viable_product()
#     builder.product.list_parts()
#
#     print("\n")
#
#     print("Standard full featured product: ")
#     director.build_full_featured_product()
#     builder.product.list_parts()
#
#     print("\n")
#
#     # Помните, что паттерн Строитель можно использовать без класса Директор.
#     print("Custom product: ")
#     builder.produce_part_a()
#     builder.produce_part_b()
#     builder.product.list_parts()

# class Target:
#     """
#     Целевой класс объявляет интерфейс, с которым может работать клиентский код.
#     """
#
#     def request(self) -> str:
#         return "Target: The default target's behavior."
#
#
# class Adaptee:
#     """
#     Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
#     несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
#     некоторой доработке, прежде чем клиентский код сможет его использовать.
#     """
#
#     def specific_request(self) -> str:
#         return ".eetpadA eht fo roivaheb laicepS"
#
#
# class Adapter(Target, Adaptee):
#     """
#     Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
#     интерфейсом благодаря множественному наследованию.
#     """
#
#     def request(self) -> str:
#         return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"
#
#
# def client_code(target: "Target") -> None:
#     """
#     Клиентский код поддерживает все классы, использующие интерфейс Target.
#     """
#
#     print(target.request(), end="")
#
#
# if __name__ == "__main__":
#     print("Client: I can work just fine with the Target objects:")
#     target = Target()
#     client_code(target)
#     print("\n")
#
#     adaptee = Adaptee()
#     print("Client: The Adaptee class has a weird interface. "
#           "See, I don't understand it:")
#     print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
#
#     print("Client: But I can work with it via the Adapter:")
#     adapter = Adapter()
#     client_code(adapter)

from  abc import ABC, abstractmethod


class Subject(ABC):
    """
    Интерфейс Субъекта объявляет общие операции как для Реального Субъекта, так
    и для Заместителя. Пока клиент работает с Реальным Субъектом, используя этот
    интерфейс, вы сможете передать ему заместителя вместо реального субъекта.
    """

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """
    Реальный Субъект содержит некоторую базовую бизнес-логику. Как правило,
    Реальные Субъекты способны выполнять некоторую полезную работу, которая к
    тому же может быть очень медленной или точной – например, коррекция входных
    данных. Заместитель может решить эти задачи без каких-либо изменений в коде
    Реального Субъекта.
    """

    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):
    """
    Интерфейс Заместителя идентичен интерфейсу Реального Субъекта.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        Наиболее распространёнными областями применения паттерна Заместитель
        являются ленивая загрузка, кэширование, контроль доступа, ведение
        журнала и т.д. Заместитель может выполнить одну из этих задач, а затем,
        в зависимости от результата, передать выполнение одноимённому методу в
        связанном объекте класса Реального Субъекта.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:
    """
    Клиентский код должен работать со всеми объектами (как с реальными, так и
    заместителями) через интерфейс Субъекта, чтобы поддерживать как реальные
    субъекты, так и заместителей. В реальной жизни, однако, клиенты в основном
    работают с реальными субъектами напрямую. В этом случае, для более простой
    реализации паттерна, можно расширить заместителя из класса реального
    субъекта.
    """

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)