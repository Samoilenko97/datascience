from dataset_structure import dataset
from test import *
def dataset_insert(dataset, provider_id, data, keys_list):
    new_data = dict(zip(keys_list, data))
    dataset.update({provider_id: new_data})
provider_id = '80000'
n = input("Введите название штата: ")
b = input("Введите процент заболевших раком: ")
c = input("Введите процет заболевших сердечнососудистыми заболеваниями: ")
data = [n, b, c]
keys_list = ["state", "percent_of_beneficiaries_with_cancer", "percent_of_beneficiaries_with_chf"]
dataset_insert(dataset, provider_id, data, keys_list)
print(dataset)