# HW2 - Down-and-out Barrier Call
## Description
Write a trinomial tree program to price a down-and-out barrier call.
### Inputs
(1) `S` (stock price)  
(2) `K` (strike price)  
(3) `r` (interest rate)  
(4) `s` (annual volatility)  
(5) `T` (time to maturity in years)  
(6) `H` (barrier)  
(7) `n` (number of time steps)  
### Outputs
`Option price` 

### Example
suppose that `S` = 95, `K` = 100, `r` = 10 (%), `s` = 25 (%), `H` = 90, and `T` = 1. The `option price` is about 5.9899 at `n` = 75 and 5.9977 at `n` = 400.

### Important notes
* The interest rate and volatility should be in percent. For example, if the interest rate is 5% and volatility 30%, the inputs are 5 and 30, respectively. 
* The trinomial tree must matches the barrier
### Submmit format
* Please send your source code, executable code, and a brief explanation file if necessary (e.g., how to run it?) using NTU COOL before 08:00 AM of May 12, 2023. No late submissions will be accepted. 
* Compress your files into a single file and name it **StudentID_HW_3** for easy reference.  

## Input format
Please refer to 1.in for generating inputs. That is, `S K r s T H n`.  
Note that you need to seperate those variables with spaces in one line.

## Execution
If your input is in `1.in`, run:
```bash
$ python main.py < 1.in
```
If you enter data via standard input:
```
$ python main.py
$ (Type your data)
```

