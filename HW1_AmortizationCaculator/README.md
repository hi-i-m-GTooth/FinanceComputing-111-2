# HW1 - Amortization Caculator
## Description
Write a program to generate an amortization schedule for repaying a loan. There are **two interest rates**. 
### Inputs  
* `L` (loan amount in dollars) 
* `r1` (annual interest rate in percent for the first n1 periods, so 12 instead of 0.12)
* `r2` (annual interest rate in percent for the remaining periods)
* `n1` (number of periods when the interest rate is r1) 
* `n` (duration of the loan in years)
* `m` (the number of payments per annum)
### Output
A csv file for the amortization schedule and the total interest paid.  
The schedule shall have five columns: 
* `Time` (0, 1, 2, ...)
* `Payment`
* `Interest` (the interest part of each payment)
* `Principal` (the principal part of each payment)
* `Remaining principal` 
For example, if `L` = 10,000,000, `r1` = 8%, `r2` = 3%, `n1` = 120, `n` = 20, and `m` = 12.  
Please check the example output file [`amortization_2023.csv`](https://github.com/hi-i-m-GTooth/NTU-FC-111-2/blob/main/HW1_AmortizationCaculator/amortization_2023.csv) and the total interest is 8593339.37.
### Important notes
* The `Time` column must be integers (no floating-point numbers). 
* The `Payment`, `Interest`, `Principal`, and `Remaining principal` columns must be floating-point numbers up to 2 decimal points. 
* The order of the columns must be respected. 
* The headers of the columns must be as in the sample file. 
* Start from `Time 0` instead of `Time 1`. This means the value of the first row will be `0, 0, 0, 0, L`.
## Input format
Please refer to `1.in` for generating inputs. That is, `L r1 r2 n1 n m`.  
Note that you need to seperate those variables with spaces in one line.  
  
### Example
`10,000,000 8 3 120 20 12` or `10000000 8 3 120 20 12` are both available.

## Make amortization schedule
If your input is in `1.in`:
```
$ python amort.py < 1.in
```

If you enter data via standard input:
```
$ python amort.py
$ (Type your data)
```
