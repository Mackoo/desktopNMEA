# -*- coding: utf-8 -*-
"""
/***************************************************************************
 nmea_main
                                 A QGIS plugin
 load nmea file to qgis
                              -------------------
        begin                : 2013-05-11
        copyright            : (C) 2013 by Maciej Olszewski
        email                : mackoo@opoczta.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from nmea_dialog import nmea_Dialog,nmea_mainDialog,nmea_settDialog
import datetime, time,os,string,numpy,sys
from pyspatialite import dbapi2 as db #Load PySpatiaLite
import time

class nmea_main:

    def __init__(self):
        # Create the dialog (after translation) and keep reference
        self.dlg = nmea_mainDialog()
        self.dlg2=nmea_Dialog()
        self.dlg3=nmea_settDialog()
        self.dlg.show()
        self.fd = QFileDialog()
        self.fd1 = QFileDialog()
        settings=QSettings()
        dir=settings.value('/nmea2dbqgis/dir', QVariant('C:\Users')).toString()
        #self.fd.setDirectory("C:\Users\Maciek\Documents\GIG\magisterka\STD Oszczak\praca_mag")
     
        self.fd.setDirectory(dir)
        
        
        
        QObject.connect(self.dlg.ui.pushButton,SIGNAL("clicked()"), self.dialog)
        QObject.connect(self.dlg.ui.ButOpenNmea,SIGNAL("clicked()"), self.openNmea)
        QObject.connect(self.dlg.ui.ButExit,SIGNAL("clicked()"), self.exit)
        QObject.connect(self.dlg.ui.addBut,SIGNAL("clicked()"), self.addLayer)
        QObject.connect(self.dlg.ui.settBut,SIGNAL("clicked()"), self.sett)
        

      
        QObject.connect(self.dlg2.ui.mat1Combo,SIGNAL("currentIndexChanged(int)"), self.chmat1)
        QObject.connect(self.dlg2.ui.mat2Combo,SIGNAL("currentIndexChanged(int)"), self.chmat2)
         
    def dialog(self):
        self.filename = self.fd.getOpenFileName()
        from os.path import isfile
        if isfile(self.filename):
            self.dlg.ui.lineEdit.setText(self.filename)
            settings=QSettings()
            settings.setValue('/nmea2qgis/dir',QVariant(self.filename))
            self.fd.setDirectory(os.path.dirname(str(self.filename)))

            
    def exit(self):    
        self.dlg.close()
        self.dlg.ui.lineEdit.setText("")
        
    def changeCombo(self):
        if self.dlg2.ui.saveCheck.isChecked():  
            self.dlg2.ui.formatCombo.setEnabled(True) 
        else:   
            self.dlg2.ui.formatCombo.setEnabled(False) 
            
    def sett(self):
        self.dlg3.show()
      
        
        
        
      
    def openNmea(self):
        self.nmeadoc=QTextDocument()
        self.nmeacur=QTextCursor(self.nmeadoc)
        #try:
        self.nmeafile=open(self.dlg.ui.lineEdit.text()) 
       
        self.nmeaDict(self.nmeafile,1)
        self.dlg2.ui.nmeaBrowser.setDocument(self.nmeadoc)
        self.plotmat()

        self.dlg2.show() 
            
        #except:
            #QMessageBox.information(self.iface.mainWindow(), "Info", "Cannot open nmea file")

        
    def addLayer(self):
        #try:
            nmeafile=open(self.dlg.ui.lineEdit.text()) 
            self.nmeaDict(nmeafile,0)
            #self.addSave()
        #except:
            #QMessageBox.information(self.iface.mainWindow(), "Info", "Cannot open nmea file")

    def nmeaDict(self,nmeafile,insert):
        
        start=time.time()
        
        try:
            self.connectionObject=db.connect('C:\Users\Maciek\Documents\GIG\magisterka\STD Oszczak\praca_mag\dbnmea.sqlite')
            #QMessageBox.critical(self.iface.mainWindow(), 'info', 'connected to database')
        except:
            pass
            #QMessageBox.critical(self.iface.mainWindow(), 'info', 'cannot connect to database')
          
        nmeafile.seek(0)
        
        for line in nmeafile:
             #if insert==1: 
                 #self.nmeacur.insertText(line)
             linee=line.split(',')
             if line[3:6]=='GGA' or line[3:6]=='RMC':
                 cur=self.connectionObject.cursor()
                 key=linee[1][:2]+':'+linee[1][2:4]+':'+linee[1][4:6]
                 qu="""insert or ignore into nmea2GGA(utc) values('"""+key+"""')"""
                 #QMessageBox.information(self.iface.mainWindow(), 'inff', qu)
                 cur.execute(qu)
                 
             if line[3:6]=='GLL':
                 cur=self.connectionObject.cursor()
                 key=linee[5][:2]+':'+linee[5][2:4]+':'+linee[5][4:6]
                 qu="""insert or ignore into nmea2GGA(utc) values('"""+key+"""')"""
                 #QMessageBox.information(self.iface.mainWindow(), 'inff2', qu)
                 cur.execute(qu)
        self.connectionObject.commit()
        
        nmeafile.seek(0)
        for line in nmeafile:
            if line.startswith('$'):
                try:
                    parser={'GGA':self.par_gga,'RMC':self.par_rmc,'GLL':self.par_gll}[line[3:6]]
                    #QMessageBox.information(self.iface.mainWindow(), 'info', line[3:6])
                    parser(line)
                except:
                    #QMessageBox.critical(self.iface.mainWindow(), 'info', line)
                    continue
        self.connectionObject.commit()
        end=time.time()
       
        nmeafile.close() 
        self.dlg.close() 
        

    

        
        
    def plotmat(self):
        self.dates=[]
        try:
            self.connectionObject=db.connect('C:\Users\Maciek\Documents\GIG\magisterka\STD Oszczak\praca_mag\dbnmea.sqlite')
            #QMessageBox.critical(self.iface.mainWindow(), 'info', 'connected to database')
        except:
            pass
        
        cur=self.connectionObject.cursor()    
        data=self.dlg2.ui.mat1Combo.currentText()
        data2=self.dlg2.ui.mat2Combo.currentText()
        #qu="""select """+data+""","""+data2+""" from nmea2GGA"""
        qu1="""select utc from nmea2GGA"""
        cur.execute(str(qu1))
        dates=cur.fetchall()
        for date in dates:
            self.dates.append(datetime.datetime.strptime(date[0],'%H:%M:%S'))
            print date
        qu2="""select """+data+""","""+data2+""" from nmea2GGA"""
        print str(qu2)
        cur.execute(str(qu2))
        results=cur.fetchall()
        print results
        self.connectionObject.commit()
    
        uu=[]
        vv=[]
        for uv in results:
            
            uu.append(uv[0])
            vv.append(uv[1])
    
        self.dlg2.ui.matplot1.canvas.ax1.cla()
        self.dlg2.ui.matplot1.canvas.ax2.cla()
        self.dlg2.ui.matplot1.canvas.ax1.vlines(self.dates,0,uu,lw=5,rasterized=True)
        #self.dlg2.ui.matplot1.canvas.ax1.bar(self.dates,self.oy1)
        self.dlg2.ui.matplot1.canvas.ax1.xaxis_date()
        self.dlg2.ui.matplot1.canvas.ax2.vlines(self.dates,0,vv,lw=5,rasterized=True)
        #self.dlg2.ui.matplot1.canvas.ax2.bar(self.dates,self.oy1)
        self.dlg2.ui.matplot1.canvas.ax2.xaxis_date()
        self.dlg2.ui.matplot1.canvas.fig.autofmt_xdate()
        self.dlg2.ui.matplot1.canvas.draw()  
        
        
        
    def chmat1(self):
        cur=self.connectionObject.cursor()  
        qu="""select """+self.dlg2.ui.mat1Combo.currentText()+""" from nmea2GGA"""
        cur.execute(str(qu))
        results=cur.fetchall()
        
        self.dlg2.ui.matplot1.canvas.ax1.cla()
        self.dlg2.ui.matplot1.canvas.ax1.vlines(self.dates,0,results,lw=5,rasterized=True) 
        #self.dlg2.ui.matplot1.canvas.ax1.xaxis_date()
        self.dlg2.ui.matplot1.canvas.ax1.grid(True)
        self.dlg2.ui.matplot1.canvas.fig.autofmt_xdate()
        self.dlg2.ui.matplot1.canvas.draw()
        
    def chmat2(self):
        cur=self.connectionObject.cursor()  
        qu="""select """+self.dlg2.ui.mat2Combo.currentText()+""" from nmea2GGA"""
        cur.execute(str(qu))
        results=cur.fetchall()
        
        self.dlg2.ui.matplot1.canvas.ax2.cla()
        self.dlg2.ui.matplot1.canvas.ax2.vlines(self.dates,0,results,lw=5,rasterized=True) 
        #self.dlg2.ui.matplot1.canvas.ax2.xaxis_date()
        self.dlg2.ui.matplot1.canvas.ax2.grid(True)
        self.dlg2.ui.matplot1.canvas.fig.autofmt_xdate()
        self.dlg2.ui.matplot1.canvas.draw()
        
        
    def par_gga(self,line):
        
        data=[]
        data=line.split(',')
        key=data[1]
        utc=data[1][:2]+':'+data[1][2:4]+':'+data[1][4:6]
        latt=float(data[2][:2])+float(data[2][2:])/60
        ind=string.find(data[4],".")
        lonn=float(data[4][:(ind-2)])+float(data[4][(ind-2):])/60
        numsv=data[7]
        hdop=data[8]
        msl=data[9]
        geoid=data[11]
        fixstatus=data[6]
        #query="""insert into nmeaGGA(utc,lat,lon,fixstatus,numsv,dop,msl,geoid,geometry) values('"""+utc+"""',"""+str(latt)+""","""+str(lonn)+""","""+str(fixstatus)+""","""+str(numsv)+""","""+str(hdop)+""","""+str(msl)+""","""+str(geoid)+""",GeomFromText('POINT("""+str(latt)+""" """+str(lonn)+""")',4326));"""
        #query="""insert into nmeaGGA(utc,lat,lon,fixstatus,numsv,dop,msl,geoid) values('"""+utc+"""',"""+str(latt)+""","""+str(lonn)+""","""+str(fixstatus)+""","""+str(numsv)+""","""+str(hdop)+""","""+str(msl)+""","""+str(geoid)+""");"""

        query="""update nmea2GGA set lat="""+str(latt)+""",lon="""+str(lonn)+""",fixstatus="""+str(fixstatus)+""",numsv="""+str(numsv)+""",dop="""+str(hdop)+""",msl="""+str(msl)+""",geoid="""+str(geoid)+""" where utc='"""+utc+"""';"""
        #QMessageBox.information(self.iface.mainWindow(), 'info', query)
        
        cursor=self.connectionObject.cursor()  
        cursor.execute(query)
        #self.connectionObject.commit()

    def par_rmc(self,line):  
        data=[]
        data=line.split(',')
        key=data[1]
        utc=data[1][:2]+':'+data[1][2:4]+':'+data[1][4:6]
        latt=float(data[3][:2])+float(data[3][2:])/60
        ind=string.find(data[5],".")
        lonn=float(data[5][:(ind-2)])+float(data[5][(ind-2):])/60
        speed=data[7]
        datastatus=data[2]
        
        query="""update nmea2GGA set lat="""+str(latt)+""",lon="""+str(lonn)+""",speed="""+str(speed)+""",datastatus='"""+str(datastatus)+"""' where utc='"""+utc+"""';"""
        #QMessageBox.information(self.iface.mainWindow(), 'info', query)
        
        cursor=self.connectionObject.cursor()  
        cursor.execute(query)   
        
        
    def par_gll(self,line):  
        data=[]
        data=line.split(',')
        key=data[5]
        utc=data[5][:2]+':'+data[5][2:4]+':'+data[5][4:6]
        latt=float(data[1][:2])+float(data[1][2:])/60
        ind=string.find(data[3],".")
        lonn=float(data[3][:(ind-2)])+float(data[3][(ind-2):])/60
        datastatus=data[6]
        query="""update nmea2GGA set lat="""+str(latt)+""",lon="""+str(lonn)+""",datastatus='"""+str(datastatus)+"""' where utc='"""+utc+"""';"""
        #QMessageBox.information(self.iface.mainWindow(), 'info', query)
        
        cursor=self.connectionObject.cursor()  
        cursor.execute(query) 
        
    def ggaOnly(self):
        lines = unicode(self.dlg2.ui.nmeaBrowser.toPlainText()).split('\n')
        nmeadocc=QTextDocument()
        nmeacurr=QTextCursor(nmeadocc)
        self.dlg2.ui.nmeaBrowser.clear()
        
        #formm=QTextCharFormat()
        #brus=QBrush()
        #brus.setColor(Qt.red)
        #formm.setBackground(brus)
        #formm.setForeground(brus)
        #formm.setFontItalic(True)
        for linee in lines:
            #QMessageBox.information( self.iface.mainWindow(),"Info", linee )
            if linee.startswith('$GPGGA'):
                nmeacurr.insertText(linee)
   
        self.dlg2.ui.nmeaBrowser.setDocument(nmeadocc)      




app=QApplication(sys.argv)
dialogg=nmea_main()
#form=dialogg.dlg()
#form.show()
app.exec_()


