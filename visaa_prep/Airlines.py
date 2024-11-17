import math
k,l=map(int,input().split())
ttl_planes_req=math.ceil(l/ 100)
new_planes_req=max(0, ttl_planes_req - k)
print(new_planes_req)
