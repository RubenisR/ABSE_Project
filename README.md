# ABSE_Project
 
 First use this in terminal:
    
 pip install -r requirements.txt

 
 
 monailabel apps --name deepedit_left_atrium --download --output apps (this line downloads the app)

 monailabel start_server --app apps/radiology --studies "D:\Github\ABSE_Project\KneeDataset" --conf models deepedit (this line starts server where you need to put your local path for the dataset)
