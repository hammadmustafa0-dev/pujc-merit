import pandas as pd


urls={
    "BSCS-1st-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/114185626", # 1
    "BSCS-2nd-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/129003608", # 1

    "BS-ENGLISH-1st-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/115057272",   # 1
    "BS-ENGLISH-2nd-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/129121398",   # 1

    "BS-MANAGEMENT-1st-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/114868808",    # 1
    "BS-MANAGEMENT-2nd-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/128579564",    # 1

    "BBA-1st-merit-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/113714466",    # 1
    "BBA-2nd-merit-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/127943498",    # 1

    "BANKING-1st-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/113384654",  # 0
    "BANKING-2nd-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/128932934",  # 0

    "ACCOUNTING-1st-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/114397648",   # 0
    "ACCOUNTING-2nd-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/129309862",   # 0

    "COMMERCE-1st-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/113290422", # 0
    "COMMERCE-2nd-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/128697354", # 0

    "E-COM-1st-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/113926488",    #0
    "E-COM-2nd-list-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/129144956"     #0

}

general_lists={

    "BSCS-general-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/113902930",

    "BS-ENGLISH-general-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/114986598",

    "BS-MANAGEMENT-general-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/114609670",  # 1

    "BBA-general-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/113690908",     # 1

    "BANKING-general-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/113361096",

    "ACCOUNTING-general-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/114067836",

    "COMMERCE-general-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/113219748",

    "E-COMMERCE-general-2026" : "https://admissions.pu.edu.pk/admissions/show-merit-list/113573118"

}







for list_name , url in general_lists.items():

    try: 

        df=pd.read_html(url)
        print(f"loaded {list_name}")

        table=df[0]


        table.to_csv(f"data/{list_name}.csv" , index=False)
        print(f"saved {list_name}")
        

    except Exception as e:
        print(f"something went wrong with {list_name}")
        print(f"ERROR: {e}")






# def find_merit_table(tables):
#     print(len(tables))
#     for df in tables:
#         #converting coloumn names to lowercase
        
    
#         for col in df.columns:
#             print(col)
#             print("----------------")
            

#     return 




