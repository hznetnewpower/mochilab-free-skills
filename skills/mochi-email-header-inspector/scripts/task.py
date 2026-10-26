import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 message=email.parser.Parser(policy=email.policy.default).parsestr(c.read(r['file']),headersonly=True);from_values=message.get_all('From',[]);auth=message.get_all('Authentication-Results',[]);signals=[]
 if len(from_values)!=1:signals.append('unexpected-from-header-count')
 if any(re.search(r'\b(?:spf|dkim|dmarc)=fail\b',str(x),re.I) for x in auth):signals.append('reported-authentication-failure')
 received=message.get_all('Received',[])
 return {'fromHeaderCount':len(from_values),'receivedHopCount':len(received),'authenticationResultHeaderCount':len(auth),'signals':signals,'headersCryptographicallyVerified':False,'bodyLinksOpened':False,'trustedMailServerRequired':True}
