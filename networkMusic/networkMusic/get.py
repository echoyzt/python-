import requests

search_url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord'

search_headers = {
    'Referer': 'http://www.kuwo.cn/search/list?key=',
    'Cookie': '_ga=GA1.2.1233562358.1618054313; _gid=GA1.2.983479161.1625207491; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1625207491,1625268303,1625268411; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1625269465; kw_token=YO4OH2VYH1A',
    'csrf': 'YO4OH2VYH1A'}

search_params = {
'key': 'str',   # 查找关键字
'pn': '1',  # 页数
'rn': '20', # 项数
'httpsStatus': '1',
'reqId': '6e028fc0-db8f-11eb-b6f5-ff7d54a57f2b'
}

from_url = 'http://www.kuwo.cn/url'
  
from_params = {
    'rid': '148526468', # 歌曲 rid
    'type': 'convert_url3',
    'br': '128kmp3',
}

lrc_url = 'http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId={rid}'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59'}

class GetError(BaseException):
    pass

class Kuwo:
    def search_kuwo(self, kw):#
        search_params.update({'key': kw})

        try:
            response = requests.get(search_url,
                                    params=search_params,
                                    headers={**headers, **search_headers},
                                    timeout=2,
                                    ).json()
        except:
            response = dict()

        datas = response.get('data', {}).get('list', {})

        result = [[r.get('name', ''),
                   r.get('artist', ''),
                   r.get('album', ''),
                   r.get('songTimeMinutes', ''),
                   r.get('pic', ''),
                   r.get('pic120', ''),
                   r.get('rid', '')]
                  for r in datas]

        return result

    def get_music_url(self, rid):#
        from_params['rid'] = rid
        url = requests.get(from_url, params=from_params, headers=headers, timeout=2).json()['url']

        return url

    def get_music_content(self, rid):
        url = self.get_music_url(rid)
        try:
            content = requests.get(url, headers=headers, timeout=2).content
        except:
            raise GetError(f'{rid} song can\'t get.')

        return content

    def get_music_lrc(self, rid):
        try:
            lrc_data = requests.get(lrc_url.format(rid=rid), headers=headers, timeout=2).json()
        except:
            return [('暂无歌词', '0')]


        lrc_list = lrc_data.get('data', {}).get('lrclist', [{1: '无歌词', 2: '0'}])

        if not lrc_list:
            return [('暂无歌词', '0')]

        lrc = [list(l.values()) for l in lrc_list]

        return lrc

    def get_pic(self, url):
        try:
            pic = requests.get(url, headers=headers).content
        except:
            raise GetError(f'{url} image can\'t get.')
        
        return pic
