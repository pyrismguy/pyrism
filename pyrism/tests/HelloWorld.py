import sys
import sdl2.ext

sdl2.ext.init()

window = sdl2.ext.Window("Hello World!", size=(640, 480))
window.show()

factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

spriterenderer = factory.create_sprite_render_system(window)