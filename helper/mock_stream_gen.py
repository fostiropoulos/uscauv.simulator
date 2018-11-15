from typing import List
import random, os
import json


class Vector3:
    def __init__(self, x: float = 0., y: float = 0., z: float = 0.):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'Vector3'):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other: 'Vector3'):
        self = self + other
        return self

    def __sub__(self, other: 'Vector3'):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __mul__(self, other: float):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other: float):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __imul__(self, other: float):
        self = self * other
        return self

    def __turediv__(self, other: float):
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __itruedif__(self, other: float):
        self = self / other
        return self


class BasicObject:
    def __init__(self, id_: int, type_: int, angle: float, probability: float, position: 'Vector3' = Vector3()):
        self.id_ = id_
        self.type_ = type_
        self.position = position
        self.angle = angle
        self.probability = probability

    def to_json_string(self):
        data = {"id": self.id_, "type": self.type_, "x": self.position.x, "y": self.position.y, "z": self.position.z,
                "th": self.angle, "p": self.probability}
        return data


class DataFrame:
    def __init__(self, timestamp: int, objects: List[BasicObject], depth: float, rotation: float,
                 position: 'Vector3' = Vector3(), acceleration: 'Vector3' = Vector3(), speed: 'Vector3' = Vector3()):
        self.timestamp = timestamp
        self.objects = objects
        self.position = position
        self.acceleration = acceleration
        self.speed = speed
        self.depth = depth
        self.rotation = rotation

    def to_json(self):
        # objects_json = []
        # for obj in self.objects:
        #     objects_json.append(obj.to_json())

        data = {"ts": self.timestamp, "objects": self.objects, "x": self.position.x, "y": self.position.y,
                "z": self.position.z, "ax": self.acceleration.x, "ay": self.acceleration.y, "az": self.acceleration.z,
                "ux": self.speed.x, "uy": self.speed.y, "uz": self.speed.z, "d": self.depth, "th": self.rotation}
        return json.dumps(data, default=lambda x: x.to_json_string(), sort_keys=False, indent=4)


# Current algorithm generates n objects and describes them as the Turtle moves in a randomly
# generated path. Objects are created at random static positions and locations change in relation
# to the Turtle, as it moves.
# Angle and probability are not accounted for at this time.
def random_world_gen(frame_count: int, object_count: int = 10, type_count: int = 3):
    timestamp = 0
    object_list = []
    current_position = Vector3(0, 0, 0)
    current_acceleration = Vector3(0, 0, 0)  # Unaccounted
    current_speed = Vector3(0, 0, 0)  # Unaccounted
    current_depth = 0
    current_rotation = 0  # Unaccounted

    # Create n objects
    for i in range(object_count):
        obj = BasicObject(i, random.randrange(0, type_count), 0, 1)
        obj.position = Vector3(random.uniform(-10., 10.), random.uniform(0., 10.), random.uniform(-10., 10.))

        # Constant angle and probability for now
        obj.angle = 0
        obj.probability = 1
        object_list.append(obj)

    # Simulate n time frames
    for i in range(frame_count):
        delta_t = random.randrange(1000, 2000)
        delta_pos = Vector3(random.random(), random.random(), random.random()) * (delta_t / 1000.)
        timestamp += delta_t

        # Turtle moves by delta_pos and everything shifts around it
        current_position += delta_pos

        for obj in object_list:
            obj.position -= delta_pos

        # Write frame object to file
        frame_obj = DataFrame(timestamp, object_list, current_depth, current_rotation, current_position,
                              current_acceleration, current_speed)

        frame_json = frame_obj.to_json()
        file_name = "{:0>6}.json".format(i)
        frame_file = open(file_name, 'w')
        frame_file.write(frame_json)
        frame_file.close()


def auto_generate():
    frame_count = int(input('Enter frame count:'))
    random_world_gen(frame_count)
    print("Frames generated!\n")
    input("Press Enter to continue...")


def menu():
    while True:
        print("==============================")
        print("     Mock Stream Generator    ")
        print("==============================")
        print("1. Auto generate stream")
        print("2. Live generate stream")
        print("3. Exit")
        print("==============================")
        selection = int(input('Enter your input:'))
        print(selection)
        if selection == 1:
            auto_generate()
        elif selection == 2:
            pass
        elif selection == 3:
            break
        os.system('cls')


if __name__ == "__main__":
    menu()
