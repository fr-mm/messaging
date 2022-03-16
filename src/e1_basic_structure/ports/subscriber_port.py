from abc import ABC, abstractmethod

from src.e1_basic_structure.ports.message_port import MessagePort
from src.e1_basic_structure.value_objects import SubscriberId


class SubscriberPort(ABC):
    @abstractmethod
    def update(self, message: MessagePort) -> None:
        pass

    @property
    @abstractmethod
    def id(self) -> SubscriberId:
        pass
