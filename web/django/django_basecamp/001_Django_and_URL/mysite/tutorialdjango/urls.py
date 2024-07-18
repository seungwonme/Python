from django.contrib import admin
from django.urls import path
from main.views import index, a, b, c, seunan, orm

# 이 위치에서 함수를 작성해도 되지만 유지보수를 위해 views.py에 작성

urlpatterns = [
    # path('원하는URL/', 함수명),
    path("admin/", admin.site.urls),
    path("", index),
    path("a/", a),
    path("b/", b),
    path("c/", c),
    path("seunan/", seunan),
    path("orm/", orm),
]
