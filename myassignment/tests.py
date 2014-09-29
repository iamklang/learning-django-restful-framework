from django.test import TestCase
from myassignment.factory import create_user_test1, create_user_test2

import simplejson


class TestPhotosListView(TestCase):

    def setUp(self):
        self.test_url_1 = 'http://localhost:9999/v1/users/?format=json'
        self.test_url_1_detail = 'http://localhost:9999/v1/users/1/?format=json'
        create_user_test1()

    def test_get_photos_list(self):
        response = self.client.get(self.test_url_1)
        self.assertEqual(response.status_code, 200)
        content = simplejson.loads(response.content)
        self.assertEqual(content[0]['first_name'], 'test1')
        self.assertEqual(content[0]['last_name'], 'lastname-test1')
        self.assertEqual(content[0]['photos'][0]['url'], '/url/test1/')
        self.assertEqual(content[0]['photos'][0]['comments']['1'], 'good!!')

    def test_get_photo_detail(self):
        response = self.client.get(self.test_url_1_detail)
        self.assertEqual(response.status_code, 200)
        content = simplejson.loads(response.content)
        self.assertEqual(content['first_name'], 'test1')
        self.assertEqual(content['last_name'], 'lastname-test1')
        self.assertEqual(content['photos'][0]['url'], '/url/test1/')
        self.assertEqual(content['photos'][0]['comments']['1'], 'good!!')