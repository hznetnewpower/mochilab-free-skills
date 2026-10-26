import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 rows=[]
 for x in r['links']:
  url=urllib.parse.urlsplit(x['url']);need(url.scheme in ['http','https'] and url.netloc and not url.username and not url.password,'Use a public HTTP(S) URL without embedded credentials');query=urllib.parse.parse_qsl(url.query,keep_blank_values=True);need(not any(k.lower() in ['token','key','api_key','password'] for k,v in query),'Remove secret query parameters before campaign planning');params={k:x[k] for k in ['utm_source','utm_medium','utm_campaign','utm_term','utm_content'] if x.get(k)};need(all(params.get(k) for k in ['utm_source','utm_medium','utm_campaign']),'source, medium and campaign are required');query=[(k,v) for k,v in query if k not in params]+list(params.items());rows.append({'url':urllib.parse.urlunsplit((url.scheme,url.netloc,url.path,urllib.parse.urlencode(query),url.fragment))})
 return {'links':rows,'count':len(rows),'linksOpened':False,'trackingEndpointCreated':False}
