validColors = [
    'White',
    'Red',
    'Green',
    'Blue',
    'Light Blue',
    'Pink',
    'Yellow',
    'Black'
]

class Goal(object):

    def __init__(self, name, color, items=None, locations=None, lock_locations=None, lock_entrances=None, required_locations=None):
        # early exit if goal initialized incorrectly
        if (items is None and locations is None):
            raise Exception('Invalid goal: no items or destinations set')
        self.name = name
        if (color in validColors):
            self.color = color
        else:
            raise Exception('Invalid goal: Color not supported')
        self.items = items
        self.locations = locations
        self.lock_locations = lock_locations
        self.lock_entrances = lock_entrances
        if required_locations is None:
            self.required_locations = []
        else:
            self.required_locations = required_locations

class GoalCategory(object):

    def __init__(self, name, priority, goal_count=0, lock_locations=None, lock_entrances=None):
        self.name = name
        self.priority = priority
        self.lock_locations = lock_locations
        self.lock_entrances = lock_entrances
        self.goals = []
        self.goal_count = goal_count