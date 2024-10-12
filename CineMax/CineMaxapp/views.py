from django.shortcuts import render,redirect,get_object_or_404
from CineMaxapp.models import hollywood,tamilMovies,webseries, anime, korean,Watchlist,Subscription
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
import razorpay

# Create your views here.
def home(request):
    context={}
    h=hollywood.objects.filter(is_active=True)
    t=tamilMovies.objects.filter(is_active=True)
    ws=webseries.objects.filter(is_active=True)
    a=anime.objects.filter(is_active=True)
    k=korean.objects.filter(is_active=True)
    context['hmovies']=h
    context['tmovies']=t
    context['WSmovies']=ws
    context['Amovies']=a
    context['Kmovies']=k
    return render(request,'index.html',context)

                                    #Filter category
def hollywood_movies(request):
    movies = hollywood.objects.filter(is_active=True)
    return render(request, 'Filter.html', {'hmovies': movies})

def tamil_movies(request):
    movies = tamilMovies.objects.filter(is_active=True)
    return render(request, 'Filter.html', {'tmovies': movies})

def web_series(request):
    movies = webseries.objects.filter(is_active=True)
    return render(request, 'Filter.html', {'WSmovies': movies})

def anime_movies(request):
    movies = anime.objects.filter(is_active=True)
    return render(request, 'Filter.html', {'Amovies': movies})

def korean_movies(request):
    movies = korean.objects.filter(is_active=True)
    return render(request, 'Filter.html', {'Kmovies': movies})

# For HollyWood Movie =HWM
def HWM(request,cid):
    context={}
    context['hmovies']=hollywood.objects.filter(id=cid)
    return render(request,'Hollywood.html',context)

# For Tamil Movie =TM
def TM(request,tid):
    context={}
    context['tmovies']=tamilMovies.objects.filter(id=tid)
    return render(request,'TamilMovies.html',context)

# For Web Series =WS
def WS(request,wid):
    context={}
    context['WSmovies']=webseries.objects.filter(id=wid)
    return render(request,'WebSeries.html',context)

#For Anime Movies = AM
def AM(request,aid):
    context={}
    context['Amovies']=anime.objects.filter(id=aid)
    return render(request,'Anime.html',context)

#For Korean Movies = KM
def KM(request,kid):
    context={}
    context['Kmovies']=korean.objects.filter(id=kid)
    return render(request,'Korean.html',context)

def Hvideo(request,trailer):
    context={}
    context['VH']=hollywood.objects.filter(id=trailer)
    return render(request,'HollyWoodvideo.html',context)

def Tvideo(request,trailer):
    context={}
    context['VTM']=tamilMovies.objects.filter(id=trailer)
    return render(request,'TamilMovievideo.html',context)

def WSvideo(request,trailer):
    context={}
    context['VWS']=webseries.objects.filter(id=trailer)
    return render(request,'WebSeriesvideo.html',context)

def Avideo(request,trailer):
    context={}
    context['VAM']=anime.objects.filter(id=trailer)
    return render(request,'Animevideo.html',context)

def Kvideo(request,trailer):
    context={}
    context['VKM']=korean.objects.filter(id=trailer)
    return render(request,'Koreanvideo.html',context)

def logindetails(request):
    context={}
    if request.method=="POST":
        
         loginname=request.POST["uname"]
         loginpassword=request.POST["upass"]
        #  print(loginname)
        #  print(loginpassword )
         if loginname=='' or loginpassword=='':
            context["errormessage"]="fields cannot be blank"
            return render(request,'login.html',context) 
         else:
             #authenticate is the predefined provided by the djang0 built in framework
             #it compare the username and password from the predefined models class
             u=authenticate(username=loginname,password=loginpassword)
             print(u)
             if u is not None:
                 login(request,u)
                 return redirect('/home')
             else:
                 context['errormessage']="invalid User"
                 return render(request,'login.html',context)


        #  s=Login.objects.create(loginname=loginname,loginpassword=loginpassword)
        #  s.save()
        #  return HttpResponse('user Login successfully')
        #  return render(request,'index.html')
    
    else:
        return render(request,'login.html')

def register(request):
    if request.method=="POST":
        context={}
        UserName=request.POST["uname"]
        Password=request.POST["upass"]
        CPassword=request.POST["ucpass"]

        if UserName==""or Password==""or CPassword=="":
            context['errormessage']="Fields cannot be blank!!!"
            return render(request,'register.html',context)
        
        elif Password!=CPassword:
            context['errormessage']="Password and confirm confirm password does not Match!!"
            return render(request,'register.html',context)

        
        else:
            try:
                u=User.objects.create(username=UserName,password=Password,email=CPassword)
                u.set_password(Password)
                u.save()
                context['success']="User Created Successfully"
                return render(request,'register.html',context)
                #return HttpResponse('user created successfully')
            except Exception:
                context['errormessage']="User already exists!!!"
                return render(request,'register.html',context)


    
    else:
        u=User.objects
        return render(request,'register.html')

def user_logout(request):
    logout(request)
    return redirect('/login')
    
def add_to_watchlist(request, category, movie_id):
    if request.method == 'GET':
        # Add the movie to the user's watchlist
        Watchlist.objects.create(user=request.user, movie_id=movie_id, category=category)
        return redirect('/watchlist')
        # return HttpResponse(f'Movie with ID {movie_id} added to {category} watchlist.')
    else:
        return HttpResponse('Invalid request method.', status=405)

def remove(request, cid):
    watchlist_item = get_object_or_404(Watchlist, id=cid)
    watchlist_item.delete()
    return redirect('/watchlist')


def watchlist(request):
    # Fetch the user's watchlist items
    watchlist_items = Watchlist.objects.filter(user=request.user)
    movies = []

    for item in watchlist_items:
        # Determine the model based on the category
        if item.category == 'hollywood':
            movie = hollywood.objects.filter(id=item.movie_id).first()
        elif item.category == 'tamilMovies':
            movie = tamilMovies.objects.filter(id=item.movie_id).first()
        elif item.category == 'webseries':
            movie = webseries.objects.filter(id=item.movie_id).first()
        elif item.category == 'anime':
            movie = anime.objects.filter(id=item.movie_id).first()
        elif item.category == 'korean':
            movie = korean.objects.filter(id=item.movie_id).first()
        else:
            movie = None  # Unknown category

        if movie:
             movies.append({'movie': movie, 'watchlist_item': item, 'category': item.category})

    return render(request, 'Watchlist.html', {'movies': movies})



# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=("rzp_test_VZbpcH0s33sGpv", "nKMohKrV5iNczM3REH4R1YeR"))

def subscription_plans(request):
    user = request.user

    # Fetch active subscriptions for the current user
    active_subscriptions = Subscription.objects.filter(user=user, is_active=True)
    
    # Create a dictionary to map the user's active subscription plans
    active_plans = {sub.plan_type: True for sub in active_subscriptions}

    # Check if the user has tried subscribing to an already paid plan
    already_subscribed = request.session.pop('already_subscribed', None)

    return render(request, 'Subscription.html', {
        'active_plans': active_plans,  # Pass active plans to the template
        'already_subscribed': already_subscribed  # Pass the message for the already subscribed plan
    })


def create_order(request, plan_type):
    user = request.user
    # Check if the user already has an active subscription
    if Subscription.objects.filter(user=user, plan_type=plan_type, is_active=True).exists():
        # Use session instead of messages to store the already subscribed plan
        request.session['already_subscribed'] = plan_type
        return redirect('subscription_plans')

    # Amount based on plan type
    plan_amounts = {
        'monthly_3': 14900,  # Amount in paise (₹149)
        'monthly_6': 49900,  # Amount in paise (₹499)
        'yearly': 99900,     # Amount in paise (₹999)
    }
    amount = plan_amounts.get(plan_type, 0)

    # Create Razorpay order
    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency='INR', payment_capture='1'))

    # Store order details in session to use after payment completion
    request.session['order_id'] = razorpay_order['id']
    request.session['amount'] = amount
    request.session['plan_type'] = plan_type

    return render(request, 'payment.html', {
        'order_id': razorpay_order['id'],
        'amount': amount,
        # 'razorpay_key_id': settings.RAZORPAY_KEY_ID
    })

def payment_success(request):
    # Retrieve order details from session
    order_id = request.session.get('order_id')
    amount = request.session.get('amount')
    plan_type = request.session.get('plan_type')

    # Check payment verification and capture response (Here you need Razorpay verification logic)
    # For now, let's assume payment is successful
    Subscription.objects.create(user=request.user, plan_type=plan_type, amount=amount/100, is_active=True)
    
    messages.success(request, "Payment is completed!")
    context={}
    h=hollywood.objects.filter(is_active=True)
    t=tamilMovies.objects.filter(is_active=True)
    ws=webseries.objects.filter(is_active=True)
    a=anime.objects.filter(is_active=True)
    k=korean.objects.filter(is_active=True)
    context['hmovies']=h
    context['tmovies']=t
    context['WSmovies']=ws
    context['Amovies']=a
    context['Kmovies']=k
    return render(request,'index.html',context)
    # return HttpResponse('<h1 style="color:green;"><i class="fas fa-check-circle"></i> Payment is completed!</h1>')

def payment_failure(request):
    return HttpResponse('<h1 style="color:red;"><i class="fas fa-times-circle"></i> Payment failed!</h1>')


def search_results(request):
    query = request.GET.get('q')
    hollywood_movies = hollywood.objects.filter(title__icontains=query) if query else []
    tamil_movies = tamilMovies.objects.filter(title__icontains=query) if query else []
    webseries_movies = webseries.objects.filter(title__icontains=query) if query else []
    anime_movies = anime.objects.filter(title__icontains=query) if query else []
    korean_movies = korean.objects.filter(title__icontains=query) if query else []

    context = {
        'query': query,
        'hollywood_movies': hollywood_movies,
        'tamil_movies': tamil_movies,
        'webseries_movies': webseries_movies,
        'anime_movies': anime_movies,
        'korean_movies': korean_movies,
        'not_found': not (hollywood_movies.exists() or tamil_movies.exists() or webseries_movies.exists() or anime_movies.exists() or korean_movies.exists())
    }

    return render(request, 'search_results.html', context)


def hollywood_details(request, id):
    movie = get_object_or_404(hollywood, id=id)  # Fetch the movie by ID
    context = {
        'hmovies': [movie],  # Pass the movie as a list to match the template's for loop
    }
    return render(request, 'Hollywood.html', context)

def tamilmovie_details(request, id):
    movie = get_object_or_404(tamilMovies, id=id)
    context = {
        'tmovies': [movie], 
    }
    return render(request,'TamilMovies.html', context)
    
def webseries_details(request, id):
    movie = get_object_or_404(webseries, id=id)
    context = {
        'WSmovies': [movie], 
    }
    return render(request, 'WebSeries.html', context)

def anime_details(request, id):
    movie = get_object_or_404(anime, id=id)
    context = {
        'Amovies': [movie], 
    }
    return render(request, 'Anime.html', context)

def korean_details(request, id):
    movie = get_object_or_404(korean, id=id)
    context = {
        'Kmovies': [movie], 
    }
    return render(request, 'Korean.html', context)


                            #footer

@login_required
def myaccount(request):
    user = request.user
    # Retrieve all active subscriptions for the user
    subscriptions = Subscription.objects.filter(user=user, is_active=True)

    if subscriptions.exists():
        context = {
            'subscriptions': subscriptions
        }
    else:
        context = {
            'error': 'No active subscriptions found for your account.'
        }

    return render(request, 'MyAccount.html', context)

def appletv(request):
    return render(request, 'appletv.html')

def Collection(request):
    return render(request, 'collection.html')

def Devices(request):
    return render(request, 'Devices.html')

def FAQ(request):
    return render(request, 'FAQ.html')

def HBO(request):
    return render(request, 'HBO.html')

def MAX(request):
    return render(request, 'Max.html')

def Mpopular(request):
    return render(request, 'Mpopular.html')

def Peacock(request):
    return render(request, 'peacock.html')

def Privacy(request):
    return render(request, 'privacy.html')

def Security(request):
    return render(request, 'security.html')

def Terms(request):
    return render(request, 'terms.html')

def Theater(request):
    return render(request, 'theater.html')

def Guide(request):
    return render(request, 'UserGuide.html')


