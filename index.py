import json

def load_data():
   try:
      with open("youtube.txt","r") as file:
        return json.load(file)
   except FileNotFoundError:
      return []
      
   
def save_data(videos):
    with open("youtube.txt","w") as file:
       json.dump(videos,file)
       

def list_All_Videos(videos):
    for index, video in enumerate(videos,start=1):
       print(f"{index}. {video['name']}, Duration : {video['time']} ")
 

def Add_Video(videos):
   name=input("Enter video name: ")
   time=input("Enter video time: ")
   videos.append({"name":name,"time":time})
   save_data(videos)
def Update_Video(videos):
   list_All_Videos(videos)
   index = int(input("Enter the video number to update: "))
   if 1 <=index <= len(videos):
      name = input("Enter the new video name: ")
      time = input("Enter the new video time: ")
      videos[index-1] = {'name':name, 'time': time}
      save_data(videos)
   else:
        print("Invalid index selected")
      
      
 
def Delete_Video(videos):
   list_All_Videos(videos)
   index = int(input("Enter the video number to be deleted: "))
   if 1<=index <= len(videos):
      del videos[index-1]
      save_data(videos)
   else:
    print("Invalid video index selected")
    

def main():
  videos=load_data()
   
  while True:
    
    print("/n Youtube Manger || choose an options ")
    print("1. List all Youtube Videos  ")
    print("2. Add a youtube video  ")
    print("3. Update a youtube video Details  ")
    print("4. Delete a youtube video  ")
    print("5. Exit the app  ")
    choice= input("Enter your choice: ")
    
    match choice:
        case '1':
           list_All_Videos(videos)
        case '2':
           Add_Video(videos)
        case '3':
           Update_Video(videos)
        case '4':
           Delete_Video(videos)
        case '5':
          break
        case _:
          print("Invalid Choice")
           
if __name__ =="__main__":
   main()

