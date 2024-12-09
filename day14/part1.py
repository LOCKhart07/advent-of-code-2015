"""AoC_Year2015_Day14_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = int(speed)
        self.fly_time = int(fly_time)
        self.rest_time = int(rest_time)
        self.is_flying = True
        self.current_resting_seconds = 0
        self.current_flying_seconds = 0
        self.distance_traveled = 0

    def process_second(self):
        if self.is_flying:

            self.current_flying_seconds += 1
            # if self.distance_traveled % (self.speed * self.fly_time) == 0:
            if self.current_flying_seconds == self.fly_time:
                self.is_flying = False
                self.current_flying_seconds = 0
            # else:
            self.distance_traveled += self.speed

        else:
            self.current_resting_seconds += 1
            if self.current_resting_seconds > self.rest_time:
                self.is_flying = True
                self.process_second()
                self.current_resting_seconds = 0

    def __str__(self):
        return f"{self.name} can fly {self.speed} km/s for {self.fly_time} seconds, but then must rest for {self.rest_time} seconds"

    def __repr__(self):
        return f"{self.name}: {self.speed} km/s for {self.fly_time} seconds, but then must rest for {self.rest_time} seconds"

    def __current_state__(self):
        state = "flying" if self.is_flying else "resting"
        return f"{self.name} is {state} at {self.distance_traveled} km."


reindeers: list[Reindeer] = []
with open(INPUT_PATH, "r") as f:

    while line := f.readline().strip().split():
        reindeers.append(Reindeer(line[0], line[3], line[6], line[13]))


TOTAL_RACE_SECONDS = 2503
for second in range(1, TOTAL_RACE_SECONDS + 1):
    for reindeer in reindeers:
        reindeer.process_second()

    #     print(f"After {second} seconds, ", reindeer.__current_state__())
    # print()


# print()
# for reindeer in reindeers:
#     print(reindeer.__current_state__())
# print()
print(max(reindeers, key=lambda x: x.distance_traveled).distance_traveled)
# print([i.__current_state__() for i in reindeers_in_lead(reindeers)])
