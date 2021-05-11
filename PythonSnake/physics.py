from pygame.math import Vector2
import map

def has_collision(a, b):
    x_overlap = (a.left < b.right) and (a.right > b.left)
    y_overlap = (a.top < b.bottom) and (a.bottom > b.top)
    return x_overlap and y_overlap

class PhysicsObject:
    _parent = None
    _epsilon = 0.01

    mass = 1.0
    force = Vector2(0, 0)
    velocity = Vector2(0, 0)
    position = Vector2(0, 0)
    
    bounce = 0.0

    def __init__(self, parent):
        self._parent = parent

    def update(self, delta, world):
        # print("Fore %s" % self.force)
        # print("Velocity %s" % self.velocity)
        # print("Position %s" % self.position)

        # acceleration = force / mass
        self.velocity = self.velocity + self.force / self.mass * delta
        self.position = self.position + self.velocity * delta

        # reseting forces every frame
        self.force = Vector2(0, 0)

        # check collisions
        for tile in world:
            if has_collision(self._parent.get_rect(), tile.get_rect()):
                # TODO: emit events
                if tile.get_type() == "ground":
                    # rewind position to edge of object
                    self.position.y = tile.get_rect().top - self._parent.get_rect().height
                    if self.velocity.magnitude_squared() > self._epsilon:
                        self.add_force(Vector2(0, -1) * self.bounce * self.mass * self.velocity.y)
                    self.velocity.y = 0
                elif tile.get_type() == "kill":
                    # reset position
                    print("player died")

    def add_force(self, force):
        self.force = self.force + force * self.mass