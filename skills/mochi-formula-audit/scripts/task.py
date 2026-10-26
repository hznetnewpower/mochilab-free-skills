import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 z=safezip(c.bytes(r['file']));ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'};rows=[];errors=[];external=[]
 for name in z.namelist():
  if re.fullmatch(r'xl/worksheets/sheet\d+\.xml',name):
   root=ET.fromstring(z.read(name))
   for cell in root.findall('.//s:c',ns):
    f=cell.find('s:f',ns);v=cell.find('s:v',ns)
    if f is not None:
     text=f.text or '';rows.append({'sheet':name,'cell':cell.get('r'),'cachedResultPresent':v is not None and v.text is not None,'refErrorInFormula':'#REF!' in text})
    if cell.get('t')=='e':errors.append({'sheet':name,'cell':cell.get('r'),'error':v.text if v is not None else None})
  if name.startswith('xl/externalLinks/') and name.endswith('.xml'):external.append(name)
 return {'formulaCount':len(rows),'formulas':rows,'cachedErrors':errors,'externalLinkParts':external,'formulasRecalculated':False,'workbookModified':False}
