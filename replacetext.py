def replacetext(filename, oldtext, newtext):
    try:
        with open(filename,'r') as r:
            text = r.read()

        newcontent = text.replace(oldtext, newtext)

        with open('example.txt','w') as w:
            w.write(newcontent)
    except Exception as e:
            raise e

filename = 'example.txt'
oldtext = 'placement'
newtext = 'screening'
replacetext(filename, oldtext, newtext)