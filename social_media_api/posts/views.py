from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets, permissions, status 
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        followed_users = user.following.all()

        # Get posts from followed users
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    # Check if the user has already liked the post
    if Like.objects.filter(user=user, post=post).exists():
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Create like
    Like.objects.create(user=user, post=post)

    # Create notification
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb="liked your post",
        target=post
    )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    # Check if the user has liked the post
    like = Like.objects.filter(user=user, post=post).first()
    if not like:
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Remove like
    like.delete()

    # Remove notification (optional, depending on requirements)
    Notification.objects.filter(
        recipient=post.author,
        actor=user,
        verb="liked your post",
        target=post
    ).delete()

    return Response({"detail": "Like removed successfully."}, status=status.HTTP_204_NO_CONTENT)

"Post.objects.filter(author__in=following_users).order_by"

"generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)"