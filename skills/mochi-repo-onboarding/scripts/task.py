import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 files=r['files'];need(all(isinstance(x,str) for x in files),'Use an explicit repository file list');signals={'node':'package.json','python':'pyproject.toml','dotnet':'.csproj','java':'pom.xml','rust':'Cargo.toml','go':'go.mod'};languages=[name for name,pattern in signals.items() if any(x.endswith(pattern) for x in files)];docs=[x for x in files if re.search(r'(readme|contributing|agents\.md)$',x,re.I) or x.lower().endswith('readme.md')];tests=[x for x in files if re.search(r'(^|/)(tests?|__tests__)/|test_[^/]+\.py$',x)]
 return {'ecosystems':languages,'documentation':docs,'testFiles':tests,'fileCount':len(files),'commandsExecuted':False,'onboardingQuestions':['Which directory is the maintained application?','Which documented checks are required?']}
