from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
	def test_create_blog(self):
		b = Blog('Teste', 'Test Author')
		self.assertEqual('Teste', b.title)
		self.assertEqual('Test Author', b.author)
		self.assertListEqual([], b.posts)
	
	def test_repr(self):
		b = Blog('Test', 'Test Author')
		self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
	
	def test_repr_multiple_posts(self):
		b = Blog('Test', 'Test Author')
		b.posts = ['Some post']	
		self.assertEqual(b.__repr__(), 'Test by Test Author (1 posts)')

