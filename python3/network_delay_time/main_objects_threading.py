import copy, time
from threading import Thread

class Node:

    def __init__(self, id):
        self.id = id
        self.dest = {}  # {Node: travel_time}
        self.visited = False

    def add_dest(self, dest_node, travel_time):
        self.dest[dest_node] = travel_time

    def receive(self, message):
        if not self.visited:
            self.visited = True
            message.visited(self)
            for d in self.dest.keys():
                copied_msg = copy.copy(message)
                copied_msg.info_center.notify_active(copied_msg)
                Thread(target=copied_msg.goto, args=(self, d, self.dest[d])).start()
        message.info_center.notify_stop(message)

class Message:

    def __init__(self, info_center):
        self.visited_nodes = []
        self.travel_time = 0
        self.info_center = info_center

    def been_there(self, node):
        if node in self.visited_nodes:
            return True
        else:
            return False

    def visited(self, node):
        if node not in self.visited_nodes:
            self.visited_nodes.append(node)

    def goto(self, src, dest, travel_time):
        time.sleep(travel_time * 0.05)
        if src not in self.visited_nodes:
            self.visited_nodes.append(src)
        if dest not in self.visited_nodes:
            self.travel_time += travel_time
            self.visited_nodes.append(dest)
            dest.receive(self)
        else:
            self.info_center.notify_stop(self)

class InfoCenter:

    def __init__(self, N):
        self.active_messages = []
        self.stopped_messages = []
        self.visited_nodes = []
        self.numbers_of_nodes = N
        self.done_delivery = False
        self.all_nodes_covered = False
        self.longest_travel_time = -1

    def notify_active(self, msg):
        if msg not in self.active_messages:
            self.active_messages.append(msg)

    def notify_stop(self, msg):
        self.stopped_messages.append(msg)
        if msg in self.active_messages:
            self.active_messages.remove(msg)
        self.visited_nodes += [n for n in msg.visited_nodes \
                                if n not in self.visited_nodes]
        # check if there is no active messages,
        # if yes, it means available nodes visited,
        # but there might be nodes unvisitable
        if len(self.active_messages) == 0:
            self.done_delivery = True
            if len(self.visited_nodes) == self.numbers_of_nodes:
                self.all_nodes_covered = True
                for m in self.stopped_messages:
                    if m.travel_time > self.longest_travel_time:
                        self.longest_travel_time = m.travel_time

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # build the network
        info_center = InfoCenter(N)
        all_nodes = {}
        for i in range(1, N+1):
            all_nodes[i] = Node(i)
        for path in times:
            all_nodes[path[0]].add_dest(all_nodes[path[1]], path[2])
        # run the network
        all_nodes[K].receive(Message(info_center))
        # check the result
        while info_center.done_delivery is False:
            continue
        if info_center.all_nodes_covered:
            return info_center.longest_travel_time
        else:
            return -1