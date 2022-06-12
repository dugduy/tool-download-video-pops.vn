from requests import post
res=post('https://stream.popsww.com/v1/drm/keys?type=widevine',"\b\u0004")
print(res,res.content)