from Trie import Trie

aye = Trie()
aye.add("abc",1)
aye.add("ace",2)
aye.add("bit",3)
aye.add("cab",4)
aye.add("cat",5)
aye.add("den",6)
aye.add("dab",7)
aye.add("dag",8)

if "den" in aye:
    print("That works son")

if "hello" in aye:
    print("it's here")

if "hello" not in aye:
    print("it's not here")
