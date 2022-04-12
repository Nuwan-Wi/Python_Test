class Mother:
    msg_m = 'I am mother.'
    money=1250

class Doughter(Mother):
    msg_d='I am doughter.'

msg=Doughter()

print(msg.msg_m)
print(msg.msg_d)