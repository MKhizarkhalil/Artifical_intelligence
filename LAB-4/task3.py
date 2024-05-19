from abc import abstractmethod
import time

class Environment(object):
    @abstractmethod
    def __init__(self, n):
        self.n = n
    
    @abstractmethod
    def executeStep(self, n=1):
        pass
    
    @abstractmethod
    def executeAll(self):
        pass
    
    def delay(self, n=100):
        time.sleep(n / 1000.0)

class NRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent, room_statuses):
        self.rooms = [Room(chr(65 + i), status) for i, status in enumerate(room_statuses)]
        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.delay = 1000
        self.step = 1
        self.action = ""
    
    def executeStep(self, n=1):
        for _ in range(n):
            self.displayPerception()
            self.agent.sense(self)
            self.action = self.agent.act()
            if self.action == 'clean':
                self.currentRoom.status = 'clean'
            elif self.action == 'right':
                self.currentRoom = self.get_next_room()
            elif self.action == 'left':
                self.currentRoom = self.get_previous_room()
            self.displayAction()
            self.step += 1
    
    def executeAll(self):
        while any(room.status == 'dirty' for room in self.rooms):
            self.executeStep()
    
    def get_next_room(self):
        index = self.rooms.index(self.currentRoom)
        return self.rooms[(index + 1) % len(self.rooms)]

    def get_previous_room(self):
        index = self.rooms.index(self.currentRoom)
        return self.rooms[(index - 1) % len(self.rooms)]
    
    def displayPerception(self):
        print(f"Perception at step {self.step} is [{self.currentRoom.status},{self.currentRoom.location}]")
    
    def displayAction(self):
        print(f"------- Action taken at step {self.step} is [{self.action}]")

class Room:
    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status

class Agent(object):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def sense(self, environment):
        pass
    
    @abstractmethod
    def act(self):
        pass

class VaccumAgent(Agent):
    def __init__(self):
        pass
    
    def sense(self, env):
        self.environment = env
    
    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        index = self.environment.rooms.index(self.environment.currentRoom)
        if index < len(self.environment.rooms) - 1:
            return 'right'
        elif index == len(self.environment.rooms) - 1 and any(r.status == 'dirty' for r in self.environment.rooms):
            return 'left'
        return 'stop'

if __name__ == '__main__':
    room_statuses = ['dirty', 'dirty', 'dirty', 'dirty']
    vcagent = VaccumAgent()
    env = NRoomVaccumCleanerEnvironment(vcagent, room_statuses)
    env.executeAll()
