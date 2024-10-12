import schedule 
import time 
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import smtplib 
import os 
  
def message(subject="Python Notification",  
            text="", img=None, attachment=None): 
    
    msg = MIMEMultipart() 
      
    msg['Subject'] = subject   
      
    
    msg.attach(MIMEText(text))   
  

    if img is not None: 
  
         
        if type(img) is not list: 
            
            
            img = [img]   
  
        
        for one_img in img: 
            
              
            img_data = open(one_img, 'rb').read()   
              
            
            msg.attach(MIMEImage(img_data,  
                                 name=os.path.basename(one_img))) 
  
    
    if attachment is not None: 
  
          
        if type(attachment) is not list: 
            
              
            attachment = [attachment]   
  
        for one_attachment in attachment: 
  
            with open(one_attachment, 'rb') as f: 
                
                
                file = MIMEApplication( 
                    f.read(), 
                    name=os.path.basename(one_attachment) 
                ) 
            file['Content-Disposition'] = f'attachment;\ 
            filename="{os.path.basename(one_attachment)}"' 
              
            
            msg.attach(file) 
    return msg 
  
  
def mail(): 
    
    
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 
    smtp.ehlo() 
    smtp.starttls() 
      
    
    smtp.login('mfreire1996@gmail.com', 'Kk@6jJ/X-Y') 
  
    
    msg = message("Good!", "Hi there!", 
                  r"C:\Users\Dell\Downloads\Garbage\Cartoon.jpg", 
                  r"C:\Users\Dell\Desktop\slack.py") 
      
    
    to = ["ABC@gmail.com", 
          "XYZ@gmail.com", "insaaf@gmail.com"] 
  
    
    smtp.sendmail(from_addr="hello@gmail.com", 
                  to_addrs=to, msg=msg.as_string()) 
      
   
    smtp.quit()   
  
  
schedule.every(2).seconds.do(mail) 
schedule.every(10).minutes.do(mail) 
schedule.every().hour.do(mail) 
schedule.every().day.at("10:30").do(mail) 
schedule.every(5).to(10).minutes.do(mail) 
schedule.every().monday.do(mail) 
schedule.every().wednesday.at("13:15").do(mail) 
schedule.every().minute.at(":17").do(mail) 
  
while True: 
    schedule.run_pending() 
    time.sleep(1)