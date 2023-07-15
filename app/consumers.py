from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json


# Sync Consumer যখন কাউকে msg send করে তখন এক সাথে এক জন এর বেশি clint কে msg send করতে পারে না। 
# এক জনকে msg send করা শেষ হলে next clint কে msg দেয়া শুরু করে।
# NOTE অর্থাত একই সাথে একাধিক Request কে hendel করতে পারে না।
class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("Connect...........")

        # এই Hendeler টি লিখাহয়েছে Connect টি accept করার জন্যে।
        self.send({
            "type": "websocket.accept",
        })


    def websocket_receive(self, event):
        print("Receive...........")
        print("Message is: ", event['text'])

        # Clint এর Data যখন এখানে পোছাবে তখন তাকে একটি fitback msg দেয়ার হয়েছে।
        # self.send({
        #     "type": "websocket.send",
        #     "text": "Message is received.",
        # })

        ## NOTE রিয়েল টাইম Data এখন থেকে send করা হয়েছে। 
        # for i in range(10):
        #     self.send({
        #         "type": "websocket.send",
        #         "text": str(i),
        #     })
        #     sleep(1)

        ## NOTE যদি আমরা কোন Dictenary পাঠাতে চাই তবে আমাদের তা json string এ convert করতে হবে,
        # for i in range(10):
        #     self.send({
        #         "type": "websocket.send",
        #         "text": json.dumps({"Count": i})
        #     })
        #     sleep(1)

        ## NOTE যদি আমরা কোন Dictenary পাঠাতে চাই তবে আমাদের তা json string এ convert করতে হবে,
        # list_data = ["Md Rakib", "Md Hassan", "Sumilon", "Rasel", "Ratul", "Rashed", "Siddek", "Monzu", "Ovi"] 
        # for i in list_data:
        #     self.send({
        #         "type": "websocket.send",
        #         "text": json.dumps(list_data)
        #     })
        #     sleep(1)

        ## NOTE যদি আমরা কোন Dictenary পাঠাতে চাই তবে আমাদের তা json string এ convert করতে হবে,
        dic_data = {"Name": "Md Rakib", "Age": 25, "Address": "Lalbagh, Dhaka"}
        self.send({
            "type": "websocket.send",
            "text": json.dumps(dic_data),
        })


    def websocket_disconnect(self, event):
        print("Disconnect...........")
        raise StopConsumer()








# Async Consumer যখন কাউকে msg send করে তখন এক সাথে এক এর আধিক clint কে msg send করতে পারে। 
# এক্ষেত্রে তার এক জনকে msg send করা শেষ হলে next clint কে msg পাঠানোর দরকার হয় না, সে এক সাথে করতে পারে।
# NOTE অর্থাত একই সাথে একাধিক Request কে hendel করতে পারে।
class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Connect...........")
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        print("Receive...........")
        print("Message is: ", event['text'])
        # await asyncio.sleep(1)
        
        # await self.send({
        #     "type": "websocket.send",
        #     "text": "Message send to Client",
        # })

        # রিয়েল টাইম Data এখন থেকে send করা হয়েছে। 
        for i in range(10):
            await self.send({
                "type": "websocket.send",
                "text": str(i),
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print("Disconnect...........")
        raise StopConsumer()