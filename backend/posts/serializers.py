from rest_framework import serializers
from .models import Post, PostImage, Pet, PostVideo, Like, Comment
from accounts.serializers import PetAbridgedSerializer

class PostSerializer(serializers.ModelSerializer):
    pet = PetAbridgedSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['pet', 'caption', 'created_at']
        read_only_fields = ('created_at', )


class PostImageSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = PostImage
        fields = ['post', 'image', 'alt_text']


class PostVideoSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = PostVideo
        fields = ['post', 'video', 'alt_text']
        
    video = serializers.FileField()  # Añadi esta línea para que me funcionara el DRF-SPECTACULAR
    video.related_model = PostVideo  # Añadi esta línea para que me funcionara el DRF-SPECTACULAR


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    pet = PetAbridgedSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['post', 'pet', 'description', 'created_at']
        read_only_fields = ('created_at', )
    

class LikeSerializer(serializers.ModelSerializer):
    pet = PetAbridgedSerializer(many=True, read_only=True)
    post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Like
        fields = ['pet', 'post']