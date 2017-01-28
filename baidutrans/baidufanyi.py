import urllib.request
import urllib.parse
import json
import os
import langdetect
trans = input('Please type in what you want to be translated:')
language = langdetect.det(trans)
if language == 'zh':ResLang = 'en'
if language == 'en':ResLang = 'zh'
url = 'http://fanyi.baidu.com/v2transapi'
data = {}
data['from'] = language
data['to'] = ResLang
data['query'] = trans
data['transtype'] = 'realtime'
data['simple_means_flag'] = '3'
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
results = json.loads(html)
text_out = results['trans_result']['data'][0]['dst']
if 'from' in results['dict_result']:
    results['dict_result']['from'] == 'kingsoft'
    print(trans + '------>' + text_out)
    if 'tag' in results['liju_result'].keys():
        print('other answers:')
        for i in range(len(results['liju_result']['tag'])):
            print(results['liju_result']['tag'][i]+ ' ;')
else:
    print('I can\'t translate the word you type in, but maybe the answers are:')
    print(text_out)

os.system('pause')
