from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import Counter, VisitorCount, Visitor, Comments, Products
from django.contrib.sessions.models import Session
from django.utils import timezone
from uuid import uuid4

# Create your views here.


def main(request):
    
    num_likes = Counter.objects.all().count()
    comments = Comments.objects.all().order_by('-id')
    count_comments = Comments.objects.all().count()
    # Retrieve the visitor count object, or create a new one if it doesn't exist yet
    visitor_count, created = VisitorCount.objects.get_or_create(pk=1)

    if created:
        visitor_count.count = 1
        visitor_count.save()

    ip_address = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')

    try:
        visitor = Visitor.objects.get(
            ip_address=ip_address, user_agent=user_agent)
    except Visitor.DoesNotExist:
        anonymous_uuid = uuid4()  # Generate a new UUID for anonymous users
        visitor = Visitor.objects.create(
            ip_address=ip_address, user_agent=user_agent, anonymous_uuid=anonymous_uuid)

    count_visitor = Visitor.objects.count()

    # Get the current time
    current_time = timezone.now()

    # Get all the sessions that are currently active
    sessions = Session.objects.filter(expire_date__gte=current_time)

    # Initialize a counter for anonymous users
    anonymous_user_count = 0

    # Iterate through each session and check if the user is anonymous
    for session in sessions:
        session_data = session.get_decoded()
        if '_auth_user_id' not in session_data:
            anonymous_user_count += 1

    # Return the count of anonymous users
    
    
    context = {
        'num_likes' : num_likes,
        'visitor_count' : visitor_count.count,
        'count_visitor' : count_visitor,
        'comments' : comments,
        'count_comments' : count_comments,
    }
    return render(request, 'base.html', context)


def comments(request):
    comments = Comments.objects.all()

    context = {
        'comments': comments
    }

    return render(request, 'comments.html', context)


def comments_page(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        status = request.POST['status']
        profilePic = request.FILES['profilePic']
        comment = request.POST['comment']

        new_comment = Comments(fname=fname, status=status,
                               profile_pic=profilePic, comment=comment)
        new_comment.save()
        return render(request, 'comments.html')

    return render(request, 'comments-page.html')


def about(request):
    return render(request, 'about.html')


def works(request):
    return render(request, 'works.html')


def shop(request):
    count_products = Products.objects.all().count()
    items = Products.objects.all().order_by('-id')
    context = {
        'items': items,
        'count_products': count_products
    }

    return render(request, 'shop.html', context)


def django(request):

    count_products = Products.objects.filter(django=True).count()
    items = Products.objects.filter(django=True)

    context = {
        'items': items,
        'count_products': count_products
    }

    return render(request, 'shop.html', context)


def php(request):

    count_products = Products.objects.filter(php=True).count()
    items = Products.objects.filter(php=True)

    context = {
        'items': items,
        'count_products': count_products
    }

    return render(request, 'shop.html', context)


def htmlcss(request):

    count_products = Products.objects.filter(html=True, css=True).count()
    items = Products.objects.filter(html=True, css=True)

    context = {
        'items': items,
        'count_products': count_products
    }

    return render(request, 'shop.html', context)


def paid(request):

    count_products = Products.objects.filter(status='Paid').count()
    items = Products.objects.filter(status='Paid')

    context = {
        'items': items,
        'count_products': count_products
    }

    return render(request, 'shop.html', context)


def free(request):

    count_products = Products.objects.filter(status='Free').count()
    items = Products.objects.filter(status='Free')

    context = {
        'items': items,
        'count_products': count_products
    }

    return render(request, 'shop.html', context)




@login_required
def counter(request):
  
    counter, created = Counter.objects.get_or_create(user=request.user)
    if created:
        counter.count = 1
        counter.save()
        
    else:
        counter.count = 0 
        
    if counter.count == 0:
        counter.delete()
        
    data = {'count': counter.count}
    return JsonResponse(data)
    
