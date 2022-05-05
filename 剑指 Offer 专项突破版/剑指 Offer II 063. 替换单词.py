from typing import List

class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_level = self.root
        for c in word:
            if c not in cur_level.child:
                cur_level.child[c] = TrieNode()
            cur_level = cur_level.child[c]

        cur_level.is_word = True


    def has_prefix(self, word):
        cur_level = self.root
        prefix = []
        if word[0] not in self.root.child:
            return False,""

        for c in word:
            if cur_level.is_word:
                return True, "".join(prefix)
            if c in cur_level.child:
                prefix.append(c)
                cur_level = cur_level.child[c]
            else:
                if cur_level.is_word:
                    return True, "".join(prefix)
                else:
                    return False, ""
        if cur_level.is_word:
            return True, "".join(prefix)
        else:
            return False, ""



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for w in dictionary:
            trie.insert(w)
        res = []
        sentence_list = sentence.split()
        for word in sentence_list:
            prefix_res = trie.has_prefix(word)
            if prefix_res[0]:
                res.append(prefix_res[1])
            else:
                res.append(word)

        return " ".join(res)

ikkbp (True, 'i')
miszkays (False, '')
wqjferqoxjwvbieyk (True, 'w')
gvcfldkiavww (False, '')
vhokchxz (True, 'v')
dvypwyb (False, '')
bxahfzcfanteibiltins (False, '')
ueebf (False, '')
lqhflvwxksi (False, '')
dco (True, 'dc')
kddxmckhvqifbuzkhstp (True, 'k')
wc (True, 'w')
ytzzlm (False, '')
gximjuhzfdjuamhsu (False, '')
gdkbmhpnvy (False, '')
ifvifheoxqlbosfww (True, 'i')
mengfdydekwttkhbzenk (False, '')
wjhmmyltmeufqvcpcxg (True, 'w')
hthcuovils (True, 'h')
ldipovluo (False, '')
aiprogn (True, 'a')
nusquzpmnogtjkklfhta (False, '')
klxvvlvyh (True, 'k')
nxzgnrveghc (False, '')
mpppfhzjkbucv (False, '')
cqcft (True, 'c')
uwmahhqradjtf (False, '')
iaaasabqqzmbcig (True, 'i')
zcpvpyypsmodtoiif (True, 'z')
qjuiqtfhzcpnmtk (True, 'q')
yzfragcextvx (False, '')
ivnvgkaqs (True, 'i')
iplazv (True, 'i')
jurtsyh (True, 'j')
gzixfeugj (False, '')
rnukjgtjpim (False, '')
hscyhgoru (True, 'h')
aledyrmzwhsz (True, 'a')
xbahcwfwm (True, 'x')
hzd (True, 'h')
ygelddphxnbh (False, '')
rvjxtlqfnlmwdoezh (False, '')
zawfkko (True, 'z')
iwhkcddxgpqtdrjrcv (True, 'i')
bbfj (False, '')
mhs (False, '')
nenrqfkbf (False, '')
spfpazr (False, '')
wrkjiwyf (True, 'w')
cw (True, 'c')
dtd (False, '')
cqibzmuuhukwylrnld (True, 'c')
dtaxhddidfwqs (False, '')
bgnnoxgyynol (False, '')
hg (True, 'h')
dijhrrpnwjlju (False, '')
muzzrrsypzgwvblf (False, '')
zbugltrnyzbg (True, 'z')
hktdviastoireyiqf (True, 'h')
qvufxgcixvhrjqtna (True, 'q')
ipfzhuvgo (True, 'i')
daee (False, '')
r (True, False, '')