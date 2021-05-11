from django.test import TestCase
from django.test.utils import tag
from .models import Editor, Article, tags

# Create your tests here.


class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james = Editor(
            first_name='James', last_name='Muriuki', email='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

        # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


    def test_delete_method(self):
        Editor.delete_editor(Editor, first_name='James')
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0)

    def test_update_method(self):
        self.james.save_editor()
        Editor.update_editor(Editor,first_name='James',new_name='Kim')
        self.assertTrue(Editor.objects.get(first_name='Kim'))


class tagsTestClass(TestCase):

   # Set up method
    def setUp(self):
        self.tag = tags(
            name='tagOne', )

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.tag, tags))


# class ArticleTestClass(TestCase):
#   def setUp(self):
#     self.article =Article(title='Django update',post='all updates done',editor='james',tags='tagOne',pub_date=2019-10-2)

  
#     # Testing  instance
#   def test_instance(self):
#         self.assertTrue(isinstance(self.article, Article))  
    
