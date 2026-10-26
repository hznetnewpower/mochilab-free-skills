import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 tasks=r['tasks'];need(len({x['id'] for x in tasks})==len(tasks),'Duplicate task ID');blockers=[]
 for x in tasks:
  if x.get('required',True) and (x.get('status')!='done' or not x.get('evidence')):blockers.append({'id':x['id'],'reason':'incomplete-or-no-evidence'})
 return {'readyForHumanDecision':not blockers,'blockers':blockers,'taskCount':len(tasks),'launchExecuted':False,'complianceCertified':False}
