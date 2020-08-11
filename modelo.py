# Andrea Abril Palencia Gutierrez, 18198
# SR5: Textures --- Graficas por computadora, seccion 20
# 04/08/2020 - 10/08/2020

from gl import Render
from obj import Obj 
from textura import Texture


modelo = Render(2000,2000)
textura = Texture('./models/model.bmp')
modelo.loadModel('./models/model.obj', (1000, 700, 700), (700, 700, 700), textura)
modelo.glFinish('modelo_obj.bmp')
modelo.glZBuffer('zbuffer.bmp')
print("¡Listo! La imagen esta creada con el nombre de 'modelo_obj.bmp'.")