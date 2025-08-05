# ALICE

Active Learning Interface (for) Circuits (and) Electronics:

The ALICE Desktop software interface is a collection of software instruments written for use with the active learning hardware modules ADALM1000 (M1K) and ADALM2000 (M2K).


## Simplified Instructions
> [!WARNING]
> This only works for Linux, Windows or OSX Machines on x86_64. aarch64/arm64 and other architectures do not work ootb here. This is because we rely on the conda package for libsmu/pysmu

### Install Instructions (Linux/Mac/Windows) (x86_64)
0. Ensure that `python3` and `git` are already installed and are accessible from the terminal! 
    - Linux: Use your default package manager. The command varies from system to system but it usually looks like this:
        - `sudo apt update; sudo apt install git python3 # Debian/Ubuntu`
        - `sudo zypper install python3 git # SUSE`
        - `sudo pacman -S git python # Arch`
        - `sudo dnf install python3 git # RHEL/Fedora`
        - `sudo apk install python3 git # Alpine`
    - Mac: Use brew to install these. That might need additional setup beforehand as well.
        - `brew install git python`
    - Windows: Use the winget tool to fetch it. You may need to update the version from 3.12 to the latest one.
        - `winget install Python.Python.3.12 git`
        - Or download it manually from:
            1. https://www.python.org/downloads/windows/
            2. https://git-scm.com/downloads/win

1. Install Prefix.Dev's `pixi` as per official instructions at https://pixi.sh/latest/#installation <!-- Instructions after here will work on Windows too provided deps like python3 and git are installed-->
    - As of Aug 04 2025, running the following command in your favorite terminal shell will set up `pixi` with minimal effort. This may break in the future, always refer to the link above! This command is only for Linux and MacOS, since Windows has a nice and simple installer at: https://github.com/prefix-dev/pixi/releases/latest
        - https://github.com/prefix-dev/pixi/releases/latest/download/pixi-x86_64-pc-windows-msvc.msi
    ```bash
    curl -fsSL https://pixi.sh/install.sh | sh
    ```
    Close your terminal window and open another one after installing.
2. Prepare workspace with the command
    ```bash
    git clone https://github.com/sounddrill31/alice-m1k
    ```
    ```bash
    cd alice-m1k
    ```
3. Run the following Command to let `pixi` setup your environment
    ```bash
    pixi install
    ```
4. Have `pixi` prepare the udev rule(Only for Linux users). This is important for the board to be detected!
    ```bash
    pixi run udev-setup
    ```
5. Start `alice-desktop-1.3.pyw` using the built-in task!
    ```bash
    pixi run start
    ```

---
## Old Instructions


### [ALICE 1.3 User Guide for M1K]:
### [ALICE 2.0 User Guide for M2K]:
[ALICE 1.3 User Guide for M1K]:https://wiki.analog.com/university/tools/m1k/alice/desk-top-users-guide
[ALICE 2.0 User Guide for M2K]:https://wiki.analog.com/university/tools/m2k/alice/users-guide-m2k

## Background:

Although the word ALICE can be spelled out from the title of this users guide, it is actually an allusion to 
the fantasy works of Lewis Carroll: 1865’s Alice’s Adventures in Wonderland and its 1871 sequel Through the 
Looking-Glass, and What Alice Found There. In these stories Alice explores a strange and wondrous world down 
a rabbit hole and on the other side of a mirror ( looking glass ).

Hopefully, through the use of this software along with the active learning hardware modules, Students 
can explore the strange and wondrous world of Circuits, Electronics and Electrical Engineering.

### Functions:

The ALICE Desktop software provides the following functions:

- Two Channel Oscilloscope for time domain display and analysis of voltage and current waveforms.
- Two Channel Arbitrary Waveform Generator (AWG) controls.
- X-Y display for plotting captured analog signal data as well as waveform histograms.
- Two Channel Spectrum Analyzer for frequency domain display and analysis of analog waveforms.
- Bode plotter and network analyzer with built-in sweep generator.
- Impedance Analyzer for analyzing complex RLC networks and as a RLC meter and Vector Voltmeter.
- DC Ohmmeter, measures unknown resistance with respect to known external resistor or known internal 50 ohms.
- M1K Board Self-Calibration using a known external reference such as an AD584 precision 2.5V reference from the ADALP2000 Analog Parts Kit

## Required files:

The ALICE Desktop programs are written in Python. The source code is compatable with version 2.7 and 3.7 
Python with the numpy numerical library package installed on the user’s computer. The program only imports modules generally included 
with standard Python installation packages.

### Windows:

Windows users who do not wish to install Python and the other required software packages can install the 
standalone executable under Releases.   

The Libsmu support library for the ADALM1000, for X86 (32 bit) must be installed first.
Run the alice-desktop-1.3-setup.exe or alice-desktop-2.0-setup.exe installer program. 
ALICE desktop opens and saves info and data to various files in the installation directory. Because of user 
permission issues with some installations of Windows you may need to install the software in a directory 
other than the default “Program Files”. C:\ALM Software\ would be a good second choice. The installer adds 
desktop icons for each tool in the suite. Alternatively, under the properties for the icons, you can change 
the directory the program(s) start in.

Or run ALICE Desktop from the Python 2.7 / 3.7 compatible source code with the following packages installed:

numpy numerical package extension
libsmu/pysmu for M1K
