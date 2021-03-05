from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """Retunrs a list of APIView features"""
        an_apiview = [
            'uses HTTP method as fiunction (get, post, delete, patch, put)',
            'is similar to a traditional Django view',
            'givs you the most controll over your application logic',
            'is mapped manually to urls',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
