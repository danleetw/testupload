# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 13:34:13 2020

@author: danle
"""

import configparser
import base64
import os




class d_config():
    def __init__(self,configfilename):
        self.configfilename=configfilename
        print(configfilename)
        pass
    
    def encodeStr(self,estr):
        if isinstance(estr, (str,)):
           estr=estr
        else:
           estr=estr.decode('utf-8')
        
        ret=base64.b64encode(estr.encode('utf-8')).decode('utf-8')
        return ret
    def decodeStr(self,codestr):
        #print(codestr)
        resu=base64.b64decode(codestr)
        if isinstance(resu, (bytes,)):
           resu=resu.decode('utf-8') 
        return resu
    
    def read(self,info):
        config = configparser.ConfigParser()
        
        if os.path.exists(self.configfilename)==False:
           #print("TEST") 
           #input()
           self.save(info)
        
        with open(self.configfilename, mode='rb') as f:
            content = f.read()
            if content.startswith(b'\xef\xbb\xbf'):
                content=content[3:]
            config.read_string(content.decode('utf8'))
            
            for i in info:
                #print("para:",i,type(pgm_info[i]))
                if i[0:1]!="_":
                
                    if isinstance(info[i], (str,)):
                       try: 
                        if config['DEFAULT'].get(i,"")!="":
                           info[i]=config['DEFAULT'].get(i).replace("#百分比#","%")
                                   #print("Get Str:",pgm_info[i])
                           #input("Get Str")
                        else:
                           info[i]=""
                       except:  
                        err=1    
                        #print("Config2:",config['DEFAULT'][i])
                        
                        #pgm_info[i]=config['DEFAULT'].get[i]
                        #print(i,"=",pgm_info[i])
                    elif isinstance(info[i], (bool,)):    
                        #print(i,"=",config['DEFAULT'][i],type(pgm_info[i]))
                        #print("Config:",config['DEFAULT'].get(i),i)
                        try:
                            c=config['DEFAULT'].getboolean(i)
                            if c==True:
                                info[i]=True
                                #print("True")
                            #elif c==False:
                            #    print("False")
                            else:
                                #print("Other",c,type(c))
                                info[i]=False
                        except:
                            err=1        
                            #ccc
                        #boolstr=config['DEFAULT'][i].upper()
                        #if boolstr=="TRUE":
                        #    pgm_info[i]=True
                        #else:
                        #    pgm_info[i]=False
                        #print("Bool:","["+boolstr+"]")
                    elif isinstance(info[i], (int,)):  
                        print("INT",i)
                        #try:
                        if True:   
                            intstr=config['DEFAULT'].get(i,"")
                            #print("Get:",intstr)
                            #input("Get---")
                            if intstr.isdigit():
                               info[i]=int(intstr)
                               #print(pgm_info[i],type(pgm_info[i]))
                        #except:
                        #    print("ERR!!")
                        #    input("")
                        #    err=1
                    elif isinstance(info[i], (list,)):   
                         #try:
                         if True:    
                             liststr=decode(config['DEFAULT'].get(i,""))
                             if liststr=="":
                                info[i] =list()
                             else:   
                                
                                liststr=liststr[1:-1]
                                #print(liststr)
                                #input("A") 
                                listarr=liststr.split(",")
                                newlist=list()
                                for list_i in listarr:
                                    newlist.append(list_i.replace("'","").replace('"',"").strip())    
                                info[i]=newlist
                                #print(pgm_info[i])
                         #except:
                         #   err=1    
                         
                        
                    else:
                        print("!"*10,i,type(info[i]))
        return info                
    def save(self,info):
        config = configparser.ConfigParser()
        
        try:
           config.add_section("DEFAULT")
        #except configparser.DuplicateSectionError:
        except Exception as e:
            faile=1
        print("SAVE")
        for i in info:
            if i[0:1]!="_":
                #print(pgm_info[i],type(pgm_info[i]))
                if isinstance(info[i], str):
                #config.set("DEFAULT",'pgm_title',pgm_info['pgm_title'])
                    #print("str:=",pgm_info[i])
                    config.set("DEFAULT",i,info[i].replace("%","#百分比#"))
                    
                    #print(i,"===#",pgm_info[i],type(pgm_info[i]))
                if isinstance(info[i], (int,bool)):
                    config.set("DEFAULT",i,str(info[i]))
                    
                if isinstance(info[i], list):    
                   #print("En:",encodeStr(str(pgm_info[i]))) 
                   
                   config.set("DEFAULT",i,encode(str(info[i])))
  
        
        with open(self.configfilename, 'w',encoding='utf-8') as configfile:
          config.write(configfile)
        
        del config 