class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        self.store = [None for _ in range(16)]

    def get(self, key):
        index = hash(key) & 15
        if self.store[index] is None:
            return None
        n = self.store[index]
        while True:
            if n.key == key:
                return n.value
            else:
                if n.next:
                    n = n.next
                else:
                    return None

    def put(self, key, value):
        nd = Node(key, value)
        index = hash(key) & 15
        n = self.store[index]
        if n is None:
            self.store[index] = nd
        else:
            if n.key == key:
                n.value = value
            else:
                while n.next:
                    if n.key == key:
                        n.value = value
                        return
                    else:
                        n = n.next
                n.next = nd


file = open("file.txt", "r")
em = HashMap()
cus = HashMap()
bal = HashMap()

# while True:
#     data = file.readline()
for data in file:
    if len(data) == 0:
        pass

    if data.startswith('e'):
        employee_data = data.split()
        # employee = {'e_id': employee_data[1], 'e_name': employee_data[2]}
        # print(employee['e_id'], employee['e_name'])
        em.put(employee_data[1], employee_data[2])

    if data.startswith('c'):
        customer_data = data.split()
        # customer = {'c_id': customer_data[1], 'c_name': customer_data[2], 'c_balance': customer_data[3]}
        # print(customer['c_id'], customer['c_name'], customer['c_balance'])
        # print(customer[5])
        cus.put(customer_data[1], customer_data[2])
        bal.put(customer_data[1], customer_data[3])

    if data.startswith('t'):
        transaction_data = data.split()
        # transaction = {'c_id': transaction_data[1], 'e_id': transaction_data[2], 'amount': transaction_data[4]}
        tc_id = transaction_data[1]
        te_id = transaction_data[2]
        amount = float(transaction_data[4])

        if transaction_data[3] == 'w':
            c_name = cus.get(tc_id)
            e_name = em.get(te_id)
            balance = float(bal.get(tc_id))
            remaining_balance = float(balance - amount)
            print(f'{c_name} {e_name} -${amount} ${remaining_balance}')
        else:
            c_name = cus.get(tc_id)
            e_name = em.get(te_id)
            balance = float(bal.get(tc_id))
            remaining_balance = float(balance + amount)
            print(f'{c_name} {e_name} +${amount} ${remaining_balance}')

