from abc import abstractmethod
import time

class Environment(object):
    @abstractmethod
    def __init__(self, n):
        # Initializes the environment with the number of rooms (n) and sets the initial score to 0
        self.n = n
        self.score = 0
    
    @abstractmethod
    def executeStep(self, n=1):
        pass
    
    @abstractmethod
    def executeAll(self):
        pass
    
    def delay(self, n=100):
        # Introduces a delay for simulation or visualization purposes
        time.sleep(n / 1000.0)

class NRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent, room_statuses):
        self.rooms = [Room(chr(65 + i), status) for i, status in enumerate(room_statuses)]
        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.delay_time = 1000  # Rename the attribute to store delay time to avoid conflict
        self.step = 1
        self.action = ""
        self.score = 0  # Initialize the score attribute


    def executeStep(self, n=1):
        for _ in range(n):
            self.displayPerception()
            self.agent.sense(self)
            # Retrieve action and score from the agent
            self.action, score = self.agent.act()
            if self.action == 'clean':
                # If the action is to clean, update the room status and add score
                self.currentRoom.status = 'clean'
                self.score += score
            elif self.action == 'right':
                # If moving right, update current room and add score
                self.currentRoom = self.get_next_room()
                self.score += score
            elif self.action == 'left':
                # If moving left, update current room and add score
                self.currentRoom = self.get_previous_room()
                self.score += score
            self.displayAction()
            print("Current Score:", self.score)  # Display current score after each action
            self.step += 1
            self.delay()  # Introduce delay
    
    def executeAll(self):
        # Execute steps until all rooms are clean
        while any(room.status == 'dirty' for room in self.rooms):
            self.executeStep()
    
    def get_next_room(self):
        # Helper method to get the next room in the sequence
        index = self.rooms.index(self.currentRoom)
        return self.rooms[(index + 1) % len(self.rooms)]

    def get_previous_room(self):
        # Helper method to get the previous room in the sequence
        index = self.rooms.index(self.currentRoom)
        return self.rooms[(index - 1) % len(self.rooms)]
    
    def displayPerception(self):
        # Display the current perception of the environment (room status and location)
        print(f"Perception at step {self.step} is [{self.currentRoom.status},{self.currentRoom.location}]")
    
    def displayAction(self):
        # Display the action taken by the agent
        print(f"------- Action taken at step {self.step} is [{self.action}]")

class Room:
    def __init__(self, location, status="dirty"):
        # Represents a room with a location and a status (default is dirty)
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
        # Set the environment object for sensing
        self.environment = env
    
    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            # If the room is dirty, return 'clean' action and add 25 points to the score
            return 'clean', 25
        index = self.environment.rooms.index(self.environment.currentRoom)
        if index < len(self.environment.rooms) - 1:
            # If not at the last room, move right and deduct 1 point for moving
            return 'right', -1
        elif index == len(self.environment.rooms) - 1 and any(r.status == 'dirty' for r in self.environment.rooms):
            # If at the last room and any room is dirty, move left and deduct 1 point for moving
            return 'left', -1
        return 'stop', 0  # Stop if at the last room and all rooms are clean

if __name__ == '__main__':
    # Example: 4-room environment with all rooms initially dirty
    room_statuses = ['dirty', 'dirty', 'dirty', 'dirty']
    vcagent = VaccumAgent()
    env = NRoomVaccumCleanerEnvironment(vcagent, room_statuses)
    env.executeAll()
