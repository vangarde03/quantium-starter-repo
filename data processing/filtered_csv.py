import csv


writer = csv.writer(open('data processing/filtered_data.csv', 'w', newline=''))
file_num = 0
while file_num < 3:
    with open(f'data/daily_sales_data_{file_num}.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        if file_num == 0:
            writer.writerow(['Sales', 'Date', 'Region'])
        for row in csv_reader:
            if row[0] == 'pink morsel':
                priceWithoutDollarSign = float(row[1][1:])
                quantityInt = int(row[2])
                writer.writerow(
                    [quantityInt*priceWithoutDollarSign, row[3], row[4]])
                line_count += 1
        print(f'Processed {line_count} lines.')
    file_num += 1
