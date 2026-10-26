import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 events=r['events'];need(len({x['id'] for x in events})==len(events),'Duplicate event ID');ordered=sorted(events,key=lambda x:instant(x['at']));rows=[]
 for i,x in enumerate(ordered):
  need(x.get('source'),'Every incident event needs a source');gap=(instant(x['at'])-instant(ordered[i-1]['at'])).total_seconds() if i else None;rows.append({'id':x['id'],'at':x['at'],'summary':x['summary'],'source':x['source'],'gapSeconds':gap})
 c.emit('timeline.md','# Incident timeline\n\n'+'\n'.join('- '+x['at']+' '+x['summary']+' ['+x['source']+']' for x in rows)+'\n');return {'events':rows,'eventCount':len(rows),'rootCauseInferred':False,'mitigationActionsExecuted':False}
