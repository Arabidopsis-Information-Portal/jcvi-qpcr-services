Expression_condition_comparison: Query x AIP native response
==========================================================

An example of how to configure a simple query API under ADAMA. One passes a GET requesting a specific "foldchange" increase in expression in "material1" over "material2" to the $API/$NS/$SERVICE_$VERSION/search endpoint. The result is fetched and returned as a prototypical AIP JSON document.

Action: Enroll via Gitrepo
```
curl -sk -L -X POST $API/$NS/services -F \
    "git_repository=https://github.com/Arabidopsis-Information-Portal/jcvi-rtpcr-demos.git" \
    -F "metadata=expression_condition_comparison" \
    -H "Authorization: Bearer $TOKEN"
```

Action: Test service
```
curl -sk -L -X GET "$API/$NS/expression_condition_comparison_v0.2/search?material1=flower&material2=root&foldchange=5" \
    -H "Authorization: Bearer $TOKEN" \
    | python -mjson.tool

{
    "metadata": {
        "time_in_main": 2.174938917160034
    },
    "result": [
        {
            "class": "transcript_property",
            "expression_comparison_record": {
                    "expression_value_material1": "0.049",
                    "expression_value_material1_stdev": "0.040",
                    "expression_value_material2": "0.0022",
                    "expression_value_material2_stdev": "0.00050",
                    "material1_text_description": "Flower Buds",
                    "material2_text_description": "Root"
            },
            "source_text_description": "RT-PCR",
            "transcript": "AT3G51590.1"
        },
        {
            "class": "transcript_property",
            "expression_comparison_record": {
                    "expression_value_material1": "0.029",
                    "expression_value_material1_stdev": "0.027",
                    "expression_value_material2": "0.0024",
                    "expression_value_material2_stdev": "0.0027",
                    "material1_text_description": "Flower Buds",
                    "material2_text_description": "Root"
            },
            "source_text_description": "RT-PCR",
            "transcript": "AT3G25050.1"
        },
        {
            "class": "transcript_property",
            "expression_comparison_record": {
                    "expression_value_material1": "0.0026",
                    "expression_value_material1_stdev": "0.0018",
                    "expression_value_material2": "0.00031",
                    "expression_value_material2_stdev": "0.00022",
                    "material1_text_description": "Flower Buds",
                    "material2_text_description": "Root"
            },
            "source_text_description": "RT-PCR",
            "transcript": "AT1G30350.1"
        }
    ],
    "status": "success"
}

```
