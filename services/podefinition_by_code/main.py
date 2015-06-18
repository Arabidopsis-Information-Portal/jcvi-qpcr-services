import json
import services.common.tools as tools

def search(args):
    """
    args contains a dict with one or key:values

    po_code is a PO code and is mandatory
    """
    po_code = args['po_code']

    """
    Make the request to the remote service
    """
    response = tools.do_request('POInfoPerCode.php', po_code=po_code)

    """
    Iterate through the results
    Foreach record from the remote service, build the response json
    Print this json to stdout followed by a record separator "---"
    ADAMA takes care of serializing these results
    """
    record = {
            'po_code': po_code,
            'class': 'po_code_property',
            'source_text_description': 'Reporter_Image_data',
            'po_definition_record': {
                    'po_name': response['po_name'],
                    'po_def': response['po_def'],
                    'po_namespace': response['po_namespace']
            }
        }
    print json.dumps(record, indent=2)
    print '---'

def list(args):
    raise Exception('not implemented yet')
