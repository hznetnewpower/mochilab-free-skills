import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 assets=r['assets'];need(len({x['file'] for x in assets})==len(assets),'Duplicate asset file');issues=[]
 for x in assets:
  p=c.path(x['file']);need(p.is_file(),'Selected asset missing')
  if not x.get('decorative') and not x.get('alt','').strip():issues.append({'file':x['file'],'issue':'missing-alt'})
  if p.stat().st_size>int(r.get('maxBytes',500000)):issues.append({'file':x['file'],'issue':'over-size-budget'})
  if x.get('width',0)<=0 or x.get('height',0)<=0:issues.append({'file':x['file'],'issue':'missing-declared-dimensions'})
 return {'assetCount':len(assets),'issues':issues,'imageContentVisuallyReviewed':False,'declaredDimensionsDecoded':False,'filesOptimized':False}
