import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 start=instant(r['start']);end=instant(r['end']);need(start<end,'Window start must precede end');duration=int(r.get('minMinutes',30));need(duration>0,'minMinutes must be positive');busy=[]
 for person in r['people']:
  for x in person.get('busy',[]):
   a,b=instant(x['start']),instant(x['end']);need(a<b,'Busy interval must have positive duration')
   if a<end and b>start:busy.append((max(a,start),min(b,end)))
 merged=[]
 for a,b in sorted(busy):
  if merged and a<=merged[-1][1]:merged[-1]=(merged[-1][0],max(b,merged[-1][1]))
  else:merged.append((a,b))
 free=[];cursor=start
 for a,b in merged+[(end,end)]:
  if (a-cursor).total_seconds()>=duration*60:free.append({'start':cursor.isoformat(),'end':a.isoformat(),'minutes':int((a-cursor).total_seconds()/60)})
  cursor=max(cursor,b)
 return {'available':free,'people':len(r['people']),'eventCreated':False,'liveCalendarsQueried':False}
