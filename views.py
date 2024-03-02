from django.shortcuts import render, HttpResponse
import requests

CLIENT_ID = #enter client id
SECRET = #enter secret
base_url = 'https://www.reddit.com/'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET)
data = {
    'grant_type': 'password',
    'username': #enter reddit username,
    'password': #enter reddit password
    }
headers = {'User-Agent': 'MyAPI/0.0.1'}
res = requests.post(base_url + 'api/v1/access_token', auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# Create your views here.
def index(request):
    context = {'first_title': 'Welcome to RedPot', 'titless':'- Here you will get News And Updates about India and Around the World!'}
    return render(request,'index.html', context)
def worldnews(request):
    r = requests.get('https://oauth.reddit.com/r/worldnews/new', headers=headers)
    resp=r.json()
    titles = []
    for post in resp['data']['children']:
        title = post['data']['title'] + " : " + post['data']['selftext'] + "\n"
        titles.append(title)
    context = {'first_title': 'Around the World:', 'titles': titles[0:],'space':'\n'}
    for title in titles:
        return render(request, 'index.html', context=context)
        #return render(request,'index.html')
def indnews(request):
    r = requests.get('https://oauth.reddit.com/r/indianews/new', headers=headers)
    resp=r.json()
    titles = []
    for post in resp['data']['children']:
        title = post['data']['title'] + " : " + post['data']['selftext'] + "\n"
        titles.append(title)
    context = {'first_title': ' India news:', 'titles': titles[0:],'space':'\n'}
    return render(request, 'index.html', context=context)
        #return render(request,'index.html')
def india(request):
    r = requests.get('https://oauth.reddit.com/r/india/new', headers=headers)
    resp=r.json()
    titles = []
    for post in resp['data']['children']:
        title = post['data']['title'] + " : " + post['data']['selftext'] + "\n"
        titles.append(title)
    context = {'first_title': ' Around India:', 'titles': titles[0:],'space':'\n'}
    return render(request, 'index.html', context=context)
def bol(request):
    r = requests.get('https://oauth.reddit.com/r/Bollywood/new', headers=headers)
    resp=r.json()
    titles = []
    for post in resp['data']['children']:
        title = post['data']['title'] + " : " + post['data']['selftext'] + "\n"
        titles.append(title)
    context = {'first_title': ' Bollywood:', 'titles': titles[0:],'space':'\n'}
    return render(request, 'index.html', context=context)
def inv(request):
    r = requests.get('https://oauth.reddit.com/r/IndiaInvestments/new', headers=headers)
    resp=r.json()
    titles = []
    for post in resp['data']['children']:
        title = post['data']['title'] + " : " + post['data']['selftext'] + "\n"
        titles.append(title)
    context = {'first_title': ' About Investments:', 'titles': titles[0:],'space':'\n'}
    return render(request, 'index.html', context=context)
def gam(request):
    r = requests.get('https://oauth.reddit.com/r/IndianGaming/new', headers=headers)
    resp=r.json()
    titles = []
    for post in resp['data']['children']:
        title = post['data']['title'] + " : " + post['data']['selftext'] + "\n"
        titles.append(title)
    context = {'first_title': ' About Gaming:', 'titles': titles[0:],'space':'\n'}
    return render(request, 'index.html', context=context)
def art(request):
    r = requests.get('https://oauth.reddit.com/r/IndianArt/new', headers=headers)
    resp=r.json()
    titles = []
    for post in resp['data']['children']:
        title = post['data']['title'] + " : " + post['data']['selftext'] + "\n"
        titles.append(title)
    context = {'first_title': ' About Art:', 'titles': titles[0:],'space':'\n'}
    return render(request, 'index.html', context=context)
def sp(request):
    r = requests.get('https://oauth.reddit.com/r/IndiaSpeaks/new', headers=headers)
    resp=r.json()
    titles = []
    for post in resp['data']['children']:
        title = post['data']['title'] + " : " + post['data']['selftext'] + "\n"
        titles.append(title)
    context = {'first_title': ' Politics, Economy & Society:', 'titles': titles[0:],'space':'\n'}
    return render(request, 'index.html', context=context)

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")
