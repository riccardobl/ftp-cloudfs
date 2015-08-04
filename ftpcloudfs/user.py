# -*- coding: utf-8 -*-

class User:
    _FTP_USER=None
    _FTP_PASSWORD=None
    _SWIFT_TENANT=None
    _SWIFT_USERNAME=None
    _SWIFT_PASSWORD=None

    def __init__(self, ftp_user,ftp_password,swift_tennant, swift_username,swift_password):
        self._FTP_USER=ftp_user
        self._FTP_PASSWORD=ftp_password
        self._SWIFT_TENANT=swift_tennant
        self._SWIFT_USERNAME=swift_username
        self._SWIFT_PASSWORD=swift_password
        
    def getFtpUser(self):
        return self._FTP_USER
    
    def getFtpPassword(self):
        return self._FTP_PASSWORD
    
    def getSwiftTenant(self):
        return self._SWIFT_TENANT
    
    def getSwiftUsername(self):
        return self._SWIFT_USERNAME
    
    def getSwiftPassword(self):
        return self._SWIFT_PASSWORD

