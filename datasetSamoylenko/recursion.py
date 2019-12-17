from dataset_structure import dataset
def er(dataset,a=0,keys_list=None):
    if keys_list==None:
        keys_list = list(dataset.keys())
        return func2(dataset,n,keys_list)
    if a==len(dataset):
        return
    if dataset[keys_list[a]]["percent_of_benefciaries_with_cancer"]>20 and dataset[keys_list[a]]["percent_of_beneficiaries_with_chf"]> 10 :
        for elements in dataset[keys_list[a]]:
            print(elements + ' - '+ str(dataset[keys_list[a]][elements]))
    er(dataset,a+1,keys_list)
