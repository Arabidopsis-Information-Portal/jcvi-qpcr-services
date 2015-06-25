import json
import services.common.tools as tools

def search(args):
    """
    args contains a dict with one or key:values

    transcript is AGI identifier and is mandatory
    material is the tissue or treatment and is restricted below to a limited list
    """
    foldchange = args['foldchange']

    """
    Check materials to make sure they're in the (hard-coded) approved list
    """
    valid_materials = { 'flower': 'Flo', 'iaa': 'IAA', 'leaf': 'Lea', \
            'root': 'Roo', 'salicylic': 'Sal', 'nacl': 'NaC', \
            'young': 'You', 't87': 'T87'}

    material1 = args['material1'].lower()
    if material1 not in valid_materials.keys():
        return
    tissue1 = valid_materials[material1]

    material2 = args['material2'].lower()
    if material2 not in valid_materials.keys():
        return
    tissue2 = valid_materials[material2]

    """
	Make the request to the remote service
    """
    payload = { 'tissue1': tissue1, 'tissue2': tissue2, 'change': foldchange }
    response = tools.do_request_cgi('ExpressionConditionComparison', **payload)

    """
    Iterate through the results
    Foreach record from the remote service, build the response json
    Print this json to stdout followed by a record separator "---"
    ADAMA takes care of serializing these results
    """
    for result in response['compare_table']:

        # check that transcript uses a valid transcript identifier
        transcript = result['elem_target_id']
        if not tools.is_valid_agi_identifier(transcript):
            continue

        record = {
                'transcript': transcript,
                'class': 'transcript_property',
                'source_text_description': 'RT-PCR',
                'expression_comparison_record': {
                        'material1_text_description': result['elem_tissue1'],
                        'expression_value_material1': result['elem_tissue1_value'],
                        'expression_value_material1_stdev': result['elem_tissue1_value2'],
                        'material2_text_description': result['elem_tissue2'],
                        'expression_value_material2': result['elem_tissue2_value'],
                        'expression_value_material2_stdev': result['elem_tissue2_value2']
                }
            }
        print json.dumps(record, indent=2)
        print '---'

def list(args):
    raise Exception('not implemented yet')
