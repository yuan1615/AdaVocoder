# AdaVocoder: Adaptive Vocoder for Custom Voice

In our [paper](https://www.isca-speech.org/archive/interspeech_2022/yuan22_interspeech.html), 
we proposed AdaVocoder: Adaptive Vocoder for Custom Voice.<br/>
We provide our implementation and pretrained models for `AdaHiFi-GAN` as open source in this repository.

**Abstract :**

Custom voice is to construct a personal speech synthesis system by adapting the source speech synthesis model 
to the target model through the target few recordings. The solution to constructing a custom voice is 
to combine an adaptive acoustic model with a robust vocoder. However, training a robust vocoder usually requires a multi-speaker dataset, 
which should include various age groups and various timbres, so that the trained vocoder can be used for unseen speakers. Collecting such a 
multi-speaker dataset is difficult, and the dataset distribution always has a mismatch with the distribution of the target speaker dataset.

This paper proposes an adaptive vocoder for custom voice from another novel perspective to solve the above problems. 
The adaptive vocoder mainly uses a cross-domain consistency loss to solve the overfitting problem encountered by the GAN-based neural 
vocoder in the transfer learning of few-shot scenes. We construct two adaptive vocoders, AdaMelGAN and AdaHiFi-GAN. 
First, We pre-train the source vocoder model on AISHELL3 and CSMSC datasets, respectively. 
Then, fine-tune it on the internal dataset VXI-children with few adaptation data. 
The empirical results show that a high-quality custom voice system can be built by combining a adaptive acoustic model with a adaptive vocoder.

## Pre-requisites
1. Python >= 3.6
2. Clone this repository.
3. Install python requirements. Please refer [requirements.txt](requirements.txt)
4. Download and extract the [AISHELL3 dataset](http://www.aishelltech.com/aishell_3), then rename or create a link to the dataset folder: `ln -s /path/to/AISHELL-3/wavs DUMMY1`
And move all wav files to `AISHELL-3/wavs`, and sample all audio files to `22050`Hz.


## Training HiFi-GAN
```
python train_hifi_gan.py --config config_v1.json
```
- Tensorboard
```
tensorboard --logdir cp_hifigan/logs/ --bind_all
```

Checkpoints and copy of the configuration file are saved in `cp_hifigan` directory by default.<br>
You can change the path by adding `--checkpoint_path` option.

## Pretrained Model
You can also use pretrained models we provide.<br/>
[Download AISHELL3 pretrained models](https://drive.google.com/file/d/1lqp-8mQIultA2nQ9lY3SNyUpqDpZTHLk/view?usp=sharing)


## Training AdaHiFi-GAN
First you need to save the pre-trained `AISHELL-3` model to `cp_ada_hifigan`.<br>

Due to the need for confidentiality, VXI-children is not used here. I tested it using the child sample shared by [Data-Baker](https://www.data-baker.com/).

```
python train_ada_hifi_gan.py --config config_v1.json
```
- Tensorboard
```
tensorboard --logdir cp_ada_hifigan/logs/ --bind_all
```
Checkpoints and copy of the configuration file are saved in `cp_ada_hifigan` directory by default.<br>
You can change the path by adding `--checkpoint_path` option.


## Inference from wav file
1. Make `test_files` directory and copy wav files into the directory.
2. Run the following command.
    ```
    python inference.py --checkpoint_file [generator checkpoint file path] --model_name [hifi-gan or adahifi-gan]
    ```
Generated wav files are saved in `generated_files` by default.<br>
You can change the path by adding `--output_dir` option.

## [Some Sample](https://yuan1615.github.io/2022/09/21/AdaVocoder/)


## Acknowledgements
We referred to [HiFi-GAN](https://github.com/jik876/hifi-gan) to implement this.

