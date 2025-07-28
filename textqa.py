from aift import setting
from aift.multimodal import textqa
setting.set_api_key('Jaq4cvMvKvA2g1nli09iN95etj7cXMPr')

result = textqa.generate('AI จะครองโลกไหม')

print(result['content'])



