"""
Yuck, day 4. Could use major cleanup.
"""

from util import *

data = get_data(4, split=False)

def p1(input):
    date_format='%Y-%m-%d %H:%M'
    p=re.compile(r"\[(.*)\] ([\w\s#]*)\n", flags=re.MULTILINE)
    guard_p=re.compile(r"Guard #(\d*) begins shift")
    matches=re.findall(p, input)

    # First things first, sort the records by chronological order.
    matches.sort(key=lambda x: datetime.strptime(x[0], date_format))

    dates_map = {}
    dates_to_guards = {}
    curr_guard=None

    last_asleep=0
    last_awake=0

    for date, action in matches:
        date=datetime.strptime(date, date_format)
        day_of=date.strftime("%Y-%m-%d")

        if day_of not in dates_map:
            dates_map[day_of] =  ['0'] * 60

        minute=date.minute

        guard_match=re.findall(guard_p, action)

        if guard_match:
            curr_guard=guard_match[0]

        if day_of not in dates_to_guards:
            dates_to_guards[day_of]=curr_guard

        # default state is awake
        if action == 'falls asleep':
            last_asleep=minute
            # mark everything before as awake
            dates_map[day_of][last_awake:last_asleep] = '0' * (last_asleep-last_awake)
        elif action == 'wakes up':
            last_awake=minute
            # mark everything before as asleep
            dates_map[day_of][last_asleep:last_awake] = '1' * (last_awake-last_asleep)

    # tally which guard slept the most
    guards_to_sleep = defaultdict(int)
    for date, guard in dates_to_guards.items():
        guards_to_sleep[guard] += dates_map[date].count('1')

    guard_who_slept_most = max(guards_to_sleep.items(), key=itemgetter(1))[0]

    guards_to_total_sleep = defaultdict(lambda: ['0'] * 60)
    guard_max_total_sleep = 0
    guard_max_total_sleep_value = 0
    for date, guard in dates_to_guards.items():
        guards_to_total_sleep[guard] = [sum(map(int, x)) for x in zip(dates_map[date], guards_to_total_sleep[guard])]
    
    max_guard = 0
    curr_max = 0
    max_minute = 0
    for guard, sleep in guards_to_total_sleep.items():
        max_sleep_per_guard =  max(map(int, guards_to_total_sleep[guard]))
        if max_sleep_per_guard > curr_max:
            curr_max = max_sleep_per_guard
            max_guard = guard
            max_minute = guards_to_total_sleep[guard].index(curr_max)
    part2 = int(max_guard) * int(max_minute)

    # maximum minute slept?
    
    # for each minute of each date the guard was active, sum all the items in the lists. 
    times_asleep = []
    for date in dates_map:
        if dates_to_guards[date] == guard_who_slept_most:
            times_asleep.append(dates_map[date])

    total_times_asleep = [sum(map(int, x)) for x in zip(*times_asleep)]
    minute_most_asleep = total_times_asleep.index(max(total_times_asleep))
    part1 = minute_most_asleep * int(guard_who_slept_most)
    return (part1, part2)

print("Part 1: ", p1(data))

test_input="""
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""
expected_result=(240, 4455)

p1_tests=[
    (test_input, expected_result)
]

run_tests(p1, p1_tests, delim=None)
