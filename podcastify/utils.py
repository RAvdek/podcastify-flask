import os
import httplib
import urllib

STATIC_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'static')


def filter_text(unicode_text):
    return (
        unicode_text
        .encode('ascii', errors='ignore')
        .replace('\n', '')
        .replace('\r', '')
    )


def fetch_article_body(soup):
    # Gets largest div by text volume after deleting bad stuff
    for tag in ['style', 'script']:
        [s.decompose() for s in soup.find_all(tag)]
    div_text = [filter_text(t.text) for t in soup.find_all('div')]
    div_text.sort(key=len, reverse=True)
    return div_text[0]


def speech(query):
    _validate_speech_query(query)
    return _get_speech(query)


def _validate_speech_query(query):
    if 'key' not in query:
        raise RuntimeError('The API key is undefined')
    if 'src' not in query:
        raise RuntimeError('The text is undefined')
    if 'hl' not in query:
        raise RuntimeError('The language is undefined')


def _get_speech(query):
    result = {'error': None, 'response': None}

    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    params = urllib.urlencode(_build_speech_request(query))

    if 'ssl' in query:
        conn = httplib.HTTPSConnection('api.voicerss.org:443')
    else:
        conn = httplib.HTTPConnection('api.voicerss.org:80')

    conn.request('POST', '/', params, headers)

    response = conn.getresponse()
    content = response.read()

    if response.status != 200:
        result['error'] = response.reason
    elif content.find('ERROR') == 0:
        result['error'] = content
    else:
        result['response'] = content

    conn.close()

    return result


def _build_speech_request(query):
    params = {
        'key': '',
        'src': '',
        'hl': '',
        'r': '',
        'c': '',
        'f': '',
        'ssml': '',
        'b64': ''
    }
    for key in query:
        params[key] = query[key]
    return params
