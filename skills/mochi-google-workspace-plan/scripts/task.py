import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 allowed={'gmail.search':False,'gmail.draft':True,'calendar.list':False,'calendar.create':True,'drive.list':False,'drive.upload':True,'sheets.read':False,'sheets.update':True,'docs.read':False,'docs.update':True};steps=[]
 for x in r['actions']:
  need(x['kind'] in allowed,'Unknown Workspace action');need(x.get('account'),'Specify the intended account');steps.append({'kind':x['kind'],'account':x['account'],'mutatesRemote':allowed[x['kind']],'ready':bool(x.get('resource') or x.get('query')),'needsToolDiscovery':True})
 return {'steps':steps,'mutatingActions':sum(x['mutatesRemote'] for x in steps),'connectorAuthenticated':False,'remoteActionsExecuted':False,'note':'Use available authorized Workspace tools or inspect the installed gog help before mapping this plan to commands.'}
