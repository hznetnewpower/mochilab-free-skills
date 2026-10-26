import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 z=safezip(c.bytes(r['file']));need('word/document.xml' in z.namelist(),'DOCX document.xml missing');w='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}';document=ET.fromstring(z.read('word/document.xml'));comments={};revisions=[];anchors=[]
 if 'word/comments.xml' in z.namelist():
  for item in ET.fromstring(z.read('word/comments.xml')).iter(w+'comment'):
   key=item.get(w+'id');need(key not in comments,'Duplicate comment ID');comments[key]={'id':key,'text':''.join(x.text or '' for x in item.iter(w+'t'))}
 for paragraph,p in enumerate(document.iter(w+'p'),1):
  for item in p.iter():
   if item.tag in [w+'ins',w+'del']:revisions.append({'id':item.get(w+'id'),'kind':'insert' if item.tag==w+'ins' else 'delete','paragraph':paragraph})
   if item.tag==w+'commentReference':anchors.append({'id':item.get(w+'id'),'paragraph':paragraph})
 missing=[x for x in anchors if x['id'] not in comments]
 return {'commentCount':len(comments),'comments':list(comments.values()),'revisionCount':len(revisions),'revisions':revisions,'commentAnchors':anchors,'missingCommentDefinitions':missing,'changesAcceptedOrRejected':False,'documentModified':False,'visualRenderingChecked':False}
