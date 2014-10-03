import unittest
import datetime
from blog.models import Blog, Category
from blog import views


class ValidacoesPost(unittest.TestCase):

	propriedade_da_classe = False

	@classmethod
	def setUpClass(cls):
		Blog.objects.all().delete()
		Category.objects.all().delete()
		categoria = Category.objects.create(title='Artes', slug='artes')

		dataAtual = datetime.datetime.now().date()
		dataFutura = dataAtual + datetime.timedelta(days=1)

		kwargs = {
			'body': 'Teste',
			'category': categoria,
		}
		
		cls.post_atual = Blog.objects.create(title='BlogTestSucesso',slug='blogtestesucesso',posted=dataAtual, **kwargs)
		cls.post_futuro = Blog.objects.create(title='BlogTestFalha',slug='blogtestefalha',posted=dataFutura, **kwargs)

	def testApenasPostsNoPassadoSaoExibidos(self):
		# posts = []
		# posts.append(Blog.objects.get(title='BlogTestSucesso'))
		# self.assertEqual(views.posts_publicados_no_passado()[0], Blog.objects.filter(title='BlogTestSucesso')[0])

		# self.assertIn(Blog.objects.get(title='BlogTestSucesso'), Blog().posts_publicados_no_passado())
		self.assertIn(self.post_atual, Blog().posts_publicados_no_passado())

	def testApenasPostsNoFuturoSaoExibidos(self):
		self.assertIn(self.post_futuro, Blog().posts_publicados_no_futuro())

		# self.assertIn(Blog.objects.get(title='BlogTestFalha'), Blog().posts_publicados_no_futuro())
		#TODO: criar uma rota para apontar apenas para os posts que ainda serao publicados com testes e tudo mais 

	# def suite():
	# 	suite = unittest.TestSuite()
	# 	suite.addTest(ValidacoesPost('testApenasPostsNoPassadoSaoExibidos'))
	# 	suite.addTest(ValidacoesPost('testApenasPostsNoFuturoSaoExibidos'))
	# 	return suite

if __name__ == '__main__':
    unittest.main()
