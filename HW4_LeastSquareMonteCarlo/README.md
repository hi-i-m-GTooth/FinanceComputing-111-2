# HW3 - Down-and-out Barrier Call
## Description
Write a trinomial tree program to price a down-and-out barrier call.
### Inputs
(1) `S` (stock price)  
(2) `K` (strike price)  
(3) `r` (interest rate)  
(4) `s` (annual volatility)  
(5) `T` (time to maturity in years)  
(6) `n` (number of time steps)  
(7) `N` (number of simulation paths)  
### Outputs
`Option price` & `Standand error`

### Example
No example is avalable. Follow the [slide](https://www.csie.ntu.edu.tw/~lyuu/finance1/2023/20230512.pdf), in `main.py`, you could set `use_init` to `True`, `degree` to `2` to reproduce the example, which should be `4.66263`, in the course.

### Important notes
* The interest rate and volatility should be in percent. For example, if the interest rate is 5% and volatility 30%, the inputs are 5 and 30, respectively. 

### Submmit format
* Please send your source code, executable code, and a brief explanation file if necessary (e.g., how to run it?) using NTU COOL before 08:00 AM of June 9, 2023. No late submissions will be accepted.
* Compress your files into a single file and name it **StudentID_HW_4** for easy reference.

## Input format
Please refer to 1.in for generating inputs. That is, `S K r s T n N`.  
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

