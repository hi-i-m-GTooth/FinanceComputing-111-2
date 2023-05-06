# HW2 - Bermudan Option
## Description
Write a binomial tree program to price a Bermudan option. The early exercise time points are T/4 and 3T/4 from now, where T is the time to maturity. The payoff function is max(K - S + 1,0). 
### Inputs
(1) `S` (stock price)  
(2) `K` (strike price)  
(3) `r` (annual interest rate continuously compounded)  
(4) `s` (annual volatility)  
(5) `T` (time to maturity in years)  
(6) `n` (number of time steps)  
### Outputs
Option price. 

### Example
suppose that S = 100, K = 100, r = 5 (%), s = 30 (%), and T = 0.5 (years). The option price is about 7.8052 at n = 100 and 7.8015 at n = 200. 

### Important notes
* The interest rate and volatility should be in percent. For example, if the interest rate is 5% and volatility 30%, the inputs are 5 and 30, respectively. 
* No need to make sure the early exercise dates are aligned with time steps of the tree. 
### Submmit format
* Please send your source code, executable code, and a brief explanation file if necessary (e.g., how to run it?) using NTU COOL before 08:00 AM of April 14, 2022. No late submissions will be accepted. 
* Compress your files into a single file and name it StudentID_HW_2 for easy reference.  

## Input format
Please refer to 1.in for generating inputs. That is, `S K r s T n`.  
Note that you need to seperate those variables with spaces in one line.

## Execution
If your input is in `1.in`, run:
```bash
$ python bermudan.py < 1.in
```
If you enter data via standard input:
```
$ python bermudan.py
$ (Type your data)
```

