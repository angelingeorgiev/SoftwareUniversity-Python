class Town:
    def __init__(self, name_of_town: str):
        self.name_of_town = name_of_town
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude: str):
        self.latitude = latitude

    def set_longitude(self, longitude: str):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name_of_town} | Latitude: {self.latitude} | Longitude: {self.longitude}"


# -- Test Code --
town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
