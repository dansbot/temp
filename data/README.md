# MIT-BIH Databases

## WaveForm DataBase (WFDB ) Software

[https://archive.physionet.org/physiotools/wfdb.shtml#intro](https://archive.physionet.org/physiotools/wfdb.shtml#intro)

### Windows Installation

[https://archive.physionet.org/physiotools/wfdb-windows-quick-start.shtml](https://archive.physionet.org/physiotools/wfdb-windows-quick-start.shtml)

- install Cygwin 64 bit - [http://cygwin.com/](http://cygwin.com/)
  - Include packages:
    - from the Devel category: gcc-core, gcc-fortran, make
    - from the Libs category: libcurl-devel, libexpat-devel
    - from the Net category: curl
- Open Cygwin terminal (C:\cygwin64\Cygwin.bat) and run the following commands:

1. Download and unpack the WFDB sources

```command
curl https://physionet.org/physiotools/wfdb.tar.gz | tar xvz
```

2. Enter the directory created by step one, and configure the package ( replace wfdb-10.m.n with the name of the directory as printed by the previous command.)

```command
cd wfdb-10.m.n
./configure
```

3. Compile and install the package

```command
make install
```

4. Test the package

```command
make check
```

## MIT-BIH Arrhythmia Database

#### Database (DB) Info

- 48 records, each record is slightly over 30 minutes
- DB is split into two groups
  - group I (numbered from 100 - 124, some numbers missing)
  - group II (numbered from 200 - 234, some numbers missing)
- Group I is a representative sample of the variety of waveforms and artifact that an arrhythmia detector might encounter in clinical use
- Group II includes complex ventricular, junctional, and supraventricular arrhythmias and conduction abnormalities
- Demographics
  - 25 male, 32 - 89 yrs-old
  - 22 female, 23 - 89 yrs-old
  - - Records 201 and 202 are from the same male subject

#### Noise in Recordings

###### Analog recording and playback

| ![Del Mar Avionics model 445.png]("./Del Mar Avionics model 445.png") |
| :-------------------------------------------------------------------: |
|  <b>Del Mar Avionics model 445 - Used to record Holter Monitors</b>   |

Tape slipping and stickage occured during analog recording of the data. The following frequency-domains have been identified to these errors:

| Frequency (Hz) | Source                                               |
| :------------: | ---------------------------------------------------- |
|     0.042      | Recorder pressure wheel                              |
|     0.083      | Playback unit capstan (for twice real-time playback) |
|     0.090      | Recorder capstan                                     |
|     0.167      | Playback unit capstan (for real-time playback)       |
|   0.18-0.10    | Takeup reel (frequency decreases over time)          |
|   0.20-0.36    | Supply reel (frequency increases over time)          |

###### Digitization

- Analog output of the playback was filtered to limit saturation and anti-aliasing, using a passband from 0.1 to 100Hz
- The filtered signal was digitized at 360Hz
- 60Hz noise was introduced by the playback device
- Some records were recorded at double speed, 60Hz noise appears at 30Hz (and multiples of 30)

######## Sample Values (voltage)

- recordings have 11-bit resoltion over +-5 mV range
- sample values range from 0 - 2047 (inclusive), with 1024 corresponding to zero volts

#### Annotations

- Beat labels are located at the R-Wave peak

an expanded view of these tables can be found at [http://www.physionet.org/physiobank/annotations.shtml](http://www.physionet.org/physiobank/annotations.shtml)

###### Beat Annotation Symbols

| Symbol | Meaning                                   |
| :----: | ----------------------------------------- |
| · or N | Normal beat                               |
|   L    | Left bundle branch block beat             |
|   R    | Right bundle branch block beat            |
|   A    | Atrial premature beat                     |
|   a    | Aberrated atrial premature beat           |
|   J    | Nodal (junctional) premature beat         |
|   S    | Supraventricular premature beat           |
|   V    | Premature ventricular contraction         |
|   F    | Fusion of ventricular and normal beat     |
|   [    | Start of ventricular flutter/fibrillation |
|   !    | Ventricular flutter wave                  |
|   ]    | End of ventricular flutter/fibrillation   |
|   e    | Atrial escape beat                        |
|   j    | Nodal (junctional) escape beat            |
|   E    | Ventricular escape beat                   |
|   /    | Paced beat                                |
|   f    | Fusion of paced and normal beat           |
|   x    | Non-conducted P-wave (blocked APB)        |
|   Q    | Unclassifiable beat                       |
|   \|   | Isolated QRS-like artifact                |

###### Rhythm Annotation Symbols

| Symbol | Meaning                          |
| :----: | -------------------------------- |
|  (AB   | Atrial bigeminy                  |
| (AFIB  | Atrial fibrillation              |
|  (AFL  | Atrial flutter                   |
|   (B   | Ventricular bigeminy             |
|  (BII  | 2° heart block                   |
|  (IVR  | Idioventricular rhythm           |
|   (N   | Normal sinus rhythm              |
|  (NOD  | Nodal (A-V junctional) rhythm    |
|   (P   | Paced rhythm                     |
| (PREX  | Pre-excitation (WPW)             |
|  (SBR  | Sinus bradycardia                |
| (SVTA  | Supraventricular tachyarrhythmia |
|   (T   | Ventricular trigeminy            |
|  (VFL  | Ventricular flutter              |
|  (VT   | Ventricular tachycardia          |

###### Signal Quality Annotation Symbols

| Symbol | Meaning                                                                                                                                                                                |
| :----: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   qq   | Signal quality change: the first character (`c' or `n') indicates the quality of the upper signal (clean or noisy), and the second character indicates the quality of the lower signal |
|   U    | Extreme noise or signal loss in both signals: ECG is unreadable                                                                                                                        |
|   M    | (or MISSB) Missed beat                                                                                                                                                                 |
|   P    | (or PSE) Pause                                                                                                                                                                         |
|   T    | (or TS) Tape slippage                                                                                                                                                                  |
