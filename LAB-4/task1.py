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

# Environment for a two-room vacuum cleaner
class ThreeRoomVaccumCleanerEnvironment(Environment):
    ''' Environment for a three-room vacuum cleaner '''

    def __init__(self, agent):
        ''' Constructor '''
        self.r1 = Room('A', 'dirty')
        self.r2 = Room('B', 'dirty')
        self.r3 = Room('C', 'dirty')  # New room C added
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 1000
        self.step = 1
        self.action = ""
    
    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                if self.currentRoom == self.r1:
                    self.currentRoom = self.r2
                elif self.currentRoom == self.r2:
                    self.currentRoom = self.r3
                # Handle moving right from room C (if needed)
            else:
                if self.currentRoom == self.r3:
                    self.currentRoom = self.r2
                elif self.currentRoom == self.r2:
                    self.currentRoom = self.r1
                # Handle moving left from room A (if needed)
            self.displayAction()
            self.step += 1

    # Method to execute all steps
    def executeAll(self):
        raise NotImplementedError('action must be defined!')
    
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
        # Update condition for moving right to room B and C
        if self.environment.currentRoom.location == 'A':
            return 'right'
        elif self.environment.currentRoom.location == 'B':
            return 'right'  # Add condition to move right from room B to C
        return 'left'

if __name__ == '__main__':
    vcagent = VaccumAgent()
    env = ThreeRoomVaccumCleanerEnvironment(vcagent)
    env.executeStep(50)
