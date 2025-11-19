import pygame
import math
import sys

# ---------------- CONFIG ---------------- #
WIDTH, HEIGHT = 800, 600        # Auto full window later if needed
TEXT = "I Love You "
FONT_SIZE = 18
PINK = (255, 166, 214)          # #ffa6d6 in hex
SCALE = 15                     # Same JS scale
ROT_SPEED = 0.003               # Same animation speed
# ---------------------------------------- #

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart Text Animation")

# Text + Glow
font = pygame.font.SysFont("Arial", FONT_SIZE, bold=False)

# Enable blend mode for glow
def draw_glow_text(text, x, y):
    # Slight blur using multiple shadows like shadowBlur in canvas
    for blur in range(6):
        color = (PINK[0], PINK[1], PINK[2], max(10, 60 - blur*10))
        glow_surface = font.render(text, True, color)
        glow_surface.set_alpha(60)
        screen.blit(glow_surface, (x, y))
    # Main solid text
    text_surface = font.render(text, True, PINK)
    screen.blit(text_surface, (x, y))

# Heart parametric formula
def heart_xy(t):
    x = SCALE * 16 * (math.sin(t)**3)
    y = -SCALE * (
        13*math.cos(t) -
        5*math.cos(2*t) -
        2*math.cos(3*t) -
        math.cos(4*t)
    )
    return x, y

def main():
    angle = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Black background

        # Center of screen
        cx, cy = WIDTH // 2, HEIGHT // 2

        total = 100  # Same as JS

        for i in range(total):
            t = (i / total) * (2 * math.pi) + angle
            x, y = heart_xy(t)
            draw_glow_text(TEXT, cx + x, cy + y)

        angle += ROT_SPEED  # same speed as JS

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
