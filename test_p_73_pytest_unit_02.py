import pytest


@pytest.mark.usefixtures("dataload")
class TestExample2:
    import pytest

    # must be informal parameter (return)
    def test_edit_Profile(self, dataload):
        print(dataload[0])
        print(dataload[1])
        print(dataload[2])
