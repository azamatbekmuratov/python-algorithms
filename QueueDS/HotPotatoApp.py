from QueueDS.Queue import Queue


def hot_potato(nameList, num):
    simqueue = Queue()
    for name in nameList:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hot_potato(["Bill", "David", "Azamat", "Aigul", "Batyrgaly", "Bayan"],7))