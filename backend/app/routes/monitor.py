from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict

router = APIRouter(prefix="/monitor", tags=["monitor"])

# Basic in-memory mapping for signaling. For production use Redis pub/sub.
ACTIVE_WS: Dict[str, WebSocket] = {}  # email -> websocket

@router.post('/request')
async def request_monitor(staff_email: str, admin_token: str):
    # admin_token validation omitted here — verify in production
    # notify staff via WS if connected
    ws = ACTIVE_WS.get(staff_email)
    if ws:
        await ws.send_json({"type": "monitor-request", "from": "admin"})
        return {"msg": "monitor request sent"}
    return {"msg": "staff not connected"}

@router.websocket('/ws/signaling/{user_email}')
async def signaling_ws(websocket: WebSocket, user_email: str):
    await websocket.accept()
    ACTIVE_WS[user_email] = websocket
    try:
        while True:
            data = await websocket.receive_json()
            # For demo: just echo or print. In production relay to intended peer
            print('Signaling recv', user_email, data)
            # If a message contains 'to' field, try to forward
            to = data.get('to')
            if to and to in ACTIVE_WS:
                await ACTIVE_WS[to].send_json(data)
    except WebSocketDisconnect:
        print('ws disconnect', user_email)
    finally:
        if user_email in ACTIVE_WS:
            del ACTIVE_WS[user_email]
