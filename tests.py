import unittest
from repository import Repository
from validation import PlaneValidator
from service import PlaneService
from errors import PlaneError

class TestPlaneService(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__repository = Repository()
        self.__validator = PlaneValidator()
        self.__service = PlaneService(self.__repository, self.__validator)
        
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    
    def test_add_plane__valid_plane__repository_with_plane(self):
        x_coordinate = 3
        y_coordinate = 3
        orientation = "up"
        self.__service.add_plane(x_coordinate, y_coordinate, orientation)
        self.assertEqual(self.__repository.get_size(), 1)
        
        
    def test_add_plane__invalid_plane__plane_error(self):
        x_coordinate = -1
        y_coordinate = 11
        orientation = "up"
        with self.assertRaises(PlaneError):
            self.__service.add_plane(x_coordinate, y_coordinate, orientation)
