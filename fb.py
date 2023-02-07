from config import *

#In progress, not currently working
msg = 'Testing 123'
post_url = 'https://graph.facebook.com/{}/feed'
payload = {
'message': msg,
'access_token': keys.facebook_access_token
}


r = requests.post(post_url, data=payload)
print(r.text)