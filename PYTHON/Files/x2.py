import pyglet

car_img = pyglet.image.load('images/car.png')
carSprite = pyglet.sprite.Sprite(car_img)
window = pyglet.window.Window()
pyglet.gl.glClearColor(1, 1, 1, 1)

@window.event
def on_draw():
    window.clear()
    carSprite.draw()

pyglet.app.run()