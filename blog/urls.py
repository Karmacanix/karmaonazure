from django.urls import path
from blog.views import ArticleListView, ArticleDetailView, TaggedArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('<pk>/', ArticleDetailView.as_view(), name='article'),
    path('tag/<tag_id>/', TaggedArticleListView.as_view(), name='article_tag'),
]