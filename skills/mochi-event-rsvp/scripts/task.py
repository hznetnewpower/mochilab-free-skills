import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 people=r['people'];need(len({x['id'] for x in people})==len(people),'Duplicate attendee ID');counts=collections.Counter();meals=collections.Counter();total=0
 for x in people:
  status=x['status'];need(status in ['yes','no','maybe','pending'],'Unknown RSVP status');count=int(x.get('partySize',1));need(count>=1,'partySize must be positive');counts[status]+=1
  if status=='yes':total+=count;meals[x.get('meal','unspecified')]+=count
 return {'responsesByStatus':dict(counts),'confirmedPeople':total,'mealCounts':dict(meals),'capacityExceeded':total>int(r['capacity']),'invitationsSent':False,'contactDetailsExported':False}
