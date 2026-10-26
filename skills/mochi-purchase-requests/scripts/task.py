import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 requests=r['requests'];need(len({x['id'] for x in requests})==len(requests),'Duplicate request ID');totals=collections.defaultdict(lambda:decimal(0));rows=[]
 for x in requests:
  quantity=decimal(x['quantity']);price=decimal(x['unitPrice']);need(quantity>0 and price>=0,'Quantity must be positive and price nonnegative');total=quantity*price;currency=x['currency'];totals[currency]+=total;threshold=decimal(r.get('approvalThresholds',{}).get(currency,0));rows.append({'id':x['id'],'estimatedTotal':str(total),'currency':currency,'approvalNeeded':total>threshold,'quoteProvided':bool(x.get('quoteSource'))})
 return {'requests':rows,'totalsByCurrency':{k:str(v) for k,v in totals.items()},'purchaseOrPaymentExecuted':False,'approvalGranted':False,'taxShippingIncludedOnlyIfInInput':True}
