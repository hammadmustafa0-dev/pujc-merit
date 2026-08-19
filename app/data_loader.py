import pandas as pd

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger=logging.getLogger(__name__)



def search_by_name(name:str , merit_list:str):

    file_name=f"data/{merit_list}-2026.csv"

    

    df=pd.read_csv(file_name)

    logger.info(f"loaded the {file_name}")



    # this will only return the names which are separated(e.g if u enter ali , it wont return alia , but can return ali , or ali ahmed etc)
    pattern=rf'\b{name}\b'                                        

    result=df[df["APPLICANT NAME"].str.contains(pattern , case=False , na=False)] 

    logger.info(f"filtered for the name {name}")

    

    # removing the remarks coloumn  / errors=ignore makes sure that theres no error if colm name isnt present in the file
    result=result.drop(columns=["REMARKS","HFZ QRN"],errors="ignore")

    logger.info(f"removed extra colomns")


    # converts pandas data into stnadard python data + fillna converts nan into clean empty space.
    clean_result=result.astype(object).fillna("")

    logger.info(f"converted to standard data type")

    

    # orient tells to convert every single row as a diff dict and put all rows in a dict
    final_result=clean_result.to_dict(orient="records")
    logger.info(f"converted to dict")


    print("----------------------------------------")

    
    return final_result



if __name__=="__main__":
    pass