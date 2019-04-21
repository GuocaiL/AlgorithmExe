'''
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:

输入: "USA"
输出: True
示例 2:

输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。
'''

#自己的解法
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) >= 2:
            if ord(word[0]) <= 90:
                if ord(word[1]) <= 90:
                    for w in word[2:]:
                        if ord(w) > 90:
                            return False
                else:
                    for w in word[2:]:
                        if ord(w) <= 90:
                            return False
            else:
                for w in word:
                    if ord(w) <= 90:
                        return False
        else:
            return True
        return True

#别人的更简介的解法
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.upper()==word or word.lower()==word or word.title()==word