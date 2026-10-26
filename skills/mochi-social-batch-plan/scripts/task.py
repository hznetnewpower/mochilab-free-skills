import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 limits=r['platformLimits'];rows=[]
 for x in r['posts']:
  need(x['platform'] in limits and int(limits[x['platform']])>0,'Provide a positive limit for each platform');length=len(x['text']);rows.append({'id':x['id'],'platform':x['platform'],'unicodeCodePoints':length,'limit':int(limits[x['platform']]),'overLimit':length>int(limits[x['platform']]),'assetCount':len(x.get('assets',[]))})
 return {'posts':rows,'overLimitCount':sum(x['overLimit'] for x in rows),'platformRulesFetched':False,'platformSpecificCountingApplied':False,'postsPublished':False}
