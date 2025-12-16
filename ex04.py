class Vector():
    def __init__(self, x: int, y: int, z:int):
        self._z = z
        self._y = y
        self._x = x
    def __str__(self):
        return f"Vector: {self._x},{self._y},{self._z}"

class VectorOperations():
    def __init__(self):
        pass
    
    def vector_sum(self, v1: Vector, v2: Vector) -> list:
        return [(v1._x + v2._x), (v1._y + v2._y), (v1._z + v2._z)]
    
    def vector_sub(self, v1: Vector, v2: Vector) -> list:
        return [(v1._x - v2._x), (v1._y - v2._y), (v1._z - v2._z)]
    
    def vector_dot(self, v1: Vector, v2: Vector) -> int:
        return (v1._x * v2._x) + (v1._y * v2._y) + (v1._z * v2._z)
    
    def vector_product(self, v1: Vector, v2: Vector) -> list:
        return [((v1._y * v2._z) - (v1._z * v2._y)), ((v1._z * v2._x) - (v1._x * v2._z)), ((v1._x * v2._y) - (v1._y * v2._x))]
    
    def vector_module(self, v1: Vector) -> int:
        x = v1._x**2
        y = v1._y**2
        z = v1._z**2
        total = x + y + z
        return total**(1/2)

