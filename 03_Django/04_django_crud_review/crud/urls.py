from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('jobs/', include('jobs.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]

# 파일이 업로드 된 이후에 프로젝트 내부에 존재하는 파일의 주소를 만들어 줌
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)