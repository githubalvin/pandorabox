from kumex import KuMexExchange
from utils import Singleton


class TradeController(Singleton):

    def __init__(self):
        self.exchanges = []

    def setup(self):
        kumex = KuMexExchange('https://api-futures.kucoin.io',
                              '5f3cf2295b13f000064986a6',
                              '8436b3ec-892b-4f2f-ae65-4a4fa3768cac',
                              '1234567')
        kumex.setup()
        self.exchanges.append(kumex)

    async def release(self):
        for obj in self.exchanges:
            await obj.release()

    @property
    def kumex(self):
        return self.exchanges[0]