"""
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若s 和 t中每个字符出现的次数都相同，则称s 和 t互为字母异位词。

示例1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false

提示:

1 <= s.length, t.length <= 5 * 104
s 和 t仅包含小写字母

进阶:如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-anagram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 方法一
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        tt = list(t)
        ss.sort()
        tt.sort()
        return ss == tt


# 方法二
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}  # {'a': 1, 'b': 2}
        dict2 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch, 0) + 1
        for ch in t:
            dict2[ch] = dict2.get(ch, 0) + 1

        return dict1 == dict2


s = "anagram"
t = "nagaram"
text = Solution()
res = text.isAnagram(s=s, t=t)
print(res)
