import json
from urllib.request import urlopen


def ripe_get_prefixes_per_asn(asn):
    """ Uses RIPE's API (https://stat.ripe.net/data/announced-prefixes/data.?)
    to list the prefixes associated to a given Autonomous System Number (ASN)

    e.g., e.g. https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime=2011-12-12T12:00

    This API is documented on https://stat.ripe.net/docs/data_api
    """
    url_base='https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS'
    rep = urlopen(url_base+str(asn)+'&starttime='+'2011-12-12T12:00')
    data= str(rep.read().decode(encoding='UTF-8'))
    rep.close()
    js_data= json.loads(data)
    pref_list=[]
    for record in js_data['data']['prefixes']:
        pref_list.append(record['prefix'])
    return pref_list

def ripe_get_asn_holder(asn):
    """ Uses RIPE's API (https://stat.ripe.net/data/as-overview/data.json?resource=)
    to query asn info associated to a given Autonomous System Number (ASN)

    e.g., e.g. https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime=2011-12-12T12:00

    This API is documented on https://stat.ripe.net/docs/data_api
    """
    url_base='https://stat.ripe.net/data/as-overview/data.json?resource=AS'
    rep = urlopen(url_base+str(asn))
    data= str(rep.read().decode(encoding='UTF-8'))
    rep.close()
    js_data= json.loads(data)
    return js_data['data']['holder']
