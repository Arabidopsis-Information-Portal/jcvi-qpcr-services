import json
import services.common.tools as tools

def search(args):
    """
    args contains a dict with one or key:values

    transcript is AGI identifier and is mandatory
    material is the tissue or treatment and is restricted below to a limited list
    """

    """
	Check that client has requested what looks like a valid transcript identifier
    """
    trans = args['transcript'].upper()
    if not tools.is_valid_agi_identifier(trans):
        return

    """
    If material was passed make sure its in the (hard-coded) approved list
    We also encode the written names of the samples here for inclusion into the JSON response
    For cross-compatibility, we could map these treatments/tissues to one or more
    third part ontologies and return those
    """
    valid_materials = { 'flower': 'Flower Buds', 'iaa': 'IAA', 'leaf': 'Leaf', \
            'root': 'Root', 'salicylic': 'Salicylic Acid', 'nacl': 'NaCl', \
            'young': 'Young Siliques', 't87': 'T87 Cell Culture'}

    if 'material' in args:
        material = args['material'].lower()
        if material not in valid_materials.keys():
            return
    else:
        material = None

    """
    Make the request to the remote service
    """
    payload = { 'gene': trans, 'format': 'json', 'Submit': 'Search' }
    if material:
        payload['tissue'] = material
    response = tools.do_request_cgi('ExpressionPerGenePerTissue', **payload)

    """
    Iterate through the results
    Foreach record from the remote service, build the response json
    Print this json to stdout followed by a record separator "---"
    ADAMA takes care of serializing these results
    """
    for result in response['expression']:
        record = {
                'transcript': trans,
                'class': 'transcript_property',
                'source_text_description': 'RT-PCR',
                'expression_record': {
                    'material_text_description': valid_materials[result['elem_tissue'].lower()],
                    'cycle_time': result['elem_cycle_time'],
                    'cycle_time_stdev': result['elem_cycle_time2'],
                    'absolute_concentration': result['elem_conc'],
                    'absolute_concentration_stdev': result['elem_conc2'],
                    'ratio_to_invariants': result['elem_ratio'],
                    'ratio_to_invariants_stdev': result['elem_ratio2']
                }
            }
        print json.dumps(record, indent=2)
        print '---'

def list(args):
    raise Exception('not implemented yet')
