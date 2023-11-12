from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

#retorna o endereco realtivo dentro da pasta input
def in_path(file_name):
    return os.path.join(INPUT_FOLDER, file_name)

def triangle(size):
    WHITE = (255,255,255)
    RED = (255, 0, 0)
    image = Image.new("RGB", (size,size), WHITE)
    
    for x in range(size): 
        for y in range(size):
            if x < y:
                image.putpixel((x,y),RED )
    return image

def bandeira_franca(height):
    widht = 3*height//2 #  ou 1050. A proporcao da largura da bandeira.
    #a altura ja e algo "definido" neste codigo, entao embasando-se nelas calculamos a largura dentro da funcao

    BLUE = (0,85, 164)
    WHITE=(255,255,255)
    RED = (239,65,53) 
    image = Image.new("RGB", (widht,height),WHITE )

    offset = widht//3#divide a bandeira em cores
    for x in range(offset):
        for y in range(height):
            image.putpixel((x,y), BLUE)
            image.putpixel((x + 2*offset, y), RED)
    return image

def bandeira_japao(height):
    widht = 3*height//2
    WHITE = (255,255,255)
    RED = (173,35,53)

    r = (3*height//10)#o raio da bandeira do japao equivale a 3/10
    #explicacao do chat: Para visualizar isso, imagine uma bandeira retangular onde a altura total é dividida em 10 partes iguais. O raio do círculo vermelho é então igual a 3 dessas partes.
    c = (widht//2, height//2)
    image = Image.new("RGB", (widht, height),  WHITE)
    for x in range(c[0]-r, c[0]+r):#pega a cordenada 0 do centro e pega o quadrado que fica em volta do circulo
        for y in range(c[1]-r, c[1]+r):
            if (x-c[0])**2 + (y-c[1])**2 <= r**2:
                image.putpixel((x,y), RED)

    return image

if __name__ == "__main__":
    #t = triangle(700)
    #bandeira_f= bandeira_franca(700)
    bandeira = bandeira_japao(700)
    bandeira.show()

    