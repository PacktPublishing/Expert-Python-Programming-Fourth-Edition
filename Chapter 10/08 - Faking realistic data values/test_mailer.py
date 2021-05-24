from unittest.mock import patch

import pytest

from mailer import send
from faker import Faker


@pytest.mark.parametrize("iteration", range(10))
def test_send(faker: Faker, iteration: int):
    sender = faker.email()
    to = faker.email()
    body = faker.paragraph()
    subject = faker.sentence()

    with patch("smtplib.SMTP") as mock:
        client = mock.return_value
        client.sendmail.return_value = {}

        res = send(sender, to, subject, body)

        assert client.sendmail.called
        assert client.sendmail.call_args[0][0] == sender
        assert client.sendmail.call_args[0][1] == to
        assert subject in client.sendmail.call_args[0][2]
        assert body in client.sendmail.call_args[0][2]
        assert res == {}
