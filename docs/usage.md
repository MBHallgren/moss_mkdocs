## Nanopore sequencing
Before using MOSS Nanopore sequencing has to be carried out.
MOSS 1.0.0 has been designed to work ONLY with ONT data.
<br /> <br />
It is recommended that sequencing is conducted using ONT's MinKNOW software.

### Base calling
It is recommended that base calling is conducted with either high-accuracy or super-high-accuracy models.
Make sure that these are run using GPU base calling.

### FastQ
During MinKNOW sequencing base calling can be performed automatically. This will produce fastQ files, which is prefered.

### Fast5
Alternatively, sequencing with MinKNOW can be performed without doing live base calling.
After sequencing the MOSS base calling function can be used.
The MOSS base calling section is found in the left-side menu of the app.

#### MOSS Base calling
Open the MOSS app and click on "Base calling" in the left-side menu.
Upload the folder containing the many, smaller fast5 files which was generated doing sequencing.
Provide a unique experiment name. The experiment name should NOT be a small, generic one. <br /> <br />
Bad experiment name: nanopore_run_1 <br />
Good experiment name: icu_patients_denmark_june_1_6_1996 <br /> <br />
Select the prefered base calling algorithm (HAC is recommended as default). Select flow-cell type, kit and barcodes. <br />
Finally, submit the base calling run. 

## Entering meta data for sequencing run
When FastQ files have been produced, either from automated base calling with MinKNOW or through the MOSS app, it is now time to submit meta data about the experiment.
In the MOSS app go to home>metadata. Enter a unique experiment name and select all the FastQ files - There should ONLY be one FastQ file for isolate. <br />
The experiment name should NOT be a small, generic one. <br /> <br />
Bad experiment name: nanopore_run_1 <br />
Good experiment name: icu_patients_denmark_june_1_6_1996 <br />
An experiment name already used will not be accepted by the system.<br /> <br />

After entering experiment name and isolate files, hit the *Generate meta data table* button.
Fill in the corresponding meta data for each isolate and generate the meta data sheet. <br /> <br />

**The meta data sheet is the only item required to begin an analysis** 

## Running an analysis
After successfully generating a meta data sheet for your sequencing experiment, go to *Home > Analyse*. <br />
Select the meta data sheet and submit the analyses. The progress and result of the analysis can be seen in the *Results* section in the left-side menu.







Docker is required and can be installed from: [Docker Ubuntu Installation](https://docs.docker.com/engine/install/ubuntu/).

After following the installation instructions above, run the following command in the terminal to complete the and then restart the terminal:

```console
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ sudo chmod 666 /var/run/docker.sock
```

## Nvidia CUDA toolkit

Nvidia CUDA toolkit can be installed from: [Nvidia CUDA toolkit](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html).

Installing the toolkit can be a bit of a challenge sometimes and requires the correct, updated and working drivers.
If installed correctly, the "nvidia-smi" command in the terminal sound promt information about your GPU. 
Nvidia driver installation challenges can be quite different, so unfortunately no universal easy-fix can be provided.
In this situation remember that google is your friend.

The MOSS system was built and tested on a HP ZBOOK studio G8 Mobile WorkStation. 
The stable kernel which works with the nvidia-510 driver is 5.10.0-1044-oem. 
For help see: [nvidia-smi ubuntu kernel HP ZBOOK](https://forums.developer.nvidia.com/t/ubuntu-20-04-4-hp-zbook-studio-g8-mobile-workstation-driver-fails/208836/3).

## Oxford Nanopore Technologies software: MinKNOW

For performing the sequencing with Oxford Nanopore sequencers MinKNOW must be installed.
It may be downloaded from [https://community.nanoporetech.com/downloads](https://community.nanoporetech.com/downloads) or alternatively from directly from the following commands:

**MinKNOW Ubuntu 20.04 (Working as of 17/3/2022):**

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
$ git clone https://github.com/MBHallgren/moss.git
$ cd moss
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
