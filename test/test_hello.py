import pytest
from mymodule.mypackage import hello

def test_hello():
	assert "Hi, ABC!" == hello.test("ABC")