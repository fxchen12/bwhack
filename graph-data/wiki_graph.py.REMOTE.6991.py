import wiki

def iterate(link):
    old_link = link
    link = wiki.get_first_link(old_link)
    while link is not None and link not in linkPairs:
        old_link = link
        link = wiki.get_first_link(old_link)
        if link is not None:
            f.write(old_link + ',' + link + '\n')
            linkPairs[old_link] = link
    print(link)


f = open("wiki_graph.csv", 'a')
linkPairs = dict()

for i in range(100):
	print i
	iterate(wiki.random_uri)

