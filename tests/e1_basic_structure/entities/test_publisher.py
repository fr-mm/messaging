from unittest import TestCase
from mockito import when, verify

from src.e1_basic_structure.entities import Publisher, Subscriber, Message


class TestPublisher(TestCase):
    def test_subscribe_WHEN_subscriber_given_THEN_subscribes_subscriber(self) -> None:
        publisher = Publisher()
        subscriber = Subscriber()

        publisher.subscribe(subscriber)

        expected_subscribers = [subscriber]
        self.assertEqual(expected_subscribers, publisher.subscribers)

    def test_unsubscribe_WHEN_subscriber_id_given_THEN_unsubscribes_subscriber_with_given_id(self) -> None:
        publisher = Publisher()
        subscriber = Subscriber()
        publisher.subscribe(subscriber)

        publisher.unsubscribe(subscriber.id)

        expected_subscribers = []
        self.assertEqual(expected_subscribers, publisher.subscribers)

    def test_publish_WHEN_message_given_THEN_calls_subscribed_subscriber_update_with_given_message(self) -> None:
        publisher = Publisher()
        subscriber = Subscriber()
        message = Message()
        when(subscriber).update(message)
        publisher.subscribe(subscriber)

        publisher.publish(message)

        verify(subscriber).update(message)
