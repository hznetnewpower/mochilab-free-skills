import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 api=c.data(r['file']);need(str(api.get('openapi','')).startswith('3.'),'OpenAPI3 JSON required');operations=[];ids=set();issues=[]
 for route,item in api.get('paths',{}).items():
  for method,op in item.items():
   if method not in ['get','put','post','delete','options','head','patch','trace']:continue
   oid=op.get('operationId');operations.append(method.upper()+' '+route)
   if oid and oid in ids:issues.append('duplicate-operationId:'+oid)
   if oid:ids.add(oid)
   parameters=item.get('parameters',[])+op.get('parameters',[]);declared={p.get('name') for p in parameters if p.get('in')=='path' and p.get('required') is True}
   for p in re.findall(r'\{([^}]+)\}',route):
    if p not in declared:issues.append('missing-required-path-parameter:'+p)
   if not op.get('responses'):issues.append('missing-responses:'+method+' '+route)
 return {'operations':operations,'issues':issues,'validForChecks':not issues,'fullSpecificationValidation':False,'remoteRequestsSent':False}
