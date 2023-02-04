import appgamekit as agk

class Stopwatch:
    def __init__(self):
        self.pause = False
        self.time = 0.0
        self.start_time = 0
        self.repeat_duration = 0
        
        
    def reset(self):
        self.pause = False
        self.time = 0.0  

    def start(self):
        self.reset()
       # self.start_time = agk.timer()

    def update(self):
        if not self.pause:
            self.time += agk.get_frame_time()
        #self.time = agk.timer() - self.start_time
        #
    def check_pulse(self):
        if self.time > self.repeat_duration:
            self.reset()
            return True 
        else:
            return False

    
