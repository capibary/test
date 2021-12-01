import pygame


class React:
    def __init__(self, obj):
        self.obj = obj
        self.x_star = 0
        self.y_start = 0
        pygame.draw.rect(self.obj, (34, 245, 76),
                         (self.x_star, self.y_start, 100, 100))

    def update(self, rel):
        self.x_star += rel[0]
        self.y_start += rel[1]
        pygame.draw.rect(self.obj, (34, 245, 76),
                         (self.x_star, self.y_start, 100, 100))

    def get_pos(self):
        return self.x_star, self.y_start, self.x_star + 100, self.y_start + 100


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    react = React(screen)
    running = True
    clicked = False
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                react_pos = react.get_pos()
                click_pos = event.pos
                if react_pos[0] <= click_pos[0] <= react_pos[2]:
                    if react_pos[1] <= click_pos[1] <= react_pos[3]:
                        clicked = True
            if event.type == pygame.WINDOWEXPOSED:
                print(4)


        pygame.display.flip()
    pygame.quit()
