from api.oanda_api import OandaApi
from infrastructure.instrument_collection import InstrumentCollection

if __name__=='__main__':
    api=OandaApi()



 #   data=api.get_instruments()
 #   [print(x['name']) for x in data]
 #   data=api.get_account_summary()
 #   print(data)

    InstrumentCollection.CreateFile(api.get_account_instruments(), "./data")
    InstrumentCollection.LoadInstruments("./data")
    InstrumentCollection.PrintInstruments()
