from django.shortcuts import render, redirect
from twilio.rest import Client

# Create your views here.


def index(request):
      if request.method == "POST":
            text = request.POST['text']
            if text:
                  account_sid = 'ACCOUNT_SID' #siz yaratgan accountdan olgan Account_SID  tokeni
                  auth_token = 'AUTH_TOKEN' #siz yaratgan accountdan olgan Auth_token  tokeni
                  client = Client(account_sid, auth_token)

                  message = client.messages.create(
                     body=text,
                     from_='+12136685825', #yuboriladigan raqam
                     to='+998903632710' #qabul qiladigan raqam, Twilioning tekin versiyasida faqat tasdiqlangan raqamga sms jo'natish mumkin.
                 )
                  return redirect('/')
      else:
            pass
      return render(request, 'index.html')



# Create your views here.
