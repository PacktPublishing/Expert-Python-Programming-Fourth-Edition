from unittest.mock import patch, Mock
from mailer import send
import smtplib


def test_send_unittest():
    sender = "john.doe@example.com"
    to = "jane.doe@example.com"
    body = "Hello jane!"
    subject = "How are you?"

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


def test_send(monkeypatch):
    sender = "john.doe@example.com"
    to = "jane.doe@example.com"
    body = "Hello jane!"
    subject = "How are you?"

    smtp = Mock()
    monkeypatch.setattr(smtplib, "SMTP", smtp)
    client = smtp.return_value
    client.sendmail.return_value = {}

    res = send(sender, to, subject, body)

    assert client.sendmail.called
    assert client.sendmail.call_args[0][0] == sender
    assert client.sendmail.call_args[0][1] == to
    assert subject in client.sendmail.call_args[0][2]
    assert body in client.sendmail.call_args[0][2]
    assert res == {}
