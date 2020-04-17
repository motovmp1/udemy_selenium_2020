import pytest
from p_75_test_base_classe import Baseclass


# use inside the class
@pytest.mark.usefixtures("dataload")
class TestExample2(Baseclass):

    # must be informal parameter (return)
    def test_edit_Profile(self, dataload):
        print(dataload[0])
        log = self.getLogger()
        log.info(dataload[0])
        print(dataload[1])
        log.warning(dataload[1])
        print(dataload[2])
