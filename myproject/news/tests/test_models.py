from django.test import TestCase

from .models import News, Comment


class NewsModelTest(TestCase):

    def setUp(self):
        self.news_with_comments = News.objects.create(title="News with comments",
                                                      content="Content with comments")
        self.news.without_comments = News.objects.create(title="News without comments",
                                                         content="Content without comments")
        Comment.objects.create(news=self.news_with_comments, content="First comment")

    def test_has_comments_true(self):
        self.assertTrue(self.news_with_comments.has_comments())

    def test_has_comments_false(self):
        self.assertFalse(self.news_with_comments.has_comments())