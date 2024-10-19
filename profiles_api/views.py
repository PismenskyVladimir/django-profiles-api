from rest_framework import (
    filters,
    status,
    viewsets,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import (
    APIView,
    Response,
)

from profiles_api import (
    models,
    permissions,
    serializers,
)


class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Creates a hello message with our name."""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        """Handle updating an object."""

        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial updating an object."""

        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object."""

        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializer

    def list_item(self, request):
        """Return a hello  message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy',
            'Automatically maps to URLs using Routers',
            'Providdes more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID."""

        return Response(
            {
                'view_method': 'retrieve()',
                'http_method': request.method,
            },
        )

    def update(self, request, pk=None):
        """Handle updating an object by its ID."""

        return Response(
            {
                'view_method': 'update()',
                'http_method': request.method,
            },
        )

    def partial_update(self, request, pk=None):
        """Handle updating part an object by its ID."""

        return Response(
            {
                'view_method': 'partial_update()',
                'http_method': request.method,
            },
        )

    def destroy(self, request):
        """Destroy an object by its ID."""

        return Response(
            {
                'view_method': 'destroy()',
                'http_method': request.method,
            },
        )


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.UpdateOwnProfile]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens."""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
