import requests
import os
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "cookie": (
        "******************8; "
        "b_nut=1719071015; "
        "_uuid=F2B81DF1************************************E2D8F9****************************622infoc; "
        "rpdid=|(u))kkuJ)Y|0J'u~um|~u||u; "
        "buvid_fp_plain=undefined; "
        "DedeUserID=1121746503; "
        "DedeUserID__ckMd5=***************ac73; "
        "is-2022-channel=1; "
        "enable_web_push=DISABLE; "
        "header_theme_version=CLOSE; "
        "CURRENT_BLACKGAP=0; "
        "LIVE_BUVID=AUTO**************************739313; "
        "hit-dyn-v2=1; "
        "************************************************0dz*********************************************************************1NGk0OU9pelF3IIEC; "
        "bili_jct=9b6ab94157366951e93778c544591257; "
        "buvid4=6D4EBA1D-335F-1EF**********************80377B1E90682-024062215-Cn7gsFR9A0msFc2f7MvSKA%3D%3D; "
        "PVID=1; "
        "enable_feed_channel=ENABLE; "
        "bili_ticket=eyJhbGciOi*****************************************************CI6IkpXVCJ9.eyJleHAiOjE3NDE2MDk5NTEsImlhdCI6MTc0MTM1MDY5MSwicGx0IjotMX0.q6nDi80gGASxUynYD8LDdeBR3M**********************************kWA; "
        "bili_ticket_expires=174********************91; "
        "fingerprint=5a65491389cb******************************75596e876c3c6; "
        "buvid_fp=77670bc64d354c**********55eeb755fb; "
        "CURRENT_QUALITY=80; "
        "bp_t_offset_112174************69263273984; "
        "home_feed_column=5; "
        "sid=8t9g3j5u; "
        "browser_resolution=1857-997; "
        "b_lsid=62EEB6FF_1957155DFF7; "
        "CURRENT_FNVAL=4048"
    )
}
web="https://api.bilibili.com/x/web-interface/search/type?&keyword="+input()+"&search_type=video"
r1=requests.get(web,headers=headers).json()
print(r1)
print(r1['data']['result'])



search_list=r1['data']['result']
bvids=[]
i1=0
print('e exit')
for i in search_list:
    search=i['bvid']
    
    bvids.append(search)
    
    print(i1+1,i['title'].replace('<em class="keyword">', "").replace("</em>", ""))
    i1+=1
num=input()
if(num)=="e":
    os.system(__file__)
bv=bvids[int(num)-1]
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    
}
response = requests.get("https://api.bilibili.com/x/player/pagelist?bvid="+bv,headers=headers)
url = "https://cn-hnzz-cm-01-15.bilivideo.com/upgcxcode/07/47/746904707/746904707-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1736009771&gen=playurlv2&os=bcache&oi=1882206393&trid=0000d7638e396bb04c2b9cf5cf6e42064634u&mid=1121746503&platform=pc&og=cos&upsig=62256754b4208e09e374a1153c95c5c7&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=40050&bvc=vod&nettype=0&orderid=0,3&buvid=96D878EF-C1CC-C000-CA1F-D506816A588390682infoc&build=0&f=u_0_0&agrr=0&bw=16345&logo=80000000"


r=response.json()
cid=r['data'][0]['cid']
print(cid)
url="https://api.bilibili.com/x/player/playurl?fnval=80&cid="+str(cid)+"&bvid="+str(bv)
headers = {
    'referer':'https://www.bilibili.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
}
response = requests.get(url, headers=headers)
print(response.json())
url=response.json()['data']['dash']['audio'][-1]["backup_url"][1]
# url="https://upos-sz-mirrorali.bilivideo.com/upgcxcode/07/47/746904707/746904707-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1741378497\u0026gen=playurlv2\u0026os=alibv\u0026oi=1882213834\u0026trid=1c28ec02e2264c5a9ddbd38b132f4be2u\u0026mid=1121746503\u0026platform=pc\u0026og=cos\u0026upsig=474cd64a2293bb8a07412615bc48308e\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026buvid=96D878EF-C1CC-C000-CA1F-D506816A588390682infoc\u0026build=0\u0026f=u_0_0\u0026agrr=1\u0026bw=16345\u0026logo=40000000"
try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open('music.mp3', 'wb') as f:
            f.write(response.content)
        print("音频文件保存成功！")
        os.system("music.mp3")
    else:
        print(f"请求失败，状态码: {response.status_code}")
except requests.RequestException as e:
    print("请求出现异常:", e)
os.system(__file__)