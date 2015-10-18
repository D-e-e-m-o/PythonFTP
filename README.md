Python FTP server
=========================
支持添加用户名、密码、修改用户权限

    Read permissions:

    "e" = change directory (CWD, CDUP commands)
    "l" = list files (LIST, NLST, STAT, MLSD, MLST, SIZE commands)
    "r" = retrieve file from the server (RETR command)

    Write permissions:

    "a" = append data to an existing file (APPE command)
    "d" = delete file or directory (DELE, RMD commands)
    "f" = rename file or directory (RNFR, RNTO commands)
    "m" = create directory (MKD command)
    "w" = store a file to the server (STOR, STOU commands)
    "M" = change mode/permission (SITE CHMOD command) New in 0.7.0

ftps目前无法使用

使用前请以管理员权限运行`install_module.sh`文件安装必须的模块，并保证你的电脑上python版本>=2.7

不过，本人为了测试，使用了python3.5
