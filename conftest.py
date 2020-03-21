from unittest.test.testmock.support import target

import pytest

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("c:\\tools\\AddressBook.exe").start(target)
    request.addfinalizer(fixture.destroy)
    return fixture
