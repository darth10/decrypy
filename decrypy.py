# -*- coding: utf-8 -*-
"""

@author:  Akhil Wali
"""

from operator import xor

class YDecryptor:
    '''a wrapper for functions to decrypt Yahoo messenger archives'''
    def __init__(self,fileName,localhandle,remotehandle):
	'''constructor; fileName is the archive file, and localhandle and remotehandle are the usernames'''
        self.file=fileName
        self.__luser=localhandle
        self.__ruser=remotehandle
        self.handle=[ord(i) for i in localhandle]
        self.__hlen=len(self.handle)
        self.datalists=[]
        self.messages=[]
    
    def __containsAny(self,string,set):
        '''checks for set in string'''
        return True in [c in string for c in set ]
        
    def getMessages(self):
        '''returns a dictionary of messages from the archive file'''
        yfile=open(self.file,'rb')
        specs="""~`!@#$%^&*()_+-=[]{}\|;:'",<.>/?"""
        
        try:	
            while True:
                header=yfile.read(16)
                rlen=ord(header[12])
                payload=yfile.read(rlen)
                pad=yfile.read(4)
                dlist = [ord(i) for i in header];plist=[ord(i) for i in payload]
                self.datalists.append((dlist,rlen,payload))
        except IndexError:
            '''end of file'''
            pass
        finally:
            yfile.close()

        for i in self.datalists:
            sr = 'sent' if i[0][8]==0 else 'recieved'
            ts = i[0][0:5];encmesg=i[2]
	
            '''TODO:process timestamp here'''

            '''decrypt payload'''
            msgchars=[]
            for j in range(0,len(encmesg)):
                k = j if j<self.__hlen else j%self.__hlen
                msgchars.append(xor(ord(encmesg[j]),self.handle[k]))
		
            '''TODO:check for unreadable chars'''
            self.messages.append({'sr':self.__ruser if sr=='recieved' else self.__luser,\
				      'timestamp':ts,'message':("".join([chr(k) for k in msgchars]))})
            
        #check for unreadable text
        #on else return messages
        flag=False
        for i in self.messages:
            if i['message'].isalnum() or self.__containsAny(i['message'],specs):
                flag=True
        # NOT WORKING
        
        if flag==True:    
            return self.messages
        else:
            return False

