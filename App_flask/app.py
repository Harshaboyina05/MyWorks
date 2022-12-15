from flask import Flask, render_template, request, redirect
import os
app=Flask(__name__)
app.config["File_Uploads"]="/var/www/html/app_upload"
@app.route("/upload_file", methods=["GET","POST"])

def upload_file():

    if request.method=="POST":
        
        if request.files:
            
            upl_file1=request.files["file_uplserver"]

            upl_file2=request.files["file_uplserver2"]

            upl_file1.save(os.path.join(app.config["File_Uploads"],upl_file1.filename))
            upl_file2.save(os.path.join(app.config["File_Uploads"],upl_file2.filename))
            fname = "/var/www/html/app_upload/"+upl_file1.filename
            num_lines = 0
            with open(fname, 'r') as f:
                for line in f:
                    num_lines += 1
            print("Number of lines in file:  "+upl_file1.filename)
            print(num_lines)
            
            fname1= "/var/www/html/app_upload/"+upl_file2.filename
            num_lines = 0
            with open(fname1, 'r') as f:
                for line in f:
                    num_lines += 1
            print("Number of lines in file:  "+upl_file2.filename)
            print(num_lines)
            print("Files Uploaded successfully")
            return redirect(request.url)
    return render_template("/upload_file.html")
if __name__=="__main__":
    app.run()
    
