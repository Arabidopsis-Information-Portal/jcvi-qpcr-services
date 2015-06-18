import json
import services.common.tools as tools

def search(args):
    """
    args contains a dict with one or key:values

    line is a combination of plate, well, plant & dip number (mandatory)
    """
    line = args['line']

    """
    Make the request to the remote service
    """
    response = tools.do_request('ImageIDPerLineID.php', line=line)

    """
    Iterate through the results
    Foreach record from the remote service, build the response json
    Print this json to stdout followed by a record separator "---"
    ADAMA takes care of serializing these results
    """
    for result in response['images']:

        record = {
                'line': line,
                'class': 'line_property',
                'source_text_description': 'Reporter_Image_data',
                'image_record': {
                        'image_id': result['image_id']
                }
            }
        print json.dumps(record, indent=2)
        print '---'

def list(args):
    raise Exception('not implemented yet')
