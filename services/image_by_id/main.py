import services.common.tools as tools

def search(args):
    """
    args contains a dict with one or key:values

    image_id: an image identifier and is mandatory
    width: image dimension to resize (optional)
    height: image dimension to resize (optional)
    """
    payload = {'image_id': args['image_id']}

    if args.has_key('width'):
        payload['width'] = args['width']
    if args.has_key('height'):
        payload['height'] = args['height']

    """
    Make the request to the remote service
    """
    response = tools.do_request_generic('get_image.php', payload)

    """
    At this point, we've gotten a 200 status from the remote GET so we
    send back the content-type of the response along with the content.
    """
    return response.headers['Content-Type'], response.content

def list(args):
    raise Exception('not implemented yet')
