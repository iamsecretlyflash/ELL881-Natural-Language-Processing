# ELL881-Natural-Language-Processing
This repository contains the assignments, mini Project and lectures for the course ELL881 offered in the second semester of 2023, by [Prof. Tanmoy Chakraborty](https://www.tanmoychak.com)

For this course, in the assignments part, it was best 2 out of 3 assignments and I chose to do first and third assignments only. I did write the code for the second assignment but didn't train the model

The course was quite fun and informative. Prof. Tanmoy really knows his stuff and has a good approach towards teaching as well. There were regular 
in-class quizzes and we also had a presentation component where we had to present a research paper. I did this course before doing a formal course
in machine learning ([COL774](https://github.com/iamsecretlyflash/COL774)) but I had no trouble in understanding the contents of the course. 
I highly recommend this course to anyone who wants to explore Language Processing and is interested in AI and LLMs.

A few tips to help you with the course:
  - Keep in touch with the classes and lecture slides. The lecture slides are quite informative but I believe it's essential to attend classes because
      a lot of explanations are done in classes which are not covered in the slides. For instance, backpropagation through time was covered in depth in class
      but the notes weren't too helpful.
  - Select your partners for the course project carefully. I had paired with two final-year
    seniors. Both of them audited/withdrew the course and I had to do the course project alone. Altough doing the project alone gives you complete
    control and it's a fun experience in itself, but having a partner helps.
  - Select your course project carefully as well.
  - Exams are pretty light. Lecture slides are sufficient imo
  - For the paper presentation, you will just get 10 minutes. So make sure you just present the main ideas of the paper. Look up on paper presentation
    in ten minutes (there are contests for the same)
  - Classical NLP could be a bit tricky so for that being attentive in class really helps.


## Topic wise tips

1) Hidden Markov Models: Read about the expectation maximization model and Markov Decision Processes for better understanding this part
2) CUDA Out of Memory Error :Don't abuse batch size. With a higher batch size training performace may imporove but can also result in a CUDA memory error and usually you will have to restart the Kernel to free up the space on GPU. You can also use torch.cuda.empty_cache() but it doesn't clear the whole GPU. Even iterating over CUDA objects using the garbage collector library didn't really help. So, restarting the kernel is usually the only way to go XD.

