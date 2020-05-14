from datetime import datetime as dt
from IPython.core.display import display, HTML
import requests


def lprint(text): # pretty log printing 
    tn = dt.now()
    print("{} : {}".format(tn.strftime("%d.%m.%y %H:%M:%S"), text))

__all__ = ['lprint', 'printReport', 'requestFromREST']


def printReport(data_item):
    display(HTML('<h3>{}</h3>'.format(data_item.name)))
    display(HTML("<hr>"))
    display(HTML('<h5>Description</h5>'))
    display(HTML(data_item.description))
    display(HTML("<hr>"))
    display(HTML("Item is owned by: <b>{}</b>, and the person shared with everyone: <b>{}</b>".format(data_item.owner, data_item.shared_with['everyone'])))
    display(HTML("<hr>"))
    display(HTML("The dataset has <b>{} layer </b> ...".format(len(data_item.tables))))
    i = 0
    for lyr in data_item.layers:
        print(i, lyr.properties.name)
        i += 1
    display(HTML("... and <b>{} tables</b>.".format(len(data_item.layers))))
    for lyr in data_item.tables:
        print(i, lyr.properties.name)
        i += 1
    display(HTML("<hr>"))
    display(HTML('<h5>Usage last 24h</h5>'))
    display(data_item.usage(date_range='24H', as_df=True).set_index('Date').plot(figsize=(15,5)))

def requestFromREST(url):
    with open( r'tokenfile_agol.txt', 'r') as outfile:
        tk = outfile.readline()
    payload= { 'where': '1=1' ,
               'returnGeometry': False,
               'outFields': 'TOTAL,M_TOTAL,F_TOTAL,MKOOD',
               'f': 'pjson', 'token':tk }
    r = requests.get(url, params=payload)
    d = r.json()
    return d
    
class mapsw:
    map1 = """<html><head>


<!-- Load require.js. Delete this if your page already loads require.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha256-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"></script>
<script src="https://unpkg.com/@jupyter-widgets/html-manager@*/dist/embed-amd.js" crossorigin="anonymous"></script>
<script type="application/vnd.jupyter.widget-state+json">
{
    "version_major": 2,
    "version_minor": 0,
    "state": {
        "d374b3ec681842fbb5a1ae16e684ea4d": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.2.0",
            "state": {
                "height": "400px",
                "width": "100%"
            }
        },
        "5ef04baeb93a4c3086becd23c42beaed": {
            "model_name": "ArcGISMapIPyWidgetModel",
            "model_module": "arcgis-map-ipywidget",
            "model_module_version": "1.7.0",
            "state": {
                "_add_this_notype_layer": {
                    "type": "FeatureLayer",
                    "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0?token=PO1rdsqHfSV4T4AV1uaC5q5bpM_Pkk3Q3h5JbrSPyE8ERLjXrrNkI9Yu3fmZVvqWfuQAhYqvkbPma_JwEgRf5l60jWWAS4nGbg3c3YPm8FsfnVJXfIqXaxTkng-O8oOIVZbBRMlzS65WFJeVr8dVNHI7mpdn5EtQGDS0CB9SmX8.",
                    "options": {},
                    "_hashFromPython": "141385006172"
                },
                "_auth_mode": "tokenBased",
                "_basemap": "default",
                "_draw_these_graphics_on_widget_load": [],
                "_draw_these_notype_layers_on_widget_load": [
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer/0?token=QV0uxVUrO_yKUyOzwfvK7n5-j8HsrAMtW27ur3wf9FpohsOlEp-AbQiNV91VvvRBJmAE92MQIIHCv7ZBzehCy2ZzDxk7EFGB_YbGuZc7F2_K9H-MQT7-SAaHQOishAol0GDMCk3GspdNp6zIwSapnLdhT_u6Mrn9naddQacm-3c.",
                        "options": {},
                        "_hashFromPython": "-9223371895484767884"
                    },
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0?token=PO1rdsqHfSV4T4AV1uaC5q5bpM_Pkk3Q3h5JbrSPyE8ERLjXrrNkI9Yu3fmZVvqWfuQAhYqvkbPma_JwEgRf5l60jWWAS4nGbg3c3YPm8FsfnVJXfIqXaxTkng-O8oOIVZbBRMlzS65WFJeVr8dVNHI7mpdn5EtQGDS0CB9SmX8.",
                        "options": {},
                        "_hashFromPython": "141385006172"
                    }
                ],
                "_extent": {
                    "xmin": 21.72500459575779,
                    "ymin": 57.47309929703872,
                    "xmax": 28.235886557575526,
                    "ymax": 59.68614855697031,
                    "spatialReference": {
                        "wkid": 4326
                    }
                },
                "_gallery_basemaps": {
                    "default": {
                        "id": "28e3c1bf39c84fedb561ba38b9757be7",
                        "title": "Light Gray Canvas",
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true,
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer"
                            }
                        ],
                        "operationalLayers": []
                    }
                },
                "_portal_sharing_rest_url": "https://ag.maps.arcgis.com/sharing/rest/",
                "_portal_url": "https://ag.maps.arcgis.com",
                "_readonly_center": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "x": 2780810.4813835686,
                    "y": 8093814.282492124
                },
                "_readonly_extent": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "xmin": 2300785.9437527894,
                    "ymin": 7849215.791979625,
                    "xmax": 3260835.019014348,
                    "ymax": 8338412.773004622
                },
                "_readonly_webmap_from_js": {
                    "layers": [
                        {
                            "id": "-9223371895484767884",
                            "refreshInterval": 0,
                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer",
                            "renderer": {
                                "authoringInfo": {
                                    "classificationMethod": "esriClassifyNaturalBreaks",
                                    "colorRamp": {
                                        "type": "multipart",
                                        "colorRamps": [
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    255,
                                                    245,
                                                    235,
                                                    255
                                                ],
                                                "toColor": [
                                                    255,
                                                    231,
                                                    207,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    255,
                                                    231,
                                                    207,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    207,
                                                    162,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    207,
                                                    162,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    174,
                                                    106,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    174,
                                                    106,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    141,
                                                    61,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    141,
                                                    61,
                                                    255
                                                ],
                                                "toColor": [
                                                    242,
                                                    105,
                                                    19,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    242,
                                                    105,
                                                    19,
                                                    255
                                                ],
                                                "toColor": [
                                                    217,
                                                    72,
                                                    0,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    217,
                                                    72,
                                                    0,
                                                    255
                                                ],
                                                "toColor": [
                                                    166,
                                                    55,
                                                    3,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    166,
                                                    55,
                                                    3,
                                                    255
                                                ],
                                                "toColor": [
                                                    128,
                                                    39,
                                                    4,
                                                    255
                                                ]
                                            }
                                        ]
                                    },
                                    "type": "classedColor"
                                },
                                "type": "classBreaks",
                                "classBreakInfos": [
                                    {
                                        "label": "≤22.5%",
                                        "classMaxValue": 0.22509074648850544,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                255,
                                                245,
                                                235,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤23.2%",
                                        "classMaxValue": 0.2316336848187202,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                254,
                                                231,
                                                209,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤24.6%",
                                        "classMaxValue": 0.245809724405945,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                212,
                                                171,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤24.9%",
                                        "classMaxValue": 0.24881370472641484,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                185,
                                                125,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤25.4%",
                                        "classMaxValue": 0.25434874840899446,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                155,
                                                80,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.0%",
                                        "classMaxValue": 0.2596328029375765,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                247,
                                                125,
                                                41,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.4%",
                                        "classMaxValue": 0.2642192670287819,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                233,
                                                94,
                                                13,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.8%",
                                        "classMaxValue": 0.2678786709745865,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                205,
                                                68,
                                                1,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤27.3%",
                                        "classMaxValue": 0.2725665522048074,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                161,
                                                52,
                                                3,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤31.5%",
                                        "classMaxValue": 0.31494649997393875,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                127,
                                                39,
                                                4,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    }
                                ],
                                "legendOptions": {},
                                "minValue": 0.22509074648850544,
                                "valueExpression": "$feature.TOT_GE60/$feature.TOTAL",
                                "valueExpressionTitle": "Custom"
                            },
                            "rendererType": "esri.renderers.ClassBreaksRenderer"
                        },
                        {
                            "id": "141385006172",
                            "refreshInterval": 0,
                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer",
                            "renderer": {
                                "authoringInfo": {
                                    "colorRamp": {
                                        "type": "multipart",
                                        "colorRamps": [
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    224,
                                                    252,
                                                    207,
                                                    255
                                                ],
                                                "toColor": [
                                                    224,
                                                    252,
                                                    207,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    228,
                                                    179,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    228,
                                                    179,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    189,
                                                    184,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    189,
                                                    184,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    202,
                                                    226,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    202,
                                                    226,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    204,
                                                    240,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    204,
                                                    240,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    184,
                                                    252,
                                                    240,
                                                    255
                                                ],
                                                "toColor": [
                                                    184,
                                                    252,
                                                    240,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    184,
                                                    252,
                                                    179,
                                                    255
                                                ],
                                                "toColor": [
                                                    184,
                                                    252,
                                                    179,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    224,
                                                    194,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    224,
                                                    194,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    187,
                                                    193,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    187,
                                                    193,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    245,
                                                    179,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    245,
                                                    179,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    221,
                                                    212,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    221,
                                                    212,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    182,
                                                    239,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    182,
                                                    239,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    189,
                                                    252,
                                                    217,
                                                    255
                                                ],
                                                "toColor": [
                                                    189,
                                                    252,
                                                    217,
                                                    255
                                                ]
                                            }
                                        ]
                                    }
                                },
                                "type": "uniqueValue",
                                "field1": "Lõpetab_tegevuse",
                                "defaultLabel": "<all other values>",
                                "defaultSymbol": {
                                    "type": "esriSMS",
                                    "color": [
                                        130,
                                        130,
                                        130,
                                        255
                                    ],
                                    "angle": 0,
                                    "xoffset": 0,
                                    "yoffset": 0,
                                    "size": 4,
                                    "style": "esriSMSCircle",
                                    "outline": {
                                        "type": "esriSLS",
                                        "color": [
                                            0,
                                            0,
                                            0,
                                            255
                                        ],
                                        "width": 0.7,
                                        "style": "esriSLSSolid"
                                    }
                                },
                                "fieldDelimiter": ",",
                                "uniqueValueInfos": [
                                    {
                                        "label": "Apteek ei vasta nõuetele, aga on osaliselt proviisoromandis",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAACq0lEQVRIibWVPU/qUBjH/20w6XGy3c7ZxElhMWUyutxEJ9gQrO71YxQ+Bt3x2MJiqosmLhIXxYnCJE633WSsibG9A7a8yNu9yX2mnvZ5fn3eTwr/UVLLFDjnLBLXVFEQaBSFDABCIXLOSqX2P8Prtq2KoVAh6yQvyzKIJIEQAgDwPN/gVhOIYCL6rGqa5q0M51ajomwoBmMU2cz2j+/xu9f+m/70/KJzq1HVyseVpXB+2XAUWcnncrtQZHleYACArfQmGKV4aD0a/LJJtZPi+Vw4txoVRVbyR4e/FkIBAP414DkgsoqjQx23d/c6txr+eAQJvG7bqrKhGLnc7mrgVmH4zApAWsfB/h6unBujbttJsRO4GAoVxujSVEyAASCtAwAIkZDN7MB1ezUAuQTOOWdkneRnFW8heN8BaD45ZjPb6LhdNT6nACAS11R53OMPfzZcVoHCVNfFuhIFADBGcWE1C6flopMCAFEQKJGkkUGrAAyWzsikFDxAoiCSBFEQ6MjzKGTxgAAACPt7eGxKCOJJnj2h3yGuLLI60yYFDHeF5/lGUtC0DvTN1eFsVGTP8xEKkZPAz0qlNreak56s+oNYF0AQfOB9MIAYfvkJHAAQwXztv+lb6c3hWa0NDdvnP4HjHqu1JCWe7wMRzHiRjcE/q0/PLzqjFIRII68WCc0n4PfBAB23i1AMk3ATuKZpHrca1YfWo5Hslr457Jx50jeTlHTcHoIgqJ6VR3t+olu08nGFXzbp7d29frC/B6LWFnueeNyD99u71k4m1+6PVtROiufcavhXzo2RzezM3OfAsHie76PjdhEEQXUaPBMeR1C3bcd1e7WO21UZo9M3Ed4HAyCCGYqhOZ6KpXBg2J743m4XVrMwfYeK4Zc/73pbCh+X03LRWUVvWv4AALEZ7sh7vy8AAAAASUVORK5CYII=",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/401b7fb6e76ef39c5daf9767b4485343",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "0"
                                    },
                                    {
                                        "label": "Apteek ei vasta nõuetele",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC50lEQVRIibWVzUvbYBzHvwnt6KOXJkwhOfkCg9ZeSnoS9TCYp/biamv0Hq/eJ6SF/QG7tvf6mLYOJHpQwYOKF19OjQVB3WUJzGG9jA7EZIcu6YvV1sF+tyf55ZPv7/Xx4T+ar5cDpVR0WL/EMozgOLYIADbj6Eup1Nk/wwvFosTaTIYMkDjHcSCBAAghAADTtFSqlQEHeTgPWVmWzb7hVCtl+CCviqKAyEToyXv32dX1jXJyeq5QrZSV0/OZnnC6XtJ5jo/HYlHwHPdcYACA8bFRiIKAw6Njla6XBXkhufwsnGqlDM/x8dkP71+EAsD9wRbuD3QMhCXMzinY3dtXqFayWiPw4IViUeKDvBqLRfsCX64kAADBnwkMzymYnprEpr6tFopFr9genLWZjCgKPVPRCgaA4TkFAEBIAJGJMAyjmgMQ8+CUUpEMkHi34r0EfvdFR3Am7p0jEyFUjAvJPfsAwGH9Etei+OHW6gofDEmI7rR3nevrHxIAAKIoYE0rJxbTSd0HACzDCCQQ8D64XEngV7XnjLRZdMeEf0gACQTAMozQVO7YojsgDRUi8Eq4a4QQuJPcdYjevBVeBRwMSV5aWs0HNHaFaVqqW9Chjwp+fM33DQ/ONItsmhZsxtE9+FIqdUa1cpuS4bn+fuD6AkC9/ht3tRpY+9Hy4AAAB/mr6xtlfGwUADCymsNAWMK3z8tdkE3Fo59yXkpMywIc5N1F1gJ/yJ6cniuiIICQgKfqJQvOxD3wXa2GinEBm7W9cD24LMsm1UrZw6Nj1d0ttxv5Ruc8Y7cbeS8lFaOKer2eXUo393xbt8jp+QxdLwu7e/vK9NQkRlZzGHlRu6u4CvO7uSUvtK/dJ60oLySXqVayNvVtNTIR7rrPgUbxTMtCxbhAvV7PdoK7wt0ICsWibhjVXMW4kERR6LyJcFerAQ7yNmvnW1PREw402hN/t9uaVk503qGs/Wg9d731hLfaYjqp9+PXaX8AEaIuA8T2djsAAAAASUVORK5CYII=",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/fa6b190e27f53ebe26b76897f0cdf23d",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "1"
                                    },
                                    {
                                        "label": "Apteek sulgeb uksed 1.04.2020",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC3klEQVRIibWVPVPiQBjH/4kwsjRCGiepDq0UGiZUjhY641XQIRjtLGJ/XyDwBWysSHGdrgEaJ9rojBY6Noo2BCq1uqQDrxFvHJMruIQXebubuafb3Wd/+7zs/teH/2i+cQ6UUsFh/SLLMLzj2AIA2Iyjb2cylX+GHxSLImszORIkyXA4DBIIgBACADBNS6FaGXCgwnnPS5JkTgynWinHhThFEHjEoguf1t25x6dn+fbuXqZaKS9lN3Jj4fSopHNhLplIxMGFw8MSAwDMz0Ug8Dyurm8UelTmpc307lA41Uo5Lswlv66vjYQCwMnDL+gPbxAjfsjrazg7v5CpVrK6M/DgB8WiyIU4JZGITwRO7TUAAKmXAOTVIFaWl3CsnyoHxaLXbA/O2kxOEPixpegGA4C8GgQAEBJALLoIw6gXACQ8OKVUIEGSHNS8UWD9G4dkfNobx6ILqBo10R37AMBh/WK4K2LrxR4IFyN+mPuzPXOuLx9iAQCCwONQK6e2smndBwAsw/AkEPA2pPYaqDy/j8yi38z9WfAhFiQQAMswfCdyxxbcBwIAQmgKFfwd3DVCCNyXPPARuSlOamLEP3CPD2hrhWlaittQeTUI9fJ1Yngq3impaVqwGUf34NuZTIVq5Z5IJj3A9QWAVusNjWYTrP1heXAAgAP18elZnp+LAAAKOzMQI37sfv85MuLCzoxXEtOyAAeqK2Rd8Pf87d29LPA8CGmnKX7xj4w6GZ/2wI1mE1WjBpu1VXfdg0uSZFKtlL+6vlFcbVEvXyGEpobC1ctXryRVo45Wq5XfznZ0vue2SNmNHD0q82fnF/LK8hIKOzMjI+9EXIf5wzyRNntl99NVlDbTu1QrWcf6qRKLLg7Uc6DdPNOyUDVqaLVa+X7wQLibwUGxqBtGvVA1aqIg8P0/ERrNJuBAtVlb7S7FWDjQvp74o26HWjnV/4ey9oc17HsbC++2rWxan8Sv334DTPotDHXEfvUAAAAASUVORK5CYII=",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/5e2970208586beafae3ff7e26d8d5a3b",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "2"
                                    },
                                    {
                                        "label": "Apteek vastab nõuetele",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC40lEQVRIibWVPU/bUBSGX1tBymVAxAOSrSzARJwFOQNCMIBEp2QLMYatg+FX4IRf0Xhgg4uTLMiwgARDEELiY4qTCVhaW+pApC6uhLA7BDsfJCSt1He79vXjc+45570R/EdFhm2glAo+OyaxDMP7vicAgMf45lYud//P8INSSWI9Jk/GSToWi4FEoyCEAABs29GoUQF86PBfC4qi2CPDqVHOc5OcJgg8kuLch/fBs8enZ/X27kGlRrmgyOv5oXB6VDa5GJdOpebBxWKDEgMAzM5MQ+B5VK+uNXpU4ZWN7PZAODXKeS7Gpb+srX4KBYDL+gku6ybEuAR5TcXZ+YVKjbLTmUEIPyiVJG6S01Kp+ZHAO/sZAMBKIgN5QcXy0iKOzVPtoFQKix3CWY/JCwI/9Cg6wQAgL6gAAEKiSIoJWFajCCAVwimlAhkn6X7F+wz87auJlUQ6XCfFOdSsuhSsIwDgs2NSrCPin7+cvnAxLqG62911wd6pCR4AIAg8Do1KZlPOmhEAYBmGJ9Fo+MHOfgbW96Ez0qXqro2pCR4kGgXLMHw7ct8TggFpRSHAwt/BAxFCEExy3yEKUhxVYlzq+00EaHmFbTtaUFB5QYVxo48MX020i2zbDjzGN0P4Vi53T41KVySj/kCMS8i9t6Pr/sZLswnWe3NCOADAh/749KzOzkwDAPayRYhxCbuV7T7IllYSGexli+GR2I4D+NADI+uAvxZu7x5UgedBSKtzknGpD7ITng7BL80malYdHuuF6YZwRVFsapQL1atrLfAW40bH1IQwEG7c6OGE1qwGXNctbMltn+/qFkVez9OjCn92fqEuLy1iL1v8NPJ2xA3YP+wTZaPbdj+0orKR3aZG2Tk2T7WkmOjr50CreLbjoGbV4bpuoRfcFx5kcFAqmZbVKNasuiQIfO9NhJdmE/Che6yndx7FUDjQak+8u9uhUcn03qGs9+YMut6Gwju1KWfNUfb16g/ZQS6KO4Of5gAAAABJRU5ErkJggg==",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/9ed7519c1fa954003da81686ca6e6100",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "3"
                                    }
                                ]
                            },
                            "rendererType": "esri.renderers.UniqueValueRenderer"
                        }
                    ],
                    "ground": {
                        "layers": [
                            {
                                "id": "worldElevation",
                                "listMode": "show",
                                "title": "Terrain3D",
                                "url": "https://elevation3d.arcgis.com/arcgis/rest/services/WorldElevation3D/Terrain3D/ImageServer",
                                "visibility": true,
                                "layerType": "ArcGISTiledElevationServiceLayer"
                            }
                        ],
                        "transparency": 0
                    },
                    "basemap": {
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "title": "World Light Gray Base",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "title": "World Light Gray Reference",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true
                            }
                        ],
                        "title": "Light Gray Canvas"
                    }
                },
                "_username": "MBennTLL",
                "_uuid": "3a3adba1-2ccc-40c6-b9d1-6f36e2bfce87",
                "jupyter_target": "notebook",
                "layout": "IPY_MODEL_d374b3ec681842fbb5a1ae16e684ea4d",
                "print_service_url": "",
                "ready": true
            }
        },
        "795b5815d40546ea8e297e7dfc0d3975": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.2.0",
            "state": {
                "height": "400px",
                "width": "100%"
            }
        },
        "6b6934599d1941a19591ccd178f92a59": {
            "model_name": "ArcGISMapIPyWidgetModel",
            "model_module": "arcgis-map-ipywidget",
            "model_module_version": "1.7.0",
            "state": {
                "_auth_mode": "tokenBased",
                "_basemap": "default",
                "_draw_these_graphics_on_widget_load": [],
                "_draw_these_notype_layers_on_widget_load": [
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer/0?token=mLeHA7l66IdcIur7RcBIH4MeT2OBBTlsqj-VKWPPsy5NWTlJebYPH7rMCT6cxv6Xf5ImxeiwdlyDSWC06yg0Fob3cVOQwLMenAsVFISmDrLAcbxyu63qSrtWhso8k9qYg-RWOaSDoTvWGUQhn6qGQpeCfGReeRyw-BsH6DQ_5ag.",
                        "options": {},
                        "_hashFromPython": "-9223371871381589644"
                    },
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0?token=rPrIOhCgcw0x5sb1tPz50a1GZiyBtueZl52we7p45HWttnwPY7hOZPX9DUmqhYsFuDntrtayww01MlXkP3x1F9E-xphm_VQwKq_Y3rdPgXkyLanmC13ReHMLGougAUQU81AdRlqqDFovbvlMwIuaTavjRt7YvwHwV0-hBX6Q_ew.",
                        "options": {},
                        "_hashFromPython": "165479361365"
                    }
                ],
                "_extent": {
                    "xmin": 21.72500459575779,
                    "ymin": 57.47309929703872,
                    "xmax": 28.235886557575526,
                    "ymax": 59.68614855697031
                },
                "_gallery_basemaps": {
                    "default": {
                        "id": "28e3c1bf39c84fedb561ba38b9757be7",
                        "title": "Light Gray Canvas",
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true,
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer"
                            }
                        ],
                        "operationalLayers": []
                    }
                },
                "_portal_sharing_rest_url": "https://ag.maps.arcgis.com/sharing/rest/",
                "_portal_token": "UTXenFsSpBy29lYC3gxjMtbNemO2TJMZByiLMpncG32CB9RwhqQGr-KuatWUrjhX4mWnpESUnguP_dbML4Rus144sk3DyYB-IlctnKJr95cPRkXUDa1wykpo2MVFXOZA",
                "_portal_url": "https://ag.maps.arcgis.com",
                "_username": "MBennTLL",
                "_uuid": "8375243c-4b53-4513-a81d-39e74f1dee61",
                "layout": "IPY_MODEL_795b5815d40546ea8e297e7dfc0d3975",
                "print_service_url": ""
            }
        },
        "298ee4a03053442aa8d28c73f82f6862": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.2.0",
            "state": {
                "height": "400px",
                "width": "100%"
            }
        },
        "aa6eb1e063bb48d2ab4d81cbe24dfc09": {
            "model_name": "ArcGISMapIPyWidgetModel",
            "model_module": "arcgis-map-ipywidget",
            "model_module_version": "1.7.0",
            "state": {
                "_auth_mode": "tokenBased",
                "_basemap": "default",
                "_draw_these_graphics_on_widget_load": [],
                "_draw_these_notype_layers_on_widget_load": [
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer/0?token=QyVChwCdYmwZ5RKJg9R00KBX9tqUQQwk0buab7lgodOBYMqDBV1iv5iHFOYr7PPsye5ABcC5wn2dcxNE2oMY11tzBEjWA8gwRnm-oqhU1Z5mRJtLwSuVaCZBJ4TC-gw1vEmOYHQ_prCz0z5QYowbA1j5GooM4wTJPyN1qmzwM0o.",
                        "options": {},
                        "_hashFromPython": "-9223371871375284378"
                    },
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0?token=zTEu0X8IPrz9jgDpg5foWPsMA3SQMzNCuKxVuCWs2ASCYz6HbXGIPPfcz_CYDR8YBJCNXaJEMKxN-IV8X16TAe3EJm_TQVqld_V-69Fd8Z8cxmrAHY6rRyYJu0_hNLid_uJzRULDQT0B6gNqD97L7yLyUV-gqwUxF5EcXUmBcrw.",
                        "options": {},
                        "_hashFromPython": "-9223371871365388877"
                    }
                ],
                "_extent": {
                    "xmin": 21.72500459575779,
                    "ymin": 57.47309929703872,
                    "xmax": 28.235886557575526,
                    "ymax": 59.68614855697031,
                    "spatialReference": {
                        "wkid": 4326
                    }
                },
                "_gallery_basemaps": {
                    "default": {
                        "id": "28e3c1bf39c84fedb561ba38b9757be7",
                        "title": "Light Gray Canvas",
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true,
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer"
                            }
                        ],
                        "operationalLayers": []
                    }
                },
                "_portal_sharing_rest_url": "https://ag.maps.arcgis.com/sharing/rest/",
                "_portal_url": "https://ag.maps.arcgis.com",
                "_readonly_center": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "x": 2780810.4813835686,
                    "y": 8093814.282492124
                },
                "_readonly_extent": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "xmin": 2300785.9437527894,
                    "ymin": 7849215.791979625,
                    "xmax": 3260835.019014348,
                    "ymax": 8338412.773004622
                },
                "_readonly_webmap_from_js": {
                    "layers": [
                        {
                            "id": "-9223371871375284378",
                            "refreshInterval": 0,
                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer",
                            "renderer": {
                                "authoringInfo": {
                                    "classificationMethod": "esriClassifyNaturalBreaks",
                                    "colorRamp": {
                                        "type": "multipart",
                                        "colorRamps": [
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    255,
                                                    245,
                                                    235,
                                                    255
                                                ],
                                                "toColor": [
                                                    255,
                                                    231,
                                                    207,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    255,
                                                    231,
                                                    207,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    207,
                                                    162,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    207,
                                                    162,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    174,
                                                    106,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    174,
                                                    106,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    141,
                                                    61,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    141,
                                                    61,
                                                    255
                                                ],
                                                "toColor": [
                                                    242,
                                                    105,
                                                    19,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    242,
                                                    105,
                                                    19,
                                                    255
                                                ],
                                                "toColor": [
                                                    217,
                                                    72,
                                                    0,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    217,
                                                    72,
                                                    0,
                                                    255
                                                ],
                                                "toColor": [
                                                    166,
                                                    55,
                                                    3,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    166,
                                                    55,
                                                    3,
                                                    255
                                                ],
                                                "toColor": [
                                                    128,
                                                    39,
                                                    4,
                                                    255
                                                ]
                                            }
                                        ]
                                    },
                                    "type": "classedColor"
                                },
                                "type": "classBreaks",
                                "classBreakInfos": [
                                    {
                                        "label": "≤22.5%",
                                        "classMaxValue": 0.22509074648850544,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                255,
                                                245,
                                                235,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤23.2%",
                                        "classMaxValue": 0.2316336848187202,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                254,
                                                231,
                                                209,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤24.6%",
                                        "classMaxValue": 0.245809724405945,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                212,
                                                171,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤24.9%",
                                        "classMaxValue": 0.24881370472641484,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                185,
                                                125,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤25.4%",
                                        "classMaxValue": 0.25434874840899446,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                155,
                                                80,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.0%",
                                        "classMaxValue": 0.2596328029375765,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                247,
                                                125,
                                                41,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.4%",
                                        "classMaxValue": 0.2642192670287819,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                233,
                                                94,
                                                13,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.8%",
                                        "classMaxValue": 0.2678786709745865,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                205,
                                                68,
                                                1,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤27.3%",
                                        "classMaxValue": 0.2725665522048074,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                161,
                                                52,
                                                3,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤31.5%",
                                        "classMaxValue": 0.31494649997393875,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                127,
                                                39,
                                                4,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    }
                                ],
                                "legendOptions": {},
                                "minValue": 0.22509074648850544,
                                "valueExpression": "$feature.TOT_GE60/$feature.TOTAL",
                                "valueExpressionTitle": "Custom"
                            },
                            "rendererType": "esri.renderers.ClassBreaksRenderer"
                        }
                    ],
                    "ground": {
                        "layers": [
                            {
                                "id": "worldElevation",
                                "listMode": "show",
                                "title": "Terrain3D",
                                "url": "https://elevation3d.arcgis.com/arcgis/rest/services/WorldElevation3D/Terrain3D/ImageServer",
                                "visibility": true,
                                "layerType": "ArcGISTiledElevationServiceLayer"
                            }
                        ],
                        "transparency": 0
                    },
                    "basemap": {
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "title": "World Light Gray Base",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "title": "World Light Gray Reference",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true
                            }
                        ],
                        "title": "Light Gray Canvas"
                    }
                },
                "_username": "MBennTLL",
                "_uuid": "a7b5f6b5-0a92-484b-a9f8-ba4a8beabf01",
                "jupyter_target": "notebook",
                "layout": "IPY_MODEL_298ee4a03053442aa8d28c73f82f6862",
                "print_service_url": "",
                "ready": true
            }
        },
        "4886921c57b54cb6a61fa3fdd81cfade": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.2.0",
            "state": {
                "height": "400px",
                "width": "100%"
            }
        },
        "b3c19af3147042f6addeb45ff8b10090": {
            "model_name": "ArcGISMapIPyWidgetModel",
            "model_module": "arcgis-map-ipywidget",
            "model_module_version": "1.7.0",
            "state": {
                "_add_this_notype_layer": {
                    "type": "FeatureLayer",
                    "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0?token=FgGbUwsYA0yzY5mcAyyGlVpJV2TOvdxS5vBO3WANhuONEG6wswo4AN7PQpn-0jhj4MmvumDovrG771OWtX6faUWClezShPX-KeRP94nnS06yUoRgSo5MZP6BZ-NAAUdfIna-bpglXt5VA7OeP170DVL2VLxvjli59yePj7EYwZw.",
                    "options": {},
                    "_hashFromPython": "-9223371910020726833"
                },
                "_auth_mode": "tokenBased",
                "_basemap": "default",
                "_draw_these_graphics_on_widget_load": [],
                "_draw_these_notype_layers_on_widget_load": [
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer/0?token=2BS452JdUzZd884Vi3d1NrH59dIknm_CubOEgz6cas6rQzcMiZsVWYOmoZWKGqwyhebigIxkjwXSMX766tpJr3ZF4Fat3gFLVDkcrk0zPoVDimra9oNSqCwOvnT6JqEM4-3q2Mj2wmigsR-9D3WTeG25WcEaD44X9PXgUDkLMk4.",
                        "options": {},
                        "_hashFromPython": "-9223371910036741779"
                    },
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0?token=qsN9IQ4S6j-zZ1VKfa57GQHZJjAQ49l-eVeO-CI3CuIDtqplanUAoARQ_6sCII7lBCBqBd2ga7aPVwuHYKj8ka2wOjaZKzmHT3VuifB6sRHaRd5s1hrBFckDXg5_fR8UDlTx0C_LsA6puMbarCJaylxQ_wRipNWT3MXa2NpW7B8.",
                        "options": {},
                        "_hashFromPython": "-9223371910020899724"
                    },
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0?token=FgGbUwsYA0yzY5mcAyyGlVpJV2TOvdxS5vBO3WANhuONEG6wswo4AN7PQpn-0jhj4MmvumDovrG771OWtX6faUWClezShPX-KeRP94nnS06yUoRgSo5MZP6BZ-NAAUdfIna-bpglXt5VA7OeP170DVL2VLxvjli59yePj7EYwZw.",
                        "options": {},
                        "_hashFromPython": "-9223371910020726833"
                    }
                ],
                "_extent": {
                    "xmin": 21.72500459575779,
                    "ymin": 57.47309929703872,
                    "xmax": 28.235886557575526,
                    "ymax": 59.68614855697031,
                    "spatialReference": {
                        "wkid": 4326
                    }
                },
                "_gallery_basemaps": {
                    "default": {
                        "id": "28e3c1bf39c84fedb561ba38b9757be7",
                        "title": "Light Gray Canvas",
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true,
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer"
                            }
                        ],
                        "operationalLayers": []
                    }
                },
                "_portal_sharing_rest_url": "https://ag.maps.arcgis.com/sharing/rest/",
                "_portal_url": "https://ag.maps.arcgis.com",
                "_readonly_center": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "x": 2780810.4813835686,
                    "y": 8093814.282492124
                },
                "_readonly_extent": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "xmin": 2309958.387147008,
                    "ymin": 7849215.791979625,
                    "xmax": 3251662.5756201292,
                    "ymax": 8338412.773004622
                },
                "_readonly_webmap_from_js": {
                    "layers": [
                        {
                            "id": "-9223371910036741779",
                            "refreshInterval": 0,
                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer",
                            "renderer": {
                                "authoringInfo": {
                                    "classificationMethod": "esriClassifyNaturalBreaks",
                                    "colorRamp": {
                                        "type": "multipart",
                                        "colorRamps": [
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    255,
                                                    245,
                                                    235,
                                                    255
                                                ],
                                                "toColor": [
                                                    255,
                                                    231,
                                                    207,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    255,
                                                    231,
                                                    207,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    207,
                                                    162,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    207,
                                                    162,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    174,
                                                    106,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    174,
                                                    106,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    141,
                                                    61,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    141,
                                                    61,
                                                    255
                                                ],
                                                "toColor": [
                                                    242,
                                                    105,
                                                    19,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    242,
                                                    105,
                                                    19,
                                                    255
                                                ],
                                                "toColor": [
                                                    217,
                                                    72,
                                                    0,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    217,
                                                    72,
                                                    0,
                                                    255
                                                ],
                                                "toColor": [
                                                    166,
                                                    55,
                                                    3,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    166,
                                                    55,
                                                    3,
                                                    255
                                                ],
                                                "toColor": [
                                                    128,
                                                    39,
                                                    4,
                                                    255
                                                ]
                                            }
                                        ]
                                    },
                                    "type": "classedColor"
                                },
                                "type": "classBreaks",
                                "classBreakInfos": [
                                    {
                                        "label": "≤22.5%",
                                        "classMaxValue": 0.22509074648850544,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                255,
                                                245,
                                                235,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤23.2%",
                                        "classMaxValue": 0.2316336848187202,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                254,
                                                231,
                                                209,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤24.6%",
                                        "classMaxValue": 0.245809724405945,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                212,
                                                171,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤24.9%",
                                        "classMaxValue": 0.24881370472641484,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                185,
                                                125,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤25.4%",
                                        "classMaxValue": 0.25434874840899446,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                155,
                                                80,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.0%",
                                        "classMaxValue": 0.2596328029375765,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                247,
                                                125,
                                                41,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.4%",
                                        "classMaxValue": 0.2642192670287819,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                233,
                                                94,
                                                13,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.8%",
                                        "classMaxValue": 0.2678786709745865,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                205,
                                                68,
                                                1,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤27.3%",
                                        "classMaxValue": 0.2725665522048074,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                161,
                                                52,
                                                3,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤31.5%",
                                        "classMaxValue": 0.31494649997393875,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                127,
                                                39,
                                                4,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    }
                                ],
                                "legendOptions": {},
                                "minValue": 0.22509074648850544,
                                "valueExpression": "$feature.TOT_GE60/$feature.TOTAL",
                                "valueExpressionTitle": "Custom"
                            },
                            "rendererType": "esri.renderers.ClassBreaksRenderer"
                        },
                        {
                            "id": "-9223371910020726833",
                            "refreshInterval": 0,
                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer",
                            "renderer": {
                                "authoringInfo": {
                                    "colorRamp": {
                                        "type": "multipart",
                                        "colorRamps": [
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    224,
                                                    252,
                                                    207,
                                                    255
                                                ],
                                                "toColor": [
                                                    224,
                                                    252,
                                                    207,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    228,
                                                    179,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    228,
                                                    179,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    189,
                                                    184,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    189,
                                                    184,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    202,
                                                    226,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    202,
                                                    226,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    204,
                                                    240,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    204,
                                                    240,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    184,
                                                    252,
                                                    240,
                                                    255
                                                ],
                                                "toColor": [
                                                    184,
                                                    252,
                                                    240,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    184,
                                                    252,
                                                    179,
                                                    255
                                                ],
                                                "toColor": [
                                                    184,
                                                    252,
                                                    179,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    224,
                                                    194,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    224,
                                                    194,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    187,
                                                    193,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    187,
                                                    193,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    245,
                                                    179,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    245,
                                                    179,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    221,
                                                    212,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    221,
                                                    212,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    182,
                                                    239,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    182,
                                                    239,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    189,
                                                    252,
                                                    217,
                                                    255
                                                ],
                                                "toColor": [
                                                    189,
                                                    252,
                                                    217,
                                                    255
                                                ]
                                            }
                                        ]
                                    }
                                },
                                "type": "uniqueValue",
                                "field1": "Lõpetab_tegevuse",
                                "defaultLabel": "<all other values>",
                                "defaultSymbol": {
                                    "type": "esriSMS",
                                    "color": [
                                        130,
                                        130,
                                        130,
                                        255
                                    ],
                                    "angle": 0,
                                    "xoffset": 0,
                                    "yoffset": 0,
                                    "size": 4,
                                    "style": "esriSMSCircle",
                                    "outline": {
                                        "type": "esriSLS",
                                        "color": [
                                            0,
                                            0,
                                            0,
                                            255
                                        ],
                                        "width": 0.7,
                                        "style": "esriSLSSolid"
                                    }
                                },
                                "fieldDelimiter": ",",
                                "uniqueValueInfos": [
                                    {
                                        "label": "Apteek ei vasta nõuetele, aga on osaliselt proviisoromandis",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAACq0lEQVRIibWVPU/qUBjH/20w6XGy3c7ZxElhMWUyutxEJ9gQrO71YxQ+Bt3x2MJiqosmLhIXxYnCJE633WSsibG9A7a8yNu9yX2mnvZ5fn3eTwr/UVLLFDjnLBLXVFEQaBSFDABCIXLOSqX2P8Prtq2KoVAh6yQvyzKIJIEQAgDwPN/gVhOIYCL6rGqa5q0M51ajomwoBmMU2cz2j+/xu9f+m/70/KJzq1HVyseVpXB+2XAUWcnncrtQZHleYACArfQmGKV4aD0a/LJJtZPi+Vw4txoVRVbyR4e/FkIBAP414DkgsoqjQx23d/c6txr+eAQJvG7bqrKhGLnc7mrgVmH4zApAWsfB/h6unBujbttJsRO4GAoVxujSVEyAASCtAwAIkZDN7MB1ezUAuQTOOWdkneRnFW8heN8BaD45ZjPb6LhdNT6nACAS11R53OMPfzZcVoHCVNfFuhIFADBGcWE1C6flopMCAFEQKJGkkUGrAAyWzsikFDxAoiCSBFEQ6MjzKGTxgAAACPt7eGxKCOJJnj2h3yGuLLI60yYFDHeF5/lGUtC0DvTN1eFsVGTP8xEKkZPAz0qlNreak56s+oNYF0AQfOB9MIAYfvkJHAAQwXztv+lb6c3hWa0NDdvnP4HjHqu1JCWe7wMRzHiRjcE/q0/PLzqjFIRII68WCc0n4PfBAB23i1AMk3ATuKZpHrca1YfWo5Hslr457Jx50jeTlHTcHoIgqJ6VR3t+olu08nGFXzbp7d29frC/B6LWFnueeNyD99u71k4m1+6PVtROiufcavhXzo2RzezM3OfAsHie76PjdhEEQXUaPBMeR1C3bcd1e7WO21UZo9M3Ed4HAyCCGYqhOZ6KpXBg2J743m4XVrMwfYeK4Zc/73pbCh+X03LRWUVvWv4AALEZ7sh7vy8AAAAASUVORK5CYII=",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/401b7fb6e76ef39c5daf9767b4485343",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "0"
                                    },
                                    {
                                        "label": "Apteek ei vasta nõuetele",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC50lEQVRIibWVzUvbYBzHvwnt6KOXJkwhOfkCg9ZeSnoS9TCYp/biamv0Hq/eJ6SF/QG7tvf6mLYOJHpQwYOKF19OjQVB3WUJzGG9jA7EZIcu6YvV1sF+tyf55ZPv7/Xx4T+ar5cDpVR0WL/EMozgOLYIADbj6Eup1Nk/wwvFosTaTIYMkDjHcSCBAAghAADTtFSqlQEHeTgPWVmWzb7hVCtl+CCviqKAyEToyXv32dX1jXJyeq5QrZSV0/OZnnC6XtJ5jo/HYlHwHPdcYACA8bFRiIKAw6Njla6XBXkhufwsnGqlDM/x8dkP71+EAsD9wRbuD3QMhCXMzinY3dtXqFayWiPw4IViUeKDvBqLRfsCX64kAADBnwkMzymYnprEpr6tFopFr9genLWZjCgKPVPRCgaA4TkFAEBIAJGJMAyjmgMQ8+CUUpEMkHi34r0EfvdFR3Am7p0jEyFUjAvJPfsAwGH9Etei+OHW6gofDEmI7rR3nevrHxIAAKIoYE0rJxbTSd0HACzDCCQQ8D64XEngV7XnjLRZdMeEf0gACQTAMozQVO7YojsgDRUi8Eq4a4QQuJPcdYjevBVeBRwMSV5aWs0HNHaFaVqqW9Chjwp+fM33DQ/ONItsmhZsxtE9+FIqdUa1cpuS4bn+fuD6AkC9/ht3tRpY+9Hy4AAAB/mr6xtlfGwUADCymsNAWMK3z8tdkE3Fo59yXkpMywIc5N1F1gJ/yJ6cniuiIICQgKfqJQvOxD3wXa2GinEBm7W9cD24LMsm1UrZw6Nj1d0ttxv5Ruc8Y7cbeS8lFaOKer2eXUo393xbt8jp+QxdLwu7e/vK9NQkRlZzGHlRu6u4CvO7uSUvtK/dJ60oLySXqVayNvVtNTIR7rrPgUbxTMtCxbhAvV7PdoK7wt0ICsWibhjVXMW4kERR6LyJcFerAQ7yNmvnW1PREw402hN/t9uaVk503qGs/Wg9d731hLfaYjqp9+PXaX8AEaIuA8T2djsAAAAASUVORK5CYII=",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/fa6b190e27f53ebe26b76897f0cdf23d",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "1"
                                    },
                                    {
                                        "label": "Apteek sulgeb uksed 1.04.2020",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC3klEQVRIibWVPVPiQBjH/4kwsjRCGiepDq0UGiZUjhY641XQIRjtLGJ/XyDwBWysSHGdrgEaJ9rojBY6Noo2BCq1uqQDrxFvHJMruIQXebubuafb3Wd/+7zs/teH/2i+cQ6UUsFh/SLLMLzj2AIA2Iyjb2cylX+GHxSLImszORIkyXA4DBIIgBACADBNS6FaGXCgwnnPS5JkTgynWinHhThFEHjEoguf1t25x6dn+fbuXqZaKS9lN3Jj4fSopHNhLplIxMGFw8MSAwDMz0Ug8Dyurm8UelTmpc307lA41Uo5Lswlv66vjYQCwMnDL+gPbxAjfsjrazg7v5CpVrK6M/DgB8WiyIU4JZGITwRO7TUAAKmXAOTVIFaWl3CsnyoHxaLXbA/O2kxOEPixpegGA4C8GgQAEBJALLoIw6gXACQ8OKVUIEGSHNS8UWD9G4dkfNobx6ILqBo10R37AMBh/WK4K2LrxR4IFyN+mPuzPXOuLx9iAQCCwONQK6e2smndBwAsw/AkEPA2pPYaqDy/j8yi38z9WfAhFiQQAMswfCdyxxbcBwIAQmgKFfwd3DVCCNyXPPARuSlOamLEP3CPD2hrhWlaittQeTUI9fJ1Yngq3impaVqwGUf34NuZTIVq5Z5IJj3A9QWAVusNjWYTrP1heXAAgAP18elZnp+LAAAKOzMQI37sfv85MuLCzoxXEtOyAAeqK2Rd8Pf87d29LPA8CGmnKX7xj4w6GZ/2wI1mE1WjBpu1VXfdg0uSZFKtlL+6vlFcbVEvXyGEpobC1ctXryRVo45Wq5XfznZ0vue2SNmNHD0q82fnF/LK8hIKOzMjI+9EXIf5wzyRNntl99NVlDbTu1QrWcf6qRKLLg7Uc6DdPNOyUDVqaLVa+X7wQLibwUGxqBtGvVA1aqIg8P0/ERrNJuBAtVlb7S7FWDjQvp74o26HWjnV/4ey9oc17HsbC++2rWxan8Sv334DTPotDHXEfvUAAAAASUVORK5CYII=",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/5e2970208586beafae3ff7e26d8d5a3b",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "2"
                                    },
                                    {
                                        "label": "Apteek vastab nõuetele",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC40lEQVRIibWVPU/bUBSGX1tBymVAxAOSrSzARJwFOQNCMIBEp2QLMYatg+FX4IRf0Xhgg4uTLMiwgARDEELiY4qTCVhaW+pApC6uhLA7BDsfJCSt1He79vXjc+45570R/EdFhm2glAo+OyaxDMP7vicAgMf45lYud//P8INSSWI9Jk/GSToWi4FEoyCEAABs29GoUQF86PBfC4qi2CPDqVHOc5OcJgg8kuLch/fBs8enZ/X27kGlRrmgyOv5oXB6VDa5GJdOpebBxWKDEgMAzM5MQ+B5VK+uNXpU4ZWN7PZAODXKeS7Gpb+srX4KBYDL+gku6ybEuAR5TcXZ+YVKjbLTmUEIPyiVJG6S01Kp+ZHAO/sZAMBKIgN5QcXy0iKOzVPtoFQKix3CWY/JCwI/9Cg6wQAgL6gAAEKiSIoJWFajCCAVwimlAhkn6X7F+wz87auJlUQ6XCfFOdSsuhSsIwDgs2NSrCPin7+cvnAxLqG62911wd6pCR4AIAg8Do1KZlPOmhEAYBmGJ9Fo+MHOfgbW96Ez0qXqro2pCR4kGgXLMHw7ct8TggFpRSHAwt/BAxFCEExy3yEKUhxVYlzq+00EaHmFbTtaUFB5QYVxo48MX020i2zbDjzGN0P4Vi53T41KVySj/kCMS8i9t6Pr/sZLswnWe3NCOADAh/749KzOzkwDAPayRYhxCbuV7T7IllYSGexli+GR2I4D+NADI+uAvxZu7x5UgedBSKtzknGpD7ITng7BL80malYdHuuF6YZwRVFsapQL1atrLfAW40bH1IQwEG7c6OGE1qwGXNctbMltn+/qFkVez9OjCn92fqEuLy1iL1v8NPJ2xA3YP+wTZaPbdj+0orKR3aZG2Tk2T7WkmOjr50CreLbjoGbV4bpuoRfcFx5kcFAqmZbVKNasuiQIfO9NhJdmE/Che6yndx7FUDjQak+8u9uhUcn03qGs9+YMut6Gwju1KWfNUfb16g/ZQS6KO4Of5gAAAABJRU5ErkJggg==",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/9ed7519c1fa954003da81686ca6e6100",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "3"
                                    }
                                ]
                            },
                            "rendererType": "esri.renderers.UniqueValueRenderer"
                        }
                    ],
                    "ground": {
                        "layers": [
                            {
                                "id": "worldElevation",
                                "listMode": "show",
                                "title": "Terrain3D",
                                "url": "https://elevation3d.arcgis.com/arcgis/rest/services/WorldElevation3D/Terrain3D/ImageServer",
                                "visibility": true,
                                "layerType": "ArcGISTiledElevationServiceLayer"
                            }
                        ],
                        "transparency": 0
                    },
                    "basemap": {
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "title": "World Light Gray Base",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "title": "World Light Gray Reference",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true
                            }
                        ],
                        "title": "Light Gray Canvas"
                    }
                },
                "_username": "MBennTLL",
                "_uuid": "a4bb9758-960b-4fb9-99ba-c48ef79e51c3",
                "jupyter_target": "notebook",
                "layout": "IPY_MODEL_4886921c57b54cb6a61fa3fdd81cfade",
                "print_service_url": "",
                "ready": true,
                "zoom": 7
            }
        },
        "9551c9c08d014adfbb6fd61ed9fa8dcb": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.2.0",
            "state": {
                "height": "400px",
                "width": "100%"
            }
        },
        "58d926434ab749d0be336c8b9000e8d6": {
            "model_name": "ArcGISMapIPyWidgetModel",
            "model_module": "arcgis-map-ipywidget",
            "model_module_version": "1.7.0",
            "state": {
                "_auth_mode": "tokenBased",
                "_basemap": "default",
                "_draw_these_graphics_on_widget_load": [],
                "_draw_these_notype_layers_on_widget_load": [],
                "_extent": {
                    "xmin": 21.72500459575779,
                    "ymin": 57.47309929703872,
                    "xmax": 28.235886557575526,
                    "ymax": 59.68614855697031,
                    "spatialReference": {
                        "wkid": 4326
                    }
                },
                "_gallery_basemaps": {
                    "default": {
                        "id": "28e3c1bf39c84fedb561ba38b9757be7",
                        "title": "Light Gray Canvas",
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true,
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer"
                            }
                        ],
                        "operationalLayers": []
                    }
                },
                "_portal_sharing_rest_url": "https://ag.maps.arcgis.com/sharing/rest/",
                "_portal_url": "https://ag.maps.arcgis.com",
                "_readonly_center": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "x": 2566960.0638036137,
                    "y": 7983102.88885779
                },
                "_readonly_extent": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "xmin": 2326947.794988172,
                    "ymin": 7860803.643601514,
                    "xmax": 2806972.332619055,
                    "ymax": 8105402.134114066
                },
                "_readonly_webmap_from_js": {
                    "layers": [],
                    "ground": {
                        "layers": [
                            {
                                "id": "worldElevation",
                                "listMode": "show",
                                "title": "Terrain3D",
                                "url": "https://elevation3d.arcgis.com/arcgis/rest/services/WorldElevation3D/Terrain3D/ImageServer",
                                "visibility": true,
                                "layerType": "ArcGISTiledElevationServiceLayer"
                            }
                        ],
                        "transparency": 0
                    },
                    "basemap": {
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "title": "World Light Gray Base",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "title": "World Light Gray Reference",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true
                            }
                        ],
                        "title": "Light Gray Canvas"
                    }
                },
                "_username": "MBennTLL",
                "_uuid": "35e13d1b-51ed-4465-ad1a-4a5ce59db641",
                "jupyter_target": "notebook",
                "layout": "IPY_MODEL_9551c9c08d014adfbb6fd61ed9fa8dcb",
                "print_service_url": "",
                "ready": true,
                "zoom": 8
            }
        },
        "742787314c7f4dc381ce1bbf008124b3": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.2.0",
            "state": {
                "height": "400px",
                "width": "100%"
            }
        },
        "d486c3e811e5493e99c735c426dfdfef": {
            "model_name": "ArcGISMapIPyWidgetModel",
            "model_module": "arcgis-map-ipywidget",
            "model_module_version": "1.7.0",
            "state": {
                "_add_this_notype_layer": {
                    "type": "FeatureLayer",
                    "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0?token=85bqc8QuRRnGIqKM_3uvdd4PazQsdw25qt1TYgoIhTfiCkC1f9Lf-E9pR3wpOm17VDtMfFYLmKp_sVR9TlQjtRiZkkoJHorUvbjIFXigfrGR9cxedHY59WqqdJWCh_UuMJP-URwFE-qe47bZUQQzxFOm49YFVdMlfsubJzv3hx8.",
                    "options": {},
                    "_hashFromPython": "-9223371907904653403"
                },
                "_auth_mode": "tokenBased",
                "_basemap": "default",
                "_draw_these_graphics_on_widget_load": [],
                "_draw_these_notype_layers_on_widget_load": [
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer/0?token=4vJXzSRUfRqOPtBZVoQLbAf6MMPjU7aqUpUpuEOVSI3eNsfFIs9xG83jnP0L6u_eQroXmpHLlT7HG1uYQBFHNoCb0MRxXT9imGJApMqLKJRv05NCL8pCFvFM_6cj9IDF7298CY4U3i8Zp-5KM4CMC6S_RTHx4oggp8Za8zN3t1s.",
                        "options": {},
                        "_hashFromPython": "-9223371907920076428"
                    },
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0?token=85bqc8QuRRnGIqKM_3uvdd4PazQsdw25qt1TYgoIhTfiCkC1f9Lf-E9pR3wpOm17VDtMfFYLmKp_sVR9TlQjtRiZkkoJHorUvbjIFXigfrGR9cxedHY59WqqdJWCh_UuMJP-URwFE-qe47bZUQQzxFOm49YFVdMlfsubJzv3hx8.",
                        "options": {},
                        "_hashFromPython": "-9223371907904653403"
                    }
                ],
                "_extent": {
                    "xmin": 21.72500459575779,
                    "ymin": 57.47309929703872,
                    "xmax": 28.235886557575526,
                    "ymax": 59.68614855697031,
                    "spatialReference": {
                        "wkid": 4326
                    }
                },
                "_gallery_basemaps": {
                    "default": {
                        "id": "28e3c1bf39c84fedb561ba38b9757be7",
                        "title": "Light Gray Canvas",
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true,
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer"
                            }
                        ],
                        "operationalLayers": []
                    }
                },
                "_portal_sharing_rest_url": "https://ag.maps.arcgis.com/sharing/rest/",
                "_portal_url": "https://ag.maps.arcgis.com",
                "_readonly_center": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "x": 2841960.1040117037,
                    "y": 8093202.786265835
                },
                "_readonly_extent": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "xmin": 2371108.009775143,
                    "ymin": 7848604.2957533365,
                    "xmax": 3312812.1982482644,
                    "ymax": 8337801.276778334
                },
                "_readonly_webmap_from_js": {
                    "layers": [
                        {
                            "id": "-9223371907920076428",
                            "refreshInterval": 0,
                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer",
                            "renderer": {
                                "authoringInfo": {
                                    "classificationMethod": "esriClassifyNaturalBreaks",
                                    "colorRamp": {
                                        "type": "multipart",
                                        "colorRamps": [
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    255,
                                                    245,
                                                    235,
                                                    255
                                                ],
                                                "toColor": [
                                                    255,
                                                    231,
                                                    207,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    255,
                                                    231,
                                                    207,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    207,
                                                    162,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    207,
                                                    162,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    174,
                                                    106,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    174,
                                                    106,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    141,
                                                    61,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    141,
                                                    61,
                                                    255
                                                ],
                                                "toColor": [
                                                    242,
                                                    105,
                                                    19,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    242,
                                                    105,
                                                    19,
                                                    255
                                                ],
                                                "toColor": [
                                                    217,
                                                    72,
                                                    0,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    217,
                                                    72,
                                                    0,
                                                    255
                                                ],
                                                "toColor": [
                                                    166,
                                                    55,
                                                    3,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    166,
                                                    55,
                                                    3,
                                                    255
                                                ],
                                                "toColor": [
                                                    128,
                                                    39,
                                                    4,
                                                    255
                                                ]
                                            }
                                        ]
                                    },
                                    "type": "classedColor"
                                },
                                "type": "classBreaks",
                                "classBreakInfos": [
                                    {
                                        "label": "≤22.5%",
                                        "classMaxValue": 0.22509074648850544,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                255,
                                                245,
                                                235,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤23.2%",
                                        "classMaxValue": 0.2316336848187202,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                254,
                                                231,
                                                209,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤24.6%",
                                        "classMaxValue": 0.245809724405945,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                212,
                                                171,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤24.9%",
                                        "classMaxValue": 0.24881370472641484,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                185,
                                                125,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤25.4%",
                                        "classMaxValue": 0.25434874840899446,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                155,
                                                80,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.0%",
                                        "classMaxValue": 0.2596328029375765,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                247,
                                                125,
                                                41,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.4%",
                                        "classMaxValue": 0.2642192670287819,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                233,
                                                94,
                                                13,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.8%",
                                        "classMaxValue": 0.2678786709745865,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                205,
                                                68,
                                                1,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤27.3%",
                                        "classMaxValue": 0.2725665522048074,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                161,
                                                52,
                                                3,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤31.5%",
                                        "classMaxValue": 0.31494649997393875,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                127,
                                                39,
                                                4,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    }
                                ],
                                "legendOptions": {},
                                "minValue": 0.22509074648850544,
                                "valueExpression": "$feature.TOT_GE60/$feature.TOTAL",
                                "valueExpressionTitle": "Custom"
                            },
                            "rendererType": "esri.renderers.ClassBreaksRenderer"
                        },
                        {
                            "id": "-9223371907904653403",
                            "refreshInterval": 0,
                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer",
                            "renderer": {
                                "authoringInfo": {
                                    "colorRamp": {
                                        "type": "multipart",
                                        "colorRamps": [
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    224,
                                                    252,
                                                    207,
                                                    255
                                                ],
                                                "toColor": [
                                                    224,
                                                    252,
                                                    207,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    228,
                                                    179,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    228,
                                                    179,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    189,
                                                    184,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    189,
                                                    184,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    202,
                                                    226,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    202,
                                                    226,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    204,
                                                    240,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    204,
                                                    240,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    184,
                                                    252,
                                                    240,
                                                    255
                                                ],
                                                "toColor": [
                                                    184,
                                                    252,
                                                    240,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    184,
                                                    252,
                                                    179,
                                                    255
                                                ],
                                                "toColor": [
                                                    184,
                                                    252,
                                                    179,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    224,
                                                    194,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    224,
                                                    194,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    187,
                                                    193,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    187,
                                                    193,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    245,
                                                    179,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    245,
                                                    179,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    221,
                                                    212,
                                                    252,
                                                    255
                                                ],
                                                "toColor": [
                                                    221,
                                                    212,
                                                    252,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    182,
                                                    239,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    182,
                                                    239,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    189,
                                                    252,
                                                    217,
                                                    255
                                                ],
                                                "toColor": [
                                                    189,
                                                    252,
                                                    217,
                                                    255
                                                ]
                                            }
                                        ]
                                    }
                                },
                                "type": "uniqueValue",
                                "field1": "Lõpetab_tegevuse",
                                "defaultLabel": "<all other values>",
                                "defaultSymbol": {
                                    "type": "esriSMS",
                                    "color": [
                                        130,
                                        130,
                                        130,
                                        255
                                    ],
                                    "angle": 0,
                                    "xoffset": 0,
                                    "yoffset": 0,
                                    "size": 4,
                                    "style": "esriSMSCircle",
                                    "outline": {
                                        "type": "esriSLS",
                                        "color": [
                                            0,
                                            0,
                                            0,
                                            255
                                        ],
                                        "width": 0.7,
                                        "style": "esriSLSSolid"
                                    }
                                },
                                "fieldDelimiter": ",",
                                "uniqueValueInfos": [
                                    {
                                        "label": "Apteek ei vasta nõuetele, aga on osaliselt proviisoromandis",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAACq0lEQVRIibWVPU/qUBjH/20w6XGy3c7ZxElhMWUyutxEJ9gQrO71YxQ+Bt3x2MJiqosmLhIXxYnCJE633WSsibG9A7a8yNu9yX2mnvZ5fn3eTwr/UVLLFDjnLBLXVFEQaBSFDABCIXLOSqX2P8Prtq2KoVAh6yQvyzKIJIEQAgDwPN/gVhOIYCL6rGqa5q0M51ajomwoBmMU2cz2j+/xu9f+m/70/KJzq1HVyseVpXB+2XAUWcnncrtQZHleYACArfQmGKV4aD0a/LJJtZPi+Vw4txoVRVbyR4e/FkIBAP414DkgsoqjQx23d/c6txr+eAQJvG7bqrKhGLnc7mrgVmH4zApAWsfB/h6unBujbttJsRO4GAoVxujSVEyAASCtAwAIkZDN7MB1ezUAuQTOOWdkneRnFW8heN8BaD45ZjPb6LhdNT6nACAS11R53OMPfzZcVoHCVNfFuhIFADBGcWE1C6flopMCAFEQKJGkkUGrAAyWzsikFDxAoiCSBFEQ6MjzKGTxgAAACPt7eGxKCOJJnj2h3yGuLLI60yYFDHeF5/lGUtC0DvTN1eFsVGTP8xEKkZPAz0qlNreak56s+oNYF0AQfOB9MIAYfvkJHAAQwXztv+lb6c3hWa0NDdvnP4HjHqu1JCWe7wMRzHiRjcE/q0/PLzqjFIRII68WCc0n4PfBAB23i1AMk3ATuKZpHrca1YfWo5Hslr457Jx50jeTlHTcHoIgqJ6VR3t+olu08nGFXzbp7d29frC/B6LWFnueeNyD99u71k4m1+6PVtROiufcavhXzo2RzezM3OfAsHie76PjdhEEQXUaPBMeR1C3bcd1e7WO21UZo9M3Ed4HAyCCGYqhOZ6KpXBg2J743m4XVrMwfYeK4Zc/73pbCh+X03LRWUVvWv4AALEZ7sh7vy8AAAAASUVORK5CYII=",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/401b7fb6e76ef39c5daf9767b4485343",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "0"
                                    },
                                    {
                                        "label": "Apteek ei vasta nõuetele",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC50lEQVRIibWVzUvbYBzHvwnt6KOXJkwhOfkCg9ZeSnoS9TCYp/biamv0Hq/eJ6SF/QG7tvf6mLYOJHpQwYOKF19OjQVB3WUJzGG9jA7EZIcu6YvV1sF+tyf55ZPv7/Xx4T+ar5cDpVR0WL/EMozgOLYIADbj6Eup1Nk/wwvFosTaTIYMkDjHcSCBAAghAADTtFSqlQEHeTgPWVmWzb7hVCtl+CCviqKAyEToyXv32dX1jXJyeq5QrZSV0/OZnnC6XtJ5jo/HYlHwHPdcYACA8bFRiIKAw6Njla6XBXkhufwsnGqlDM/x8dkP71+EAsD9wRbuD3QMhCXMzinY3dtXqFayWiPw4IViUeKDvBqLRfsCX64kAADBnwkMzymYnprEpr6tFopFr9genLWZjCgKPVPRCgaA4TkFAEBIAJGJMAyjmgMQ8+CUUpEMkHi34r0EfvdFR3Am7p0jEyFUjAvJPfsAwGH9Etei+OHW6gofDEmI7rR3nevrHxIAAKIoYE0rJxbTSd0HACzDCCQQ8D64XEngV7XnjLRZdMeEf0gACQTAMozQVO7YojsgDRUi8Eq4a4QQuJPcdYjevBVeBRwMSV5aWs0HNHaFaVqqW9Chjwp+fM33DQ/ONItsmhZsxtE9+FIqdUa1cpuS4bn+fuD6AkC9/ht3tRpY+9Hy4AAAB/mr6xtlfGwUADCymsNAWMK3z8tdkE3Fo59yXkpMywIc5N1F1gJ/yJ6cniuiIICQgKfqJQvOxD3wXa2GinEBm7W9cD24LMsm1UrZw6Nj1d0ttxv5Ruc8Y7cbeS8lFaOKer2eXUo393xbt8jp+QxdLwu7e/vK9NQkRlZzGHlRu6u4CvO7uSUvtK/dJ60oLySXqVayNvVtNTIR7rrPgUbxTMtCxbhAvV7PdoK7wt0ICsWibhjVXMW4kERR6LyJcFerAQ7yNmvnW1PREw402hN/t9uaVk503qGs/Wg9d731hLfaYjqp9+PXaX8AEaIuA8T2djsAAAAASUVORK5CYII=",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/fa6b190e27f53ebe26b76897f0cdf23d",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "1"
                                    },
                                    {
                                        "label": "Apteek sulgeb uksed 1.04.2020",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC3klEQVRIibWVPVPiQBjH/4kwsjRCGiepDq0UGiZUjhY641XQIRjtLGJ/XyDwBWysSHGdrgEaJ9rojBY6Noo2BCq1uqQDrxFvHJMruIQXebubuafb3Wd/+7zs/teH/2i+cQ6UUsFh/SLLMLzj2AIA2Iyjb2cylX+GHxSLImszORIkyXA4DBIIgBACADBNS6FaGXCgwnnPS5JkTgynWinHhThFEHjEoguf1t25x6dn+fbuXqZaKS9lN3Jj4fSopHNhLplIxMGFw8MSAwDMz0Ug8Dyurm8UelTmpc307lA41Uo5Lswlv66vjYQCwMnDL+gPbxAjfsjrazg7v5CpVrK6M/DgB8WiyIU4JZGITwRO7TUAAKmXAOTVIFaWl3CsnyoHxaLXbA/O2kxOEPixpegGA4C8GgQAEBJALLoIw6gXACQ8OKVUIEGSHNS8UWD9G4dkfNobx6ILqBo10R37AMBh/WK4K2LrxR4IFyN+mPuzPXOuLx9iAQCCwONQK6e2smndBwAsw/AkEPA2pPYaqDy/j8yi38z9WfAhFiQQAMswfCdyxxbcBwIAQmgKFfwd3DVCCNyXPPARuSlOamLEP3CPD2hrhWlaittQeTUI9fJ1Yngq3impaVqwGUf34NuZTIVq5Z5IJj3A9QWAVusNjWYTrP1heXAAgAP18elZnp+LAAAKOzMQI37sfv85MuLCzoxXEtOyAAeqK2Rd8Pf87d29LPA8CGmnKX7xj4w6GZ/2wI1mE1WjBpu1VXfdg0uSZFKtlL+6vlFcbVEvXyGEpobC1ctXryRVo45Wq5XfznZ0vue2SNmNHD0q82fnF/LK8hIKOzMjI+9EXIf5wzyRNntl99NVlDbTu1QrWcf6qRKLLg7Uc6DdPNOyUDVqaLVa+X7wQLibwUGxqBtGvVA1aqIg8P0/ERrNJuBAtVlb7S7FWDjQvp74o26HWjnV/4ey9oc17HsbC++2rWxan8Sv334DTPotDHXEfvUAAAAASUVORK5CYII=",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/5e2970208586beafae3ff7e26d8d5a3b",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "2"
                                    },
                                    {
                                        "label": "Apteek vastab nõuetele",
                                        "symbol": {
                                            "type": "esriPMS",
                                            "angle": 0,
                                            "xoffset": 0,
                                            "yoffset": 0,
                                            "contentType": "image/png",
                                            "imageData": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC40lEQVRIibWVPU/bUBSGX1tBymVAxAOSrSzARJwFOQNCMIBEp2QLMYatg+FX4IRf0Xhgg4uTLMiwgARDEELiY4qTCVhaW+pApC6uhLA7BDsfJCSt1He79vXjc+45570R/EdFhm2glAo+OyaxDMP7vicAgMf45lYud//P8INSSWI9Jk/GSToWi4FEoyCEAABs29GoUQF86PBfC4qi2CPDqVHOc5OcJgg8kuLch/fBs8enZ/X27kGlRrmgyOv5oXB6VDa5GJdOpebBxWKDEgMAzM5MQ+B5VK+uNXpU4ZWN7PZAODXKeS7Gpb+srX4KBYDL+gku6ybEuAR5TcXZ+YVKjbLTmUEIPyiVJG6S01Kp+ZHAO/sZAMBKIgN5QcXy0iKOzVPtoFQKix3CWY/JCwI/9Cg6wQAgL6gAAEKiSIoJWFajCCAVwimlAhkn6X7F+wz87auJlUQ6XCfFOdSsuhSsIwDgs2NSrCPin7+cvnAxLqG62911wd6pCR4AIAg8Do1KZlPOmhEAYBmGJ9Fo+MHOfgbW96Ez0qXqro2pCR4kGgXLMHw7ct8TggFpRSHAwt/BAxFCEExy3yEKUhxVYlzq+00EaHmFbTtaUFB5QYVxo48MX020i2zbDjzGN0P4Vi53T41KVySj/kCMS8i9t6Pr/sZLswnWe3NCOADAh/749KzOzkwDAPayRYhxCbuV7T7IllYSGexli+GR2I4D+NADI+uAvxZu7x5UgedBSKtzknGpD7ITng7BL80malYdHuuF6YZwRVFsapQL1atrLfAW40bH1IQwEG7c6OGE1qwGXNctbMltn+/qFkVez9OjCn92fqEuLy1iL1v8NPJ2xA3YP+wTZaPbdj+0orKR3aZG2Tk2T7WkmOjr50CreLbjoGbV4bpuoRfcFx5kcFAqmZbVKNasuiQIfO9NhJdmE/Che6yndx7FUDjQak+8u9uhUcn03qGs9+YMut6Gwju1KWfNUfb16g/ZQS6KO4Of5gAAAABJRU5ErkJggg==",
                                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/Apteegireform/FeatureServer/0/images/9ed7519c1fa954003da81686ca6e6100",
                                            "height": 17,
                                            "width": 17
                                        },
                                        "value": "3"
                                    }
                                ]
                            },
                            "rendererType": "esri.renderers.UniqueValueRenderer"
                        }
                    ],
                    "ground": {
                        "layers": [
                            {
                                "id": "worldElevation",
                                "listMode": "show",
                                "title": "Terrain3D",
                                "url": "https://elevation3d.arcgis.com/arcgis/rest/services/WorldElevation3D/Terrain3D/ImageServer",
                                "visibility": true,
                                "layerType": "ArcGISTiledElevationServiceLayer"
                            }
                        ],
                        "transparency": 0
                    },
                    "basemap": {
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "title": "World Light Gray Base",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "title": "World Light Gray Reference",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true
                            }
                        ],
                        "title": "Light Gray Canvas"
                    }
                },
                "_username": "MBennTLL",
                "_uuid": "16c575e5-20bc-41d8-969f-373209a479ed",
                "jupyter_target": "notebook",
                "layout": "IPY_MODEL_742787314c7f4dc381ce1bbf008124b3",
                "print_service_url": "",
                "ready": true,
                "zoom": 7
            }
        },
        "9ecc5f30df954875a1de55e77dfe97ab": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.2.0",
            "state": {
                "height": "400px",
                "width": "100%"
            }
        },
        "55cc74c415f24b969688ff75f8265308": {
            "model_name": "ArcGISMapIPyWidgetModel",
            "model_module": "arcgis-map-ipywidget",
            "model_module_version": "1.7.0",
            "state": {
                "_add_this_notype_layer": {
                    "type": "FeatureLayer",
                    "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer/0?token=249pXT_B-r6ft7XoxjkeZhR5mW9agH-_FJHcKu92AiitEl9gmGpH66M9kao649gdvnhL1Mt1gf2O4q5BnoyAMN4Q1O7vmpQJXTXPmFpvJIXqOFcmtyaOv4rXL5gB8K8UBy0lk1qThob565ZvcCuWsKzxyMDaMar7PWl-X51bGX0.",
                    "options": {},
                    "_hashFromPython": "-9223371872612274067"
                },
                "_auth_mode": "tokenBased",
                "_basemap": "default",
                "_draw_these_graphics_on_widget_load": [],
                "_draw_these_notype_layers_on_widget_load": [
                    {
                        "type": "FeatureLayer",
                        "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer/0?token=249pXT_B-r6ft7XoxjkeZhR5mW9agH-_FJHcKu92AiitEl9gmGpH66M9kao649gdvnhL1Mt1gf2O4q5BnoyAMN4Q1O7vmpQJXTXPmFpvJIXqOFcmtyaOv4rXL5gB8K8UBy0lk1qThob565ZvcCuWsKzxyMDaMar7PWl-X51bGX0.",
                        "options": {},
                        "_hashFromPython": "-9223371872612274067"
                    }
                ],
                "_extent": {
                    "xmin": 21.72500459575779,
                    "ymin": 57.47309929703872,
                    "xmax": 28.235886557575526,
                    "ymax": 59.68614855697031,
                    "spatialReference": {
                        "wkid": 4326
                    }
                },
                "_gallery_basemaps": {
                    "default": {
                        "id": "28e3c1bf39c84fedb561ba38b9757be7",
                        "title": "Light Gray Canvas",
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true,
                                "opacity": 1,
                                "visibility": true,
                                "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer"
                            }
                        ],
                        "operationalLayers": []
                    }
                },
                "_portal_sharing_rest_url": "https://ag.maps.arcgis.com/sharing/rest/",
                "_portal_url": "https://ag.maps.arcgis.com",
                "_readonly_center": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "x": 2780810.4813835686,
                    "y": 8093814.282492124
                },
                "_readonly_extent": {
                    "spatialReference": {
                        "latestWkid": 3857,
                        "wkid": 102100
                    },
                    "xmin": 2300785.9437527894,
                    "ymin": 7849215.791979625,
                    "xmax": 3260835.019014348,
                    "ymax": 8338412.773004622
                },
                "_readonly_webmap_from_js": {
                    "layers": [
                        {
                            "id": "-9223371872612274067",
                            "refreshInterval": 0,
                            "url": "https://services.arcgis.com/yp7JCKsp46eWsUfk/arcgis/rest/services/CovDemo1/FeatureServer",
                            "renderer": {
                                "authoringInfo": {
                                    "classificationMethod": "esriClassifyNaturalBreaks",
                                    "colorRamp": {
                                        "type": "multipart",
                                        "colorRamps": [
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    255,
                                                    245,
                                                    235,
                                                    255
                                                ],
                                                "toColor": [
                                                    255,
                                                    231,
                                                    207,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    255,
                                                    231,
                                                    207,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    207,
                                                    162,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    207,
                                                    162,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    174,
                                                    106,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    174,
                                                    106,
                                                    255
                                                ],
                                                "toColor": [
                                                    252,
                                                    141,
                                                    61,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    252,
                                                    141,
                                                    61,
                                                    255
                                                ],
                                                "toColor": [
                                                    242,
                                                    105,
                                                    19,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    242,
                                                    105,
                                                    19,
                                                    255
                                                ],
                                                "toColor": [
                                                    217,
                                                    72,
                                                    0,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    217,
                                                    72,
                                                    0,
                                                    255
                                                ],
                                                "toColor": [
                                                    166,
                                                    55,
                                                    3,
                                                    255
                                                ]
                                            },
                                            {
                                                "type": "algorithmic",
                                                "algorithm": "esriCIELabAlgorithm",
                                                "fromColor": [
                                                    166,
                                                    55,
                                                    3,
                                                    255
                                                ],
                                                "toColor": [
                                                    128,
                                                    39,
                                                    4,
                                                    255
                                                ]
                                            }
                                        ]
                                    },
                                    "type": "classedColor"
                                },
                                "type": "classBreaks",
                                "classBreakInfos": [
                                    {
                                        "label": "≤22.5%",
                                        "classMaxValue": 0.22509074648850544,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                255,
                                                245,
                                                235,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤23.2%",
                                        "classMaxValue": 0.2316336848187202,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                254,
                                                231,
                                                209,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤24.6%",
                                        "classMaxValue": 0.245809724405945,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                212,
                                                171,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤24.9%",
                                        "classMaxValue": 0.24881370472641484,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                185,
                                                125,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤25.4%",
                                        "classMaxValue": 0.25434874840899446,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                253,
                                                155,
                                                80,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.0%",
                                        "classMaxValue": 0.2596328029375765,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                247,
                                                125,
                                                41,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.4%",
                                        "classMaxValue": 0.2642192670287819,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                233,
                                                94,
                                                13,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤26.8%",
                                        "classMaxValue": 0.2678786709745865,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                205,
                                                68,
                                                1,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤27.3%",
                                        "classMaxValue": 0.2725665522048074,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                161,
                                                52,
                                                3,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    },
                                    {
                                        "label": "≤31.5%",
                                        "classMaxValue": 0.31494649997393875,
                                        "symbol": {
                                            "type": "esriSFS",
                                            "color": [
                                                127,
                                                39,
                                                4,
                                                255
                                            ],
                                            "outline": {
                                                "type": "esriSLS",
                                                "color": [
                                                    110,
                                                    110,
                                                    110,
                                                    255
                                                ],
                                                "width": 0.7,
                                                "style": "esriSLSSolid"
                                            },
                                            "style": "esriSFSSolid"
                                        }
                                    }
                                ],
                                "legendOptions": {},
                                "minValue": 0.22509074648850544,
                                "valueExpression": "$feature.TOT_GE60/$feature.TOTAL",
                                "valueExpressionTitle": "Custom"
                            },
                            "rendererType": "esri.renderers.ClassBreaksRenderer"
                        }
                    ],
                    "ground": {
                        "layers": [
                            {
                                "id": "worldElevation",
                                "listMode": "show",
                                "title": "Terrain3D",
                                "url": "https://elevation3d.arcgis.com/arcgis/rest/services/WorldElevation3D/Terrain3D/ImageServer",
                                "visibility": true,
                                "layerType": "ArcGISTiledElevationServiceLayer"
                            }
                        ],
                        "transparency": 0
                    },
                    "basemap": {
                        "baseMapLayers": [
                            {
                                "id": "World_Light_Gray_Base_2890",
                                "title": "World Light Gray Base",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer"
                            },
                            {
                                "id": "World_Light_Gray_Reference_7134",
                                "title": "World Light Gray Reference",
                                "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer",
                                "layerType": "ArcGISTiledMapServiceLayer",
                                "isReference": true
                            }
                        ],
                        "title": "Light Gray Canvas"
                    }
                },
                "_username": "MBennTLL",
                "_uuid": "04527992-c29d-4880-99b7-167303c4cc48",
                "jupyter_target": "notebook",
                "layout": "IPY_MODEL_9ecc5f30df954875a1de55e77dfe97ab",
                "print_service_url": "",
                "ready": true,
                "zoom": 7
            }
        }
    }
}
</script>
</head>
<body>

<script type="application/vnd.jupyter.widget-view+json">
{
    "version_major": 2,
    "version_minor": 0,
    "model_id": "55cc74c415f24b969688ff75f8265308"
}
</script>

</body>
</html>"""


class remap:
    MNIMI_MKOOD = {
             'Pärnu maakond': '0068',
             'Saare maakond': '0074',
             'Lääne-Viru maakond': '0060',
             'Harju maakond': '0037',
             'Viljandi maakond': '0084',
             'Tartu maakond': '0079',
             'Jõgeva maakond': '0050',
             'Põlva maakond': '0064',
             'Ida-Viru maakond': '0045',
             'Võru maakond': '0087',
             'Lääne maakond': '0056',
             'Rapla maakond': '0071',
             'Valga maakond': '0081',
             'Hiiu maakond': '0039',
             'Järva maakond': '0052',
             'Eesti': '9999',
             'Välismaa' : '9998',
             None: '9997'}
    
    MKOOD_MNIMI = {
             '0068' : 'Pärnu maakond' ,
             '0074' : 'Saare maakond' ,
             '0060' : 'Lääne-Viru maakond' ,
             '0037' : 'Harju maakond' ,
             '0084' : 'Viljandi maakond' ,
             '0079' : 'Tartu maakond' ,
             '0050' : 'Jõgeva maakond' ,
             '0064' : 'Põlva maakond' ,
             '0045' : 'Ida-Viru maakond' ,
             '0087' : 'Võru maakond' ,
             '0056' : 'Lääne maakond' ,
             '0071' : 'Rapla maakond' ,
             '0081' : 'Valga maakond' ,
             '0039' : 'Hiiu maakond' ,
             '0052' : 'Järva maakond' ,
             '9999' : 'Eesti' ,
             '9998' : 'Välismaa' ,
             '9997' :  None }
             
    VANUSER_STR = {  None: 'Tundmatu',
                 '0-4': '00-04',
                 '5-9': '05-09',
                 '10-14': '10-14',
                 '15-19': '15-19',
                 '20-24': '20-24',
                 '25-29': '25-29',
                 '30-34': '30-34',
                 '35-39': '35-39',
                 '40-44': '40-44',
                 '45-49': '45-49',
                 '50-54': '50-54',
                 '55-59': '55-59',
                 '60-64': '60-64',
                 '65-69': '65-69',
                 '70-74': '70-74',
                 '75-79': '75-79',
                 '80-84': '80-84',
                 'üle 85': '85+'}    
                 
    VANUSER_FLOAT = {   None: 0,
                 '0-4': 2.5,
                 '5-9': 7.5,
                 '10-14': 12.5,
                 '15-19': 17.5,
                 '20-24': 22.5,
                 '25-29': 27.5,
                 '30-34': 32.5,
                 '35-39': 37.5,
                 '40-44': 42.5,
                 '45-49': 47.5,
                 '50-54': 52.5,
                 '55-59': 57.5,
                 '60-64': 62.5,
                 '65-69': 67.5,
                 '70-74': 72.5,
                 '75-79': 77.5,
                 '80-84': 82.5,
                 'üle 85': 87.5}
                 
                 
    VANUSERRK_STR = {'LT5' : '00-04',
                 '5_9' : '05-09',
                 '10_14' : '10-14',
                 '15_19' : '15-19',
                 '20_24' : '20-24',
                 '25_29' : '25-29',
                 '30_34' : '30-34',
                 '35_39' : '35-39',
                 '40_44' : '40-44',
                 '45_49' : '45-49',
                 '50_54' : '50-54',
                 '55_59' : '55-59',
                 '60_64' : '60-64',
                 '65_69' : '65-69',
                 '70_74' : '70-74',
                 '75_79' : '75-79',
                 '80_84' : '80-84',
                 'GE85' : '85+'}