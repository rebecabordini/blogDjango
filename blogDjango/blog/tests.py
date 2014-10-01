import unittest
from blog.models import Blog, Category

class ValidacoesPost(unittest.TestCase):

	def test_teste(self):
		for post in Blog.objects.all():
			print(post.title)
		self.assertEqual(1, 1)
		
if __name__ == '__main__':
    unittest.main()
