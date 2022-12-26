import pygame

# ---Setup---
pygame.init()   # Initialise pygame

# Set the dimensions of the window
window_width = 1280
window_height = 720

# Set up the window to the required dimensions, name it and create a clock object
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("[Game]")
clock = pygame.time.Clock()

# ---Main Game Loop---
while True:
    # Check event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("black")
    # Update sprites here
    
    # Display screen updates here
    
    pygame.display.flip()  # Display the screen updates
    frame_time = clock.tick(60)    # Advance the clock (limited to 60FPS)
