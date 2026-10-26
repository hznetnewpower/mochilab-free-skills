import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 stops=sorted(r['stops'],key=lambda x:instant(x['start']));issues=[];totals=collections.defaultdict(lambda:decimal(0));previous=None;lines=['# '+r.get('title','Itinerary')]
 for x in stops:
  a,b=instant(x['start']),instant(x['end']);need(a<b,'Stop end must follow start')
  if previous is not None and a<previous:issues.append({'stop':x['name'],'issue':'time-overlap'})
  previous=max(previous,b) if previous is not None else b;amount=decimal(x.get('cost',0));need(amount>=0,'Cost must be nonnegative');totals[x.get('currency','unspecified')]+=amount;lines.append('- '+a.isoformat()+' '+x['name'])
 c.emit('itinerary.md','\n'.join(lines)+'\n');return {'stops':len(stops),'issues':issues,'estimatedTotalsByCurrency':{k:str(v) for k,v in totals.items()},'travelTimeOrAvailabilityChecked':False,'bookingsMade':False}
