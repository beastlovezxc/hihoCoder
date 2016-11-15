import sys
import collections

# urls = []

n, m = map(int, sys.stdin.readline().split())

mp = collections.OrderedDict()
for i in range(n):
	url = raw_input()
	if url in mp:
		print "Cache"
		mp.pop(url)
	else:
		print "Internet"
		if len(mp) >= m:
			mp.popitem(last = False)
	mp[url] = 1

# TLE 
# for i in range(n):
# 	flag = 0
# 	url = raw_input()

# 	uLen = len(urls)
# 	j = 0
# 	while j < uLen:
# 		if urls[j] == url:
# 			print "Cache"
# 			urls.remove(url)
# 			urls.append(url)
# 			flag = 1
# 			break
# 		j += 1
# 	if not flag:
# 		print "Internet"
# 		if uLen < m:
# 			urls.append(url)
# 		else:
# 			urls.pop(0)
# 			urls.append(url)

