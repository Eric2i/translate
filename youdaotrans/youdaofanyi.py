import urllib.request
import urllib.parse
import json
import os
trans = input('Please type in what you want to be translated:\n')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
data = {}
data['type'] = 'AUTO'
data['i'] = trans
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'yetrue'
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
results = json.loads(html)
text_in = results['translateResult'][0][0]['src']
text_out = results['translateResult'][0][0]['tgt']
if text_out != text_in :
    print(text_in + '------>' + text_out)
    print('other answers:')
else:
    print('I can\'t translate the word you type in, but maybe the answers are:')
for i in range(len(results['smartResult']['entries'])):
    if i !=0:
        print(results['smartResult']['entries'][i]+ ' ;')
os.system('pause')
