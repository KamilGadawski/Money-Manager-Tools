import pandas as pd

FILE_NAME = 'amount.csv'

amount_file = pd.read_csv(FILE_NAME)

category = list(set(amount_file['Category']))  # read all categories

amount_file['Amount'] = amount_file['Amount'].abs()
amount = amount_file["Amount"].sum().round(2)

print('Expenses from the beginning of the year:')
for cat in category:
    cat_sum = amount_file.loc[amount_file['Category'] == f'{cat}', 'Amount'].abs().sum().round(2)
    print(f'{cat}: {cat_sum}')
print('##############')
print(f'All: {amount}')