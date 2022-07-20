import re
def s(url):
    m = re.fullmatch(r'https?://([^/]+).*',url)
    if m ==