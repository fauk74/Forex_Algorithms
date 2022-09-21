import json
from models.instrument import Instrument 

class InstrumentCollection:



    def __init__(self):
        self.instruments_dict={}
        self.FILENAME = "instruments.json"
        self.API_KEYS = ['name', 'type', 'displayName', 'pipLocation', 'displayPrecision', 'tradeUnitsPrecision',
                         'marginRate']

    def LoadInstruments(self, path):
        self.instruments_dict={}
        fileName=f"{path}/{self.FILENAME}"
        with open(fileName, "r") as f:
            data=json.load(f)
            for k,v in data.items():
                self.instruments_dict[k]= Instrument.FromApiObject(v)

    def CreateFile(self, data, path):
        if data is None:
            print("Instrument file creation failed")
            return
        self.instruments_dict={}
        for i in data:
            key=i['name']
            self.instruments_dict[key]={k: i[k] for k in self.API_KEYS}
        fileName=f"{path}/{self.FILENAME}"
        with open(fileName, "w") as f:
             f.write(json.dumps(self.instruments_dict, indent=2))

    def PrintInstruments(self):
        [print(k,v) for k,v in self.instruments_dict.items()]
        print(len(self.instruments_dict.keys()), "instruments")

InstrumentCollection=InstrumentCollection()