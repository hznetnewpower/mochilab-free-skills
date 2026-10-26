import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 dates=sorted({dt.date.fromisoformat(x) for x in r['dates']});asof=dt.date.fromisoformat(r['asOf']);need(all(x<=asof for x in dates),'Future completion date');done=set(dates);streak=0;cursor=asof
 while cursor in done:streak+=1;cursor-=dt.timedelta(days=1)
 window=int(r.get('windowDays',30));need(1<=window<=3660,'windowDays must be1..3660');inside=[x for x in dates if 0<=(asof-x).days<window]
 return {'completedDays':len(dates),'streakEndingAsOf':streak,'windowCompletedDays':len(inside),'windowDays':window,'completionRate':round(len(inside)/window,4),'healthAdviceProvided':False,'remindersScheduled':False}
