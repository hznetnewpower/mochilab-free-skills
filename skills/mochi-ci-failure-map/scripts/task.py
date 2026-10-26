import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 text=c.read(r['file']);lines=text.splitlines();patterns={'tests':r'FAILED|AssertionError|tests? failed','dependencies':r'ModuleNotFoundError|Cannot find module|ERESOLVE','compile':r'error TS\d+|SyntaxError|compilation failed','permission':r'Permission denied|EACCES','timeout':r'timed out|TimeoutError'};found=[]
 for i,line in enumerate(lines,1):
  tags=[k for k,p in patterns.items() if re.search(p,line,re.I)]
  if tags:found.append({'line':i,'categories':tags})
 return {'signals':found,'categories':dict(collections.Counter(t for x in found for t in x['categories'])),'rootCauseConfirmed':False,'workflowReRun':False}
