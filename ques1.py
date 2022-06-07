
if __name__=='__main__':
    try:
        with open('example.txt','r+') as f:
            file_text = f.read()
            new_text = file_text.replace('placement','screening')
            f.seek(0)
            f.write(new_text)
            f.truncate()
    except Exception as e:
        print("Error occured while making modifications to file: "+str(e))