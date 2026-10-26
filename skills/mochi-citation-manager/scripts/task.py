import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 records=r['records'];seen=set();entries=[];duplicates=[]
 def esc(s):return str(s).replace('\\','\\textbackslash{}').replace('{','\\{').replace('}','\\}').replace('\n',' ')
 for x in records:
  doi=x.get('doi','').strip().lower();doi=re.sub(r'^https?://(?:dx\.)?doi\.org/','',doi);key=doi or re.sub(r'\W+','',x['title'].lower());need(x.get('title') and x.get('id'),'Each reference needs title and id')
  if key in seen:duplicates.append(x['id']);continue
  seen.add(key);need(re.fullmatch(r'[A-Za-z0-9_-]+',x['id']),'Simple citation ID required');fields={'title':x['title'],'author':' and '.join(x.get('authors',[])),'year':x.get('year',''),'doi':doi};entries.append('@misc{'+x['id']+',\n'+',\n'.join('  '+k+' = {'+esc(v)+'}' for k,v in fields.items() if v)+'\n}')
 c.emit('references.bib','\n\n'.join(entries)+'\n');return {'uniqueReferences':len(entries),'duplicateIds':duplicates,'doiResolvedOrVerified':False,'bibliographyCompiled':False}
