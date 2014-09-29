from django.test import TestCase
from myassignment.factory import create_user_test1, create_user_test2

import simplejson


class TestCommentsListView(TestCase):

    def setUp(self):
        self.test_url_1 = 'http://localhost:9999/v1/comments/?format=json'
        self.test_url_2 = 'http://localhost:9999/v1/comments/2/?format=json'
        create_user_test1()
        create_user_test2()

    def test_get_comment_list(self):
        response = self.client.get(self.test_url_1)
        self.assertEqual(response.status_code, 200)
        content = simplejson.loads(response.content)
        self.assertEqual(content[0]['comment'], 'good!!')
        self.assertEqual(content[0]['photo'], 1)

    def test_get_comment_detail(self):
        response = self.client.get(self.test_url_2)
        self.assertEqual(response.status_code, 200)
        content = simplejson.loads(response.content)
        self.assertEqual(content['comment'], 'good good!!')
        self.assertEqual(content['photo'], 2)