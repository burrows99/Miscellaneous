class Node:
    def __init__(self,data):
        self.data=data
        self.children={}
        self.end=False
class Trie:
    def __init__(self):
        self.root=Node('')
    def insert(self,word):
        current=self.root
        n=len(word)
        for i,char in enumerate(word):
            if(char not in current.children):
                current.children[char]=Node(char)
            current=current.children[char]
            if(i>=n-1):
                current.end=True
    def search(self,word):
        current=self.root
        for i,char in enumerate(word):
            if(char not in current.children):
                return(False)
            current=current.children[char]
        return(current.end)
    def wordsWithPrefix(self,prefix):
        def dfs(node,word,ans):
            if(node.end==False):
                for i in node.children:
                    dfs(node.children[i],word+node.data,ans)
            else:
                ans.append(word[1:]+node.data)
        current=self.root
        for i,char in enumerate(prefix):
            if(char not in current.children):
                return(False)
            current=current.children[char]
        ans=[]
        dfs(current,'',ans)
        for i in enumerate(ans):
            ans[(i[0])]=prefix+ans[(i[0])]
        return(ans)
array=['raunak','ramesh','abhinandan','aditi','abhishek','vedant']
t=Trie()
for i in array:
    t.insert(i)
print(t.wordsWithPrefix('abh'))
