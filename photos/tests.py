from django.test import TestCase
from myassignment.factory import create_user_test1, create_user_test2

import simplejson


class TestPhotosListView(TestCase):

    def setUp(self):
        self.test_url_1 = 'http://localhost:9999/v1/photos/?format=json'
        self.test_url_2 = 'http://localhost:9999/v1/photos/2/?format=json'
        create_user_test1()
        create_user_test2()

    def test_get_photos_list(self):
        response = self.client.get(self.test_url_1)
        self.assertEqual(response.status_code, 200)
        content = simplejson.loads(response.content)
        self.assertEqual(content[0]['url'], '/url/test1/')
        self.assertEqual(content[0]['comments']['1'], 'good!!')
        

    def test_get_photo_detail(self):
        response = self.client.get(self.test_url_2)
        self.assertEqual(response.status_code, 200)
        content = simplejson.loads(response.content)
        self.assertEqual(content['url'], '/url/test2/')
        self.assertEqual(content['comments']['2'], 'good good!!')