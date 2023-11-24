import pygame

pygame.init()

width = 400
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Music Player')

music_files = [
    "C:/Users/Admin/lab9_pp2/music/v-bts-rainy-days-mp3.mp3",
    "C:/Users/Admin/lab9_pp2/music/la_la_land_09 - Ryan Gosling & Emma Stone - City of Stars.mp3",
    "C:/Users/Admin/lab9_pp2/music/Ed Sheeran – Perfect.mp3"
]

selected_sound_index = 0
playing = True  # Изменено на True, чтобы музыка начинала воспроизводиться сразу

pygame.mixer.music.load(music_files[selected_sound_index])
pygame.mixer.music.play()  # Начать воспроизведение сразу

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing
            elif event.key == pygame.K_RIGHT:
                selected_sound_index = (selected_sound_index + 1) % len(music_files)
                pygame.mixer.music.load(music_files[selected_sound_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                selected_sound_index = (selected_sound_index - 1) % len(music_files)
                pygame.mixer.music.load(music_files[selected_sound_index])
                pygame.mixer.music.play()

    screen.fill((255, 255, 255)) 

    pygame.display.update()

pygame.quit()
