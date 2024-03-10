from django.shortcuts import render
from notification.models import Notification

# Create your views here.

def notification(request):
    user = request.user
    # Retrieve notifications for the current user, ordered by creation date
    notifications = Notification.objects.filter(receiver=user).order_by('-created_at')
    # Mark all unread notifications as seen
    Notification.objects.filter(receiver=user, seen=False).update(seen=True)

    # Prepare context data to be passed to the template
    context = {'title': 'Notifications', 'notifications': notifications}
    # Render the notification.html template with the context data
    return render(request, 'notification.html', context)

def notification_counts(request):
    # Get the current logged-in user
    user = request.user
    # Initialize notification count
    count = 0
    if user.is_authenticated:
        # Count the number of unread notifications for the current user
        count = Notification.objects.filter(receiver=user, seen=False).count()

    # Return a dictionary containing the notification count
    return {'notification_count': count}
