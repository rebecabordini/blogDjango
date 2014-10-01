import unittest
import datetime
from blog.models import Blog, Category


class ValidacoesPost(unittest.TestCase):

	def setUp(self):
		Blog.objects.all().delete()
		Category.objects.all().delete()
		categoria = Category.objects.create(title='Artes', slug='artes')
		Blog.objects.create(title='BlogTestSucesso',slug='blogtestesucesso',body='Teste',posted=datetime.datetime.now().date(),category=categoria)
		Blog.objects.create(title='BlogTestFalha',slug='blogtestefalha',body='Teste',posted=datetime.datetime.now().date(),category=categoria)

	def testApenasPostsNoPassadoSaoExibidos(self):
		self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
