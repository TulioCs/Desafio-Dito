import requests
import json

r = requests.get('https://storage.googleapis.com/dito-questions/events.json')
data = r.json()
events = data['events']


def get_info_compras():
    '''
    Description:
        This is a function responsible for returning a shopping list grouped by id.
        and sorted by the timestamp field

    Use:
        get_info_compras()

    Parameters:
        without parameters

    '''

    comprou = [item for item in events if (item['event'] == 'comprou')]

    # store buy details
    buys = []

    customData = [item['custom_data'] for item in comprou]

    for x in range(len(comprou)):
        transaction_id, store_name = get_customData(x, customData)
        products = get_produtos_compra(transaction_id)
        buys.append(
            {"timestamp": comprou[x]['timestamp'], "revenue": comprou[x]['revenue'], "transaction_id": transaction_id, "store_name": store_name, "products": products})

    buys = sorted(buys, key=lambda k: k['timestamp'], reverse=True)

    return buys


def get_produtos_compra(id):
    '''
    Description:
        Function responsible for searching all products of a transaction.
    Use:
      get_produtos_compras()

    Parameters:
        Transaction ID from which to search for products.

    '''
    # name product
    name = ""

    # price product
    price = ""

    # product list
    products = []

    buyProduct = [item for item in events if (
        item['event'] == 'comprou-produto')]
    customData = [item['custom_data'] for item in buyProduct]
    for i in range(len(customData)):
        for j in range(len(customData[i])):
            if((customData[i][j]['key'] == 'transaction_id') and (customData[i][j]['value'] == id)):
                for x in range(len(customData[i])):
                    if (customData[i][x]['key'] == 'product_name'):
                        name = customData[i][x]['value']
                    if (customData[i][x]['key'] == 'product_price'):
                        price = customData[i][x]['value']
                products.append({"name": name, "price": price})

    return products


def get_customData(pos, customData):
    '''
    Description:
    Function responsible for returning the transaction ID and the store where a product was purchased.
    Use:
      get_customData(param1, param2)

    Parameters:
        param1
            position of the constomData list you want to extract the information
        param2
            list containing purchase information
    '''
    trasactionId = ""
    storeName = ""
    for x in range(len(customData[pos])):
        if (customData[pos][x]['key'] == 'transaction_id'):
            trasactionId = customData[pos][x]['value']
        if (customData[pos][x]['key'] == 'store_name'):
            storeName = customData[pos][x]['value']
    return(trasactionId, storeName)


def main():

    buys = get_info_compras()

    timeline = {"timeline": buys}

    print(json.dumps(timeline, indent=4, sort_keys=False, ensure_ascii=False))


if __name__ == "__main__":
    main()
