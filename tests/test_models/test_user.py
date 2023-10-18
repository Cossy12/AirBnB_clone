#!/usr/bin/env python3
"""model - user test case"""
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """testing  user model"""

    def __init__(self, *args, **kwargs):
        """   function """

        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def trial_first_name(self):
        """   first name is a string"""
        User = self.value()
        self.assertEqual(type(User.first_name), str)

    def trial_last_name(self):
        """ last name is a string"""
        user = self.value()
        self.assertEqual(type(user.last_name), str)

    def trial_email(self):
        """ email is a string"""
        user = self.value()
        self.assertEqual(type(user.email), str)

    def trial_password(self):
        """ password is a string """
        user = self.value()
        self.assertEqual(type(user.password), str)
