import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 topics=r['topics'];need(topics and all(isinstance(v,list) and v for v in topics.values()),'Topics need keyword lists');rows=[];counts=collections.Counter()
 for x in r['feedback']:
  matched=[k for k,words in topics.items() if any(word.casefold() in x['text'].casefold() for word in words)];matched=matched or ['unclassified'];counts.update(matched);rows.append({'id':x['id'],'topics':matched})
 return {'assignments':rows,'topicCounts':dict(counts),'records':len(rows),'method':'user-defined keyword matching; multiple labels allowed','sentimentOrIntentInferred':False}
