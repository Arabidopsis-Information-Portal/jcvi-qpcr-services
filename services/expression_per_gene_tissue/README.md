Expression_per_gene_tissue_02: Query x AIP native response
==========================================================

An example of how to configure a simple query API under ADAMA. One passes a GET requesting a specific "transcript" to the $API/$NS/$SERVICE_$VERSION/search endpoint. The "material" term is optional and allows one to request data from a specific experiment. The result is fetched and returned as a prototypical AIP JSON document.

Action: Enroll via Gitrepo
```
curl -sk -L -X POST $API/$NS/services -F \
    "git_repository=https://github.com/Arabidopsis-Information-Portal/jcvi-rtpcr-demos.git" \
    -F "metadata=expression_per_gene_tissue_02" \
    -H "Authorization: Bearer $TOKEN"
```

Action: Test service
```
curl -sk -L -X GET "$API/$NS/expression_per_gene_tissue_02_v0.2/search?transcript=AT1G33930.1&material=Young" \
    -H "Authorization: Bearer $TOKEN" \
    | python -mjson.tool

{
    "metadata": {
        "time_in_main": 0.378154993057251
    },
    "result": [
        {
            "class": "transcript_property",
            "expression_record": {
                "absolute_concentration": "1.80e-05",
                "absolute_concentration_stdev": "1.37e-05",
                "cycle_time": "29.41",
                "cycle_time_stdev": "0.33",
                "material_text_description": "Young Siliques",
                "ratio_to_invariants": "0.0048",
                "ratio_to_invariants_stdev": "0.00015"
            },
            "source_text_description": "RT-PCR",
            "transcript": "AT1G33930.1"
        }
    ],
    "status": "success"
}
```
