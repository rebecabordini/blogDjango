import unittest
from blog.models import Blog, Category
from blog.views import index

class ValidacoesPost(unittest.TestCase):

	def test_teste(self):
		self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
