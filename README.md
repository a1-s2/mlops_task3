# MLOps Task3 
Integration of Machine Learning And DevOps

For More Details & Documentation Please Download & Visit :- https://github.com/a1-s2/mlops_task3/blob/master/ML%26%20DevOps%20Integration.docx


# DOCUMENTATION

INTEGRATION_OF_MACHINE_LEARNING_WITH_DEVOPS TASK3 (GIVEN BY MR. VIMAL DAGA SIR)


#ML-DevOps integration $task 3
Task Description :- 

1. Create container image that’s has Python3 and Keras or numpy  installed using dockerfile 

2. When we launch this image, it should automatically starts train the model in the container.

3. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins 

4.  Job1 : Pull  the Github repo automatically when some developers push repo to Github.

5.  Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code  and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).

6. Job3 : Train your model and predict accuracy or metrics.

7. Job4 : if metrics accuracy is less than 80%  , then tweak the machine learning model architecture.

8. Job5: Retrain the model or notify that the best model is being created

9.Create One extra job job6 for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left

Pre-requisites :-

- Base OS in my case it is Windows 10 and On the Top of Windows 10 I am using Red Hat Enterprise Linux (RHEL 8 ) with the Help of Virtual Box

- Inside Rhel we need some setup to be ready like we need docker , Jenkins , centos image like I am using centos latest and and using that image I have created one Dockerfile by installing some required python modules like tensorflow , keras , numy , pillow etc. 
and we need git to be installed in RHEL8

- And for this work weight need to disable some security in RHEL 8 like firewall and SELinux Security 

Now i am sharing Screenshot of my  practical done during this task and in between I will keep on explaining how I have done this :-


 

Dockerfile:
 

Mail.py



This is the data which I needed for this task so I uploaded it on github using it bash because the dataset is large in size so I a not showing here and u can download it from internet BTW I have downloaded this dataset from kaggle.com




 
Then this code will be uploaded to github successfully and then we will create jenkins job that will get downloaded+ this uploaded data in the directory of RHEL 8 of our choice (directory)






Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code  and start training( eg. In my casei m using CNN, then Jenkins will start the container that has already installed all the softwares required for the cnn processing Tensorflow, Keras).

J








 Job3 : Train your model and predict accuracy or metrics.And will mail the output. 









so here I am using this python program to send the mail on my mail id and u can see how it’s working






++
















Build Pipeline :- 























Note :- This Task is noT Completed(100%) as I am Learning new new tools and technologies EveryDay from Mr.Vimal Daga Sir so soon I will convert this Project into Complete Automation Keep on Checking For UpDates 


Thank you vimal sir for teaching us such an great tools technology like RHEL 8 , Docker , Machine Learning , Jenkins and many more. So that today we are capable of create such an great project by our own .

Thank you EveryOne For Reading !
