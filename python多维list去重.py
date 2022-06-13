'''

【python多维list去重】
一维的list去重可以用set(list)，但是二维的list转set就会报错 unhashable type: ‘list’
原因是set传进来的是不可哈希的变量
Python中那么哪些是可哈希元素？哪些是不可哈希元素？
可哈希的元素有：int、float、str、tuple
不可哈希的元素有：list、set、dict

为什么 list 是不可哈希的，而 tuple 是可哈希的
（1）因为 list 是可变的在它的生命期内，你可以在任意时间改变其内的元素值。
（2）所谓元素可不可哈希，意味着是否使用 hash 进行索引
（3）list 不使用 hash 进行元素的索引，自然它对存储的元素有可哈希的要求；而 set 使用 hash 值进行索引

正确做法：将list转成tuple，这样就可以用set去重。
        # 对二维list去重：
        # >>> list1=[1,1,2]
        # >>> set(list1)
        # {1, 2}
        # >>> list2=[[2,2],[2,2]]
        #
        # >>> set(list2)
        # Traceback (most recent call last):
        #   File "<stdin>", line 1, in <module>
        # TypeError: unhashable type: 'list'
        # >>> unique_list2=list(set([tuple(t) for t in list2]))
        # >>> unique_list2
        # [(2, 2)]
        # >>>
'''


# right answer:
'''
>>> ls1=[[2, 1, 5], [1, 7], [1, 6, 1], [2, 6], [2, 1, 5], [7, 1]]
>>> ls1=[sorted(i) for i in ls1]
>>> ls1
[[1, 2, 5], [1, 7], [1, 1, 6], [2, 6], [1, 2, 5], [1, 7]]
>>> nodup_ls1=list(set([tuple(i) for i in ls1]))
>>> nodup_ls1
[(1, 7), (1, 1, 6), (1, 2, 5), (2, 6)]
>>> res=[list(i) for i in nodup_ls1]
>>> res
[[1, 7], [1, 1, 6], [1, 2, 5], [2, 6]]
'''

# NOTE1:需使用内置方法sorted，而非无返回值原地排序的list的sort()方法
# list_new_sort=sorted(list_old)
# list_old.sort()
'''
>>> ls1
[[2, 1, 5], [1, 7], [1, 6, 1], [2, 6], [2, 1, 5], [7, 1]]
>>> ls1=[i.sort() for i in ls1]
>>> ls1
[None, None, None, None, None, None]
'''

# NOTE2:python元组有序性(7,1)!=(1,7)
'''
>>> ls1=[[2, 1, 5], [1, 7], [1, 6, 1], [2, 6], [2, 1, 5], [7, 1]]
>>> nodup_ls1=[set(tuple(i)) for i in ls1]
>>> nodup_ls1
[{1, 2, 5}, {1, 7}, {1, 6}, {2, 6}, {1, 2, 5}, {1, 7}]
>>> nodup_ls1=list(set([tuple(i) for i in ls1]))
>>> nodup_ls1
[(7, 1), (1, 7), (2, 6), (2, 1, 5), (1, 6, 1)]
>>> (7,1)==(1,7)
False
'''

