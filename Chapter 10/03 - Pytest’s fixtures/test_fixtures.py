import pytest


@pytest.fixture
def dependency():
    return "fixture value"


@pytest.fixture
def dependency_as_generator():
    # setup code
    yield "fixture value"
    # teardown code


def test_fixture(dependency):
    pass
