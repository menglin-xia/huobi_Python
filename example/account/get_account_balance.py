from huobi.client.account import AccountClient
from huobi.constant import *
from huobi.utils import LogInfo
from config import *

if __name__ =="__main__":
    account_client = AccountClient(api_key=g_api_key,
                                   secret_key=g_secret_key)
    LogInfo.output("====== (SDK encapsulated api) not recommend for low performance and frequence limitation ======")
    account_balance_list = account_client.get_account_balance()
    if account_balance_list and len(account_balance_list):
        for account_obj in account_balance_list:
            for i in range(len(account_obj.list)):
                if float(account_obj.list[i].balance)>0:
                    print('Currency: ',account_obj.list[i].currency)
                    print('Balance: ', account_obj.list[i].balance)
                    print('Type: ', account_obj.list[i].type)
                    # account_obj.print_object()
                    print()