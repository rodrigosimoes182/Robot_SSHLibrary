from SSHLibrary import SSHLibrary
def conecta_pi(localhost):
    ssh = SSHLibrary()
    x=ssh.open_connection("localhost",port=22)
    ssh.close_connection()
    return x