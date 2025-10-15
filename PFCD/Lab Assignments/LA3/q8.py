def no_of_days(s):
    s = s.lower()
    if s=='february':
        print('28/29 days')
    elif s=='april' or s=='june' or s=='september' or s=='november':
        print('30 days')
    elif s=='january' or s=='march' or s=='may' or s=='july' or s=='august' or s=='october' or s=='december':
        print('31 days')
    else:
        print('Invalid')

s = input()
no_of_days(s)