LRU: Least Recently Used，最近最少使用，
一种常见的页面置换算法， 选择最近最久未被使用的页面予以淘汰。
由于计算机缓存容量有限，当缓存区满后优先删除很久未使用的数据。

> 请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。
>
> 实现 LRUCache 类：
> 1. LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
> 2. int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值同时将该key变为最近使用的，否则返回 -1 。
> 3. void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；
> 如果不存在，则向缓存中插入该组 key-value 。
> 如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
>
> 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

> <br/>**工作原理：**
> <br/>// 缓存容量为2
> <br/>LRUCache cache = new LRUCache(2);
> <br/>// 可将此cache当成一个双端队列：左边队头，右边队尾
> <br/>// 最近使用的放在队头，久未被访问的放在队尾
> <br/>// 放入数据对使用(key, val)表示
>
> cache.put(1, 1); //cache = {(1, 1)}
>
> cache.put(2, 2); //cache = {(2, 2), (1, 1)}
>
> cache.get(1); //返回1
> <br/>// cache = {(1, 1), (2, 2)}
> <br/>// 因为访问了key=1，故将(1, 1)提至队头
>
> cache.put(3, 3)
> <br/>// cache = {(3, 3), (1, 1)}
> <br/>// 由于缓存容量已满，需要删除最近未使用的队尾(2, 2)
> <br/>// 然后将新数据加入到队头
>
> cache.get(2)  //返回-1，未找到
> <br/>// cache = {(3, 3), (1, 1)}
>
> cache.put(1， 4)
> <br/>// cache = {(1, 4), (3, 3)}
> <br/>// 键1已经存在，将其原始值1改为新值4并将该项提至队头


注意题目要求：函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
cache实现的数据结构需满足以下条件：

1. cache中元素需有时序性，用以区分最近使用和很久未使用的元素，当容量满了之后需要删除最久未使用的元素。
2. 需在O(1)时间内快速找到key对应的val：使用map数据结构。
3. 每次访问cache中的某个key，需要将其变为最近使用的，即cache需要在O(1)
   时间内快速插入和删除：使用双向链表结构，单链表不能满足O(1)的删除，因为删除一个节点需要知道其前驱节点。

- 查找：哈希表可满足快速查找，但哈希表中数据无固定顺序
- 插入、删除：双向链表
- 综合上述要求，Java可使用`LinkedHashMap`数据结构。

借助哈希链表`LinkedHashMap`：

1. 如果每次默认从链表尾部添加元素，则越靠近尾部的元素就是最近使用的，越靠近头部的就是最久未使用的
2. 对于某一个key，可以通过哈希表快速定位到其在链表中的节点，从而取得对应的val；
3. 链表通过修改指针指向可实现快速的插入和删除操作，但传统链表无法按照索引快速访问某一个位置的元素，但这里借助哈希表，可以通过key快速映射到链表的任意节点，然后进行插入和删除。

不使用库函数，自己实现双向链表DoubleList + HashMap 完成：

```java
class Node {
    public int key, val;
    public Node prev, next;
    
    public Node(int k, int v) {
        this.key = k;
        this.val = v;
    }
}


class DoubleList {
    // 头尾虚拟节点
    private Node head, tail;
    // 链表元素个数
    private size;
    
    public DoubleList() {
        // 初始化双向链表数据结构
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
        size = 0;
    }
    
    // 在链表尾部添加节点x，时间复杂度O(1)
    // 注意该双向链表只能从尾部插入，
    // 即靠近尾部的是最近使用的，靠近头部的是最久未使用的
    public void addLast(Node x) {
        x.prev = tail.prev;
        x.next = tail;
        tail.prev.next = x;
        tail.prev = x;
        size++;
    }
    
    // 删除链表中的x节点，x一定存在
    public void remove(Node x) {
        x.prev.next = x.next;
        x.next.prev = x.prev;
        size--;
    }
    
    // 删除链表中的第一个节点，并返回该节点，时间复杂度O(1)
    public Node removeFirst() {
        if (head.next == tail)
            return null;
            
        
        Node first = head.next;
        remove(first);
        return first;
    }
    
    // 返回链表长度，时间复杂度O(1)
    public int size() {
        return size;
    }
}        
    

class LRUCache {
    // key -> Node(key, val)
    private HashMap<Integer, Node> map;
    
    // Node(k1, v1) <-> Node(k2, v2) <-> ...
    private DoubleList cache;
    
    // 最大容量
    private int cap;
    
    public LRUCache(int capacity) {
        this.cap = capacity;
        map = new HashMap<>();
        cache = new DoubleList;
    }
    
    // LRU算法的put及get方法需要同时维护一个双链表cache和一个哈希表map，
    // 容易漏掉某些操作，比如说删除某个key时，在cache中删除了对应的Node，但是却忘记删除map中的key；
    // 解决上述问题的方法：在这两种数据结构之上提供一层抽象API，尽量避免LRU的主方法put和get直接操作map和cache的细节部分。
    
    //将某个key提升为最近使用的
    private void makeRecently(int key) {
        Node x = map.get(key);
        // 先从链表中删除该节点
        cache.remove(x);
        // 重新插到队尾
        cache.addLast(x);
    }
    
    // 添加最近使用的元素
    private void addRecently(int key, int val) {
        Node x = new Node(key, val);
        // 链表尾部就是最近使用的元素
        cache.addLast(x);
        // 同时在map中添加key的映射
        map.put(key, x);
    }
    
    // 删除某个key
    private void deleteKey(int key) {
        Node x = map.get(key);
        // 从链表中删除
        cache.remove(key);
        // 从map中删除        
        map.remove(key);
    }
    
    // 删除最久未使用的元素，即删除虚拟表头的下一个元素
    private void removeLeastRecently() {
        // 链表虚拟表头的下个元素即为最久未被使用的
        Node deleteNode = cache.removeFirst();
        // 同时从map中删除该key
        int deleteKey = deleteNode.key;
        map.remove(deleteKey);
    }    
    
    // get方法，不存在返回-1，key存在返回响应val，并将其提升为最近使用的
    public int get(int key) {
        if(!map.containsKey(key)) {
            return -1;
        }
        
        // 将该key提升为最近使用的
        makeRecently(key);
        return map.get(key).val;
    }
             
    public void put(int key, int val) {
        // 若该key存在：需删除旧有数据，插入新数据作为最近使用的元素
        if (map.containsKey(key) {
            deleteKey(key);
            addRecently(key, val);
            return;
        }
        
        // 添加新项之前需判断是否达最大容量
        if (cap == cache.size) {
            removeLeastRecently(key);
        }    
        
        // 若该key不存在，直接添加该项为最近使用的
        addRecently(key, val);
    }        
```

使用Java内置类型LinkedHashMap实现上述功能：
```java
class LRUCache {
    int cap;
    LinkedHashMap<Integer, Integer> cache = new LinkedHashMap<>();
    
    public LRUCache(int capacity) {
        this.cap = capacity;
    }
    
    private void addRecently(int key) {
        int val = cache.get(key);
        // 删除旧key
        cache.remove(key);
        // 重新将该项添加到队尾变为最近使用项
        cache.put(key, val);
    }
        
    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        
        // 将key变为最近使用
        makeRecently(key);
        return cache.get(key);
    }
    
    public void put(int key, int val) {
        if (cache.containsKey(key)) {
            // 修改key值
            cache.put(key, val);
            // 将该key提升为最近使用的
            makeRecenty(key);
            return;
        } 
        
        // 添加前需判断是否达最大容量限制，若容量已满，需删除旧key才可添加新key
        if (cache.size() >= this.cap) {
            // 链表表头就是最久未使用的元素
            int oldKey = cache.keySet().iterator().next();
            // 删除旧key
            cache.remove(oldKey);
        }
        
        // 添加新key
        cache.put(key, val);
    }
    
        
                           
    
```