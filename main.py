import sys
import pygame as pg
WIDTH = 1024
HEIGHT = 1024
class Player(pg.sprite.Sprite):
    move_dict = {
        pg.K_LEFT: (-1, 0),
        pg.K_a: (-1, 0),
        pg.K_RIGHT: (1, 0),
        pg.K_d: (1, 0),
        pg.K_UP: (0, -1),
        pg.K_SPACE: (0, -1)
    }
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pg.Surface((64, 64))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.gravity_vel = 5
        self.jump_power = 256
        self.isGround = False
    def update(self, key_lst: dict):
        for d in __class__.move_dict:
            if key_lst[d]:
                self.rect.x += self.move_dict[d][0] * 3
                if self.isGround:
                    self.rect.y += self.move_dict[d][1] * self.jump_power
                    if self.move_dict[d][1] < 0:
                        self.isGround = False
        if not self.isGround:
            self.rect.y += self.gravity_vel
class Block(pg.sprite.Sprite):
    size = (32, 32)
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pg.Surface((32, 32))
        self.image.fill((127, 127, 127))
        self.rect = self.image.get_rect()
        self.rect.center = pos


class Score:
    """
    時間経過で増えていくスコアと
    プレイヤー死亡時の最終スコアの表示
    """
    def __init__(self):
        self.score = 0
        self.final_score = 0
        self.font = pg.font.Font(None, 36)
        self.game_over_font = pg.font.Font(None, 50)
        

    def increase(self, points):
        self.score += points

    def render(self, surface, pos):
        score_surface = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        surface.blit(score_surface, pos)

    def render_final(self):
        final_score_surface = self.font.render("GameOver!! \n Final Score: " + str(self.score), True, (255, 255, 255))
        restart_surface = self.font.render("Restart: press:'TAB' Quit: press:'ESC'", True, (255, 255, 255))
        final_score_surface.blit(final_score_surface, (WIDTH / 2, HEIGHT / 2 -50))
        restart_surface.blit(restart_surface, (WIDTH / 2, HEIGHT / 2))
        for event in pg.event.get():
            if event.type == pg.key.get_pressed:
                if pg.key.get_pressed == pg.K_TAB:
                    main()
                elif pg.key.get_pressed == pg.K_ESCAPE:
                    break


def main():
    pg.display.set_caption("proto")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.Surface((WIDTH, HEIGHT))
    bg_img.fill((0, 0, 0))
    all_rect_lst = []
    player = Player((500, HEIGHT - 50))
    all_rect_lst.append(player.rect)
    blocks = pg.sprite.Group()
    for i in range(256):
        blocks.add(Block((i * Block.size[0], HEIGHT)))
    for i in range(10):
        blocks.add(Block((WIDTH // 2, WIDTH - i * Block.size[1])))
    for b in blocks:
        all_rect_lst.append(b.rect)

    score = Score()

    tmr = 0
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return 0
                elif event.key == pg.K_TAB:
                    main()


        key_lst = pg.key.get_pressed()
        player.update(key_lst)
        player.isGround = False
        collide_lst = pg.sprite.spritecollide(player, blocks, False)
        if len(collide_lst) > 0:
            for b in collide_lst:
                if player.rect.top < b.rect.bottom:
                    player.rect.top = b.rect.bottom
                if player.rect.bottom > b.rect.top:
                    player.rect.bottom = b.rect.top
                    player.isGround = True
        screen.blit(bg_img, (0, 0))
        blocks.draw(screen)
        screen.blit(player.image, player.rect)
        score.render(screen, (WIDTH - 150, 10))
        pg.display.update()

        tmr += 1
        if tmr % 60 == 0:
            score.increase(1)
        clock.tick(60)

    pg.quit()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()