import collections


def test():
    nums = [1,2,1,1,8,1]
    map = collections.defaultdict(list)
    for i,num in enumerate(nums):
        map[num].append(i)
    print(map)
    res = []
    n = len(map)
    for i in range(n):
        cur_nums = sorted(map.keys(), reverse=True)
        cur_max_num_index = -1
        for j in range(len(cur_nums)):
            cur_max_valid = True
            for k in range(j+1, len(cur_nums)):
                if map[cur_nums[k]][-1] < map[cur_nums[j]][0]:
                    cur_max_valid = False
                    break
            if cur_max_valid:
                cur_max_num_index = j
                break
        cur_max_num = cur_nums[cur_max_num_index]
        map.pop(cur_max_num)
        res.append(cur_max_num)

    print("res ", res)


test()