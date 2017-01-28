import urllib.request
import urllib.parse
url = 'http://fanyi.baidu.com/langdetect'
def det(words):
    data = {'query':words}
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')
    return eval(html)['lan']
