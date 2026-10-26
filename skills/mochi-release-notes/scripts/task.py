import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 groups=collections.defaultdict(list);breaking=[]
 for x in r['commits']:
  subject=x['subject'];m=re.match(r'([a-z]+)(?:\([^)]*\))?(!)?:\s*(.*)',subject);kind=m[1] if m else 'other';groups[kind].append({'id':x['id'],'subject':m[3] if m else subject})
  if (m and m[2]) or 'BREAKING CHANGE:' in x.get('body',''):breaking.append(x['id'])
 text='# '+r.get('version','Release')+'\n\n'+'\n'.join('## '+k+'\n'+'\n'.join('- '+x['subject']+' ('+x['id']+')' for x in xs)+'\n' for k,xs in sorted(groups.items()));c.emit('release-notes.md',text)
 return {'groups':dict(groups),'breakingCommitIds':breaking,'commitCount':len(r['commits']),'releasePublished':False}
