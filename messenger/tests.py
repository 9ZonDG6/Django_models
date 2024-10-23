from django.test import TestCase
from django.urls import reverse

from messenger import factories, models


# Create your tests here.
class MessengerTestCase(TestCase):
    def setUp(self):
        self.post = factories.PostFactory()

    def test_get_post_list(self):
        url = reverse('Posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['posts'].count(), models.Post.objects.count())

    def test_get_post_detail(self):
        url = reverse('PostDetail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.post_subject)

    def test_update_post(self):
        url = reverse('PostUpdate', kwargs={'pk': self.post.pk})
        old_subject = self.post.post_subject
        old_text = self.post.post_text
        response = self.client.post(url, {
            'post_subject': 'new subject',
            'post_text': old_text,
            'author': self.post.author.pk
        })
        self.post.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.post.post_subject, old_subject)

    def test_delete_post(self):
        url = reverse('PostDelete', kwargs={'pk': self.post.pk})
        old_post_count = models.Post.objects.count()
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreaterEqual(old_post_count, models.Post.objects.count())

    def test_create_post(self):
        url = reverse('PostCreate')
        old_post_count = models.Post.objects.count()
        response = self.client.post(url, {
            'author': self.post.author.pk,
            'post_subject': self.post.post_subject,
            'post_text': self.post.post_text,
            'created_at': self.post.created_at
        })
        self.assertEqual(response.status_code, 302)
        self.assertGreater(models.Post.objects.count(), old_post_count)
