import pygame


class Board:
    def __init__(self, width, height):
        self.width_sqr = width
        self.height_sqr = height
        self.board = []
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.width_brd = width * self.cell_size
        self.height_brd = height * self.cell_size
        self.board_dict = dict()
        self.set_board()

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.board = []
        self.set_board()

    def get_cell(self, click):
        x = click[0]
        y = click[1]
        if self.left < x < self.width_brd and self.top < y < self.height_brd:
            return (x - self.left) // self.cell_size, (y - self.top) // self.cell_size
        else:
            return None

    def set_board(self):
        print(self.board)
        x_now = self.left
        y_now = self.top
        for i in range(self.height_sqr):
            ln = []
            for j in range(self.width_sqr):
                ln.append([(x_now, y_now), (j, i)])
                x_now += self.cell_size
            self.board.append(ln)
            x_now = self.left
            y_now += self.cell_size

        print(self.board)

    def render(self, obj):
        for i in self.board:
            for j in i:
                pygame.draw.rect(obj, (255, 255, 255),
                                 (j[0][0], j[0][1], self.cell_size, self.cell_size), 1)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    board = Board(15, 8)
    board.render(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = board.get_cell(event.pos)
                print(a)
        pygame.display.flip()
    pygame.quit()
