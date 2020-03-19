from django.http import HttpResponse, JsonResponse

# third party app
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"name": "Soknoy", "age": 19})
