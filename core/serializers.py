from rest_framework import serializers

from .models import Site, Gallery, Team, Client, Course


class SiteSerializer(serializers.ModelSerializer):
    gallery = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    client = serializers.SerializerMethodField()
    courses = serializers.SerializerMethodField()
    header_image = serializers.SerializerMethodField()
    
    def get_header_image(self, obj):
        if obj.header_image:
            return obj.header_image.url
        return ""
    
    def get_gallery(self, obj):
        return GallerySerializer(Gallery.objects.all(), many=True).data
    
    def get_courses(self, obj):
        return CourseSerializer(Course.objects.all(), many=True).data

    def get_team(self, obj):
        return TeamSerializer(Team.objects.all(), many=True).data

    def get_client(self, obj):
        return ClientSerializer(Client.objects.all(), many=True).data

    class Meta:
        model = Site
        fields = "__all__"


class CommonImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return ""
    
    
class GallerySerializer(CommonImageSerializer):
    class Meta:
        model = Gallery
        exclude = ["index_order", "created_at", "updated_at", "id",]


class CourseSerializer(CommonImageSerializer):
    class Meta:
        model = Course
        exclude = ["index_order", "created_at", "updated_at", "id",]


class TeamSerializer(CommonImageSerializer):
    class Meta:
        model = Team
        exclude = ["index_order", "created_at", "updated_at", "id",]


class ClientSerializer(CommonImageSerializer):
    class Meta:
        model = Client
        exclude = ["index_order", "created_at", "updated_at", "id",]
