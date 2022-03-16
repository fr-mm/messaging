from typing import Dict, List

from src.e1_basic_structure.ports import SubscriberPort, MessagePort
from src.e1_basic_structure.value_objects import SubscriberId


class Publisher:
    __subscribers: Dict[SubscriberId, SubscriberPort]

    def __init__(self) -> None:
        self.__subscribers = {}

    def subscribe(self, subscriber: SubscriberPort) -> None:
        self.__subscribers[subscriber.id] = subscriber

    def unsubscribe(self, subscriber_id: SubscriberId) -> None:
        del self.__subscribers[subscriber_id]

    def publish(self, message: MessagePort) -> None:
        [subscriber.update(message) for subscriber in self.__subscribers.values()]

    @property
    def subscribers(self) -> List[SubscriberPort]:
        return [subscriber for subscriber in self.__subscribers.values()]
