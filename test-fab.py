
import fabric
from fabric.api import env , run, roles, cd, settings


env.hosts = ['192.168.8.85', '127.0.0.1']
env.user = 'deepak'
USERS = ['deepak', 'deepak']
CODE_DIR = '/home'
APP_CODE_DIR = '/web/'


#@env.hosts
def fetch_code():
    for user1 in USERS:
        print "1"
        print user1
#         with cd("/home/%s/amber" %user1):
        with settings(sudo_user=("%s" %user1),disable_known_hosts=True):
            print "2"
            print user1
#            GIT_URL = 'https://deepak7093:19d6f00500362a0aabca1bffac66b59a0d790667@github.com/deepak7093/hello-world.git'
#                if run("test -d %s/%s/amber" %(CODE_DIR, user1)).failed:
#                     run("git clone %s" %GIT_URL)
#                else:
            with cd("/home/%s/amber" %user1):
                print "3"
                run("git pull")
        

def compile_code():
    for user in USERS:
        with cd("/home/%s/amber/java/common" %user):
            run("ant")

#def restart_resin():










