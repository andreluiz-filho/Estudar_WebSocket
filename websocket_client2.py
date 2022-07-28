import asyncio
from websockets import connect

async def listen():

    url = "ws://localhost:5000"
    async with connect(url) as ws:
        mensagem = "Mensagem do Cliente"

        for i in range(10):
            await ws.send(str(i))

        try:
            while True:
                msg = await ws.recv()
                #print(msg)
        except:
            print("Sem conexão com o Servidor !")    

asyncio.run(listen())