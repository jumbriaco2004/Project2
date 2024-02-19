from direct.showbase.ShowBase import ShowBase
import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses

class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()

    def SetupScene(self):

        self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.obj", self.render, "Universe", "./Assets/Universe/starfield-in-blue.jpg", (0, 0, 0), 10000)
        self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet1", "Assets/Planets/planet1.jpg", (150, 5000, 67), 350)
        self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet2", "Assets/Planets/planet2.jpg", (5000, 5000, 100), 350)
        self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet3", "Assets/Planets/planet3.jpg", (5000, 100, -500), 500)
        self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet4", "Assets/Planets/planet4.jpg", (3000, 10000, 1000), 1000)
        self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet5", "Assets/Planets/planet5.jpg", (-1000, 2000, 200), 200)
        self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet6", "Assets/Planets/planet6.jpg", (1000, 3000, -300), 500)
        self.SpaceStation1 = spaceJamClasses.SpaceStation(self.loader, "./Assets/Space Station/spaceStation.x", self.render, "Space Station", (1000, 500, 0), (0, 90, 0), 10)
        self.Player = spaceJamClasses.Player(self.loader, "./Assets/SpaceShips/theBorg.x", self.render, "Player", "./Assets/SpaceShips/theBorg.jpg", (100, 100, 0), (0, 90, 0), 2)

        #Setting Drones
        fullCycle = 60
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            droneName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            centralObject = self.Player.modelNode.getPos()
            #self.DrawCloudDefense(centralObject, droneName)
            #self.DrawBaseballSeams(centralObject, droneName, 2, 10)
            #self.DrawCircleXY(centralObject, droneName)
            #self.DrawCircleYZ(centralObject, droneName)
            #self.DrawCircleYZ(centralObject, droneName)

    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject
        spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender.obj", self.render, droneName, "./Assets/Drone Defender/octotoad1_auv.png", position, 10)

    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject
        spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender.obj", self.render, droneName, "./Assets/Drone Defender/octotoad1_auv.png", position, 10)

    def DrawCircleXY(self, centralObject, droneName):
        unitVec = defensePaths.CircleXY()
        unitVec.normalize()
        position = unitVec * 500 + centralObject
        spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender.obj", self.render, droneName, "./Assets/Drone Defender/octotoad1_auv.png", position, 10)

    def DrawCircleXZ(self, centralObject, droneName):
        unitVec = defensePaths.CircleXZ()
        unitVec.normalize()
        position = unitVec * 500 + centralObject
        spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender.obj", self.render, droneName, "./Assets/Drone Defender/octotoad1_auv.png", position, 10)

    def DrawCircleYZ(self, centralObject, droneName):
        unitVec = defensePaths.CircleYZ()
        unitVec.normalize()
        position = unitVec * 500 + centralObject
        spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender.obj", self.render, droneName, "./Assets/Drone Defender/octotoad1_auv.png", position, 10)

play = SpaceJam()
play.run()