import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 a=r['before'];b=r['after'];need(isinstance(a,dict) and isinstance(b,dict),'Use name-to-version maps');changes=[]
 for name in sorted(set(a)|set(b)):
  if a.get(name)==b.get(name):continue
  old=a.get(name);new=b.get(name);kind='added' if name not in a else 'removed' if name not in b else 'changed';major=False
  if old and new:
   p=re.match(r'^(\d+)\.',str(old));q=re.match(r'^(\d+)\.',str(new));major=bool(p and q and p[1]!=q[1])
  changes.append({'name':name,'before':old,'after':new,'change':kind,'majorVersionChanged':major})
 return {'changes':changes,'changedCount':len(changes),'vulnerabilitiesChecked':False,'dependenciesInstalled':False}
