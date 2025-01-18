import pygame
import os
import sys
import random


# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 500, 500
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Platform2(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.Surface((10, 50))
        self.image.fill(pygame.Color("red"))  # Заполнение поверхности серым цветом
        self.rect = self.image.get_rect(topleft=pos)


    def update(self, event):
        pass


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.Surface((50, 10))
        self.image.fill(pygame.Color("gray"))  # Заполнение поверхности серым цветом
        self.rect = self.image.get_rect(topleft=pos)


    def update(self, event):
        pass


class Character(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.Color("blue"))  # Заполнение поверхности серым цветом
        self.rect = self.image.get_rect(topleft=pos)


    def update(self, *args):
        if (len(pygame.sprite.spritecollide(self, all_sprites, 0)) == 1 and
                type(pygame.sprite.spritecollide(self, all_sprites, 0)[0]) == Character):
            self.rect = self.rect.move(0, 1)
        if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_LEFT:
            self.rect = self.rect.move(-10, 0)
        if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_RIGHT:
            self.rect = self.rect.move(10, 0)
        if any(type(i) == Platform2 for i in pygame.sprite.spritecollide(self, all_sprites, 0)):
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_UP:
                self.rect = self.rect.move(0, -10)
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_DOWN:
                self.rect = self.rect.move(0, 10)


if __name__ == '__main__':
    # команды рисования на холсте
    pygame.display.set_caption('Платформы')

    running = True
    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    character = None
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    keys = pygame.key.get_pressed()  # Получаем состояние клавиш
                    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                        Platform2(event.pos)
                    else:
                        Platform(event.pos)
                elif event.button == 3:
                    if not character:
                        character = Character(event.pos)
                    else:
                        character.rect.x = event.pos[0]
                        character.rect.y = event.pos[1]

        screen.fill('black')
        all_sprites.draw(screen)
        all_sprites.update(event)
        clock.tick(50)
        # обновление экрана
        pygame.display.flip()
    # завершение работы:
    pygame.quit()
