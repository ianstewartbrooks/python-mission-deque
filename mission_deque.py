from collections import deque
import datetime

# This small piece of code is an example of how to use deque to
# give the user 3 new missions on a daily basis based upon
# a predefined list of mission types.


def get_next_missions():
    
    # Populate mission list and sort it
    mission_list = [
        "bicycle rack",
        "bollard",
        "utility box",
        "postbox",
        "bench",
        "pole",
        "litter bin",
        "wheelie bin",
        "tree trunk",
        "rail",
        "bus shelter",
    ]
    mission_list.sort()

    # How many possible mission do we have?
    num_missions = len(mission_list)

    # How many missions can the player have?
    step_size = 3

    # Get the player's time/date and then the day of the month
    player_time = datetime.datetime.utcnow()
    day_of_month = player_time.day

    # Get 3 new missions for the player by using Ian T's mission-choice-algorithm
    shift_amount = ((day_of_month - 1) % num_missions) * step_size
    mission_queue = deque(mission_list)
    mission_queue.rotate(-shift_amount)
    missions_list = list(mission_queue)

    # for x in range(1,32):
    #     shift_amount = ((x - 1) % num_missions) * step_size
    #     mission_queue = deque(mission_list)
    #     mission_queue.rotate(-shift_amount)
    #     missions_list = list(mission_queue)
    #     print('Day {0}: {1}, {2}, {3}.'.format(x, missions_list[0],
    #                                         missions_list[1],
    #                                         missions_list[2]))

    # return the 3 mission
    return missions_list[0], missions_list[1], missions_list[2]


# M A I N

mission_one, mission_two, mission_three = get_next_missions()

print(
    "Your mission today is to take photos of: {0}, {1}, {2}".format(
        mission_one, mission_two, mission_three
    )
)