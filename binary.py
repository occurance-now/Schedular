from datetime import datetime, timedelta

class Node:
    def __init__(self, key):
        sched_time, duration, name_of_job = key.split(',')
        raw_sched_time = datetime.strptime(sched_time, '%H:%M')
        key = raw_sched_time.time()
        end_time = (raw_sched_time + timedelta(minutes=int(duration))).time()
        self.data = key
        self.left_child = None
        self.right_child = None
        self.duration = duration
        self.end_time = end_time
        self.name_of_job = name_of_job.rstrip()

class BSTDemo:
    def __init__(self):
        self.root = None
    def length(self):
        return self._length(self.root)

    def _length(self, curr):
        if curr is None:
            return 0
        return 1 + self._length(curr.left_child) + self._length(curr.right_child)

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
            self.schedule_exe(key, True)
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.data > curr.data and key.data >= curr.end_time:
            if curr.right_child == None:
                curr.right_child = key
                self.schedule_exe(key, True)

            else:
                self._insert(curr.right_child, key)

        elif key.data < curr.data and key.data <= curr.end_time:
            if curr.left_child == None:
                curr.left_child = key
                self.schedule_exe(key, True)
            else:
                self._insert(curr.left_child, key)
        else:
            self.schedule_exe(key, False)

    def schedule_exe(self, key, succeeded):
        if succeeded:
            print('-'*50)
            print(f"Job Name:\t\t {key.name_of_job}")
            print(f"Start Time:\t\t {key.data}")
            print(f"End Time:\t\t {key.end_time}")
        else:
            print('-'*50)
            print(f"Rejected:\t\t {key.name_of_job}")
            print(f"Start Time:\t\t {key.data}")
            print(f"End Time:\t\t {key.end_time}")
            print(f"Reason:\t\t\t Time slot overlap please verify!")
        return succeeded

    def in_order(self):
        print("Full Job Schedule for Today:\n")
        self._in_order(self.root)


    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(f"Time: {curr.data}, Duration: {curr.duration}, End: {curr.end_time}, Jobname: {curr.name_of_job}")
            self._in_order(curr.right_child)


    def find_val(self, key):
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                return curr
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)

        return

    def pre_order(self):
        pass
    def _pre_order(self, curr):
        pass
    def post_order(self):
        pass
    def _post_order(self, curr):
        pass

    def min_right_subtree(self, curr):
        if curr.left_child == None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)

    def delete(self, key):
        self._delete(self.root, None, None, key)

    def _delete(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                if curr.left_child and curr.right_child:
                    min_child = self.min_right_subtree(curr.right_child)
                    curr.data = min_child.data
                    self._delete(curr.right_child, curr, False, min_child.data)
                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif curr.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                else:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child

            elif key < curr.data:
                return self._delete(curr.left_child, curr, True, key)
            elif key > curr.data:
                return self._delete(curr.right_child, curr, False, key)

        else:
            print(f"Key: {key} not found")
