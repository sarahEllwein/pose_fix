import unittest
from annotate_images import *


class TestProfiles(unittest.TestCase):

    def test_is_side_profile_false(self):
        img, res = get_image_info('../test/image_test_set_v2/front_profile_1.jpeg')
        self.assertFalse(is_side_profile(img, res))

    def test_is_side_profile_true_1(self):
        img, res = get_image_info('../test/image_test_set_v2/side_profile_1.jpeg')
        self.assertTrue(is_side_profile(img, res))

    def test_is_side_profile_true_2(self):
        img, res = get_image_info('../test/image_test_set_v2/side_profile_2.jpeg')
        self.assertTrue(is_side_profile(img, res))

    def test_is_side_profile_true_3(self):
        img, res = get_image_info('../test/image_test_set_v2/side_profile_3.jpeg')
        self.assertTrue(is_side_profile(img, res))


if __name__ == '__main__':
    unittest.main()
