import services.common.tools as tools

def search(args):
    """
    args contains a dict with one or key:values

    image_id: an image identifier and is mandatory
    width: image dimension to resize (optional)
    height: image dimension to resize (optional)
    """
    payload = {'search_term': args['search_term']}

    """
    Make the request to the remote service
    """
    response = tools.do_request_generic('SearchAvailableAGITranscript.php', **payload)

    """
    At this point, we've gotten a 200 status from the remote GET so we
    send back the content-type of the response along with the content.
    """
    return response.headers['Content-Type'], response.content

def list(args):
    response = tools.do_request_generic('SearchAvailableAGITranscript.php')
    return response.headers['Content-Type'], response.content
