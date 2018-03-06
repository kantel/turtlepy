class Creature:
    
    def __init__(self, x, y, speed = 1.0, size = 4.0):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        
        self._vx = 0
        self._vy = 0
        
    def wander(self):
        v = self.speed
        self._vx += random(-v, v)
        self._vy += random(-v, v)
        
        self._vx = max(-v, min(self._vx, v))
        self._vy = max(-v, min(self._vy, v))
        
        self.x += self._vx
        # checking boundaries
        if self.x > WIDTH:
            self.x = self._vx
        elif self.x < 0:
            self.x = WIDTH - self._vx
        self.y += self._vy
        # checking boundaries
        if self.y > HEIGHT:
            self.y = self._vy
        elif self.y < 0:
            self.y = WIDTH - self._vy
