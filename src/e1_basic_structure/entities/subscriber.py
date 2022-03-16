from src.e1_basic_structure.ports import SubscriberPort, MessagePort
from src.e1_basic_structure.value_objects import SubscriberId


class Subscriber(SubscriberPort):
    __id: SubscriberId

    def __init__(self) -> None:
        self.__id = SubscriberId()

    def update(self, message: MessagePort) -> None:
        print(f'Subscriber {self.__id} has been updated')

    @property
    def id(self) -> SubscriberId:
        return self.__id
