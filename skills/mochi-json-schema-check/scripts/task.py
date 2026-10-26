import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 schema=r['schema'];value=r['value'];errors=[];unsupported=set()
 def check(s,v,p):
  supported={'type','properties','required','items','enum','minimum','maximum','additionalProperties','description','title'};unsupported.update(set(s)-supported)
  types={'object':lambda:isinstance(v,dict),'array':lambda:isinstance(v,list),'string':lambda:isinstance(v,str),'integer':lambda:isinstance(v,int) and not isinstance(v,bool),'number':lambda:isinstance(v,(int,float)) and not isinstance(v,bool),'boolean':lambda:isinstance(v,bool),'null':lambda:v is None}
  if 'type' in s:
   need(s['type'] in types,'Unsupported type declaration')
   if not types[s['type']]():errors.append(p+':type');return
  if isinstance(s.get('additionalProperties'),dict):unsupported.add('additionalProperties:schema')
  if 'enum' in s and not any((type(v)==type(x) or (isinstance(v,(int,float)) and isinstance(x,(int,float)) and not isinstance(v,bool) and not isinstance(x,bool))) and v==x for x in s['enum']):errors.append(p+':enum')
  if isinstance(v,dict):
   for k in s.get('required',[]):
    if k not in v:errors.append(p+'/'+k+':required')
   for k,x in v.items():
    if k in s.get('properties',{}):check(s['properties'][k],x,p+'/'+k)
    elif s.get('additionalProperties') is False:errors.append(p+'/'+k+':additional-property')
  if isinstance(v,list) and 'items' in s:
   for i,x in enumerate(v):check(s['items'],x,p+'/'+str(i))
  if isinstance(v,(int,float)) and not isinstance(v,bool):
   if 'minimum' in s and v<s['minimum']:errors.append(p+':minimum')
   if 'maximum' in s and v>s['maximum']:errors.append(p+':maximum')
 check(schema,value,'$');return {'validForSupportedSubset':not errors and not unsupported,'errors':errors,'unsupportedKeywords':sorted(unsupported),'fullJsonSchemaValidation':False}
