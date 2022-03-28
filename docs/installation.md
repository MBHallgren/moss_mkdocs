# MOSS Installation Guide

## Operational System

Microbial Outbreak Surveillance System (MOSS) was designed to run on a linux distribution.
It was both developed and tested on various Ubuntu distributions, and it is therefore **strongly**
recommended that users of MOSS use Ubuntu as their operational system. The latest tested Ubuntu version
is 21.10. 

## Anaconda

The latest version of Anaconda is required, and the installation guide can be found here: [Anaconda Linux Download](https://docs.anaconda.com/anaconda/install/linux/).

## Docker

Docker is required and can be installed from: [Docker Ubuntu Installation](https://docs.docker.com/engine/install/ubuntu/).

## Nvidia CUDA toolkit

Nvidia CUDA toolkit can be installed from: [Nvidia CUDA toolkit](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html).

Installing the toolkit can be a bit of a challenge sometimes and requires the correct, updated and working drivers.
If installed correctly, the "nvidia-smi" command in the terminal sound promt information about your GPU. 
Nvidia driver installation challenges can be quite different, so unfortunately no universal easy-fix can be provided.
In this situation remember that google is your friend.

## Oxford Nanopore Technologies software: MinKNOW

For performing the sequencing with Oxford Nanopore sequencers MinKNOW must be installed.
It may be downloaded from [https://community.nanoporetech.com/downloads](https://community.nanoporetech.com/downloads) or alternatively from directly from the following commands:

**MinKNOW Ubuntu >=20 (Working as of 17/3/2022):**

```console
$ sudo apt-get update
$ sudo apt-get install wget
$ wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub | sudo apt-key add -
$ echo "deb http://mirror.oxfordnanoportal.com/apt focal-stable non-free" | sudo tee /etc/apt/sources.list.d/nanoporetech.sources.list
$ sudo apt-get update
$ sudo apt-get install minion-nc

```

## Cloning from Github

If git is not installed on the computer, it can be installed from:

```console
$ sudo apt install git
```

When the dependencies above have been installed, MOSS can be cloned from [Github](https://github.com/MBHallgren/MOSS).
The cloning and subsequent installation of docker images and MOSS can be done with the following set of commands: 
```console
$ git clone https://github.com/MBHallgren/MOSS.git
$ cd MOSS
$ python3 moss_install.py
```





Lorem markdownum [pollice
Hypseus](http://www.corpore-data.com/cnosiaco-sidera.aspx) per certe patria
gloria. Portasse marmoris, tardae non: dicere nisi, domus. Rigidis contemptor
profundum Iovis bracchia, et enim abstemius cepi facere nostri, trahit motu
pariter bina aut adopertaque populo.

- Facta forma deorum ulnas
- Puer cornu
- Superbum se modo
- De deus silvae adsumere capillos restabat
- Faciat intendensque vultibus Milon dedit loco fatentem

## Fuit animi soporis

Vocant tum crines nate illa? Non florebat curvare. **Sui** atque Epaphi me
pollice pectore quos eripe adimit vocem. Tibi hastam: esset longa nunc, iam
tollens non foedere matris, nisi. Et nec sorori herbosaque virtute hoc ipse
velamina fatigat: unius.

## Tibi coniuge

Mea et numinis sedem Rex undique primum capacibus nefas tune casuque patrios.
Vicimus sacrorum pariterque *nemus comitum sedent* arboribus tempore Avernas
**ducitur**!

## Confessam freta et collo conplet fudit natos

Adicit manu at fessas; retiaque novus. Dorceus sum munera ver Phrygiisque fata,
in arce ille ad! Exercet lacrimas ut hunc humano illam lati fecisse; atque
infra, bimari est imago in finemque gravida dabitis.

Sternuntur stabant rogis perque vita baculum columbas culmina virgis rubigine
iacentem arce potuisse volucrem credere modo. Anili pallet fatendo novus, ad et
auster dextera eam cingere denique genitoris. Lyncides loquor. Rear lassata
terra corpora primo frondes memorat, ipsa talia patrem **pictarumque viam
vitae** pudibunda quod. Illam si, accipit te lege cupiens curvamine pennas missa
Onetor aurora neve; cessante.

Teneris iuvenum: recanduit corpore. Qualis est per celsa reficisque silva,
utque, sic acrior, pedibus. Et dum quo gestasset promittit furorem; tibi vota
circumdet quid longa *peregit*.
