
```text
LFU缓存淘汰算法原理：淘汰访问频率最低的数据；（频次性）
                   若访问频次相同的数据有多条，淘汰最旧的数据。（时序性）
```
```text
要求写一个类，接受一个capacity参数，实现get和put方法：
class LFUCache {
    // 构造容量为capacity的缓存
    public LFUCache(int capacity) {}
    
    // 在缓存中查询key：key存在返回val；不存在返回-1。
    public int get(int key) {}
    
    // 将key和val存入缓存：
    // key存在修改对应值为val，且将其变为同val下最新使用的；
    // key不存在插入该项：若容量已满则需先删除 最小频次、最久未使用 的项在进行插入。
    public void put(int key, int val) {}
```
```text
// 构造一个容量为2的LFU缓存
LFUCache cache = new LFUCache(2);

// 插入两对(k, v)，对应的freq为1
cache.put(1, 10);
cache.put(2, 20);

// 查询key为1对应的val
// 返回10，同时1对应的freq加1，变为2
cache.get(1);

// 容量已满，淘汰最小频次的键2
// 插入(3, 30)，其对应的频次为1
cache.put(3, 30);

// 键2已经被淘汰，返回-1
cache.get(2);
```

```text
上述算法需满足以下条件：
1. 调用get(key)方法时，需返回该key对应的val，不存在返回-1；存在返回相应的val，同时该key的访问频次需加1
2. 调用put(key, val)方法时，若容量已满，需先删除访问频次最小的key，若存在多个freq相同的key，则需删除最久未使用的key；
    若容量未满，直接插入该项：若该项已经存在，需更新该key对应的val值，且freq+1；
                            若该项不存在，直接插入该项，其freq=1.
3. 满足O(1)的时间复杂度要求。                           
```

```text
数据结构选用：

```

