# Assignment: Call Center
# You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.
class Call(object):
    def __init__(self, id, caller_name, caller_number, time, reason):
        self.id = id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time = time
        self.reason = reason
    def display(self):
        print "id:", self.id
        print "caller_name:", self.caller_name
        print "caller_number:", self.caller_number
        print "time:", self.time
        print "reason:", self.reason
        return self
class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    def add(self, id, caller_name, caller_number, time, reason):
        call_list = Call(id, caller_name, caller_number, time, reason)
        self.calls.append(call_list)
        self.queue_size += 1
        return self
    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self
    def info(self):
        print ' '*25
        print 'Queue order by time call received:'
        q_position = 1
        for caller in range(len(self.calls)):
            print self.calls[caller].caller_name
            print self.calls[caller].caller_number
            print 'queue position', q_position
            q_position +=1
        print '=='*10,  'queue length:', self.queue_size
        return self
call_queue = CallCenter()
call_queue.add('1', 'Jeff', '630-666-2240', '11:00 AM', 'Shitty Service').add('2', 'Mark', '630-666-6666', '11:00 PM', 'Bored')
call_queue.info()