"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        начало очереди - слева (первый индекс списка)
        конец очереди - справа (последний индекс списка)
        """
        self.queue = []

    def enqueue(self, elem: Any) -> None:
        """
        Операция добавления элемента в конец очереди.
        :param elem: элемент, который следует добавить в очередь
        :return: None
        """
        self.queue.insert(0, elem)
        return None

    def dequeue(self) -> Any:
        """
        Вернуть элемент с начала очереди. Следует вернуть None, если элемента нет.
        :return: Снятый с начала очереди элемент
        """
        if len(self.queue) == 0:
            return None

        value = self.queue.pop(len(self.queue)-1)
        return value

    def peek(self, ind: int = 0) -> Any:
        """
        Метод позволяет вам увидеть элемент в очереди, не удаляя его из очереди
        :param ind: индекс элемента с начала очереди
        :return: Просмотренный элемент
        """
        if ind < 0 or ind > len(self.queue):
            return None

        value = self.queue[ind]
        return value

    def clear(self) -> None:
        """ Очистить очередь. """
        if len(self.queue) == 0:
            return None

        self.queue.clear()
        return None
