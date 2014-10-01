import unittest
import datetime
from blog.models import Blog, Category
from blog import views


class ValidacoesPost(unittest.TestCase):

	def setUp(self):
		Blog.objects.all().delete()
		Category.objects.all().delete()
		categoria = Category.objects.create(title='Artes', slug='artes')
		dataFutura = datetime.datetime.now().date() + datetime.timedelta(days=1)
		Blog.objects.create(title='BlogTestSucesso',slug='blogtestesucesso',body='Teste',posted=datetime.datetime.now().date(),category=categoria)
		Blog.objects.create(title='BlogTestFalha',slug='blogtestefalha',body='Teste',posted=dataFutura,category=categoria)

	def testApenasPostsNoPassadoSaoExibidos(self):
		# posts = []
		# posts.append(Blog.objects.get(title='BlogTestSucesso'))
		# self.assertEqual(views.posts_publicados_no_passado()[0], Blog.objects.filter(title='BlogTestSucesso')[0])
		self.assertIn(Blog.objects.get(title='BlogTestSucesso'), views.posts_publicados_no_passado())

	def testApenasPostsNoFuturoSaoExibidos(self):
		self.assertIn(Blog.objects.get(title='BlogTestFalha'), views.posts_publicados_no_futuro())
		#TODO: criar uma rota para apontar apenas para os posts que ainda serao publicados com testes e tudo mais 

	def suite():
		suite = unittest.TestSuite()
		suite.addTest(ValidacoesPost('testApenasPostsNoPassadoSaoExibidos'))
		suite.addTest(ValidacoesPost('testApenasPostsNoFuturoSaoExibidos'))
		return suite

if __name__ == '__main__':
    unittest.main()
