
ROOT_ENDPOINT = "https://api.github.com"
URL_BASE = "https://developer.github.com/v3/"


def reverse_url(url):
    return ''.join([ROOT_ENDPOINT, url])