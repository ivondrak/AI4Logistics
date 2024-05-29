from histogram import Histogram

# Clock
class Clock:

    def __init__(self, time=0):
        self.time = time
        self.time_of_next_event = float('inf')

    def show(self):
        print("Clock time is: ", round(self.time, 2))

class Monitor:
    def __init__(self, clock, number_of_samples):
        self.clock = clock
        self.agenda = Agenda(self.clock)
        self.number_of_samples = number_of_samples
        self.samples_taken = 0

    def moreEvents(self):
        if self.agenda.isEmpty():
            return False
        else:
            return True
        
    def moreSamples(self):
        if self.samples_taken < self.number_of_samples:
            return True
        else:
            return False
        
    def update(self):
        self.samples_taken += 1

    def show(self):
        print("Number of samples taken: ", self.samples_taken)

# Source and Sink
class SourceAndSink:
    def __init__(self):
        self.count = 0

class Source(SourceAndSink):
    def create(self, clock):
        self.count += 1
        this_client = Transaction(clock)
        this_client.next_in_line = None
        return this_client
    
    def show(self):
        print("Number of clients generated: ", self.count)

class Sink(SourceAndSink):

    def remove(self, client):
        client = None
        self.count += 1

    def show(self):
        print("Number of clients served: ", self.count)

# Event Notice
class EventNotice:
    def __init__(self, clock, time, event_type, transaction):
        self.clock = clock
        self.event_time = self.clock.time + time
        self.event_type = event_type
        self.transaction = transaction
        self.next_event = None

# Event List
class EventList:

    def __init__(self):
        self.first_event = None
        self.length = 0

# Agenda
class Agenda:

    def __init__(self, clock):
        self.clock = clock
        self.agenda = EventList()

    def insert(self, event, before, after):
        before.next_event = event
        event.next_event = after

    def scheduleEvent(self, event):
        that = event
        that.next_event = None
        self.agenda.length += 1
        if self.agenda.first_event == None:
            self.agenda.first_event = that
        else:
            if that.event_time < self.agenda.first_event.event_time:
                that.next_event = self.agenda.first_event
                self.agenda.first_event = that
                self.clock.time_of_next_event = self.agenda.first_event.event_time
            else:
                next = self.agenda.first_event
                while that.event_time >= next.event_time and next.next_event:
                    prev = next
                    next = next.next_event
                if that.event_time >= next.event_time and next.next_event == None:
                    self.insert(that, next, None)
                else:
                    self.insert(that, prev, next)
        self.agenda.length += 1

    def getNextEvent(self):
        if self.agenda.first_event == None:
            print("Can't remove any item from empty event list!")
        else:
            current = self.agenda.first_event
            self.agenda.first_event = current.next_event
            self.agenda.length -= 1
            self.clock.time = current.event_time
            if self.agenda.first_event != None:
                self.clock.time_of_next_event = self.agenda.first_event.event_time
            else:
                self.clock.time_of_next_event = float('inf')
            self.current_event = current

    def flushOutEvent(self):
        self.current_event = None

    def transaction(self):
        return self.current_event.transaction
    
    def getEventType(self):
        return self.current_event.event_type
    
    def isEmpty(self):
        return self.agenda.length <= 0


# Queue   
class Queue:
    def __init__(self, clock):
        self.clock = clock
        self.start_time = self.clock.time
        self.first = None
        self.last = None
        self.length = 0
        self.max_length = 0
        self.time_of_last_change = 0
        self.length_integral = 0
        self.num_of_entries = 0
        self.num_of_departures = 0

    def meanQueueLength(self):
        if self.clock.time > 0:
            return self.length_integral / (self.clock.time - self.start_time)
        else:
            return 0
        
    def meanQueueDelay(self):
        if self.clock.time > 0:
            return self.length_integral / self.num_of_departures
        else:
            return 0
    
    def fileInto(self, transaction):
        self.num_of_entries += 1
        self.length += 1
        self.length_integral += (self.length-1) * (self.clock.time - self.time_of_last_change)
        self.time_of_last_change = self.clock.time
        if self.length > self.max_length:
            self.max_length = self.length
        if (self.length - 1) == 0:
            self.first = transaction
        else:
            self.last.next_in_line = transaction
        transaction.next_in_line = None
        self.last = transaction
    
    def takeFirst(self):
        if self.length <= 0:
            print("Can't remove item from an empty queue!")
            return None
        else:
            self.num_of_departures += 1
            self.length -= 1
            self.length_integral += (self.length+1) * (self.clock.time - self.time_of_last_change)
            self.time_of_last_change = self.clock.time
            transaction = self.first
            self.first = transaction.next_in_line
            if self.length == 0:
                self.last = None
            return transaction
    
    def show(self):
        max = self.max_length
        mean = self.meanQueueLength()
        delay = self.meanQueueDelay()
        print('Queue report:')
        print('Items entered: ', self.num_of_entries)
        print('Items departed: ', self.num_of_departures)
        print('Queue current length: ', self.length)
        print('Queue max length: ', max)
        print('Queue mean length: ', round(mean, 2))
        print('Queue mean delay: ', round (delay, 2))

# Server
class Server:
    def __init__(self, clock):
        self.clock = clock
        self.available = True
        self.start_time = self.clock.time
        self.time_of_last_change = 0
        self.use_integral = 0

    def isAvailable(self):
        return self.available

    def seize(self):
        if self.available:
            self.available = False
            self.time_of_last_change = self.clock.time
        else:
            print('Server is busy')
        self.available = False

    def release(self):
        if not self.available:
            self.available = True
            self.use_integral += self.clock.time - self.time_of_last_change
            self.time_of_last_change = self.clock.time
        else:
            print('Server is available')
        self.available = True

    def utilization(self):
        if self.clock.time > 0:
            return self.use_integral / (self.clock.time - self.start_time)
        else:
            return 0

    def show(self):
        print('Server utiliation: ', round(self.utilization(), 2))

# Transaction
class Transaction:
    def __init__(self, clock):
        self.clock = clock
        self.birth_time = clock.time
        self.next_in_line = None

    def flowTime(self):
        return self.clock.time - self.birth_time

# Generator Factory
class GeneratorFactory:
    def __init__(self, number_of_samples=1000, seed=None):
        self.number_of_samples = number_of_samples
        self.seed = seed

    def createArrivals(self):
        pass
    def createServices(self):
        pass

# Simulation
class Simulation:
    
    def __init__(self, title, generator_factory):
        self.title = title
        self.clock = Clock()
        self.monitor = Monitor(self.clock, generator_factory.number_of_samples)
        self.source = Source()
        self.sink = Sink()
        self.queue = Queue(self.clock)
        self.server = Server(self.clock)
        self.arrivals = generator_factory.createArrivals()
        self.services = generator_factory.createServices()
        self.arrivals.generate()
        self.services.generate()
        self.spent_time = []
        self.monitor.agenda.scheduleEvent(EventNotice(self.clock, 0, 'arrival', None))
    
    def run(self):
        while self.monitor.moreSamples() and self.monitor.moreEvents():
            self.monitor.agenda.getNextEvent()
            self.execute()
            self.monitor.agenda.flushOutEvent()
        self.show()
    
    def execute(self):
        event_type = self.monitor.agenda.getEventType()
        if event_type == 'arrival':
            self.arrival()
        elif event_type == 'start':
            self.start()
        elif event_type == 'finish':
            self.finish(self.monitor.agenda.transaction())
        elif event_type == 'departure':
            self.departure(self.monitor.agenda.transaction())
        else:
            print('Unknown event type')

    def arrival(self):
        time = self.arrivals.next()
        self.monitor.agenda.scheduleEvent(EventNotice(self.clock, time, 'arrival', None))
        client = self.source.create(self.clock)
        self.queue.fileInto(client)
        self.monitor.agenda.scheduleEvent(EventNotice(self.clock, 0, 'start', None))

    def start(self):
        time = self.services.next()
        if self.server.isAvailable() and self.queue.length > 0:
            self.server.seize()
            client = self.queue.takeFirst()
            self.monitor.agenda.scheduleEvent(EventNotice(self.clock, time, 'finish', client))

    def finish(self, client):
        self.server.release()
        self.monitor.agenda.scheduleEvent(EventNotice(self.clock, 0, 'departure', client))
        self.monitor.agenda.scheduleEvent(EventNotice(self.clock, 0, 'start', None))

    def departure(self, client):
        time = client.flowTime()
        self.spent_time.append(time)
        self.sink.remove(client)
        self.monitor.update()

    def show(self):
        print(self.title)
        self.monitor.show()
        self.source.show()
        self.sink.show()
        self.queue.show()
        self.server.show()
        self.sink.show()
        Histogram(self.arrivals.data, "Arrivals time distribution","Arrival Time","Frequency").plot()
        Histogram(self.services.data, "Service time distribution","Service Time","Frequency").plot()
        Histogram(self.spent_time, "Spent time distribution","Time spent in a system","Frequency").plot()