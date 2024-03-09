from django.shortcuts import render
from notification.models import Notification

def notification(request):
    # Get the current user
    user = request.user
    
    # Retrieve all notifications for the user and order them by creation date
    notifications = Notification.objects.filter(receiver=user).order_by('-created_at')
    
    # Mark all unread notifications as seen
    Notification.objects.filter(receiver=user, seen=False).update(seen=True)

    # Prepare context data to be passed to the template
    context = {'title': 'Notifications', 'notifications': notifications}
    
    # Render the notification template with the context data
    return render(request, 'notification.html', context)

def notification_counts(request):
    # Get the current user
    user = request.user
    
    # Initialize the notification count to 0
    count = 0
    
    # If the user is authenticated, count the number of unread notifications
    if user.is_authenticated:
        count = Notification.objects.filter(receiver=user, seen=False).count()

    # Return the notification count
    return {'notification_count': count}

