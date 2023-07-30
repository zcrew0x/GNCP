__author__ = 'Kyle Tran'
__version__ = '1.2'
__github__ = 'github.com/kyletran191'
__license__ = 'GNU General Public License v3.0'
#=====Import Module=====#
import os, sys, requests, json, re, datetime, threading, time
from pystyle import *
from os import name 
#=====Banner=====#
text = r"""
 .d8888b.  888b    888  .d8888b.  8888888b.  
d88P  Y88b 8888b   888 d88P  Y88b 888   Y88b 
888    888 88888b  888 888    888 888    888 
888        888Y88b 888 888        888   d88P 
888  88888 888 Y88b888 888        8888888P"  
888    888 888  Y88888 888    888 888        
Y88b  d88P 888   Y8888 Y88b  d88P 888        
 "Y8888P88 888    Y888  "Y8888P"  888   

           By @tranbaokha    
"""[:-1]

banner = Add.Add(text, '', center=True)
dark = Col.dark_gray
light = Col.light_gray
cyan = Col.light_blue
purple = Colors.StaticMIX((Col.purple, Col.blue))
bpurple = Colors.StaticMIX((Col.purple, Col.blue, Col.blue))
#=====Main=====#
class run_proxy():
    #=====Get Proxy from github and another site=====#
    def __init__(self) -> None:
        self.api = {
    'socks4':["https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all","https://www.proxy-list.download/api/v1/get?type=socks4","https://www.proxyscan.io/download?type=socks4","https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt","https://api.openproxylist.xyz/socks4.txt","https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt","https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt','https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt','https://proxylist.live/nodes/socks4_1.php?page=1&showall=1','https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt','https://openproxy.space/list/socks4','https://github.com/hanwayTech/free-proxy-list/blob/main/socks4.txt','https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt','https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/socks4.txt','https://proxyspace.pro/socks4.txt','https://raw.githubusercontent.com/ObcbO/getproxy/master/socks4.txt''https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt'],
    'socks5': ["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true","https://www.proxy-list.download/api/v1/get?type=socks5","https://www.proxyscan.io/download?type=socks5","https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt","https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt","https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt","https://api.openproxylist.xyz/socks5.txt","https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt','https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt','https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt','https://github.com/hanwayTech/free-proxy-list/blob/main/socks5.txt','https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt','https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt','https://openproxy.space/list/socks5','https://proxylist.live/nodes/socks5_1.php?page=1&showall=1','https://spys.me/socks.txt','https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/socks5.txt','https://proxyspace.pro/socks5.txt','https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt',],
    'http': ["https://api.proxyscrape.com/?request=displayproxies&proxytype=http","https://www.proxy-list.download/api/v1/get?type=http",'https://www.proxy-list.download/api/v1/get?type=https'"https://www.proxyscan.io/download?type=http","https://spys.me/proxy.txt","https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt","https://api.openproxylist.xyz/http.txt","https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt","http://alexa.lr2b.com/proxylist.txt","http://rootjazz.com/proxies/proxies.txt","https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt","https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt","https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt","https://proxy-spider.com/api/proxies.example.txt","https://multiproxy.org/txt_all/proxy.txt","https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt","https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt","https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt",'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt','https://openproxy.space/list/http','https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt','https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt','https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt','https://raw.githubusercontent.com/almroot/proxylist/master/list.txt','https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt','https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt','https://proxylist.live/nodes/free_1.php?page=1&showall=1','https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/http.txt','https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/https.txt','https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt','https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt','https://raw.githubusercontent.com/rx443/proxy-list/online/all.txt','https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/http.txt','https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/https.txt','https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt','https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxy-list/data.txt','https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt''https://raw.githubusercontent.com/ObcbO/getproxy/master/http.txt''https://raw.githubusercontent.com/ObcbO/getproxy/master/https.txt''https://rootjazz.com/proxies/proxies.txt','https://proxyspace.pro/http.txt','https://proxyspace.pro/https.txt''https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt']
    }
        self.proxy_dict = {'socks4':[],'socks5':[],'http':[]}
        pass
    def get1(self):
        proxy_list = []
        try:
            r = requests.get("https://www.socks-proxy.net/",timeout=5)
            part = str(r.text)
            part = part.split("<tbody>")
            part = part[1].split("</tbody>")
            part = part[0].split("<tr><td>")
            proxies = ""
            for proxy in part:
                proxy = proxy.split("</td><td>")
                try:
                    if proxies != '':
                        proxies = proxies + proxy[0] + ":" + proxy[1] + "\n"
                        if proxies != '':
                            proxy_list += proxies.split('\n')
                except:
                    pass
                
            return proxy_list
        except:
            return []
    def get2(self):
        for q in range(20):
            self.count = {'http':0,'socks5':0}
            self.day = datetime.date.today() + datetime.timedelta(-q)
            self.r = requests.get('https://checkerproxy.net/api/archive/{}-{}-{}'.format(self.day.year,self.day.month,self.day.day))
            if self.r.text != '[]': 
                self.json_result = json.loads(self.r.text)
                for i in self.json_result:
                    if i['ip'] == '172.23.0.1':
                        if i['type'] in [1,2] and i['addr'] in self.proxy_dict['http']:
                            self.proxy_dict['http'].remove(i['addr'])
                        if i['type'] == 4 and i['addr'] in self.proxy_dict['socks5']:
                            self.proxy_dict['socks5'].remove(i['addr'])
                    else:
                        if i['type'] in [1,2] :
                            self.count['http'] += 1
                            self.proxy_dict['http'].append(i['addr'])
                        if i['type'] == 4 :
                            self.count['socks5'] += 1
                            self.proxy_dict['socks5'].append(i['addr'])
                print('\033[1;97m[\033[1;92m'+datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\033[1;97m] [\033[1;92mSUCCESS\033[1;97m] Got {} http proxy from {}'.format(self.count['http'],self.r.url))
                print('\033[1;97m[\033[1;92m'+datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\033[1;97m] [\033[1;92mSUCCESS\033[1;97m] Got {} socks5 proxy from {}'.format(self.count['socks5'],self.r.url))
        
        self.proxy_dict['socks4'] = list(set(self.proxy_dict['socks4']))
        self.proxy_dict['socks5'] = list(set(self.proxy_dict['socks5']))
        self.proxy_dict['http'] = list(set(self.proxy_dict['http']))
    def get(self):
        self.proxy_dict['socks4'] += self.get1()
        self.get2()
        
        for type in ['socks4','socks5','http']:
            for api in self.api[type]:
                self.proxy_list = []
                try:
                    self.r = requests.get(api,timeout=5)
                    if self.r.status_code == requests.codes.ok :
                        self.proxy_list += re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}',self.r.text)
                        self.proxy_dict[type] += list(set(self.proxy_list))
                        print('\033[1;97m[\033[1;92m'+datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\033[1;97m] [\033[1;92mSUCCESS\033[1;97m] Got {} {} proxy from {}'.format(len(self.proxy_list),type,api))
                except:
                    pass

    
    #=====Save proxy to 3 file with 3 type http, socks4 and socks5=====#
    def save(self):
        for type in ['socks4','socks5','http']:
            self.proxy_dict[type] = list(set(self.proxy_dict[type]))
            self.out_file = './{}.txt'.format(type)
            f = open(self.out_file,'w')
            for i in self.proxy_dict[type]:
                if '#' in i or i == '\n':
                    self.proxy_dict[type].remove(i)
                else:
                    f.write(i + '\n')
            print('\033[1;97m[\033[1;92m'+datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\033[1;97m] [\033[1;92mSUCCESS\033[1;97m] Saved {} proxies list as '.format(len(self.proxy_dict[type])) + self.out_file)
#=====Check 3 proxy list=====#
def check(type):
    dt = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    if type in ['http','https']:
        with open("http.txt","r") as f:
            data=f.read().split("\n")
    else:
        with open("{}.txt".format(type),"r") as f:
            data=f.read().split("\n")
    print('\033[1;97m[\033[1;92m'+datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\033[1;97m] [\033[1;96mINFO\033[1;97m] {} {} proxies will be check'.format(len(data),type))
    
    def process(i):
        try:
            requests.get("http://ip-api.com/json/",proxies={"https":f"{type}://{i}"},timeout=30,)
        except:
            pass
        else:
            with open("{}_checked_{}.txt".format(type, dt),"a+") as f:
                f.write(i+"\n")

    for i in data:
        threading.Thread(target=process,args=(i,)).start()

    while threading.active_count() >1:
        time.sleep(1)
#=====RUN SCRIPT=====#
if __name__ == '__main__':
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(Colorate.Diagonal(Colors.DynamicMIX((purple, cyan)), Center.XCenter(banner)))
    print('\033[1;97m[\033[1;92m'+datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\033[1;97m] [\033[1;96mINFO\033[1;97m] Getting proxies, please wait...')
    run = run_proxy()
    run.get()
    print('\033[1;97m[\033[1;92m'+datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\033[1;97m] [\033[1;96mINFO\033[1;97m] Saving proxies, please wait...')
    run.save()
    print('\033[1;97m[\033[1;92m'+datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\033[1;97m] [\033[1;96mINFO\033[1;97m] Checking http proxies, please wait...')
    check('http')
    print('\033[1;97m[\033[1;92m'+datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\033[1;97m] [\033[1;96mINFO\033[1;97m] Checking socks4 proxies, please wait...')
    check('socks4')
    print('\033[1;97m[\033[1;92m'+datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\033[1;97m] [\033[1;96mINFO\033[1;97m] Checking socks5 proxies, please wait...')
    check('socks5')
    print('\033[1;97m[\033[1;92m'+datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\033[1;97m] [\033[1;96mINFO\033[1;97m] Get & Check proxies successfully. @tranbaokha')
    #=====Delete Uncheck proxies=====#
    os.remove("http.txt")
    os.remove("socks4.txt")
    os.remove("socks5.txt")

