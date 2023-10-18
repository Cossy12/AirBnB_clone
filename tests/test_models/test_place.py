#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class test_Place(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def trial_city_id(self):
        """ """

        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def trial_user_id(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.user_id), str)

    def trial_name(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.name), str)

    def trial_description(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.description), str)

    def trial_number_rooms(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.number_rooms), int)

    def trial_number_bathrooms(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.number_bathrooms), int)

    def trial_max_guest(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.max_guest), int)

    def trial_price_by_night(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.price_by_night), int)

    def trial_latitude(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.latitude), float)

    def trial_longitude(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.latitude), float)

    def trial_amenity_ids(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.amenity_ids), list)
