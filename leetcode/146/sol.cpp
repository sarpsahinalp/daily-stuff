#include <vector>
#include <unordered_map>
class DoublyLinkedListNode
{
public:
    DoublyLinkedListNode *prev;
    DoublyLinkedListNode *next;
    int val;

    DoublyLinkedListNode(DoublyLinkedListNode *next, DoublyLinkedListNode *prev, int val) : next(next), prev(prev), val(val)
    {
    }
};

class DoublyLinkedList
{
public:
    DoublyLinkedListNode *head;
    DoublyLinkedListNode *tail;
    int size;

    DoublyLinkedList()
    {
        head = nullptr;
        tail = nullptr;
        size = 0;
    }

    DoublyLinkedListNode *removeHead()
    {
        if (head == nullptr)
        {
            return nullptr;
        }

        head = head->next;

        if (head != nullptr)
        {
            head->prev = nullptr;
        }
    }

    void addToBack(DoublyLinkedListNode *newNode)
    {
        if (tail == nullptr)
        {
            head = newNode;
            tail = newNode;
        }
        else
        {
            tail->next = newNode;
            newNode->prev = tail;
            newNode->next = nullptr;

            tail = newNode;
        }

        size++;
    }
};

class LRUCache
{
public:
    std::unordered_map<int, DoublyLinkedListNode *> lru;
    DoublyLinkedList linkedList;
    int capacity;

    LRUCache(int capacity)
    {
        lru.reserve(capacity);
    }

    int get(int key)
    {
        if (lru.contains(key))
        {
            return lru[key]->val;
        }

        return -1;
    }

    void put(int key, int value)
    {
        if (linkedList.size + 1 > capacity)
        {
            return;
        }

        DoublyLinkedListNode *new_node = new DoublyLinkedListNode(nullptr, nullptr, value);
        linkedList.addToBack(new_node);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */