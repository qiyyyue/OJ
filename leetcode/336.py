from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        fw_dict = {}
        ls_dict = {}
        rs_dict = {}

        self_re_list = []
        null_list = []

        res_pairs = []

        for i in range(len(words)):
            word = words[i]
            revers_word = word[::-1]
            if revers_word in fw_dict:
                for j in fw_dict[revers_word]:
                    res_pairs.append([j, i])
                    res_pairs.append([i, j])
            if revers_word in ls_dict:
                for j in ls_dict[revers_word]:
                    res_pairs.append([j, i])
            if revers_word in rs_dict:
                for j in rs_dict[revers_word]:
                    res_pairs.append([i, j])

            if word in fw_dict:
                fw_dict[word].append(i)
            else:
                fw_dict[word] = [i]

            if len(word) == 0:
                null_list.append(i)
            elif word == revers_word:
                self_re_list.append(i)

            for j in range(1, len(word)):
                ls = word[:j]
                rs = word[j:]
                if ls == ls[::-1]:
                    if rs[::-1] in fw_dict:
                        for k in fw_dict[rs[::-1]]:
                            res_pairs.append([k, i])
                    if rs in rs_dict:
                        rs_dict[rs].append(i)
                    else:
                        rs_dict[rs] = [i]
                if rs == rs[::-1]:
                    if ls[::-1] in fw_dict:
                        for k in fw_dict[ls[::-1]]:
                            res_pairs.append([i, k])
                    if ls in ls_dict:
                        ls_dict[ls].append(i)
                    else:
                        ls_dict[ls] = [i]
        for i in null_list:
            for j in self_re_list:
                res_pairs.append([i, j])
                res_pairs.append([j, i])
        return res_pairs