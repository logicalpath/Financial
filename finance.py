import sys
import numpy_financial as npf
# help(npf.fv)



def futureV(rate, nper, pmt, pv, when='end'):
    return npf.fv(rate, nper, pmt, pv)




def main(args=None):
    if args is None:
        args = sys.argv[1:]
    # From _financial.py:
    # What is the future value after 10 years of saving $100 now, with
    # an additional monthly savings of $100.  Assume the interest rate is
    # 5% (annually) compounded monthly?

    # rate: Rate of interest as decimal (not per cent) per period
    # nper: Number of compounding periods
    # pmt: Payment (annuity) made each period
    # pv: Present value
    # when: When payments are due ('begin' (default), 'end')
    
    # amt = futureV(rate=0.05/12, nper=10*12, pmt=-100, pv=-100, when='end')

    amt = futureV(rate=0.05/12, nper=10*12, pmt=-3500, pv=-2000, when='end')

    print(f'Future value is {amt:.2f}')

if __name__ == "__main__":
    main()

    
