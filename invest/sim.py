import sys

variables = {
    'salary' : 45*(10**3),
    'salary_tax'  : 0.3,
    'option_tax'  : 0.28,
    'base_salary' : 120*(10**3),
    'base_salary_tax'  : 0.45,
    'years_to_sale' : 3,
    'mill':10**6
}

senarios = [
    ('worstcase', 20), 
    ('likely', 45), 
    ('bestcase', 100), 
]

def human_format(num):
    prefix, magnitude = "", 0

    if num < 0:
        prefix = "-"
        num = num *-1

    while num >= 1000: 
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    suffixes = ['', 'K', 'M', 'G', 'T', 'P']
    try:
        s = suffixes[magnitude]
    except Exception e:   #This maybe the list key error
        raise Exception("The number: %s was so big we've run out of human readable suffixes: %s" %(num, suffixes))

    return  '%s%.2f%s' % (prefix, num, s)


if __name__ == '__main__':
    if len(sys.argv)>1:
        arg = sys.argv[1]
        option_pcent = float(arg)
    else:
        option_pcent = 0.5
    pcent = (option_pcent*1.0)/100
    
    multi = variables['mill']
    option_tax = variables['option_tax']
    
    compare = variables['years_to_sale'] * (variables['base_salary'] * (1-variables['base_salary_tax']))
    
    print ""
    print "SALARY COMPARISON FOR %s PERCENT OWNERSHIP" % option_pcent
    print "Your comparison is a take home of %s" % human_format(compare)
    print ""
    
    for s, val in senarios:
        stake =  (val * multi) * pcent
        take_home = stake * (1-option_tax)
        print "***** For senario: %s (%s million) *****" % (s, val)
        print "Your stake is %s and take home is %s" % (human_format(stake), human_format(take_home))
        full_take_home = take_home + (variables['years_to_sale'] * (variables['salary'] * (1 - variables['salary_tax'])) )
        print "With the base salary this is %s (%s vs a comparison)" % (human_format(full_take_home),  human_format(full_take_home-compare))
        print ""

        