#!/usr/bin/env python
import numpy as np
from space import space
from panda3d.core import Filename

class airplane_animation(space):
    def __init__(self):
        super().__init__()
        
        # Load the airplane mesh
        self.airplane = self.load_mesh("airplane.glb")
        self.airplane.setScale(0.5)
        
        # Define start and end positions
        self.p1 = np.array([0, 5, 0])
        self.p2 = np.array([1, -6, 5])
        
        # Set the initial position
        self.airplane.setPos(*self.p1)
        
        # Animation state
        self.t = 0
        self.animating = False
        
        # Bind spacebar to start animation
        self.accept('space', self.start_animation)
        
        # Add animation task
        self.taskMgr.add(self.animate_airplane, "AnimateAirplane")
        
    
    def start_animation(self):
        self.t = 0
        self.animating = True
    
    def animate_airplane(self, task):
        if self.animating:
            # Interpolation formula
            current_pos = (1 - self.t) * self.p1 + self.t * self.p2
            
            # Update position
            self.airplane.setPos(*current_pos)
            
            # Increment t (controls speed)
            self.t += 0.005
            
            # Stop at end
            if self.t >= 1.0:
                self.t = 1.0
                self.animating = False
                print("Landing complete!")
        
        return task.cont

app = airplane_animation()
app.run()