import re

class Lrc:
	def __init__(self):
		self.SP_DTWDSTR = re.compile(r'(?P<time>(?:(?:\[)[\d\.:]+(?:\]))+)(?P<word>[^\n\[\]]*)')
		self.SP_DTSTR = re.compile(r'(?<=\[)([\d\.:]+)(?=\])')

		self.LRC = [[0.0, '无歌词']]
		self.Times = [0.0]
		self.Words = ['无歌词']

	def decode_from_str(self, lrc: str):
		lrc = lrc.strip('\n')
		res1 = self.SP_DTWDSTR.findall(lrc)
		res2 = list()
		res3 = dict()
		result = dict()
		for r in res1:
			res2.append([self.SP_DTSTR.findall(r[0]), r[1]])
		for r in res2:
			for t in r[0]:
				res3[self.tosec(t)] = r[1]

		result = sorted(list(res3.items()), key=lambda x: x[0])

		self.decode(result)

		return self.LRC

	def decode(self, lrcs):
		self.LRC = lrcs
		r = list(zip(*lrcs))
		self.Words = list(r[0])
		self.Times = list(map(self.tosec, list(r[1])))

	# 将字符串时间变为秒
	def tosec(self, t:str):
		res1 = t.split(':')[::-1]
		res2 = [float(r) * (60 ** i) for i, r in enumerate(res1)]
		result = sum(res2)

		return result

	# 根据浮点数播放进度获取对应歌词索引
	def get_index(self, t:float):
		times = [*self.Times, t]
		times.sort()
		
		return times.index(t) - 1

	def get_word(self, t:float):

		return self.Words[self.get_index(t)]
