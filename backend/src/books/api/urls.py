from books.api.views import BookViewSet, CategoryViewSet, LanguageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'languages', LanguageViewSet, basename='languages')
router.register(r'categories', CategoryViewSet, basename='categories')
urlpatterns = router.urls