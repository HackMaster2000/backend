from django.contrib.auth.models import User
from app.models import Product
from app.models import Testimonial
from app.models import BlogPost
from app.models import TeamMember
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from .functions import generateAccessToken, create_order, capture_order
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .serializer import ProductSerializer, UserSerializer, UserSerializerWithToken, TestimonialSerializer, BlogPostSerializer, TeamMemberSerializer
from app.insert_products import insertProducts
from app.insert_blogs import insertBlogs
from app.insert_testimonials import insertTestimonials
from app.insert_team_members import insertTeamMembers

@api_view(['GET'])
def getRoutes(request):
    return Response('Hola')

@api_view(['GET'])
def getTestimonials(request):
    testimonials = Testimonial.objects.all()
    if not testimonials:	
        insertTestimonials()
    serializer = TestimonialSerializer(testimonials, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBlogs(request):
    blogs = BlogPost.objects.all()
    if not blogs:	
        insertBlogs()
    serializer = BlogPostSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTeamMembers(request):
    team_members = TeamMember.objects.all()
    if not team_members:	
        insertTeamMembers()
    serializer = TeamMemberSerializer(team_members, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    if not products:	
        insertProducts()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateProductStock(request, pk):
    try:
        product = Product.objects.get(_id=pk)
    except Product.DoesNotExist:
        return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data
    product.stock = data.get('stock', product.stock)
    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_multiple_products_stock(request):
    stock_updates = request.data
    response_data = []
    for update in stock_updates:
        try:
            product = Product.objects.get(_id=update['_id'])
            product.stock = update['stock']
            product.save()
            serializer = ProductSerializer(product, many=False)
            response_data.append(serializer.data)
        except Product.DoesNotExist:
            response_data.append({'detail': f'Product with ID {update["_id"]} not found'})
    return Response(response_data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': 'No se pudo encontrar una cuenta activa con las credenciales proporcionadas.',
        'invalid_credentials': 'No fue posible iniciar sesión con las credenciales proporcionadas.',
    }

    def validate(self, attrs):
        data = super().validate(attrs) 
        if not self.user.is_active:
            raise serializers.ValidationError(
                    self.error_messages['no_active_account'],
                    code='no_active_account',
            )
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
                data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfiles(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerUser(request):
    data = request.data
    print(data)
    try:
        user = User.objects.create(
            first_name = data['name'],
            username = data['email'],
            email = data['email'],
            password = make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'details': '¡El correo electrónico ya existe!'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

class CrearOrden(APIView):
    
    def post(self, request):
        amount = request.data.get('amount', '0.0')
        order = create_order('Productos', amount)
        print('=====')
        print(order['id'])
        return Response(order, status=status.HTTP_200_OK)

class CapturarOdernPaypal(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            order_id = request.data['orderID']
            response = capture_order(order_id)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'error': 'error aqui'}, status=status.HTTP_400_BAD_REQUEST)