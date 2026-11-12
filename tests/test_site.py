from pathlib import Path
from html.parser import HTMLParser
import json, hashlib, unittest
R=Path(__file__).resolve().parents[1]
class PageLinks(HTMLParser):
 def __init__(self): super().__init__();self.paths=[];self.ids=set();self.anchors=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  for key in ('src','href'):
   if key in a:
    value=a[key]
    if value.startswith('#'):self.anchors.append(value[1:])
    elif not value.startswith(('https://','http://','mailto:','data:')):self.paths.append(value.split('#')[0])
class SiteTest(unittest.TestCase):
 def test_local_links_and_anchors(self):
  p=PageLinks();p.feed((R/'index.html').read_text(encoding='utf8'))
  for path in p.paths:self.assertTrue((R/path).is_file(),path)
  for anchor in p.anchors:self.assertIn(anchor,p.ids,anchor)
 def test_manifest(self):
  m=json.loads((R/'source/AXEZENT_Original_Design_Manifest.json').read_text())
  self.assertEqual(m['design']['side_mm'],63.5)
 def test_stl_header_counts(self):
  for file in (R/'assets/models').glob('*.stl'):
   with file.open('rb') as f:f.seek(80);n=int.from_bytes(f.read(4),'little')
   self.assertEqual(file.stat().st_size,84+50*n)
 def test_sha256(self):
  for line in (R/'docs/SHA256SUMS.txt').read_text().splitlines():
   sha, path=line.split('  ',1)
   self.assertEqual(hashlib.sha256((R/path).read_bytes()).hexdigest(),sha)
 def test_scholarly_name_and_disclosures(self):
  t=(R/'index.html').read_text(encoding='utf8')
  self.assertIn('Shawn Calvin Snelling',t)
  self.assertIn('not established',t)
  self.assertIn('simulated stress or strength prediction',t)
if __name__=='__main__':unittest.main()
