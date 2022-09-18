from osrs_fcns import *


def runTableAdder():
    csvList = getCSVList()
#     print(csvList)
    for i in tqdm(csvList):
        dfName = 'Data_CSVs\\'+i
        
        price_df = pd.read_csv(dfName)
        price_df.drop('Unnamed: 0',axis=1,inplace=True)
        shutil.move(dfName,'Imported\\'+i)
        if(len(price_df) == 0):
#             print('No Columns!')
            continue
        #move dfName to folder called Imported
        
        addCSV_ToDB(price_df)
        
runTableAdder()