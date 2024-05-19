from abc import abstractmethod

# Base class for environment
class Environment(object):
    ''' Base class for environment '''

    @abstractmethod
    def __init__(self, n):
        self.n = n
    
    # Method to execute a single step
    @abstractmethod
    def executeStep(self, n=1):
        raise NotImplementedError('action must be defined!')
    
    # Method to execute all steps
    @abstractmethod
    def executeAll(self):
        raise NotImplementedError('action must be defined!')
    
    # Method to set delay
    def delay(self, n=100):
        self.delay = n

# Environment for an n-room vacuum cleaner
class NRoomVaccumCleanerEnvironment(Environment):
    ''' Environment for an n-room vacuum cleaner '''

    def __init__(self, agent, room_statuses):
        ''' Constructor '''
        self.rooms = [Room(chr(65 + i), status) for i, status in enumerate(room_statuses)]
        self.agent = agent
        self.currentRoom = self.rooms[0]  # Start from the first room
        self.delay = 1000
        self.step = 1
        self.action = ""
    
    # Method to execute a single step
    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                self.currentRoom = self.get_next_room()
            else:
                self.currentRoom = self.get_previous_room()
            self.displayAction()
            self.step += 1

    # Method to execute all steps
    def executeAll(self):
        raise NotImplementedError('action must be defined!')
    
    # Method to get the next room in the sequence
    def get_next_room(self):
        current_index = self.rooms.index(self.currentRoom)
        next_index = (current_index + 1) % len(self.rooms)  # Wrap around to the first room if at the last room
        return self.rooms[next_index]

    # Method to get the previous room in the sequence
    def get_previous_room(self):
        current_index = self.rooms.index(self.currentRoom)
        previous_index = (current_index - 1) % len(self.rooms)  # Wrap around to the last room if at the first room
        return self.rooms[previous_index]
    
    # Method to display perception
    def displayPerception(self):
        print("Perception at step %d is [%s,%s]" % (self.step, self.currentRoom.status, self.currentRoom.location))
    
    # Method to display action
    def displayAction(self):
        print("------- Action taken at step %d is [%s]" % (self.step, self.action))

    # Method to set delay
    def delay(self, n=100):
        self.delay = n

# Room class
class Room:
    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status

# Abstract agent class
class Agent(object):
    ''' Base class for agents '''

    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def sense(self, environment):
        pass
    
    @abstractmethod
    def act(self):
        pass

# Vacuum cleaner agent class
# Vacuum cleaner agent class
class VaccumAgent(Agent):
    ''' Vacuum cleaner agent class '''

    def __init__(self):
        ''' Constructor '''
        pass
    
    # Sense method
    def sense(self, env):
        self.environment = env
    
    # Act method
    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'

        # Get current room index
        current_index = self.environment.rooms.index(self.environment.currentRoom)

        # Decide whether to move to the next room or the previous room
        if current_index < len(self.environment.rooms) - 1:
            return 'right'  # Move to the next room if not in the last room
        elif current_index > 0:
            return 'left'  # Move to the previous room if not in the first room
        
        # If the agent is at the last room and all rooms are clean, stop or repeat the loop
        return 'right'  # This assumes a wrap around behavior; adjust as needed



if __name__ == '__main__':
    # Example: 4-room environment with all rooms initially dirty
    room_statuses = ['dirty'] * 4
    vcagent = VaccumAgent()
    env = NRoomVaccumCleanerEnvironment(vcagent, room_statuses)
    env.executeStep(100)
