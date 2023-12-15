Tips for NER :

1) Kaggle GPU should work fine. Do not use Google Colab as the free version has quite terrible variable and memory retention and the Kernel also dies
   quickly. Also, Kaggle offers a wider range of GPUs and GPUs with more memory.
2) For using CRF with your PyTorch model you can use [PyTorch-CRF](https://pytorch-crf.readthedocs.io/en/stable/)
3) Don't abuse batch size. With a higher batch size training performace can imporove but can also result in a CUDA memory error and usually you will
   have to restart the Kernel to free up the space on GPU. You can also use torch.cuda.empty_cache() but it doesn't clear the whole GPU. Even iterating
   over CUDA object using the garbage collector library didn't really help. So, restarting the kernel is usually the only way to go XD.
