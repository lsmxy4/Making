from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from app.config import MONGO_DB_NAME, MONGO_URI

class MongoDB:
    def __init__(self):
        self.client=None
        self.engine=None
    
    def connect(self):
        self.client=AsyncIOMotorClient(MONGO_URI)
        self.engine=AIOEngine(client=self.client, database=MONGO_DB_NAME)
        print("성공적으로 연결 되었습니다.")

    def close(self):
        self.client.close()

mongodb=MongoDB()