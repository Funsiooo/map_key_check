import requests

def banner():
    banner = r'''
       .__                   __    
  ____ |  |__   ____   ____ |  | __
_/ ___\|  |  \_/ __ \_/ ___\|  |/ /
\  \___|   Y  \  ___/\  \___|    < 
 \___  >___|  /\___  >\___  >__|_ \
     \/     \/     \/     \/     \/ 
    http://github.com/Funsiooo By Funsiooo
    '''

    print(banner)

def check():
    try:
        key = input("[*] 请输入需要进行检测的地图 Key : ")

        if not key:
            print(f"[*] Key 值不能为空,请重新运行。")
            return
        
        print(f"[*] 正在检测")

        # 腾讯地图
        tencent_api_one = f"https://apis.map.qq.com/ws/place/v1/search?boundary=nearby(··)&keyword=%E5%85%AC%E5%9B%AD&page_size=10&page_index=1&key={key}"
        tencent_api_two = f"https://apis.map.qq.com/ws/geocoder/v1?location=28.7033487,115.8660847&key={key}"
        
        try:
            tencent_api_one_requests = requests.get(tencent_api_one,timeout=5)
            if tencent_api_one_requests.status_code == 200:
                tencent_api_one_response = tencent_api_one_requests.json()

                if '北京' in str(tencent_api_one_response):
                    print(f"[*] 检测到腾讯地图 Api Key")
                    print(f"[*] 验证地址: {tencent_api_one}")
                    return
        except requests.RequestException as e:
            print(f"[*] 请求错误，检测网络连接情况:{e}")
        
        try:
            tencent_api_two_requests = requests.get(tencent_api_two,timeout=5)
            if tencent_api_two_requests.status_code == 200:
                tencent_api_two_response = tencent_api_two_requests.json()

                if '江西' in str(tencent_api_two_response):
                    print(f"[*] 检测到腾讯地图 Api Key")
                    print(f"[*] 验证地址: {tencent_api_two}")
                    return
        except requests.RequestException as e:
            print(f"[*] 请求错误，检测网络连接情况:{e}")

        # 高德地图
        amap_api_one = f"https://restapi.amap.com/v3/geocode/geo?address=北京市朝阳区阜通东大街6号&output=XML&key={key}"
        amap_api_one_requests = requests.get(amap_api_one,timeout=5)

        try:
            if amap_api_one_requests.status_code == 200:
                amap_api_one_response = amap_api_one_requests.text

                if "北京市朝阳区阜通东大街6号院" in str(amap_api_one_response):
                    print(f"[*] 检测到高德地图 Api Key")
                    print(f"[*] 验证地址: {amap_api_one}")
                    return
        except requests.RequestException as e:
            print(f"[*] 请求错误，检测网络连接情况:{e}")


        # 百度地图
        baidu_api_one = f"https://api.map.baidu.com/place/v2/search?query=银行&location=39.915,116.404&radius=2000&output=json&ak={key}"
        baidu_api_one_requests = requests.get(baidu_api_one,timeout=5)

        try:
            if baidu_api_one_requests.status_code == 200:
                baidu_api_one_response = baidu_api_one_requests.text

                if "北京市" in str(baidu_api_one_response):
                    print(f"[*] 检测到百度地图 Api Key")
                    print(f"[*] 验证地址: {baidu_api_one}")
                    return
        except requests.RequestException as e:
            print(f"[*] 请求错误，检测网络连接情况:{e}")

        # 天地图
        tianditu_api_one = f"https://api.tianditu.gov.cn/geocoder?postStr=%7B%2527lon%2527%3A116.37304%2C%2527lat%2527%3A39.92594%2C%2527ver%2527%3A1%7D&type=geocode&tk={key}"
        tianditu_api_two = f"https://api.tianditu.gov.cn/v2/administrative?keyword=156110000&childLevel=0&extensions=true&tk={key}"

        tian_headers = {
            "Cookie": "HWWAFSESID=192ad3c16a99f15e64e; HWWAFSESTIME=1733314808706; TDTSESID=f742224fc9e18085c6dc7098d1de5b66|e3a685faf3d6f307e30c6070682303b5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }

        try:
            tianditu_api_one_requests = requests.get(tianditu_api_one,headers=tian_headers,timeout=5)
            if tianditu_api_one_requests.status_code == 200:
                tianditu_api_one_response = tianditu_api_one_requests.text

                if "北京市" in str(tianditu_api_one_response):
                    print(f"[*] 检测到天地图 Api Key")
                    print(f"[*] 验证地址: {tianditu_api_one}")
                    return
        except requests.RequestException as e:
            print(f"[*] 请求错误，检测网络连接情况:{e}")


        tianditu_api_two_requests = requests.get(tianditu_api_two,headers=tian_headers,timeout=5)

        try:
            if tianditu_api_two_requests.status_code == 200:
                tianditu_api_two_response = tianditu_api_two_requests.text

                if "北京市" in str(tianditu_api_two_response):
                    print(f"[*] 检测到天地图 Api Key")
                    print(f"[*] 验证地址: {tianditu_api_two}")
                    return
        except requests.RequestException as e:
            print(f"[*] 请求错误，检测网络连接情况:{e}")

        else:
            print("[*] Key 值无效,或未通过验证。")
            return
        
    except Exception as e:
        print(f"[*] 程序运行错误:{e}")

if __name__ == "__main__":
    banner()
    check()
