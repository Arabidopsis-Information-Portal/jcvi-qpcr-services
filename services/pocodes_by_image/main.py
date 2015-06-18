import json
import services.common.tools as tools

def search(args):
    """
    args contains a dict with one or key:values

    image is an identifier and is mandatory
    """
    image = args['image']

    """
    Make the request to the remote service
    """
    response = tools.do_request('POCodePerImageID.php', image=image)

    """
    Iterate through the results
    Foreach record from the remote service, build the response json
    Print this json to stdout followed by a record separator "---"
    ADAMA takes care of serializing these results
    """
    for result in response['po_codes']:

        record = {
                'image': image,
                'class': 'image_property',
                'source_text_description': 'Reporter_Image_data',
                'po_code_record': {
                        'po_code': result['po_code'],
                        'po_name': result['po_name'],
                        'expression': result['expression']
                }
            }
        print json.dumps(record, indent=2)
        print '---'

def list(args):
    raise Exception('not implemented yet')
