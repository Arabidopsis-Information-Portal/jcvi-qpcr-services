import json
import services.common.tools as tools

def search(args):
    """
    args contains a dict with one or key:values

    line is a combination of plate, well, plant & dip number (mandatory)
    """
    line_id = args['line_id']

    """
    Make the request to the remote service
    """
    response = tools.do_request('ImageDataPerLineID.php', line_id=line_id)

    """
    Iterate through the results
    Foreach record from the remote service, build the response json
    Print this json to stdout followed by a record separator "---"
    ADAMA takes care of serializing these results
    """
    for result in response['images']:

        record = {
                'line_id': line_id,
                'class': 'line_property',
                'source_text_description': 'Reporter_Image_data',
                'image_record': {
                        'image_id': result['image_id'],
                        'image_url': result['image_url'],
                        'po_codes': result['po_codes']
                }
            }
        print json.dumps(record, indent=2)
        print '---'

def list(args):
    raise Exception('not implemented yet')
