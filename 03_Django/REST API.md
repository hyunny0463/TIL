REST API

RESTful: 전송하는 상태를 표현하는 방법

API(Application Programming Interfase)

정해진 형식으로 요청을 보내면 요청한 정보를 받을 수 있는 소통 방법



![image](https://user-images.githubusercontent.com/12672315/67646950-c436ed00-f973-11e9-9323-c75bef837b45.png)

REST API



각 요청이 어떠한 동작&정보를 위한 것인지 **요청 형식 자체(주소)로 파악이 가능**한 것

```
GET https://hphk/members/

body {"id":2, "name": "justin"}
```



```
POST https://hphk/members/
```



```
PUT https://hphk/members/2/

body {"name": "tony"}
```



```
DELETE https://hphk/members/14/
```



Django에는 REST API 서버를 쉽게 개발할 수 있도록 Djangorestframework 제공



이제는 우리가 직접 REST API 서버를 개발해보자!



Django 에서 REST API 를 위한 프레임워크가 있는데 그것이 DRF(Django REST Framework)이다.

실제 Django에서 PUT, PATCH, DELETE 를 제대로 지원하지 않기 때문에 RESTful 하게 작업하려면 DRF가 필요하다. (PUT은 데이터 전체를 바꾸는 것을 뜻하고, PATCH는 일부를 바꾸는 것을 뜻한다. PUT은 입력하지 않은 데이터는 NULL로 바꾼다는 뜻이다.)

```
$ pip install djangorestframework
```



앱 등록

```python
INSTALLED_APPS = [
    'rest_framework',
    
    'drf_yasg',
]
```



```python
# admin.py
from .models import Artist, Music, Comment

admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(Comment)
```



database seeding

```
$ python manage.py dumpdata -indent 2 musics > dummy.json
```



파일 위치

```
musics[APP_NAME]
	└ fixtures
		└ musics[NAME_SPACE]
			└ dummy.json
```



```python
# serializers.py
from rest_framework import serializers
from .model import Music

class MusciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id', )
```



```python
# views.py
from .models import Music
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusciSerializer

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    # serializer: musics(queryset) -> json
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)
```



swagger: 자동으로 API 목록과 각 API의 Request Body, Query Parameter 를 문서화해주며 바로 Postman과 같이 API를 테스트해 볼 수 있는 문서화 도구이다.

```python
# urls.py
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
]
```



수정, 삭제 method

```python
# views.py
@api_view(['PUT', 'DELETE'])
def comments_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    # PUT
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Comment has been updated!!'})
    # DELETE    
    else:
        comment.delete()
        return Response({'message': 'Comment has been deleted!!'})
```

