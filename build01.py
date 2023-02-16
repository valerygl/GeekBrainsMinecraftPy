from pprint import pprint
import requests
from mcpi.minecraft import Minecraft
import time
import re
mc = Minecraft.create()

def build_floor(data,floor,x,y,z,length,width):
    global count_blocks
    for j in range(width):
        for i in range(length):
            #Получаем информацию о блоке
            block_data = data[j*length+i].split('-')
            main_id_block = int(block_data[0])
            second_id_block = int(block_data[1])
            print(main_id_block,second_id_block, end =' ')
            #Строим блок в мире майнкрафт
            mc.setBlock(i+x, floor+y-1, j+z, main_id_block, second_id_block)
            #Считаем количество использованны блоков
            count_blocks += 1
            # time.sleep(0.001)
        print()

def get_data(id):
    url = f'https://mcpehub.org/plan.php?id={id}'
    response = requests.get(url)
    id_build = int(re.findall(r'data-build-id="(\d+)', response.text)[0])

    url = f'https://mcpehub.org/engine/ajax/building-get.php?id={id_build}'
    build_data = requests.get(url).json()

    return build_data, id_build

buildings = {}

width = 20
height = 16
pages = 22

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

count_blocks = 0


build_id = int(input('Введите id постройки: '))
build_data, build_id = get_data(build_id)

height = int(build_data['height']) + 1
length = int(build_data['length'])
width = int(build_data['width'])


for i in range(1, height):
    url = f'https://mcpehub.org/uploads/buildings/{build_id}/{i}.json'
    response = requests.get(url)
    data = response.json()
    build_floor(data,i,x,y,z,width,length)
print('Всего блоков использовано:',count_blocks)




