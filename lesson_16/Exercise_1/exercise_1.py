"""
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
"""

from pytest import fail, mark
from src1 import *

class TestTeamLeadClassInheritance:
    # Arrange
    new_lead = TeamLead()

    @mark.parametrize("attribute", [
        (new_lead.department),
        (new_lead.programming_language)
    ])
    def test_manager_atributes(self, attribute):
        # Act
        try:
            assert attribute is not None
        except AttributeError:
            fail("Attribute is missing!")


