from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse
import uuid

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # Files will be uploaded to users directory
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Hashtag(models.Model):
    title = models.CharField(max_length=75, verbose_name='Hashtag')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = 'hashtag'

    def get_absolute_url(self):
        return reverse("hashtags", arg=[self.slug])
    
    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ImageField(upload_to=user_directory_path, verbose_name='picture', null=False)
    caption = models.TextField(verbose_name='caption', null=False)
    posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Hashtag, related_name='tags')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()

    def get_absolute_url(self):
        return reverse('postdetails', args=[str(self.id)])

    def __str__(self):
        return str(self.user)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    
    def __str__(self):
        return str(self.follower)

class Stream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def add_post(sender, instance, *args, **kwargs):
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)
        for follower in followers:
            stream = Stream(post=post, user=follower.follower, 
             date=post.posted, following=user)
            stream.save()

    def __str__(self):
        return str(self.user)

post_save.connect(Stream.add_post, sender=Post)

# OneToOne, ManyToMany and ForeignKey Fields 
# https://stackoverflow.com/questions/25386119/whats-the-difference-between-a-onetoone-manytomany-and-a-foreignkey-field-in-d