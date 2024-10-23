import os
try:
  import requests
  from faker import Faker
  import random
except:
  os.system("pip install requests faker")
  os.system('clear')
import requests
from faker import Faker
import random


print("""
رشق 100 مشاهدات مجانيه تيك توككك 
BY : AHMED ~~ @maho_s9
""")
link = input("Enter Your TikTok Link : ")
print("_" *60)
faker = Faker()
faker1 = Faker('ru_RU')
faker2 = Faker('fa')
faker3 = Faker('en')
faker4 = Faker('zh')
faker5 = Faker('ar')
faker6 = Faker('ko_KR')
def Ahmed():
    while True:          
      name = faker.name()
      mu = faker.user_name()
      bh = faker1.user_name()
      ch = faker2.user_name()
      dh = faker3.user_name()
      hh = faker4.user_name()
      gh = faker5.user_name()
      bu = faker6.user_name()
      user = random.choice([mu, bh, ch, dh, hh, gh, bu])
      email = user + random.choice(["@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com", "@aol.com", "@mail.ru" "@outlook.sa", "@inbox.com", "@mahos.com"

" @gmail.com",
"@yahoo.com",
". @hotmail.com",
". @outlook.com",
"@icloud.com",
"@aol.com",
"@live.com",
"@mail.com",
"@zoho.com",
"@gmx.com",
"@msn.com",
"@yandex.com",
"@protonmail.com",
"@mail.ru",
"@inbox.com",
"@fastmail.com",
"@hushmail.com",
"@tutanota.com",
"@mailinator.com",
"@rediffmail.com",
"@lynx.co.uk",
"@blueyonder.co.uk",
"@virginmedia.com",
"@talktalk.net",
"@btinternet.com",
"@sbcglobal.net",
"@att.net",
"@comcast.net",
"@bellsouth.net",
"@charter.net",
"@frontier.com",
"@web.de",
" @t-online.de",
"@orange.fr",
"@wanadoo.fr",
"@terra.com.br",
"@uol.com.br",
"@bol.com.br",
" @mail.com.au",
"@optusnet.com.au",
"@bigpond.com",
"@xtra.co.nz",
"@clear.net.nz",
"@yahoo.co.jp",
"@nifty.com",
"@rakuten.co.jp",
"@hinet.net",
"@163.com",
"@126.com",
"@qq.com",
"@live.ca",
"@shaw.ca",
"@telus.net",
"@sympatico.ca",
"@freenet.de",
"@gmx.net",
"@mailbox.org",
"@hushmail.com",
"@myway.com",
"@email.com",
"@fastwebnet.it",
"@alice.it",
"@libero.it",
"@virgilio.it",
"@tiscali.it",
"@wanadoo.nl",
"@xs4all.nl",
"@chello.nl",
"@zonnet.nl",
"@sky.com",
"@talktalk.co.uk",
"@btopenworld.com",
"@fsmail.net",
"@mail.be",
"@skynet.be",
"@telenet.be",
"@hotmail.co.uk",
" @yahoo.co.uk",
"@live.co.uk",
"@outlook.co.uk",
"@sina.com",
"@163.net",
"@sohu.com",
"@tom.com",
"@yeah.net",
"@vip.sina.com",
"@139.com",
"@mail.ee",
"@mail.bg",
"@abv.bg",
"@dir.bg",
"@inbox.ru",
"@list.ru",
"@mail.ru",
"@rambler.ru",
" @yandex.ru",
"@ukr.net",
"@meta.ua",
"@i.ua",
"@bigmir.net"

])
      psw = name + '@' + str(random.randint(111, 999))
      data = f"username={user}&password={psw}&name={name}&email={email}"

      hd = {
  'User-Agent': "Dart/3.1 (dart:io)",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/x-www-form-urlencoded",
  'authorization': "Bearer kasper"
}

      req = requests.post("https://perfectfollow.app/api/v1/register", data=data, headers=hd).json()
      try:
          token = req['token']         
      except:
          token = "69770|RJOSyWwBEy9kLbVGMcBRgPTLvga9bf6I6EbIBCaW"

      url = "https://perfectfollow.app/api/v1/setOrder"

      payload = f"=&username={link}&=&amount=100&type=other&service_id=129"

      headers = {
  'User-Agent': "Dart/3.1 (dart:io)",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/x-www-form-urlencoded",
  'authorization': f"Bearer {token}"
}

      response = requests.post(url, data=payload, headers=headers)

      print(response.json())
      
Ahmed()