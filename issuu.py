import urllib, re
import sys, getopt


base = "http://issuu.com/marcosnogueira0/docs/the_legend_of_zelda_oracle_of_seaso"
tag = '<link rel="image_src" href='
pageNum = 1

if len(sys.argv) > 1:
    base = str(sys.argv[1])
    resp = urllib.urlopen(base)
    content = resp.read()
    with open("foo.txt", "r+") as f:
        f.write(content)
        f.close()
    with open('foo.txt') as f:
        for i, line in enumerate(f, 1):
            if tag in line:
                break
    line = line.replace('<link rel="image_src" href="', '')
    line = line.replace('1.jpg">', '')
    print line


else:
    print("Usage: python issuu.py http://issuu.com/user/docs/file")
    sys.exit(2)