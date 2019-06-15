from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):
        return Response({'message' : 'Hello!!', 'an_apiview': {'A', 'B', 'C'}})


class NamasteyApiView(APIView):
    def get(self, request, format=None):
        return Response({'message' : 'Namastey Django'})