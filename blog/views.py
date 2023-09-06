from django.contrib.contenttypes.models import ContentType 
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from blog.models import Article
from taggit.models import Tag, TaggedItem

# Create your views here.
def index(request):
    print("Request for blog index page received")
    developer = "karmacanix"
    context = {"developer": developer}
    return render(request, "blog/index.html", context)


class ArticleListView(ListView):
    paginate_by = 2
    model = Article
    # need to find out the tags 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_list"] = Tag.objects.filter(taggit_taggeditem_items__content_type_id=9).distinct
        context["spotlight_article_list"] = Article.spotlight_objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_list"] = Tag.objects.filter(taggit_taggeditem_items__content_type_id=9).distinct
        context["spotlight_article_list"] = Article.spotlight_objects.all()
        return context


class TaggedArticleListView(ListView):
    context_object_name = "tagged_article_list"
    template_name = "blog/tagged_article_list.html"
    paginate_by = 2
	
    def get_queryset(self):
        return Article.objects.filter(tags__exact=self.kwargs['tag_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_list"] = Tag.objects.filter(taggit_taggeditem_items__content_type_id=9).distinct
        context["spotlight_article_list"] = Article.spotlight_objects.all()
        context["tag_boo"] = Tag.objects.get(id=self.kwargs['tag_id'])
        return context