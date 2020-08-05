file_name = "application_data.csv"
file = open(file_name)

data = file.readlines()
print(data.pop(0))

for line in data:

    cols = line.split(',')

    (customerID,
    loanId,
    appilcationDate,
    LoanNumber,
    LoanAmount,
    InterestRate,
    TermDays,
    repaymentDueDate,
    repaymentPaidDate) = (cols[0],
                        cols[1],
                        cols[2],
                        cols[3],
                        cols[4],
                        cols[5],
                        cols[6],
                        cols[7],
                        cols[8])



    print(customerID)

    export


