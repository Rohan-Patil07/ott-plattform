from django.db.models.expressions import F
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from ott.models import AdminMaster, videos
from ott.models import User
from django.contrib.auth import authenticate, login


# Create your views here.


def openPage(request):
    return render(request, 'web/home.html')


def seriesPage(request):
    return render(request, 'web/series.html')


def songsPage(request):
    return render(request, 'web/songs.html')


def mylistPage(request):
    return render(request, 'web/mylist.html')


def loginPage(request):
    return render(request, 'web/login.html')


def registerPage(request):
    return render(request, 'web/register.html')


def vPage(request):
    return render(request, 'web/vpage.html')


def seemorePage(request):
    return render(request, 'web/seemore.html')


def removeAdsPage(request):
    return render(request, 'web/buy.html')


def videosPage(request):
    return render(request, 'web/videos.html')


def settingsPage(request):
    jsonData = User.objects.filter(
    user_email=request.session["Email"]).values()
    data = (jsonData)
    articles_list = list(data)
    return render(request, 'web/settings.html', articles_list[0])


def view1page(request):
    return render(request, 'web/view1page.html')


def mychannel(request):
    jsonData = User.objects.filter(
    user_email=request.session["Email"]).values()
    data = (jsonData)
    articles_list = list(data)
    return render(request, 'web/mychannel.html', articles_list[0])


def Channel_Content(request):
    return render(request, 'web/Channel_Content.html')


def Channel_settings(request):
    return render(request, 'web/Channel_settings.html')


def Analytics(request):
    return render(request, 'web/Analytics.html')


def myprofilePage(request):
    return render(request, 'web/myprofile.html')


def buyplanPage(request):
    return render(request, 'web/buyplan.html')


def adminPage(request):
    return render(request, 'admin/dashboard.html')


def uploadPage(request):
    return render(request, 'admin/upload.html')


def uploadformPage(request):
    return render(request, 'web/uploadform.html')

def adminuploadform(request):
    return render(request,'admin/adminuploadform.html')


def subscriptionPage(request):
    return render(request, 'web/subscription.html')


def likedPage(request):
    return render(request, 'web/liked.html')


def userlistPage(request):
    return render(request, 'admin/userlist.html')


def watchhistoryPage(request):
    return render(request, 'web/watchhistory.html')


def channelview(request):
    return render(request, 'web/channelview.html')


def reported_videos(request):
    return render(request, 'admin/reported_videos.html')


def admin_videos(request):
    return render(request, 'admin/videos.html')


def userReg(request):
    if User.objects.filter(user_un=request.POST['username']).exists():
        return HttpResponse("10")
    else:
        lclId = User.objects.count()
        lclId = lclId + 1
        User.objects.create(
            user_id=lclId,
            user_un=request.POST['username'],
            user_name=request.POST["name"],
            user_email=request.POST['email-id'],
            user_phone=request.POST['phoneno'],
            user_pw=request.POST['password'],
            user_status="0",
            user_ChannelName=request.POST["name"]
        )
        return HttpResponse("1")


def userLogin(request):
    if User.objects.filter(user_un=request.POST['name'], user_pw=request.POST['password']).exists():
        jsonData = User.objects.filter(user_un=request.POST['name']).values()
        data = list(jsonData)
        listValue = data[0]
        request.session['Email'] = listValue['user_email']
        request.session['channel_name'] = listValue['user_ChannelName']
        print(request.session)
        return HttpResponse("11")

    else:
        return HttpResponse("12")


def Logout(request):
    try:
        del request.session['Email']
    except KeyError:
        pass
    return HttpResponse("29")


def updateView(request):
    User.objects.filter(user_email=request.session['Email']).update(
        user_un=request.POST['username'],
        user_name=request.POST["name"],
        user_email=request.POST['email-id']
    )
    return HttpResponse()


def updatePassword(request):
    if User.objects.filter(user_pw=request.POST['password']).exists():
        User.objects.filter(user_email=request.session['Email']).update(
            user_pw=request.POST["newpassword"]
        )
        return HttpResponse("dn")
    else:
        return print(User.objects.filter(user_pw=request.POST['password']))

def userVideo(request):
    lclId = videos.objects.count()
    lclId = lclId + 1
    videos.objects.create(
        v_id=lclId,
        v_title=request.POST['videoTitle'],
        v_desc =request.POST["videoDesc"],
        v_tags =request.POST['videoTags'],
        v_cat=request.POST['videoCat'],
        v_views=0,
        v_likes=0,
        v_wh=0,
        v_channel_name = request.session['channel_name'],
        v_image= request.FILES['imagee'],
        v_video= request.FILES['videoo'],
        v_status="0"
    )
    return HttpResponse("1")

def getVideos(request):
    json_object = videos.objects.values()
    data = list(json_object)
    value=JsonResponse(data,safe=False)

    return value

def getSongs(request):
    json_object = videos.objects.values()
    data = list(json_object)
    value=JsonResponse(data,safe=False)

    return value

def getViewVideos(request): 
    json_object = videos.objects.filter(v_id=request.POST["txtID"]).values()
    data = list(json_object)
    value=JsonResponse(data,safe=False)
    listValue = data[0]

    videos.objects.filter(v_id=request.POST["txtID"]).update(v_views=listValue['v_views']+1);
    return value

def order(request):
    User.objects.filter(user_email=request.session['Email']).update(
        user_status=1
    )
    return HttpResponse()