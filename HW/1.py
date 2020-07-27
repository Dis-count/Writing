from scipy.stats import norm
# cumulative function
norm.cdf(0)
# density function
norm.pdf(0.05)
# inverse function
norm.ppf(0.5)

def my_pdf(num):
    N_num = (num-1000)/200
    return norm.pdf(N_num)

my_pdf(990)

def my_cdf(num):
    N_num = (num-1000)/200
    return norm.cdf(N_num)

my_cdf(990)

def ff(num):
    mynum = 0.99*num
    I = my_cdf(mynum)+my_pdf(mynum)-1
    V = 200*I + mynum*(1- my_cdf(mynum))
    f = mynum*my_cdf(mynum) + V
    return f

ff(916.5)
