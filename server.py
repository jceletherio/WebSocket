import asyncio
import websockets

async def score(websocket, path):
    score = await websocket.recv()
    print(score)
    await websocket.send(score)
    
start_server = websockets.serve(score, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
