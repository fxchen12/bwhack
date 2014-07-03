import wiki

def iterate(link):
	old_link = link
	link = wiki.get_first_link(link)
	while link is not None and link not in links:
		links.add(link)
		old_link = link
		link = wiki.get_first_link(link)
		if link is not None:
			f.write(old_link + ',' + link + '\n')

f = open("wiki_graph.csv", 'w')
links = set()
for i in range(100):
	print i
	iterate(wiki.random_uri)
