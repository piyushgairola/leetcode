class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class WordDictonary(TrieNode):
    def __init__(self):
        self.root = TrieNode()

    def _char_to_int(self,ch):
        return ord(ch)-ord('a')

    def insert(self, word):
        p_crawl = self.root
        length = len(word)
        for idx in range(length):
            index = self._char_to_int(word[idx])
            if not p_crawl.children[index]:
                p_crawl.children[index] = TrieNode()
            p_crawl = p_crawl.children[index]
        p_crawl.is_end_of_word = True

    def search(self,word):
        return self. search_word(word,0,self.root)

    def search_word(self,word,idx,node):
        if node == None:
            return False
        if len(word) == idx:
            return node.is_end_of_word
        index = self._char_to_int(word[idx])
        if word[idx] == '.':
            for child in node.children:
                if child and self.search_word(word,idx+1,child):
                    return True
        else:
            child = node.children[index]
            return self.search_word(word,idx+1,child)

        return False


if __name__ == '__main__':
    word_dict = WordDictonary()
    word_list = ['bad','dad']
    word_dict.insert(word_list[0])
    print(word_dict.search('.dd'))




