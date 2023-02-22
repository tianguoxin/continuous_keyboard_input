# -*- encoding: utf-8 -*-

# 判断字符串中是否存在在键盘上连续三个字符以上的字符串
def check_keyboard_coiled_input(target_str):
    try:
        t_str = target_str.lower()
        # row 行坐标
        row = []
        # col 列坐标
        col = []

        # 全都转小写
        char_list_no_shift = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', None],
            [None, 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
            [None, 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', None, None],
            [None, 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', None, None, None]
        ]

        char_list_shift = [
            ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', None],
            [None, 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '{', '}', '|'],
            [None, 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':', '"', None, None],
            [None, 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', '?', None, None, None],
        ]

        for t in range(len(t_str)):
            for clnt_idx, clnt in enumerate(char_list_no_shift):
                for i_idx, i in enumerate(clnt):
                    if t_str[t] == i:
                        row.insert(t, clnt_idx)
                        col.insert(t, i_idx)
            # 表示第一组找到了
            if len(row) > t: continue

            for clt_idx, clt in enumerate(char_list_shift):
                for j_idx, j in enumerate(clt):
                    if t_str[t] == j:
                        row.insert(t, clt_idx)
                        col.insert(t, j_idx)
        # 连续三个
        for x in range(1, len(t_str) - 1):
            # 判断是不是在一行 或者 是不是 连续同一个字符
            if row[x - 1] == row[x] and row[x] == row[x + 1]:
                if (col[x - 1] + 1 == col[x] and col[x] + 1 == col[x + 1]) or \
                        (col[x + 1] + 1 == col[x] and col[x] + 1 == col[x - 1]) or \
                        (col[x + 1]  == col[x]  and col[x] == col[x - 1] ):
                    t_set = set()
                    t_set.add("".join([char_list_no_shift[row[x - 1]][col[x - 1]],
                                       char_list_no_shift[row[x]][col[x]],
                                       char_list_no_shift[row[x + 1]][col[x + 1]]]))
                    t_set.add("".join([char_list_shift[row[x - 1]][col[x - 1]],
                                       char_list_shift[row[x]][col[x]],
                                       char_list_shift[row[x + 1]][col[x + 1]]]))
                    return {"res": True, "keyword": " or ".join(list(t_set))}

            elif col[x - 1] == col[x] and col[x] == col[x + 1]:
                if (row[x - 1] + 1 == row[x] and row[x] + 1 == row[x + 1]) or \
                        (row[x + 1] + 1 == row[x] and row[x] + 1 == row[x - 1]):
                    t_set = set()
                    t_set.add("".join([char_list_no_shift[row[x - 1]][col[x - 1]],
                                       char_list_no_shift[row[x]][col[x]],
                                       char_list_no_shift[row[x + 1]][col[x + 1]]]))
                    t_set.add("".join([char_list_shift[row[x - 1]][col[x - 1]],
                                       char_list_shift[row[x]][col[x]],
                                       char_list_shift[row[x + 1]][col[x + 1]]]))

                    return {"res": True, "keyword": " or ".join(list(t_set))}
    except:
        pass

    return {"res": False}


print(check_keyboard_coiled_input("qaz"))
print(check_keyboard_coiled_input("qdf"))
print(check_keyboard_coiled_input("!@#"))
print(check_keyboard_coiled_input("111"))