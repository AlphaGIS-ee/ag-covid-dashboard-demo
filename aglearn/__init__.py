from datetime import datetime as dt
from IPython.core.display import display, HTML
import requests


def lprint(text): # pretty log printing 
    tn = dt.now()
    print("{} : {}".format(tn.strftime("%d.%m.%y %H:%M:%S"), text))

__all__ = ['lprint', 'printReport', 'requestFromREST']


def printReport(data_item):
    display(HTML('<h3>{}</h3>'.format(data_item.name)))
    #display(HTML("<hr>"))
    display(HTML('<h5>Description</h5>'))
    display(HTML(data_item.description))
    #display(HTML("<hr>"))
    #display(HTML("Item is owned by: <b>{}</b>, and the person shared with everyone: <b>{}</b>".format(data_item.owner, data_item.shared_with['everyone'])))
    #display(HTML("<hr>"))
    display(HTML("The dataset has <b>{} layer </b> ...".format(len(data_item.tables))))
    i = 0
    for lyr in data_item.layers:
        print(i, lyr.properties.name)
        i += 1
    display(HTML("... and <b>{} tables</b>.".format(len(data_item.layers))))
    for lyr in data_item.tables:
        print(i, lyr.properties.name)
        i += 1
    #display(HTML("<hr>"))
    #display(HTML('<h5>Usage last 24h</h5>'))
    #display(data_item.usage(date_range='24H', as_df=True).set_index('Date').plot(figsize=(15,5)))

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