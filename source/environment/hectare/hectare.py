from source.entities.avatar import avatar
from source.entities.rock import rock
from source.entities.tile import tile

class Hectare:
    coordinates     = (0,0)
    size            = 100
    entities        = []
    avatar          = None
    rock            = None
    __tiles         = [[None]]
    alreadyRendered = []

    def __init__(self):
        self.avatar = avatar.Avatar(self)
        self.rock = rock.Rock()
        self.rock.position.x = 300
        self.rock.position.y = 300

        self.populate_ground_tiles()

        self.entities = [
            self.avatar,
            self.rock
        ]
        pass

    def get_tile(self, x, y):
        if x < self.size and y < self.size:
            if self.__tiles[x][y] == None:
                self.__tiles[x][y] = tile.Tile()
                self.__tiles[x][y].position.x = (x * self.__tiles[x][y].width)
                self.__tiles[x][y].position.y = (y * self.__tiles[x][y].height)
            return self.__tiles[x][y]
        return None
    
    def populate_ground_tiles(self):
        self.__tiles = [[None for x in range(self.size)] for y in range(self.size)]

        pass
    
    def get_tiles(self, a):
        x = a[0]
        y = a[1]
        w = a[2]
        h = a[3]

        if x <= 0:
            x = 0
        if y <= 0:
            y = 0

        tmp_tiles = [[self.get_tile(k, l) for k in range(x, x+w)] for l in range(y, y+h)]
        return tmp_tiles

    def convert_pixel_dimensions_to_tile_dimensions(self, a, b, c, d):
        tile_width = self.get_tile(0, 0).width
        tile_height = self.get_tile(0, 0).height
        x = int((a - (c / 2)) / tile_width)
        y = int((b - (d / 2)) / tile_height)
        w = int((c + (c)) / tile_width) + 1
        h = int((d + (d)) / tile_height) + 1
        return (x, y, w, h)
    
    def get_near_tiles(self, obj):
        return self.get_tiles(
            self.convert_pixel_dimensions_to_tile_dimensions(
                obj.position.x,
                obj.position.y,
                obj.resolution.x,
                obj.resolution.y
            )
        )

    def on_render(self, camera):
        for row in self.get_near_tiles(camera):
            for t in row:
                if t != None:
                    if camera.in_viewport(t):
                        t.on_render(camera)

        for entity in self.entities:
            entity.on_render(
                camera
            )
        pass

    def on_loop(self):
        for row in self.get_near_tiles(self.avatar):
            for t in row:
                if t != None:
                    t.on_loop()
        
        for entity in self.entities:
            entity.on_loop()
