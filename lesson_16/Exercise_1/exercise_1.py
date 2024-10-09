"""
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
"""

from pytest import fail
from src1 import *

class TestTeamLeadClassInheritance:
    def test_manager_atributes_positive(self):
        # Arrange & Act
        new_lead = TeamLead()
        try:
            assert new_lead.department != None
        except AttributeError:
            fail("Manager attribute is missing!")

    def test_developer_atributes_positive(self):
        # Arrange & Act
        new_lead = TeamLead()
        # Assert
        try:
            assert new_lead.programming_language != None
        except AttributeError:
            fail("Developer attribute is missing!")


