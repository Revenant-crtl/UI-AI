from aift import setting
from aift.multimodal import vqa

setting.set_api_key('Jaq4cvMvKvA2g1nli09iN95etj7cXMPr')


result = vqa.generate('doraemon.jpg', 'บรรยายรูปนี้')
print(result)




