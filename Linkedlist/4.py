# Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x . lf x is contained within the list, the values of x only need
# to be after the elements less than x (see below) . The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

from Class_Linkedlist import randomLinkedList

def partition(linkedlist,pvalue):
    stat_ptr = linkedlist.head
    runn_ptr = linkedlist.head
    while runn_ptr:
        if runn_ptr.value < pvalue:
            temp = stat_ptr.value
            stat_ptr.value = runn_ptr.value
            runn_ptr.value = temp

            stat_ptr = stat_ptr.next
            runn_ptr = runn_ptr.next
        else:
            runn_ptr = runn_ptr.next
    return stat_ptr

L1 = randomLinkedList(9,1,8)
print(L1)
partition(L1,5)
print(L1)