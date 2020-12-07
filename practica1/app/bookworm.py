from app.character import Character

class Bookworm(Character):

    def __init__(self):
        super().__init__(25, 9)
        self.skill = "Una vez cada 4 rondas puede resucitar a otro jugador que haya "
        self.skill += "perdido todos los puntos de vida.\nSi se utiliza la habilidad y no "
        self.skill += "hay ningún jugador sin puntos de vida no cuenta como usada."
        self.skill_used = False

    def getSkill(self):
        return self.skill

    def setSkill(self, skill):
        self.skill = skill

    def isSkillUsed(self):
        return self.skill_used

    def setSkillUsed(self, used):
        self.skill_used = used

    def __str__(self):
        return "BOOKWORM\n" +"\nSkill: " + self.skill + "\nUsed: " + str(self.skill_used) + "\n"

# player = Bookworm(25, 9)

# print(player.__str__())
# print(player.hp)
# print(player.dmg)
