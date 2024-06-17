from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Review, Contact, Service, BlogPost, Testimonial, TeamMember, ContactInfo
from rest_framework_simplejwt.tokens import RefreshToken


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get_name(self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email
        return name

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)