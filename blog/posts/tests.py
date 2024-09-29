from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from posts.models import Post


class HomeViewTestCase(TestCase):
    fixture = ['posts.json', ]

    def test_view(self):
        path = reverse('home')
        response = self.client.get(path)
        posts = Post.objects.order_by('-date_create')[:3]

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Блог')
        self.assertTemplateUsed(response, 'posts/index.html')
        self.assertEqual(list(response.context_data['object_list']), list(posts))
