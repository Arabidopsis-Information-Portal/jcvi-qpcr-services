import json
import services.common.tools as tools

def search(args):
    """
    args contains a dict with one or key:values

    locus is AGI identifier and is mandatory
    """
    locus = args['locus']

    """
    Make the request to the remote service
    """
    response = tools.do_request('LineIDPerLocus.php', locus=locus)

    """
    Iterate through the results
    Foreach record from the remote service, build the response json
    Print this json to stdout followed by a record separator "---"
    ADAMA takes care of serializing these results
    """
    for result in response['lines']:

        record = {
                'locus': locus,
                'class': 'locus_property',
                'source_text_description': 'Reporter_Image_data',
                'line_record': {
                        'line_id': result['line_id']
                }
            }
        print json.dumps(record, indent=2)
        print '---'

def list(args):
    raise Exception('not implemented yet')
