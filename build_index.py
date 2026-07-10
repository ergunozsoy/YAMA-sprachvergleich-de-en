import json, content
tpl=open("index.template.html",encoding="utf-8").read()
data=json.dumps(content.app_json(), ensure_ascii=False)
out=tpl.replace("__APP_DATA__", data)
open("index.html","w",encoding="utf-8").write(out)
print("index.html written:", len(out), "bytes; topics:", len(content.DETAIL))
