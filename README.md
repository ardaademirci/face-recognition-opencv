# Attendance List using Face Recognition OpenCV

This project the use of Face Recognition using OpenCV on an Attendance List Project.

After providing only 1 good photo of a person, it recognizes them from different angles, hairstyles, faical hairs and more.

It checks for faces in real time using an external camera, in my case my phone.
Because I had to use third party softwares for this I was allowed to record with only 24fps.
However, when used with 60fps or higher, it can detect and regocnize from videos as well.
This means it can be placed on the entrance of an exclusive event with celebrities check the people coming towards the entrence whether or not they are in the guest list. So, the people who are recognized will keep walking whereas the people who are not will be asked to identify themselves.

What I have described so far happens in the Attendace.py.

But before moving on to that, you should check out Basics.py to check out how it works and what each line does by playing around.

I will post the photos I used for my code and then the screenshots of the program working.

Andrew Garfield

![Andrew Garfield](https://github.com/user-attachments/assets/c3b97492-4761-44e5-ad4b-1e5618f57ae1)

Owen Wilson

![Owen Wilson](https://github.com/user-attachments/assets/b7fd1004-9809-405d-892d-a35855c9ac9a)

Robert Pattionson

![Robert Pattinson](https://github.com/user-attachments/assets/757d8e8f-7834-489a-9a65-f2cd4bd3529b)



The screenshots:

On the left side you can see the image I picked on google to compare. 
On the right side is the webcam footage.
And behind the webcam footage there is the Attendance list, with names and time.

![andrew](https://github.com/user-attachments/assets/54291421-34e5-423d-ad01-0382205f24d8)

![owen](https://github.com/user-attachments/assets/b56fd34c-5b09-4074-b120-74a3f920540f)

![robert](https://github.com/user-attachments/assets/81f4eca7-6758-4ca9-b04c-9a8a792fd2fd)


And these are the extra ones where they lees look like the initial picture or the angle is different:

![owen 2](https://github.com/user-attachments/assets/865bd866-d683-4021-9594-aebe67718235)

![robert 2](https://github.com/user-attachments/assets/25e14bbf-05fc-40b4-a9f9-95254841fd4e)

![robert 3](https://github.com/user-attachments/assets/8904b2df-7fd9-4f34-a0ba-2a8b972a0c74)


For this project you should add or install numpy, cmake, opencv-python, dlib, face-recognition. In this order.
If you encounter problems with dlib, check out 'dependency errors.txt'.

