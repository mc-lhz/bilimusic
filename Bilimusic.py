import requests
import os, sys
import subprocess

# 定义请求头，包含浏览器信息、cookie等，用于模拟浏览器请求
def get_recommend():
    # 请求的 URL
    url = "https://api.bilibili.com/x/web-interface/region/feed/rcmd"

    # 请求参数
    params = {
        "display_id": 1,
        "request_cnt": 15,
        "from_region": 1003,
        "device": "web",
        "plat": 30,
        "web_location": 333.40138,
        "w_rid": "d4a867ec7ab52b57f8aaadef953ece06",
        "wts": 1742576655
    }

    # 请求头（模拟浏览器行为）
    headers = {
        "authority": "api.bilibili.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

    # Cookies（包含用户身份信息）
    cookies = {
        "buvid3": "589FE849-0846-DF63-67D5-5B42D9939B1454369infoc",
        "b_nut": "1740146254",
        "_uuid": "10106F13E8-AF56-B10DD-63510-FDF64FFAB66270584infoc",
        "CURRENT_FNVAL": "4048",
        "buvid_fp": "bfa2330b06f0a6fe29fcac1baf2b851d",
        "rpdid": "|(u))kkuJ)JR0J'u~RuRRk|~k",
        "bili_ticket": "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDI4MTY0MjksImlhdCI6MTc0MjU1NzE2OSwicGx0IjotMX0.cLdrW2Jc9JexyRZMGiBSEcv-fXjKoyMAshzodjL1Z6c",
        "bili_ticket_expires": "1742816369",
        "buvid4": "17DDDE58-0A92-F8FB-37DC-6D5254E2018972277-025030813-6sIZ%2BmOosHLlAHu5QyzvOQ%3D%3D"
    }

    # 发送 GET 请求
    response = requests.get(url, params=params, headers=headers, cookies=cookies)
    # 检查响应状态码（若失败则抛出异常）
    response.raise_for_status()
    # 解析JSON数据并提取视频列表
    song_list = response.json()['data']['archives']
    # 存储视频信息的列表
    songs = []
    for i in song_list:
        # 提取关键信息存入字典
        songs.append({'bvid': i['bvid'], 'title': i['title']})
    # 打印推荐列表
    i1 = 0
    for i in songs:
        print(i1 + 1, i['title'])
        i1 += 1
    return songs

# 定义搜索用的请求头（包含Edge浏览器标识）
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
    "cookie": 
    (
        "buvid3=589FE849-0846-DF63-67D5-5B42D9939B1454369infoc; "
        "b_nut=1740146254; "
        "_uuid=10106F13E8-AF56-B10DD-63510-FDF64FFAB66270584infoc; "
        "CURRENT_FNVAL=4048; "
        "buvid_fp=bfa2330b06f0a6fe29fcac1baf2b851d; "
        "buvid4=17DDDE58-0A92-F8FB-37DC-6D5254E2018972277-025030813-6sIZ+mOosHLlAHu5QyzvOQ==; "
        "rpdid=|(u))kkuJ)JR0J'u~RuRRk|~k; "
        "b_lsid=2BD9B3CE_195B8810975; "
        "bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDI4MjksImlhdCI6MTc0MjU1NzE2OSwicGx0IjotMX0.cLdrW2Jc9JexyRZMGiBSEcv-fXjKoyMAshzodjL1Z6c; "
        "bili_ticket_expires=1742816369; "
        "sid=o1vyn3mw"
    )
}

# 定义搜索函数，根据输入的关键词搜索视频
def search(inp):
    # 构建搜索的 API URL（包含关键词参数）
    web = "https://api.bilibili.com/x/web-interface/search/type?&keyword=" + inp + "&search_type=video"
    # 发送 GET 请求获取搜索结果
    r1 = requests.get(web, headers=headers)
    # 解析JSON数据
    r1 = r1.json()
    # 提取搜索结果列表
    search_list = r1['data']['result']
    return search_list

# 定义选择函数，让用户从搜索结果中选择一个视频
def choose(search_list):
    # 存储视频的 BVID
    bvids = []
    # 用于记录当前结果的序号
    i1 = 0
    print("键入e返回搜索")
    # 遍历搜索结果列表
    for i in search_list:
        # 提取视频的 BVID
        search = i['bvid']
        bvids.append(search)
        # 打印视频标题（去除HTML标签）
        print(i1 + 1, i['title'].replace('<em class="keyword">', "").replace("</em>", ""))
        i1 += 1
    # 获取用户输入
    num = input()
    if num == 'e':
        return 0
    # 根据用户输入的序号获取对应的 BVID
    bv = bvids[int(num) - 1]
    return bv

# 定义获取音频文件的函数
def get_mp3(bv):
    # 重新定义请求头（用于获取视频信息）
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
    # 获取视频的分 P 信息（需要cid来获取真实播放地址）
    response = requests.get("https://api.bilibili.com/x/player/pagelist?bvid=" + bv, headers=headers)
    # 解析JSON数据
    r = response.json()
    # 提取视频的cid（内容标识符）
    cid = r['data'][0]['cid']
    print(cid)
    # 构建获取视频播放地址的URL
    url = "https://api.bilibili.com/x/player/playurl?fnval=80&cid=" + str(cid) + "&bvid=" + str(bv)
    # 重新定义请求头（包含referer和user-agent）
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    }
    # 获取视频播放地址信息
    response = requests.get(url, headers=headers)
    # 提取音频的备份URL（选择最后一个备用地址）
    url = response.json()['data']['dash']['audio'][-1]["backup_url"][1]
    try:
        # 下载音频文件
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # 保存为music.mp3
            with open('music.mp3', 'wb') as f:
                f.write(response.content)
            print("音频文件保存成功！")
            # 自动打开音频文件（依赖系统默认播放器）
            os.system('music.mp3')
        else:
            print(f"请求失败，状态码: {response.status_code}")
    except requests.RequestException as e:
        print("请求出现异常:", e)

# 主循环，持续提供服务
while 1:
    print("欢迎使用Bilimusic")
    print("键入q退出，以下为推荐内容，可输入序号或输入搜索内容")
    songs = get_recommend()  # 获取推荐列表
    keyword = input()        # 获取用户输入
    if keyword == 'q':
        sys.exit()           # 退出程序
    
    # 尝试直接选择推荐列表中的视频
    try:
        if int(keyword) <= 15:
            song = songs[int(keyword) - 1]
            bv = song['bvid']
            get_mp3(bv)      # 下载音频
            os.system('cls') # 清屏
            continue
    except Exception as e:
        print(e)
    
    # 执行关键词搜索
    search_list = search(keyword)
    os.system('cls')
    # 用户选择搜索结果
    bv = choose(search_list)
    if bv != 0: 
        get_mp3(bv)          # 下载音频
    os.system('cls')