from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get unread notifications for the logged-in user
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications.update(read=True)  # Mark notifications as read when fetched
        notification_data = [{
            'actor': notif.actor.username,
            'verb': notif.verb,
            'target': str(notif.target),
            'timestamp': notif.timestamp
        } for notif in notifications]
        
        return Response(notification_data, status=200)
