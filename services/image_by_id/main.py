import services.common.tools as tools

def search(args):
    """
    args contains a dict with one or key:values

    image_id is an image identifier and is mandatory
    """
    image_id = args['image_id']

    """
    Make the request to the remote service
    """
    response = tools.do_request_generic('view.php', file=image_id)

    """
    At this point, we've gotten a 200 status from the remote GET so we
    send back the content-type of the response along with the content.
    """
    return response.headers['Content-Type'], response.content

def list(args):
    raise Exception('not implemented yet')
