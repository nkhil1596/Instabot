import urllib
import requests
from key import ACCESS_TOKEN
insta_user_name='jakhmolanidhi22'
BASE_URL = 'https://api.instagram.com/v1/'
# get self info
def self_info():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
  print 'Requesting info for:'+  (request_url)
  my_info = requests.get(request_url).json()
  print 'my info is/n',my_info
self_info();


def getDetails():
    url = "https://api.instagram.com/v1/users/search?q=jakhmolanidhi22&access_token=5793537413.13b9c2a.0e37b8ae91714cdfab5ae87559175055";
    obj = requests.get(url);
    print obj.json();
getDetails();

def get_user_id(insta_user_name):
  request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_user_name, ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()
  print 'user info is/n',user_info
  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      return user_info['data'][0]['id']
      print 'Username: %s' % (user_info['data']['username'])
      print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_info['data']['counts']['media'])
    else:
      return None
  else:
    print 'Something went wrong..please try later!'
    exit()

get_user_id(insta_user_name);

def get_own_post():
  request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
  print 'GET request url: %s' % (request_url)
  own_media=requests.get(request_url).json()
  if (own_media['meta']['code']) == 200:
    if len(own_media['data']):
     return own_media['data'][0]['id']
    else:
     print 'no post to show'
  else:
    print 'something is wrong'
    return None

get_own_post();



def get_user_post(insta_user_name):
  user_id=get_user_id(insta_user_name)
  if user_id == None:
    print 'User does not exist'
    exit
  request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id , ACCESS_TOKEN)
  print 'GET request url: %s' % (request_url)
  user_media=requests.get(request_url).json()
  # print 'user media/n',user_media
  if user_media['meta']['code'] == 200:
    if len(user_media['data']):
      image_name = user_media['data'][0]['id'] + '.jpeg'
      image_url = user_media['data'][0]['images']['standard_resolution']['url']
      urllib.urlretrieve(image_url, image_name)
      print 'Your image has been downloaded!'
    else:
      print 'Post does not exist!'
  else:
    print 'Something went wrong..please try later!'

get_user_post(insta_user_name)



def get_id_post(insta_user_name):
  user_id=get_user_id(insta_user_name)
  if user_id == None:
    print 'User does not exist'
    exit
  request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id , ACCESS_TOKEN)
  print 'GET request url: %s' % (request_url)
  user_media=requests.get(request_url).json()
  if user_media['meta']['code'] == 200:
    if len(user_media['data']):
      return user_media['data'][0]['id']
    else:
      print 'Post does not exist!'
  else:
    print 'Something went wrong..please try later!'

get_id_post(insta_user_name);



def like_user_post(insta_username):
  media_id = get_id_post(insta_username)
  request_url = (BASE_URL + 'media/%s/likes') % (media_id)
  payload = {"access_token": ACCESS_TOKEN}
  print 'POST request url : %s' % (request_url)
  like_media = requests.post(request_url, payload).json()
  if like_media['meta']['code'] == 200:
    print 'Like was successful!'
  else:
    print 'Your like was unsuccessful. Try again!'
like_user_post(insta_user_name)


def comment_user_post(insta_username):
  media_id=get_id_post(insta_user_name)
  text_comment=raw_input('enter your text:')
  request_url = (BASE_URL + 'media/%s/comments') % (media_id)
  payload = {"access_token": ACCESS_TOKEN , "text":text_comment}
  print 'POST request url : %s' % (request_url)
  comment_media = requests.post(request_url, payload).json()
  if comment_media['meta']['code'] == 200:
    print 'comment was successful!'
  else:
    print 'Your comment was unsuccessful. Try again!'


comment_user_post(insta_user_name)
