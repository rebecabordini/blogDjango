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
		self.assertIn(self.post_atual, Blog().posts_publicados_no_passado())

	def testApenasPostsNoFuturoSaoExibidos(self):
		self.assertIn(self.post_futuro, Blog().posts_publicados_no_futuro())


if __name__ == '__main__':
    unittest.main()
