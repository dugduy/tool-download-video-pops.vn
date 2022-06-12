from requests import get
res=get('https://vnw-vod-cdn.popsww.com/dw-McYKAdFGYr7xal0VTO5imryr3YE/videos/transcoded/upload_thamtulungdanhconan_tap_571_app-popsapp/init-v1-f2-v1.mp4')
print(res)
open('./vid_data/init.mp4','wb').write(res.content)
for i in range(1,376):
    res=get('https://vnw-vod-cdn.popsww.com/dw-McYKAdFGYr7xal0VTO5imryr3YE/videos/transcoded/upload_thamtulungdanhconan_tap_571_app-popsapp/eseg-v1-%s-f2-v1.m4s'%i)
    print(i,res)
    open('./vid_data/eseg%s.m4s'%i,'wb').write(res.content)