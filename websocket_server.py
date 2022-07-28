import asyncio
import websockets


connected = set()

async def echo(websocket):

    try:
        connected.add(websocket)

        async for message in websocket:
            await websocket.send(message)
            print("***", message)
            for conn in connected:
                await conn.send("Alguem falou: " + message)

    except websockets.exceptions.ConnectionClosed as e:
        print("Cliente Desconectado")

    finally:
        connected.remove(websocket)

async def main():
    async with websockets.serve(echo, "localhost", 5000):
        await asyncio.Future()


asyncio.run(main())