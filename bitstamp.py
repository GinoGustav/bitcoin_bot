import json

import websocket

def comprar():
    pass

def vender():
    pass
def on_open(ws):
    print("Abriu Conexão")

    json_subscribe = """
       
{
        "event": "bts:subscribe",
        "data": 
        {
            "channel": "live_trades_btcusd"
        }
}
    
    """
    ws.send(json_subscribe)
def on_close(ws):
    print("Fechou Conexão")
def on_error(ws, erro):
    print(erro)
def on_message(ws, message):

    message = json.loads(message)
    price = message["data"]["price"]
    print(price)


    if price > 9000:
        vender()
    elif price < 3000:
        comprar()
    else:
        print("Aguardar")




if __name__ == "__main__":
        ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                                    on_open=on_open,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.run_forever()
