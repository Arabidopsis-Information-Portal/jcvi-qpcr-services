import requests
import re
import urlparse
import json

JCVI_BASE_URL = 'http://www.jcvi.org/arabidopsis/qpcr/'
JCVI_BASE_CGI_URL = 'http://www.jcvi.org/cgi-bin/arabidopsis/qpcr/'

def is_valid_agi_identifier(ident):
    p = re.compile(r'AT[1-5MC]G[0-9]{5,5}\.[0-9]+', re.IGNORECASE)
    if not p.search(ident):
        return False
    return True

def do_request(endpoint, **kwargs):
    """Perform a request to SITE and return JSON."""

    url = urlparse.urljoin(JCVI_BASE_URL, endpoint)
    response = requests.get(url, verify=False, params=kwargs)

    # Raise exception and abort if requests is not successful
    response.raise_for_status()

    try:
        # Try to convert result to JSON
        # abort if not possible
        return response.json()
    except ValueError:
        raise Exception('not a JSON object: {}'.format(response.text))

def do_request_cgi(endpoint, **kwargs):
    """Perform a request to SITE and return JSON."""

    url = urlparse.urljoin(JCVI_BASE_CGI_URL, endpoint)
    response = requests.get(url, verify=False, params=kwargs)

    # Raise exception and abort if requests is not successful
    response.raise_for_status()

    try:
        # Try to convert result to JSON
        # abort if not possible
        return response.json()
    except ValueError:
        raise Exception('not a JSON object: {}'.format(response.text))

def do_request_generic(endpoint, **kwargs):
    """Perform a request to SITE and return response."""

    url = urlparse.urljoin(JCVI_BASE_URL, endpoint)
    response = requests.get(url, verify=False, params=kwargs)

    # Raise exception and abort if requests is not successful
    response.raise_for_status()

    return response

def send(data):
    """Display `data` in the format required by Adama.
    :type data: list
    """

    for elt in data:
        print json.dumps(elt)
        print '---'

def fail(message):
    # failure message for generic adapters
    return 'text/plaintext; charset=ISO-8859-1', message
