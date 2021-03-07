from post import Post
import unittest

class PostTest(unittest.TestCase):
	def test_create_post(self):
		p = Post('Title', 'Title Content')
		self.assertEqual('Title', p.title)
		self.assertEqual('Title Content', p.content)

	def test_json(self):
		p = Post('Title', 'Title Content')
		expected = {'title': 'Title', 'content': 'Title Content'}
		self.assertDictEqual(expected, p.json())
