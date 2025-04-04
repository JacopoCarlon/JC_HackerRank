use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};
use std::ptr;

struct DoublyLinkedListNode {
    data: i32,
    next: *mut DoublyLinkedListNode,
    prev: *mut DoublyLinkedListNode,
}

struct DoublyLinkedList {
    head: *mut DoublyLinkedListNode,
    tail: *mut DoublyLinkedListNode,
}

impl DoublyLinkedListNode {
    pub fn new(data: i32) -> *mut Self {
        Box::into_raw(Box::new(DoublyLinkedListNode {
            data,
            next: ptr::null_mut(),
            prev: ptr::null_mut(),
        }))
    }
}

impl Drop for DoublyLinkedListNode {
    fn drop(&mut self) {
        self.next = ptr::null_mut();
        self.prev = ptr::null_mut();
    }
}

impl DoublyLinkedList {
    pub fn new() -> Self {
        DoublyLinkedList { head: ptr::null_mut(), tail: ptr::null_mut() }
    }

    pub fn insert_node(&mut self, data: i32) {
        unsafe {
            let node = DoublyLinkedListNode::new(data);

            if self.head.is_null() {
                self.head = node;
            } else {
                (*self.tail).next = node;
                (*node).prev = self.tail;
            }

            self.tail = node;
        }
    }
}

impl Drop for DoublyLinkedList {
    fn drop(&mut self) {
        while !self.head.is_null() {
            unsafe {
                if !self.head.is_null() {
                    let head = Box::from_raw(self.head);
                    self.head = head.next;
                }
            }
        }

        self.tail = ptr::null_mut();
    }
}

fn print_doubly_linked_list(head: *const DoublyLinkedListNode, sep: &str, fptr: &mut File) {
    let mut node = head;

    while !node.is_null() {
        unsafe {
            write!(fptr, "{}", (*node).data).ok();

            node = (*node).next;
        }

        if !node.is_null() {
            write!(fptr, "{}", sep).ok();
        }
    }
}

/*
 * Complete the 'reverse' function below.
 *
 * The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
 * The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
 */

/*
 * For your reference:
 *
 * DoublyLinkedListNode {
 *     data: i32,
 *     next: *mut DoublyLinkedListNode,
 * };
 *
 */

fn reverse(llist: *const DoublyLinkedListNode) -> *const DoublyLinkedListNode {
    if llist.is_null() {
        return ptr::null();
    }
    
    let mut curr = llist as *mut DoublyLinkedListNode;
    
    unsafe {
        if (*curr).next.is_null() {
            return curr as *const DoublyLinkedListNode;
        }
    }
    
    let mut aft;
    let mut bef = ptr::null_mut();

    while !curr.is_null() {
        unsafe {
            aft = (*curr).next; // Get node after curr
            bef = (*curr).prev; // Get node before curr
            (*curr).prev = aft; // Swap pointers
            (*curr).next = bef; 
            curr = aft; // Move to next node (in original ordering)
        }
    }
    // now "bef" node is first-to-last element in original ordering, 
    // and "bef.prev" field has been updated to new ordering, 
    //      thus pointing to last element in original == first in new

    unsafe {
        // Return the new head (original tail)
        return (*bef).prev as *const DoublyLinkedListNode;
    }
}



fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let t = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    for _ in 0..t {
        let llist_count = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();
        let mut llist = DoublyLinkedList::new();

        for _ in 0..llist_count {
            let llist_item = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

            llist.insert_node(llist_item);
        }

        let llist1 = reverse(llist.head);

        print_doubly_linked_list(llist1, " ", &mut fptr);
        writeln!(&mut fptr).ok();
    }
}
