import pygame, modules.path_file as path
import modules.data_base as data
pygame.mixer.init()
#Класс эффект
class Effect:
    #Метод конструктор
    def __init__(self, effect, cors):
        self.EFFECT = effect
        self.TIME = 0
        self.SOUND_PASSER = 0
        self.SOUND = pygame.mixer.Sound(path.path_to_file(f"sounds\\{effect}_sound_effect.mp3"))
        self.SOUND.set_volume(data.volume)
        self.CORS = cors
        self.play_sound()
    def play_sound(self):
        if self.SOUND_PASSER + 1:
            pygame.mixer.Sound.play(self.SOUND)
            self.SOUND_PASSER = 1
    def blit_effect(self, screen):
        if self.EFFECT == "explosion" and 1 < self.TIME < 5 or self.EFFECT == "miss" and 1 < self.TIME < 6:
            effect_image = pygame.image.load(path.path_to_file(f"images\\effects\\{self.EFFECT}-{self.TIME}.png"))
        else:
            effect_image = pygame.image.load(path.path_to_file(f"images\\effects\\{self.EFFECT}-1.png"))
        effect_image = pygame.transform.scale(effect_image, (32, 32))
        screen.blit(effect_image, self.CORS)