memory_size = 0
Holes_list = []
Memory = []
Processes = []
process_segments = []
# segment table
input_process = ""
Process_Segments_Names = []
Process_Segments_Limits = []
Process_Segments_Bases = []

from operator import attrgetter

class Hole:
    def __init__(self, pid, start, size):
        self.pid = pid
        self.start = start
        self.size = size

# Segment class
class Segment:
    def __init__(self, segment_name, segment_size, process_name):
        self.name = segment_name
        self.size = segment_size
        self.process = process_name

# Process class
class Process:
    def __init__(self, Process_name, no_of_segments, segments):
        self.name = Process_name
        self.no_of_segments = no_of_segments
        self.segments = segments

def new_allocation():
    global memory_size
    global Holes_list
    global Processes
    global process_segments
    global Memory
    memory_size = 0
    Holes_list.clear()
    Processes.clear()
    process_segments.clear()
    Memory.clear()


def setMemorysize(memorysize):
    global memory_size
    memory_size = memorysize
    print(memory_size)

def holes_entry(h_id, h_base, h_size):
    global Holes_list
    Holes_list.append(Hole(h_id, h_base, h_size))
    print(Holes_list)

def memory_first_allocation():
    global Memory
    global Holes_list
    global memory_size
    ptr = 0
    for j in range(len(Holes_list)):
            ######### first position ########
            if Holes_list[j].start == 0:
                Memory.append(Holes_list[j])
                ptr += Holes_list[j].size
            elif (Holes_list[j].start > 0) and (j == 0):
                Memory.append(Hole("Allocated", 0, Holes_list[j].start))
                Memory.append(Holes_list[j])
                ptr = Holes_list[j].start + Holes_list[j].size
            ######### Nth  Position ########
            else:
                if Holes_list[j].start == ptr:
                    Memory.append(Holes_list[j])
                    ptr += Holes_list[j].size
                elif Holes_list[j].start > ptr:
                    Memory.append(Hole("Allocated", ptr, (Holes_list[j].start-ptr)))
                    Memory.append(Holes_list[j])
                    ptr = Holes_list[j].start + Holes_list[j].size
    if ptr < memory_size:
        Memory.append(Hole("Allocated", ptr, memory_size-ptr))

    for item in Memory:
        print(item.pid, item.start, item.size)


def update_memory_after_check(changed, segment_changed):
    global Memory
    global Holes_list
    for i in range(len(changed)):
        Memory[changed[i]].pid = "Hole"
    for i in range(len(segment_changed)):
        print(segment_changed[i])
        for j in range(len(Memory)):
            print(Memory[j].pid[9:])
            if Memory[j].pid[9:] == segment_changed[i]:
                Memory[j].pid = "Hole"

def segments_creation(segment_name, segment_size, process_name):
    global process_segments
    process_segments.append(Segment(segment_name, segment_size, process_name))


def process_creation(process_name, no_of_segments, segments):
    global Processes
    Processes.append(Process(process_name, no_of_segments, segments))
    for item in Processes:
        print(item)


def first_fit():
    global process_segments
    global Memory
    error = 0
    HolesList = []
    print(process_segments[0].name)
    print(process_segments[0].size)
    print(Memory[1].size)
    for j in range(len(Memory)):
        if Memory[j].pid[0:4] == "Hole":
            HolesList.append(Hole("Hole", Memory[j].start, Memory[j].size))
    print(len(process_segments))
    for i in range(len(process_segments)):
        indicator = len(HolesList)
        for j in range(len(HolesList)):
            if process_segments[i].size <= HolesList[j].size:
                HolesList.pop(j)
                break
        if indicator == len(HolesList):
            error = 1

    if error == 0:
        for i in range(len(process_segments)):
            for j in range(len(Memory)):
                if Memory[j].pid[0:4] == "Hole":
                    if process_segments[i].size == Memory[j].size:
                        name = process_segments[i].name + " " + process_segments[i].process
                        start = Memory[j].start
                        size = process_segments[i].size
                        new_alloc = Hole(name, start, size)
                        Memory.pop(j)
                        Memory.insert(j, new_alloc)
                        break
                    elif process_segments[i].size < Memory[j].size:
                        temp = Memory[j].size
                        name = process_segments[i].name + " " + process_segments[i].process
                        start = Memory[j].start
                        size = process_segments[i].size
                        new_alloc = Hole(name, start, size)
                        Memory.pop(j)
                        Memory.insert(j, new_alloc)
                        break
                        # new_hole = Hole("Hole", new_alloc.start + new_alloc.size, temp-new_alloc.size)
                        # Memory.insert(j+1, new_hole)
    for item in Memory:
        print(item.pid)
    return error

def best_fit():
    global Holes_list
    global process_segments
    global Memory
    global memory_size
    error = 0
    HolesList = []
    for j in range(len(Memory)):
        if Memory[j].pid[0:4] == "Hole":
            HolesList.append(Hole("Hole", Memory[j].start, Memory[j].size))
    for i in range(len(process_segments)):
        indicator = len(HolesList)
        for j in range(len(HolesList)):
            if process_segments[i].size <= HolesList[j].size:
                HolesList.pop(j)
                break
        if indicator == len(HolesList):
            error = 1
    if error == 0:
        Memory.clear()
        Sorted_Holes = sorted(Holes_list, key=attrgetter('size'))
        for j in range(len(process_segments)):
            for i in range(len(Sorted_Holes)):
                if Sorted_Holes[i].size >= process_segments[j].size and Sorted_Holes[i].pid[0] == 'H':
                    Sorted_Holes[i].pid = process_segments[j].name +" " +  process_segments[j].process
                    break


        Sorted_Holes.sort(key=attrgetter('start'))
        ptr = 0
        for j in range(len(Holes_list)):
            ######### first position ########
            if Sorted_Holes[j].start == 0:
                Memory.append(Sorted_Holes[j])
                ptr += Sorted_Holes[j].size

            elif (Sorted_Holes[j].start > 0) and (j == 0):
                Memory.append(Hole("Allocated", 0, Sorted_Holes[j].start))
                Memory.append(Sorted_Holes[j])
                ptr = Sorted_Holes[j].start + Sorted_Holes[j].size
            ######### Nth  Position ########    `q
            else:
                if Sorted_Holes[j].start == ptr:
                    Memory.append(Sorted_Holes[j])
                    ptr += Sorted_Holes[j].size

                elif Sorted_Holes[j].start > ptr:
                    Memory.append(Hole("Allocated", ptr, (Sorted_Holes[j].start - ptr)))
                    Memory.append(Sorted_Holes[j])
                    ptr = Sorted_Holes[j].start + Sorted_Holes[j].size

        if ptr < memory_size:
            Memory.append(Hole("Allocated", ptr, memory_size - ptr))

        for item in Memory:
            print(item.pid, item.start, item.size)
    return error
# segment table

def chosen_process(InputProcess):
    global input_process
    input_process = InputProcess  # ex:p1
    print(input_process)


def segments_table():
    global input_process
    global process_segments
    global Process_Segments_Names
    global Process_Segments_Limits
    global Process_Segments_Bases
    global Memory
    n = 0
    m = 0
    while n < len(Memory):
        if input_process == Memory[n].pid[9:]:  # ex: p1
            Process_Segments_Names.append(Memory[n].pid[0:8])  # ex: segment1
            Process_Segments_Bases.append(Memory[n].start)
            m = 0
            while m < len(process_segments):
                if process_segments[m].name + " " + process_segments[m].process == Memory[n].pid:
                    Process_Segments_Limits.append(process_segments[m].size)
                m += 1
        n += 1

    print(input_process)
    print(Process_Segments_Names)
    print(Process_Segments_Bases)
    print(Process_Segments_Limits)

def main():
    memorySize = int(input("Enter Memory Size"))
    setMemorysize(memorySize)
    numberofholes = int(input("Enter number of holes"))
    for i in range(0, numberofholes):
        name = input("Enter name of hole ")
        start = int(input("Enter its start address"))
        size =int(input("Enter size of hole"))
        holes_entry(name,start,size)
    memory_first_allocation()
    processname = input("Enter Process name")
    nosegments = int(input("Enter number of segments"))
    for i in range (0, nosegments):
        sname = input("Enter segment name")
        ssize = int(input("Enter size of segment"))
        segments_creation(sname, ssize, processname)
    first_fit()
    chosep = input("Enter name of process")
    chosen_process(chosep)
    segments_table()


    print("Memory")
    print(Memory)
    print(Memory[0].pid)
    print(Memory[0].start)
    print(Memory[1].pid)
    print(Memory[1].start)
    print(Memory[2].pid)
    print(Memory[2].start)
    print(Memory[3].pid)
    print(Memory[3].start)
    print(Memory[4].pid)
    print(Memory[4].start)
    print(Memory[5].pid)
    print(Memory[5].start)
    print(Memory[6].pid)
    print(Memory[6].start)

    print("process_segments")
    print(process_segments)
    print(process_segments[0].process)
    print(process_segments[0].size)
    print(process_segments[1].process)
    print(process_segments[1].size)


if __name__ == "__main__": main()
